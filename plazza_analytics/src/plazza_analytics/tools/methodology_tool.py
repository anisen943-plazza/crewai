# src/plazza_analytics/tools/methodology_tool.py

import os
import psycopg2
import psycopg2.extras
from crewai.tools import BaseTool
from plazza_analytics.tools.config import DB_CONNECTION_VARS

class MethodologyTool(BaseTool):
    name: str = "MethodologyTool"
    description: str = """Executes structured SQL queries with methodology tracking.
    Provides clean documentation of multi-source analysis and results."""
    
    def run(self, queries: list = []):
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
        return self._run(queries=queries)
    
    def _run(self, queries: list = []) -> str:
        if not isinstance(queries, list):
            return "❌ Input must be a list of query objects."

        results = []

        for q in queries:
            db = q.get("database")
            sql = q.get("query")
            desc = q.get("description", "Query")

            if not db or db not in DB_CONNECTION_VARS:
                results.append(f"### {desc}\n- ❌ Invalid or missing database: {db}\n")
                continue
            if not sql:
                results.append(f"### {desc}\n- ❌ Missing SQL query\n")
                continue

            conn_str = os.getenv(DB_CONNECTION_VARS[db])
            if not conn_str:
                results.append(f"### {desc}\n- ❌ Environment variable for '{db}' not set\n")
                continue

            try:
                conn = psycopg2.connect(conn_str)
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                    cursor.execute(sql)
                    rows = cursor.fetchall()

                    results.append(f"### {desc}")
                    results.append(f"- Database: `{db}`")
                    results.append("```sql\n" + sql.strip() + "\n```")

                    if not rows:
                        results.append("ℹ️ No results\n")
                        continue

                    header = list(rows[0].keys())
                    data_lines = [" | ".join(map(str, header))]
                    data_lines.append("-" * len(data_lines[0]))

                    for row in rows[:10]:
                        data_lines.append(" | ".join(str(row[h]) for h in header))

                    results.append("```\n" + "\n".join(data_lines) + "\n```\n")

            except Exception as e:
                results.append(f"### {desc}\n- ❌ Query error: {str(e)}\n")
            finally:
                if 'conn' in locals() and conn:
                    conn.close()

        return "\n".join(results)