# src/plazza_analytics/tools/methodology_tool.py

import os
import psycopg2
import psycopg2.extras
from typing import List, Dict, Any, Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from plazza_analytics.tools.config import DB_CONNECTION_VARS

# Version History
# 2025-03-28: Updated for CrewAI v0.108.0+ compatibility
#   - Added proper type annotations for name and description 
#   - Added args_schema with Pydantic BaseModel validation
#   - Enhanced parameter validation with robust error handling
#   - Added **kwargs to run method for better compatibility
#   - Improved error messages with troubleshooting guidance

class QueryItem(BaseModel):
    database: str = Field(
        default="defaultdb",
        description="Database to query (defaultdb, user_transactions, plazza_erp, user_events)"
    )
    query: str = Field(
        description="SQL query to execute"
    )
    description: Optional[str] = Field(
        default=None,
        description="Description of what the query is checking"
    )

class MethodologyToolArgs(BaseModel):
    queries: List[QueryItem] = Field(
        default=[],
        description="List of query objects to execute with database, query, and description"
    )

class MethodologyTool(BaseTool):
    name: str = "MethodologyTool"
    description: str = """Executes structured SQL queries with methodology tracking.
    Provides clean documentation of multi-source analysis and results."""
    
    args_schema: type[MethodologyToolArgs] = MethodologyToolArgs
    
    def run(self, queries: List[Dict[str, Any]] = [], **kwargs):
        """Execute multiple SQL queries with detailed methodology documentation.
        
        Args:
            queries: A list of query objects, each with database, query, and description
        
        Example:
            [{
              "database": "user_transactions",
              "query": "SELECT COUNT(*) FROM orders",
              "description": "Count total orders"
            },
            {
              "database": "defaultdb",
              "query": "SELECT COUNT(*) FROM products",
              "description": "Count total products"
            }]
        """
        try:
            # Simple validation for queries list
            if not isinstance(queries, list):
                return "❌ Input must be a list of query objects."
                
            print(f"MethodologyTool executing {len(queries)} queries")
            return self._run(queries=queries)
        except Exception as e:
            error_message = f"ERROR in MethodologyTool.run: {str(e)}"
            print(error_message)
            import traceback
            print(traceback.format_exc())
            return error_message
    
    def _run(self, queries: List[Dict[str, Any]] = []) -> str:
        """Execute multiple SQL queries with detailed methodology documentation.
        
        This is the internal implementation called by run() after parameter validation.
        
        Args:
            queries: A list of query objects with database, query, and description keys
            
        Returns:
            str: Formatted query results with methodology documentation
        """
        if not isinstance(queries, list):
            return "❌ Input must be a list of query objects."

        # Group queries by database to minimize connection creation
        queries_by_db = {}
        for i, q in enumerate(queries):
            # Skip invalid queries
            if not isinstance(q, dict):
                continue
                
            db = q.get("database")
            sql = q.get("query")
            desc = q.get("description", f"Query #{i+1}")
            
            # Add to appropriate database group
            if db not in queries_by_db:
                queries_by_db[db] = []
                
            queries_by_db[db].append({
                "index": i,
                "query": sql,
                "description": desc
            })

        # Process each database group
        results = []
        aggregate_values = {}
        
        for db, db_queries in queries_by_db.items():
            if not db or db not in DB_CONNECTION_VARS:
                results.append(f"### ⚠️ Invalid or missing database: {db}\n")
                continue
                
            conn_str = os.getenv(DB_CONNECTION_VARS[db])
            if not conn_str:
                results.append(f"### ⚠️ Environment variable for '{db}' not set\n")
                continue
            
            # Process all queries for this database with a single connection
            conn = None
            try:
                conn = psycopg2.connect(conn_str)
                
                for q in db_queries:
                    sql = q.get("query")
                    desc = q.get("description")
                    
                    if not sql:
                        results.append(f"### {desc}\n- ❌ Missing SQL query\n")
                        continue
                    
                    # Format query section header
                    results.append(f"### {desc}")
                    results.append(f"- Database: `{db}`")
                    results.append("```sql\n" + sql.strip() + "\n```")
                    
                    try:
                        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                            cursor.execute(sql)
                            rows = cursor.fetchall()

                            if not rows:
                                results.append("ℹ️ No results\n")
                                continue
                            
                            # For single-row, single-column results, extract the value for summary
                            is_aggregate = False
                            if len(rows) == 1 and len(rows[0]) == 1:
                                is_aggregate = True
                                for col_name in rows[0].keys():
                                    aggregate_values[desc] = rows[0][col_name]
                            
                            # Format as table for multiple rows or columns
                            header = list(rows[0].keys())
                            data_lines = [" | ".join(map(str, header))]
                            data_lines.append("-" * len(data_lines[0]))
                            
                            for row in rows[:10]:
                                data_lines.append(" | ".join(str(row[h]) for h in header))
                                
                            if len(rows) > 10:
                                data_lines.append(f"... and {len(rows) - 10} more rows")
                                
                            results.append("```\n" + "\n".join(data_lines) + "\n```\n")
                    except Exception as query_error:
                        results.append(f"- ❌ Query error: {str(query_error)}\n")
                        
            except Exception as conn_error:
                results.append(f"### ⚠️ Database connection error: {str(conn_error)}\n")
            finally:
                if conn:
                    conn.close()
        
        # Add a summary section for aggregate values
        if aggregate_values:
            summary = ["## Summary of Findings"]
            for desc, val in aggregate_values.items():
                # Format numerical values with commas for thousands
                if isinstance(val, (int, float)):
                    # Format rupees if likely a monetary value
                    if "price" in desc.lower() or "amount" in desc.lower() or "total" in desc.lower() or "sales" in desc.lower():
                        summary.append(f"- {desc}: ₹{val:,.2f}")
                    else:
                        summary.append(f"- {desc}: {val:,}")
                else:
                    summary.append(f"- {desc}: {val}")
            
            summary.append("")  # Add empty line
            results = summary + results
        
        return "\n".join(results)