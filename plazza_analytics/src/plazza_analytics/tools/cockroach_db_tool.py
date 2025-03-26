# src/plazza_analytics/tools/cockroach_db_tool.py

import os
import psycopg2
import psycopg2.extras
from langchain.tools import BaseTool
from plazza_analytics.tools.config import DB_CONNECTION_VARS, DB_SCHEMA_CACHE

class CockroachDBTool(BaseTool):
    name = "CockroachDBTool"
    description = """Execute SQL queries against any CockroachDB database in the Plazza ecosystem.
    Supports schema discovery, table exploration, and live query execution."""
    
    def run(self, query: str = "", database: str = "defaultdb"):
        """Execute SQL query against the specified database.
        query: The SQL query to execute. Use "SHOW DATABASES;" to see all available databases.
        database: The database to run the query against (defaultdb, user_transactions, plazza_erp, user_events).
        """
        return self._run(query=query, database=database)
    
    # Keep run for compatibility with langchain tool standards
    def __call__(self, query: str = "", database: str = "defaultdb"):
        return self.run(query=query, database=database)

    def _list_all_databases(self):
        """List all available databases in the CockroachDB cluster."""
        global DB_SCHEMA_CACHE
        if 'all_databases' in DB_SCHEMA_CACHE:
            return DB_SCHEMA_CACHE['all_databases']

        result = ["Available databases in CockroachDB cluster:"]
        for db_name in DB_CONNECTION_VARS.keys():
            result.append(f"- {db_name}")

        conn = None
        for db_name, env_var in DB_CONNECTION_VARS.items():
            connection_string = os.getenv(env_var)
            if connection_string:
                try:
                    conn = psycopg2.connect(connection_string)
                    break
                except Exception:
                    continue

        if not conn:
            result.append("\n⚠️ Could not connect to any database to discover additional databases.")
            return "\n".join(result)

        additional_dbs = set()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT datname FROM pg_database WHERE datname NOT IN ('postgres', 'template0', 'template1')")
                rows = cursor.fetchall()
                for row in rows:
                    if row[0] not in DB_CONNECTION_VARS and row[0] not in additional_dbs:
                        additional_dbs.add(row[0])
        finally:
            conn.close()

        if additional_dbs:
            result.append("\n🆕 Additional discovered databases (not pre-configured):")
            for db in sorted(additional_dbs):
                result.append(f"- {db}")

        result.append("\nℹ️ Use only the configured databases for running actual queries.")
        output = "\n".join(result)
        DB_SCHEMA_CACHE['all_databases'] = output
        return output

    def _run(self, query: str = "", database: str = "defaultdb") -> str:
        if query.strip().upper() == "SHOW DATABASES;":
            return self._list_all_databases()

        if database not in DB_CONNECTION_VARS:
            return f"❌ '{database}' is not a valid database. Choose from: {', '.join(DB_CONNECTION_VARS.keys())}"

        connection_var = DB_CONNECTION_VARS[database]
        connection_string = os.getenv(connection_var)
        if not connection_string:
            return f"❌ Environment variable {connection_var} is not set."

        test_filter = (
            "product_id NOT LIKE '%TEST%' AND "
            "product_id NOT LIKE '%test%' AND "
            "product_id NOT LIKE 'p%' AND "
            "medicine_name NOT LIKE 'Test%' AND "
            "product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002') AND "
            "order_id NOT LIKE '%TEST%' AND "
            "order_id NOT LIKE 'POD-WEBHOOK%' AND "
            "bill_total_amount > 10"
        )

        try:
            conn = psycopg2.connect(connection_string)
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                if "GROUP BY" in query and "SUM(" in query.upper() and "medicine_name" not in query:
                    query = query.replace("GROUP BY product_id", "GROUP BY product_id, medicine_name")
                    query = query.replace("SELECT product_id", "SELECT product_id, medicine_name")
                    if "WHERE" in query:
                        query = query.replace("WHERE", f"WHERE {test_filter} AND ")
                    else:
                        parts = query.split("GROUP BY")
                        query = f"{parts[0]} WHERE {test_filter} GROUP BY {parts[1]}"
                cursor.execute(query)
                rows = cursor.fetchall()
                if not rows:
                    return "No results found."

                results = "\n".join([str(dict(row)) for row in rows[:20]])
                if len(rows) > 20:
                    results += f"\n...and {len(rows) - 20} more rows"
                return results
        except Exception as e:
            return f"❌ Error running query: {str(e)}"
        finally:
            if conn:
                conn.close()