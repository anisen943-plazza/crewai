from crewai.tools import BaseTool
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from typing import Dict, Any, List, Optional, ClassVar
import re

class PostgreSQLTool(BaseTool):
    name: str = "query_postgres"
    description: str = """Executes a SQL query on the connected PostgreSQL database and returns the result.
    
    DATABASE MAPPING:
    - user_transactions database (CONNECTION: DATABASE_URL_USER_TRANSACTIONS):
      - orders table: Contains order records with bill_total_amount, status, etc.
      - contacts table: Contains customer information
      - order_items table: Contains line items for each order
      
    - plazza_erp database (CONNECTION: DATABASE_URL_ERP):
      - inventory_transactions table: Contains inventory transactions
      
    - defaultdb database (CONNECTION: DATABASE_URL):
      - all_products table: Contains product catalog information
    
    The tool will automatically determine which database to use based on the table(s) in your query.
    Make sure to specify the table name clearly in your SQL query.
    
    Examples:
    - To query orders: "SELECT * FROM orders WHERE status='paid'"
    - To query inventory: "SELECT * FROM inventory_transactions WHERE vendor_name='Example'"
    - To query products: "SELECT * FROM all_products WHERE name LIKE '%Medicine%'"
    """
    
    # Map of table names to database connection environment variables
    TABLE_TO_DB_MAP: ClassVar[Dict[str, str]] = {
        "orders": "DATABASE_URL_USER_TRANSACTIONS",
        "contacts": "DATABASE_URL_USER_TRANSACTIONS",
        "order_items": "DATABASE_URL_USER_TRANSACTIONS",
        "inventory_transactions": "DATABASE_URL_ERP",
        "all_products": "DATABASE_URL"
    }
    
    # Map of connection variables to database names (for error messages)
    CONN_TO_DB_NAME: ClassVar[Dict[str, str]] = {
        "DATABASE_URL_USER_TRANSACTIONS": "user_transactions",
        "DATABASE_URL_ERP": "plazza_erp",
        "DATABASE_URL": "defaultdb"
    }
    
    def _detect_table_in_query(self, sql: str) -> str:
        """
        Analyzes the SQL query to detect which table is being queried.
        Returns the appropriate connection string environment variable.
        """
        sql_lower = sql.lower()
        
        # Try to find table names in the query using regex to match:
        # - from table_name
        # - join table_name
        # - update table_name
        # - insert into table_name
        table_pattern = r'(?:from|join|update|into)\s+([a-z0-9_]+)'
        matches = re.findall(table_pattern, sql_lower)
        
        # Check if any of the matched tables are in our mapping
        for table in matches:
            if table in self.TABLE_TO_DB_MAP:
                return self.TABLE_TO_DB_MAP[table]
        
        # If no table matched, check for any keywords in the query
        for table, conn_var in self.TABLE_TO_DB_MAP.items():
            if table in sql_lower:
                return conn_var
        
        # Default to ERP database if we can't determine
        return "DATABASE_URL_ERP"
    
    def _format_results(self, cursor) -> str:
        """Format query results in a more readable way"""
        try:
            # Fetch column names
            columns = [desc[0] for desc in cursor.description]
            
            # Fetch data
            rows = cursor.fetchall()
            if not rows:
                return "Query executed successfully. No results returned."
            
            # If using RealDictCursor, rows are already dictionaries
            if isinstance(cursor.row_factory, RealDictCursor):
                results = rows
            else:
                # Convert to list of dictionaries
                results = []
                for row in rows:
                    result_dict = {}
                    for i, col in enumerate(columns):
                        result_dict[col] = row[i]
                    results.append(result_dict)
            
            # Format output
            if len(results) > 20:
                output = f"Query returned {len(results)} rows. Showing first 20:\n\n"
                results = results[:20]
            else:
                output = f"Query returned {len(results)} rows:\n\n"
            
            # Format each row
            for i, row in enumerate(results):
                output += f"Row {i+1}:\n"
                for col, val in row.items():
                    output += f"  {col}: {val}\n"
                output += "\n"
            
            return output
        except Exception as e:
            # If formatting fails, return raw results
            return str(cursor.fetchall())
    
    def _run(self, sql: str) -> str:
        """Executes a SQL query on the connected PostgreSQL DB and returns the result."""
        try:
            # Determine which database to connect to based on the SQL query
            conn_var = self._detect_table_in_query(sql)
            conn_string = os.getenv(conn_var)
            db_name = self.CONN_TO_DB_NAME.get(conn_var, "unknown")
            
            # Log which database we're connecting to
            print(f"Connecting to {db_name} database using {conn_var}")
            
            if not conn_string:
                return f"Query failed: Connection string for {db_name} database not found in environment variables"
            
            # Connect to the database
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            
            try:
                # Execute the query
                cursor.execute(sql)
                
                # Format the results
                if cursor.description:  # If the query returns results
                    result = self._format_results(cursor)
                else:
                    # For queries that don't return results (INSERT, UPDATE, etc.)
                    conn.commit()
                    result = f"Query executed successfully. Affected rows: {cursor.rowcount}"
                
                return result
            finally:
                cursor.close()
                conn.close()
                
        except Exception as e:
            return f"Query failed: {str(e)}\n\nPlease make sure you're querying a table that exists in the database.\nTable to database mapping:\n- orders, contacts, order_items → user_transactions\n- inventory_transactions → plazza_erp\n- all_products → defaultdb"

# Create an instance of the tool for use with crewai
query_postgres = PostgreSQLTool()