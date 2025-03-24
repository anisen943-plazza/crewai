import os
import psycopg2
import psycopg2.extras
import json
import shutil
import time
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import BaseTool
from pydantic import Field
from crewai.knowledge.knowledge import Knowledge
from crewai_visualization import visualize_analysis_results, VisualizationTool

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it in your .env file or environment.")
os.environ["OPENAI_API_KEY"] = openai_key

# Path to the analysis results file
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANALYSIS_RESULTS_PATH = os.path.join(parent_dir, "Run_Results", "sales_ai_run_result.md")

class PreviousAnalysisTool(BaseTool):
    name: str = "PreviousAnalysisTool"
    description: str = """Access the historical analysis results.
    
    This tool retrieves the previous analysis results that were stored from past runs.
    Use this tool to:
    1. Check what insights were discovered in previous analyses
    2. Compare new findings against historical data
    3. Build upon previous recommendations rather than starting from scratch
    
    The previous analysis contains information about:
    - Database structure summary
    - Inventory-Sales Gap Analysis
    - Data Consistency Analysis
    - Actionable Recommendations
    
    USAGE:
    Simply call the tool with no parameters to retrieve the entire previous analysis.
    
    NOTE: For specific queries about previous analysis, the built-in knowledge system 
    will automatically retrieve relevant information. Use this tool only when you need
    to see the full previous analysis.
    """
    
    def _run(self) -> str:
        try:
            if os.path.exists(ANALYSIS_RESULTS_PATH):
                with open(ANALYSIS_RESULTS_PATH, 'r') as file:
                    content = file.read()
                    
                    # Extract the final answer section which contains the actual analysis
                    if "## Final Answer:" in content:
                        final_answer = content.split("## Final Answer:")[1].strip()
                        
                        # Format the content for better readability
                        formatted_content = self._format_analysis_content(final_answer)
                        return f"## Previous Analysis Results\n\n{formatted_content}"
                    
                    # If no final answer section, return the whole content
                    formatted_content = self._format_analysis_content(content)
                    return f"## Previous Analysis Results\n\n{formatted_content}"
            else:
                return "No previous analysis results found."
        except Exception as e:
            return f"Error retrieving previous analysis: {str(e)}"
    
    def _format_analysis_content(self, content: str) -> str:
        """Format the analysis content for better readability."""
        # Split content into sections
        sections = []
        current_section = ""
        current_title = "Overview"
        
        for line in content.split("\n"):
            # Check if this is a section header
            if line.startswith("## "):
                # Save the previous section if it's not empty
                if current_section.strip():
                    sections.append({
                        "title": current_title,
                        "content": current_section.strip()
                    })
                
                # Start a new section
                current_title = line.replace("## ", "").strip()
                current_section = ""
            else:
                current_section += line + "\n"
        
        # Add the last section
        if current_section.strip():
            sections.append({
                "title": current_title,
                "content": current_section.strip()
            })
        
        # Format sections into a readable format
        if not sections:
            return content  # Return original if parsing failed
        
        formatted_text = ""
        for section in sections:
            formatted_text += f"### {section['title']}\n\n{section['content']}\n\n"
        
        return formatted_text

# Database connection mapping - moved to module level for reuse
DB_CONNECTION_VARS = {
    "user_transactions": "DATABASE_URL_USER_TRANSACTIONS",
    "defaultdb": "DATABASE_URL",
    "plazza_erp": "DATABASE_URL_ERP",
    "user_events": "DATABASE_URL_USER"
}

# Cache for database schema information
DB_SCHEMA_CACHE = {}

class CockroachDBTool(BaseTool):
    name: str = "CockroachDBTool"
    description: str = """Execute SQL queries against any CockroachDB database in the Plazza ecosystem.
    
    This tool allows you to explore and query multiple databases in the environment. 
    You can discover available databases, explore their schema, and execute queries
    against any tables you discover.
    
    SCHEMA DISCOVERY:
    
    You should begin by discovering the available databases and their schema. Use these
    information_schema queries to understand the database environment:
    
    - List all available databases:
      ```sql
      SHOW DATABASES;
      ```
      
    - Or alternatively:
      ```sql
      SELECT datname FROM pg_database 
      WHERE datname NOT IN ('postgres', 'template0', 'template1')
      ```
      
    - List all tables in a specific database:
      ```sql
      SELECT table_name
      FROM information_schema.tables
      WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
      ```
      
    - Get column details for a specific table:
      ```sql
      SELECT column_name, data_type, is_nullable
      FROM information_schema.columns
      WHERE table_schema = 'public' AND table_name = '[TABLE_NAME]'
      ORDER BY ordinal_position
      ```
      
    - Discover relationships between tables:
      ```sql
      SELECT tc.constraint_name, kcu.column_name,
          ccu.table_schema AS foreign_table_schema,
          ccu.table_name AS foreign_table_name,
          ccu.column_name AS foreign_column_name
      FROM information_schema.table_constraints AS tc
      JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name
      JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
      WHERE tc.constraint_type = 'FOREIGN KEY'
          AND tc.table_schema = 'public'
          AND tc.table_name = '[TABLE_NAME]'
      ```
    
    REQUIRED PARAMETERS:
    - query: The SQL query to execute against the selected database
    - database: The database to query (can be any valid database from your discovery)
    
    COMMON DATABASE ACCESS:
    - Use "user_transactions" for customer and order management data
    - Use "defaultdb" for core product catalog data
    - Use "plazza_erp" for business operations data
    - Use "user_events" for user activity tracking data
    - You may discover other databases that are not listed here
    
    IMPORTANT BEST PRACTICES: 
    - Start by exploring the database schema to understand what's available
    - Document any new databases or tables you discover
    - When analyzing product data, include descriptive names along with IDs
    - Format your results in a clean, well-structured format
    - Filter out test data using appropriate WHERE clauses
    - Document your database schema findings to help future analysis
    """
    
    def _list_all_databases(self):
        """List all available databases in the CockroachDB cluster."""
        # Return cached result if available for memory-enabled agents
        global DB_SCHEMA_CACHE
        if 'all_databases' in DB_SCHEMA_CACHE:
            return DB_SCHEMA_CACHE['all_databases']
            
        result = ["Available databases in CockroachDB cluster:"]
        
        # Add the known databases from our mapping
        for db_name in DB_CONNECTION_VARS.keys():
            result.append(f"- {db_name}")
            
        # Use just one connection to discover all databases
        # Find the first available connection
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
            result.append("\nWarning: Could not connect to any database to discover additional databases.")
            return "\n".join(result)
        
        # Now use this single connection to discover all databases
        additional_dbs = set()
        try:
            with conn.cursor() as cursor:
                # Try to query system tables for other databases
                cursor.execute("SELECT datname FROM pg_database WHERE datname NOT IN ('postgres', 'template0', 'template1')")
                rows = cursor.fetchall()
                for row in rows:
                    if row[0] not in DB_CONNECTION_VARS and row[0] not in additional_dbs:
                        additional_dbs.add(row[0])
        except Exception as e:
            pass  # Silently fail, as we're just trying to discover
        finally:
            conn.close()
        
        # Add any additional discovered databases
        if additional_dbs:
            result.append("\nAdditional databases discovered (not directly accessible):")
            for db in sorted(additional_dbs):
                result.append(f"- {db}")
                
        result.append("\nNote: For executing queries, use one of the main databases listed at the top.")
        
        # Cache the result for future use
        output = "\n".join(result)
        DB_SCHEMA_CACHE['all_databases'] = output
        return output
        
    def _run(self, query: str, database: str) -> str:
        # Special case for listing all databases
        if query.strip().upper() == "SHOW DATABASES;":
            return self._list_all_databases()
            
        # Validate database parameter
        if database not in DB_CONNECTION_VARS:
            return f"Error: '{database}' is not a valid database. Choose from: {', '.join(DB_CONNECTION_VARS.keys())}"
        
        # Get the appropriate connection string
        connection_var = DB_CONNECTION_VARS[database]
        connection_string = os.getenv(connection_var)
        
        if not connection_string:
            return f"Error: Environment variable {connection_var} is not set"
        
        # Always apply test data filtering to any product-related query
        # This ensures consistent filtering regardless of query structure
        test_product_filter = (
            "product_id NOT LIKE '%TEST%' AND "
            "product_id NOT LIKE '%test%' AND "
            "product_id NOT LIKE 'p%' AND "
            "medicine_name NOT LIKE 'Test%' AND "
            "product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002') AND "
            "order_id NOT LIKE '%TEST%' AND "
            "order_id NOT LIKE 'POD-WEBHOOK%' AND "
            "bill_total_amount > 10"
        )
        
        # Check if this is a top products query for special handling
        is_top_products_query = False
        if ('SUM(quantity)' in query or 'sum(' in query.lower()) and 'GROUP BY' in query and 'ORDER BY' in query:
            is_top_products_query = True
            
            # Modify query to include medicine_name
            if 'medicine_name' not in query:
                # Replace GROUP BY product_id with GROUP BY product_id, medicine_name
                query = query.replace(
                    'GROUP BY product_id', 
                    'GROUP BY product_id, medicine_name'
                )
                
                # Replace SELECT product_id with SELECT product_id, medicine_name
                if 'SELECT product_id' in query:
                    query = query.replace(
                        'SELECT product_id', 
                        'SELECT product_id, medicine_name'
                    )
                
                # Apply test data filtering
                if 'WHERE' in query:
                    # Add test filters to existing WHERE clause
                    query = query.replace(
                        'WHERE', 
                        f"WHERE {test_product_filter} AND "
                    )
                else:
                    # Add new WHERE clause with test filters
                    before_group = query.split('GROUP BY')[0]
                    after_group = 'GROUP BY' + query.split('GROUP BY')[1]
                    query = f"{before_group} WHERE {test_product_filter} {after_group}"
            
        try:
            conn = psycopg2.connect(connection_string)
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                
                if not rows:
                    return f"No results found for query in {database} database"
                
                result_str = f"Results from {database} database:\n"
                
                # Special handling for top products query
                if is_top_products_query and 'medicine_name' in query:
                    filtered_rows = []
                    for row in rows:
                        row_dict = dict(row)
                        # Extra test data filter at display level
                        product_id = row_dict.get('product_id', '')
                        if product_id and (
                            'TEST' in product_id or 
                            'test' in product_id or 
                            product_id in ['MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2'] or
                            product_id.startswith('p')):
                            continue
                        filtered_rows.append(row_dict)
                    
                    # Display filtered rows
                    for row_dict in filtered_rows[:20]:
                        if 'product_id' in row_dict and 'medicine_name' in row_dict:
                            result_str += f"{{'product_id': '{row_dict['product_id']}', 'medicine_name': '{row_dict['medicine_name']}', 'total_quantity': {row_dict.get('total_quantity', row_dict.get('sum', 0))}}}\n"
                        else:
                            result_str += f"{row_dict}\n"
                else:
                    result_str += "\n".join([str(dict(row)) for row in rows[:20]])
                    
                if len(rows) > 20:
                    result_str += f"\n...and {len(rows) - 20} more rows"
                return result_str
                
        except Exception as e:
            return f"Error executing query on {database} database: {str(e)}"
        finally:
            if conn:
                conn.close()

class MethodologyTool(BaseTool):
    name: str = "MethodologyTool"
    description: str = """Execute, log, and document SQL queries with proper methodology reporting.
    
    This specialized tool helps you provide transparent, consistent query execution with methodology documentation.
    It addresses the need for better consistency and transparency in database queries by:
    1. Safely executing multiple queries independently (not using UNION for different tables)
    2. Always logging both the queries executed and the results received
    3. Properly handling NULL/None results
    4. Documenting when particular tables have no matching data
    5. Providing a clean summary of all query results
    
    USAGE:
    Use this tool when you need to perform multi-source analysis (like Airtable vs non-Airtable data)
    or when you need to clearly document your methodology for the user.
    
    REQUIRED PARAMETERS:
    - queries: A list of SQL query objects, where each object has:
      * "query": The SQL query to execute
      * "database": The database to run the query against (e.g., "user_transactions")
      * "description": A short description of what this query is checking
      
    EXAMPLE:
    ```
    [
      {
        "query": "SELECT SUM(bill_total_amount) AS total_sales FROM orders WHERE created_at >= '2025-03-01' AND created_at < '2025-04-01' AND status = 'paid';",
        "database": "user_transactions",
        "description": "Calculate March 2025 sales from regular orders"
      },
      {
        "query": "SELECT SUM(bill_total_amount) AS total_sales FROM airtable_orders WHERE created_at >= '2025-03-01' AND created_at < '2025-04-01' AND status = 'paid';",
        "database": "user_transactions",
        "description": "Calculate March 2025 sales from Airtable orders"
      }
    ]
    ```
    
    RESULTS INCLUDE:
    - A markdown formatted methodology section that documents all queries
    - The SQL queries used, formatted for readability
    - The results from each query, with clear labeling
    - A proper results summary that combines all data points
    - Clear indicators when a query returns no results
    """
    
    def _run(self, queries: list) -> str:
        """Execute multiple SQL queries and provide a methodology summary"""
        try:
            # Validate input
            if not queries or not isinstance(queries, list):
                return "Error: Please provide a list of query objects with query, database, and description fields."
            
            # Initialize results
            results = []
            query_results = []
            
            # Group queries by database to minimize connection creation
            queries_by_db = {}
            for i, query_obj in enumerate(queries):
                # Validate query object
                if not isinstance(query_obj, dict):
                    results.append(f"Error in query #{i+1}: Query object must be a dictionary.")
                    continue
                    
                if "query" not in query_obj or "database" not in query_obj:
                    results.append(f"Error in query #{i+1}: Missing required 'query' or 'database' field.")
                    continue
                
                database = query_obj["database"]
                if database not in queries_by_db:
                    queries_by_db[database] = []
                    
                queries_by_db[database].append({
                    "index": i,
                    "query": query_obj["query"],
                    "description": query_obj.get("description", f"Query #{i+1}"),
                    "original": query_obj
                })
            
            # Process queries grouped by database to reuse connections
            for database, db_queries in queries_by_db.items():
                # Validate database
                if database not in DB_CONNECTION_VARS:
                    for q in db_queries:
                        query_results.append({
                            "description": q["description"],
                            "database": database,
                            "sql": q["query"],
                            "has_results": False,
                            "error": f"Invalid database '{database}'. Choose from: {', '.join(DB_CONNECTION_VARS.keys())}"
                        })
                    continue
                
                # Get connection string
                connection_var = DB_CONNECTION_VARS[database]
                connection_string = os.getenv(connection_var)
                
                if not connection_string:
                    for q in db_queries:
                        query_results.append({
                            "description": q["description"],
                            "database": database,
                            "sql": q["query"],
                            "has_results": False,
                            "error": f"Environment variable {connection_var} is not set"
                        })
                    continue
                
                # Create a single connection for all queries to this database
                try:
                    conn = psycopg2.connect(connection_string)
                    
                    # Execute each query using the same connection
                    for q in db_queries:
                        try:
                            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                                cursor.execute(q["query"])
                                rows = cursor.fetchall()
                                
                                # Process query results
                                if rows and len(rows) > 0:
                                    # Convert to list of dictionaries for consistent handling
                                    row_dicts = [dict(row) for row in rows]
                                    first_row = row_dicts[0]
                                    
                                    # Check if this is an aggregate query (has SUM, COUNT, etc.)
                                    is_aggregate = any(col for col in first_row.keys() if any(agg in col.lower() for agg in ["sum", "count", "avg", "min", "max", "total"]))
                                    
                                    # For aggregate queries, we usually just want the first row
                                    if is_aggregate:
                                        query_results.append({
                                            "description": q["description"],
                                            "database": database,
                                            "sql": q["query"],
                                            "has_results": True,
                                            "is_aggregate": True,
                                            "result": first_row,
                                            "row_count": len(rows)
                                        })
                                    else:
                                        # For non-aggregate queries, include all rows (up to a limit)
                                        display_rows = row_dicts[:10]  # Limit to 10 rows for display
                                        query_results.append({
                                            "description": q["description"],
                                            "database": database,
                                            "sql": q["query"],
                                            "has_results": True,
                                            "is_aggregate": False,
                                            "result": display_rows,
                                            "row_count": len(rows),
                                            "limited_display": len(rows) > 10
                                        })
                                else:
                                    # Handle empty results
                                    query_results.append({
                                        "description": q["description"],
                                        "database": database,
                                        "sql": q["query"],
                                        "has_results": False,
                                        "result": None,
                                        "row_count": 0
                                    })
                        except Exception as e:
                            # Handle query execution errors
                            query_results.append({
                                "description": q["description"],
                                "database": database,
                                "sql": q["query"],
                                "has_results": False,
                                "error": str(e)
                            })
                except Exception as e:
                    # Connection error affects all queries for this database
                    for q in db_queries:
                        query_results.append({
                            "description": q["description"],
                            "database": database,
                            "sql": q["query"],
                            "has_results": False,
                            "error": f"Connection error: {str(e)}"
                        })
                finally:
                    if 'conn' in locals() and conn:
                        conn.close()
            
            # Create methodology summary
            methodology = self._format_methodology(query_results)
            return methodology
            
        except Exception as e:
            return f"Error executing queries: {str(e)}"
    
    def _format_methodology(self, query_results):
        """Format the query results into a methodology section"""
        # Create a concise summary for direct answers
        concise_summary = []
        
        # Create summary values for aggregate queries
        summary_values = {}
        for result in query_results:
            if result.get('has_results', False) and result.get('is_aggregate', False):
                for key, value in result['result'].items():
                    summary_key = f"{result['description']} ({key})"
                    summary_values[summary_key] = value
        
        # Generate concise summary first (1-2 lines)
        if summary_values:
            results_str = ", ".join([f"{desc.split('(')[0].strip()}: {val if val is not None else 'No data'}" 
                               for desc, val in summary_values.items()])
            concise_summary.append(f"{results_str}")
        
        # Check for empty or NULL results across all queries
        all_empty = all(not result.get('has_results', False) for result in query_results)
        if all_empty:
            concise_summary.append("No data found matching your criteria.")
        
        # Start detailed methodology section (only shown when requested)
        methodology = ["## Methodology\n"]
        methodology.append("I executed the following queries to answer your question:\n")
        
        # Add each query with its description and SQL
        for i, result in enumerate(query_results):
            # Add description header
            methodology.append(f"### {i+1}. {result['description']}\n")
            
            # Add database and SQL
            methodology.append(f"**Database:** `{result['database']}`\n")
            methodology.append("**SQL Query:**\n```sql\n" + result['sql'] + "\n```\n")
            
            # Add results section
            methodology.append("**Results:**\n")
            
            if "error" in result:
                methodology.append(f"❌ Error executing query: {result['error']}\n")
            elif not result['has_results']:
                methodology.append("ℹ️ This query returned no results (NULL or empty set)\n")
            else:
                if result.get('is_aggregate', False):
                    # Format aggregate results
                    methodology.append("```\n")
                    for key, value in result['result'].items():
                        methodology.append(f"{key}: {value if value is not None else 'NULL'}")
                    methodology.append("```\n")
                else:
                    # Format tabular results (limited rows)
                    if result['row_count'] > 0:
                        methodology.append(f"Found {result['row_count']} rows. ")
                        if result.get('limited_display', False):
                            methodology.append(f"Showing first 10 rows:\n")
                        else:
                            methodology.append("\n")
                            
                        methodology.append("```\n")
                        # Get the column names from the first row
                        if isinstance(result['result'], list) and len(result['result']) > 0:
                            first_row = result['result'][0]
                            columns = list(first_row.keys())
                            # Format header
                            header = " | ".join(columns)
                            separator = "-" * len(header)
                            methodology.append(header)
                            methodology.append(separator)
                            
                            # Format each row
                            for row in result['result']:
                                row_str = " | ".join([str(row[col] if row[col] is not None else "NULL") for col in columns])
                                methodology.append(row_str)
                        methodology.append("```\n")
        
        # Add summary section
        methodology.append("## Summary of Findings\n")
        
        # If we have aggregate results, summarize them
        if summary_values:
            methodology.append("Based on the queries executed:\n")
            for description, value in summary_values.items():
                methodology.append(f"- {description}: {value if value is not None else 'No data'}")
        else:
            methodology.append("No aggregate results found in the queries.")
        
        # Flag to identify if this is a methodology request
        methodology_requested = any(key.lower() in ['how', 'methodology', 'explain', 'detail'] 
                                  for result in query_results 
                                  for key in result.get('description', '').lower().split())
        
        # Return just the concise summary if methodology not requested
        if not methodology_requested and concise_summary:
            return "\n".join(concise_summary)
            
        # Otherwise return the full methodology
        return "\n".join(methodology)

class RetentionAnalysisTool(BaseTool):
    name: str = "RetentionAnalysisTool"
    description: str = """Perform comprehensive customer retention analysis across the Plazza ecosystem.
    
    This specialized tool analyzes customer retention patterns by:
    1. Filtering out test data and outliers
    2. Calculating key retention metrics (repeat rates, time between purchases)
    3. Identifying product categories that drive repeat purchases
    4. Analyzing the correlation between discounts and customer retention
    
    The tool performs multiple coordinated SQL queries and statistical analyses to provide a
    complete picture of customer retention dynamics.
    
    USAGE:
    Simply call this tool with no parameters to execute a full retention analysis.
    
    RESULTS INCLUDE:
    - Repeat vs one-time customer percentages (with test data filtered)
    - Average time between first and second purchases
    - Product categories that drive highest retention
    - Discount impact analysis on repeat purchase behavior
    - Customer lifecycle value estimates
    - Retention rate by cohort (when data available)
    
    VISUALIZATION:
    Automatically generates customer retention pie chart and other visualizations
    when appropriate, saving them to the visuals directory.
    """
    
    # Class-level cache for expensive retention analysis results
    _retention_cache = None
    
    def _run(self, generate_visuals=True) -> str:
        """
        Execute comprehensive retention analysis across databases
        
        Args:
            generate_visuals (bool): Whether to generate visualizations (default: True)
            
        Returns:
            str: Formatted retention analysis results
        """
        try:
            # Initialize analysis results
            results = []
            
            # Check if we have database access
            connection_string = os.getenv("DATABASE_URL_USER_TRANSACTIONS")
            if not connection_string:
                return "Error: Environment variable DATABASE_URL_USER_TRANSACTIONS is not set"
            
            # Connect to the database
            conn = psycopg2.connect(connection_string)
            
            # QUERY 1: Calculate clean repeat vs. one-time customer percentages
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                # Filter out test orders and customers
                cursor.execute("""
                SELECT 
                    COUNT(DISTINCT contact_id) as total_customers,
                    COUNT(DISTINCT CASE WHEN customer_order_count > 1 THEN contact_id END) as repeat_customers,
                    ROUND(COUNT(DISTINCT CASE WHEN customer_order_count > 1 THEN contact_id END)::numeric / 
                          NULLIF(COUNT(DISTINCT contact_id), 0)::numeric * 100, 1) as repeat_percentage
                FROM (
                    SELECT 
                        o.contact_id, 
                        COUNT(o.order_id) as customer_order_count
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    WHERE 
                        o.contact_id IS NOT NULL
                        AND o.status = 'paid'
                        AND o.order_id NOT LIKE '%TEST%'
                        AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                        AND oi.product_id NOT LIKE '%TEST%'
                        AND oi.product_id NOT LIKE '%test%'
                        AND oi.product_id NOT LIKE 'p%'
                        AND oi.medicine_name NOT LIKE 'Test%'
                        AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                        AND o.bill_total_amount > 10  -- Filter out very small test transactions
                    GROUP BY o.contact_id
                ) as customer_counts
                """)
                
                retention_data = cursor.fetchone()
                if retention_data:
                    results.append(f"## Customer Retention Analysis (Clean Data)\n")
                    results.append(f"Total unique customers: {retention_data['total_customers']}")
                    results.append(f"Repeat customers: {retention_data['repeat_customers']}")
                    results.append(f"One-time customers: {retention_data['total_customers'] - retention_data['repeat_customers']}")
                    results.append(f"Repeat customer percentage: {retention_data['repeat_percentage']}%")
                    results.append(f"One-time customer percentage: {100 - retention_data['repeat_percentage']}%\n")
            
            # QUERY 2: Calculate time between purchases
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                WITH filtered_orders AS (
                    SELECT 
                        o.contact_id, 
                        o.order_id,
                        o.created_at,
                        ROW_NUMBER() OVER (PARTITION BY o.contact_id ORDER BY o.created_at) as purchase_number
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    WHERE 
                        o.contact_id IS NOT NULL
                        AND o.status = 'paid'
                        AND o.order_id NOT LIKE '%TEST%'
                        AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                        AND oi.product_id NOT LIKE '%TEST%'
                        AND oi.product_id NOT LIKE '%test%'
                        AND oi.product_id NOT LIKE 'p%'
                        AND oi.medicine_name NOT LIKE 'Test%'
                        AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                        AND o.bill_total_amount > 10
                )
                SELECT
                    AVG(EXTRACT(DAY FROM (second_purchase.created_at - first_purchase.created_at))) as avg_days_between_purchases,
                    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY EXTRACT(DAY FROM (second_purchase.created_at - first_purchase.created_at))) as median_days_between_purchases
                FROM 
                    filtered_orders first_purchase
                JOIN 
                    filtered_orders second_purchase 
                    ON first_purchase.contact_id = second_purchase.contact_id
                    AND first_purchase.purchase_number = 1
                    AND second_purchase.purchase_number = 2
                """)
                
                time_data = cursor.fetchone()
                if time_data and time_data['avg_days_between_purchases'] is not None:
                    results.append(f"## Time Between Purchases\n")
                    results.append(f"Average days between first and second purchase: {time_data['avg_days_between_purchases']:.1f} days")
                    results.append(f"Median days between first and second purchase: {time_data['median_days_between_purchases']:.1f} days\n")
            
            # QUERY 3: Products that drive repeat purchases
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                WITH repeat_customers AS (
                    SELECT DISTINCT contact_id
                    FROM (
                        SELECT 
                            o.contact_id, 
                            COUNT(o.order_id) as order_count
                        FROM orders o
                        JOIN order_items oi ON o.order_id = oi.order_id
                        WHERE 
                            o.contact_id IS NOT NULL
                            AND o.status = 'paid'
                            AND o.order_id NOT LIKE '%TEST%'
                            AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                            AND oi.product_id NOT LIKE '%TEST%'
                            AND oi.product_id NOT LIKE '%test%'
                            AND oi.product_id NOT LIKE 'p%'
                            AND oi.medicine_name NOT LIKE 'Test%'
                            AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                            AND o.bill_total_amount > 10
                        GROUP BY o.contact_id
                        HAVING COUNT(o.order_id) > 1
                    ) as multi_purchasers
                ),
                first_purchase_products AS (
                    SELECT 
                        o.contact_id,
                        oi.product_id,
                        oi.medicine_name,
                        ROW_NUMBER() OVER (PARTITION BY o.contact_id ORDER BY o.created_at) as purchase_order
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    WHERE 
                        o.contact_id IN (SELECT contact_id FROM repeat_customers)
                        AND o.status = 'paid'
                        AND o.order_id NOT LIKE '%TEST%'
                        AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                        AND oi.product_id NOT LIKE '%TEST%'
                        AND oi.product_id NOT LIKE '%test%'
                        AND oi.product_id NOT LIKE 'p%'
                        AND oi.medicine_name NOT LIKE 'Test%'
                        AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                        AND o.bill_total_amount > 10
                )
                SELECT 
                    product_id,
                    medicine_name,
                    COUNT(*) as first_purchase_count,
                    ROUND((COUNT(*)::numeric / NULLIF((SELECT COUNT(*) FROM repeat_customers), 0)::numeric) * 100, 1) as percentage_of_repeat_customers
                FROM first_purchase_products
                WHERE purchase_order = 1
                GROUP BY product_id, medicine_name
                ORDER BY first_purchase_count DESC
                LIMIT 5
                """)
                
                driving_products = cursor.fetchall()
                if driving_products:
                    results.append(f"## Products Driving Repeat Purchases\n")
                    results.append(f"Products most commonly purchased in first orders by customers who later made repeat purchases:")
                    for i, product in enumerate(driving_products, 1):
                        results.append(f"{i}. Product: {product['medicine_name']} ({product['product_id']}), " +
                                     f"First-time purchases: {product['first_purchase_count']}, " +
                                     f"Present in {product['percentage_of_repeat_customers']}% of repeat customers' first orders")
                    results.append("")
            
            # QUERY 4: Discount impact on retention
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                WITH order_discounts AS (
                    SELECT 
                        o.contact_id,
                        o.order_id,
                        o.bill_total_amount,
                        o.item_total,
                        CASE 
                            WHEN o.item_total > 0 THEN (1 - (o.bill_total_amount / o.item_total)) * 100 
                            ELSE 0 
                        END as discount_percentage,
                        ROW_NUMBER() OVER (PARTITION BY o.contact_id ORDER BY o.created_at) as purchase_number
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    WHERE 
                        o.contact_id IS NOT NULL
                        AND o.status = 'paid'
                        AND o.order_id NOT LIKE '%TEST%'
                        AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                        AND oi.product_id NOT LIKE '%TEST%'
                        AND oi.product_id NOT LIKE '%test%'
                        AND oi.product_id NOT LIKE 'p%'
                        AND oi.medicine_name NOT LIKE 'Test%'
                        AND oi.product_id NOT IN ('MED001', 'TEST-MED-001', 'TEST001', 'TEST002', 'p1', 'p2')
                        AND o.bill_total_amount > 10
                        AND o.item_total > 0
                )
                SELECT
                    CASE 
                        WHEN discount_percentage = 0 THEN 'No discount'
                        WHEN discount_percentage > 0 AND discount_percentage <= 10 THEN '0-10% discount'
                        WHEN discount_percentage > 10 AND discount_percentage <= 20 THEN '10-20% discount'
                        WHEN discount_percentage > 20 THEN '20%+ discount'
                    END as discount_bracket,
                    COUNT(DISTINCT contact_id) as total_customers,
                    COUNT(DISTINCT CASE WHEN contact_id IN (
                        SELECT contact_id FROM order_discounts WHERE purchase_number > 1
                    ) THEN contact_id END) as returning_customers,
                    ROUND(COUNT(DISTINCT CASE WHEN contact_id IN (
                        SELECT contact_id FROM order_discounts WHERE purchase_number > 1
                    ) THEN contact_id END)::numeric / 
                    NULLIF(COUNT(DISTINCT contact_id), 0)::numeric * 100, 1) as retention_rate
                FROM order_discounts
                WHERE purchase_number = 1
                GROUP BY discount_bracket
                ORDER BY MIN(discount_percentage)
                """)
                
                discount_impact = cursor.fetchall()
                if discount_impact:
                    results.append(f"## Discount Impact on Retention\n")
                    results.append(f"Retention rates based on first purchase discount:")
                    for bracket in discount_impact:
                        results.append(f"- {bracket['discount_bracket']}: {bracket['retention_rate']}% retention rate " +
                                     f"({bracket['returning_customers']} returning out of {bracket['total_customers']} customers)")
                    results.append("")
            
            # Combine all results into a single string
            analysis_results = "\n".join(results)
            
            # Generate visualizations if requested
            if generate_visuals and retention_data:
                try:
                    # Generate visualizations using the retention analysis results
                    viz_results = self._generate_visualizations(analysis_results)
                    
                    # Add visualization paths to the results
                    if viz_results:
                        viz_info = "\n## Generated Visualizations\n"
                        for viz_type, viz_path in viz_results.items():
                            if viz_type != "enhanced_markdown":
                                viz_info += f"\n- {viz_type.replace('_', ' ').title()}: `{os.path.basename(viz_path)}`"
                        
                        # Add visualization information to the results
                        analysis_results += viz_info
                except Exception as viz_error:
                    # Log the error but continue with the analysis results
                    print(f"Error generating visualizations: {str(viz_error)}")
            
            # Store the results in the class-level cache for memory-enabled agents
            RetentionAnalysisTool._retention_cache = analysis_results
            
            return analysis_results
            
        except Exception as e:
            return f"Error performing retention analysis: {str(e)}"
        finally:
            if 'conn' in locals() and conn:
                conn.close()
                
    def _generate_visualizations(self, analysis_results):
        """
        Generate visualizations from retention analysis results
        
        Args:
            analysis_results (str): Formatted retention analysis text
            
        Returns:
            dict: Paths to generated visualization files
        """
        try:
            # Import the visualization functions
            from crewai_visualization import visualize_analysis_results, CustomerRetentionChartTool
            
            # First try the specialized Customer Retention Tool
            retention_tool = CustomerRetentionChartTool()
            retention_chart = retention_tool._run(analysis_results)
            
            # Then generate the full dashboard visualization
            viz_results = visualize_analysis_results(content=analysis_results, enable_json_output=True)
            
            return viz_results
        except Exception as e:
            print(f"Error in _generate_visualizations: {str(e)}")
            return None

# Modified Knowledge integration with direct file handling
def create_knowledge_source():
    """Create a knowledge source from the analysis results file with better error handling."""
    from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
    
    # Create empty knowledge object first as fallback
    empty_knowledge = Knowledge(
        collection_name="sales_analysis",
        sources=[]
    )
    
    # Directly use the knowledge directory path without importing constants
    # CrewAI expects files to be IN a directory called 'knowledge' at the root level
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    knowledge_dir = os.path.join(parent_dir, 'knowledge')
    knowledge_file = os.path.join(knowledge_dir, 'sales_analysis_results.md')
    
    # Create the knowledge directory if it doesn't exist
    os.makedirs(knowledge_dir, exist_ok=True)
    
    # Check if the file exists in knowledge directory
    if not os.path.exists(knowledge_file):
        print(f"Knowledge file not found at {knowledge_file}, checking for files to copy...")
        
        # Check for files to copy
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        possible_sources = [
            os.path.join(parent_dir, 'knowledge', 'sales_analysis_results.md'),
            ANALYSIS_RESULTS_PATH
        ]
        
        source_file = None
        for src in possible_sources:
            if os.path.exists(src):
                source_file = src
                break
        
        if source_file:
            print(f"Copying from {source_file} to {knowledge_file}")
            shutil.copy2(source_file, knowledge_file)
        else:
            print(f"No source files found, creating starter file")
            with open(knowledge_file, 'w') as f:
                f.write("# Sales Analysis Results\n\nThis is the initial knowledge file for Plazza Analytics.\n")
    
    # Check if the file exists now
    if not os.path.exists(knowledge_file):
        print(f"Failed to create or copy knowledge file to {knowledge_file}")
        return empty_knowledge
    
    try:
        print(f"Creating knowledge source from {knowledge_file}")
        
        # Use Path object instead of string to avoid CrewAI's path manipulation
        from pathlib import Path
        file_path = Path(knowledge_file)
        
        # Create knowledge source with the file path
        markdown_source = TextFileKnowledgeSource(
            file_paths=[file_path],  # Path object to avoid CrewAI's path manipulation
            chunk_size=800,
            chunk_overlap=200,
            metadata={"source": "sales_analysis", "date": os.path.getmtime(knowledge_file)}
        )
        
        # Create and return the knowledge object
        return Knowledge(
            collection_name="sales_analysis",
            sources=[markdown_source]
        )
    except Exception as e:
        print(f"Error creating knowledge source: {str(e)}")
        print("Using empty knowledge object instead")
        return empty_knowledge

# Create knowledge source
try:
    sales_knowledge = create_knowledge_source()
except Exception as e:
    print(f"Warning: Could not create knowledge source: {str(e)}")
    sales_knowledge = None

# Create the data analysis agent
data_analyst = Agent(
    role="Enterprise Data Analyst",
    goal="Maintain the business intelligence foundation of Plazza. You generate deep analytical reports on request and ensure that the Knowledge Base (KB) stays fully up to date.",
    backstory="""You are a senior data analyst embedded in Plazza's data team.
    Your job is to generate high-quality, structured analysis reports
    when no prior knowledge exists. You only trigger fresh discovery or
    SQL-based analysis when the knowledge base lacks the required insight.
    
    You NEVER overwrite existing valuable sections in the KB. You only append new
    structured analysis unless explicitly told otherwise. You're also responsible for
    formatting analysis into markdown, saving it to the KB, and surfacing new insights
    to other agents through the shared knowledge document.

    For retention insights, use the `RetentionAnalysisTool`. Do not attempt to compute
    retention yourself. You are not responsible for live Q&A. That job belongs to the
    Data Q&A Expert.
    
    Your primary responsibility is TWOFOLD:
    
    1. DATABASE SCHEMA DISCOVERY: Only when needed, explore and document database schemas by:
       - Discovering all available databases using information_schema queries
       - Mapping all tables within each database
       - Documenting column structures and relationships
       - Creating comprehensive schema documentation
       - Updating the knowledge base with your findings WITHOUT overwriting existing documentation
    
    2. BUSINESS ANALYSIS: With schema knowledge (preferably from the Knowledge Base), analyze the data to find:
       - Sales patterns and trends
       - Customer behavior insights
       - Product performance metrics
       - Business optimization opportunities
    
    You have several tools to accomplish your tasks:
    
    1. Your KNOWLEDGE BASE contains previous analysis results and schema documentation
       that will help guide your exploration and analysis. ALWAYS CHECK THIS FIRST.
       
    2. The CockroachDBTool lets you execute SQL queries to explore schema and analyze data.
       Use this ONLY when knowledge base information is insufficient.
       
    3. The PreviousAnalysisTool gives you access to historical analysis if needed.
    
    4. The RetentionAnalysisTool provides specialized customer retention metrics.
    
    5. The MethodologyTool allows you to run and document multiple SQL queries with
       structured methodology reporting. Use this for multi-source analysis.
       
    Format your output with clear documentation of any newly discovered database elements,
    followed by your business analysis. Structure your findings with clean sections and
    consistent data formats that will be easy for the Visualization Specialist to transform
    into visualizations.
    
    Use database queries sparingly and only to fill gaps.
    You are concise, data-driven, and explain findings with clear metrics.""",
    tools=[CockroachDBTool(), PreviousAnalysisTool(), RetentionAnalysisTool(), MethodologyTool()],
    llm=LLM(model="gpt-4o", temperature=0.2, max_tokens=4000),
    knowledge=sales_knowledge,
    verbose=False  # Disable verbose mode to hide thought process and just show final answer
)

# Create a specialized visualization agent
visualization_specialist = Agent(
    role="Data Visualization Expert",
    goal="Transform analytical insights into clear, compelling visualizations. Help decision makers quickly grasp key patterns from business data.",
    backstory="""You are the visual storytelling expert at Plazza. Your primary role
    is to read existing business analysis and turn it into the most
    impactful charts and graphs possible. You always check the shared
    Knowledge Base before attempting to generate any visualizations.

    You do not query databases or generate insights from raw data. You
    only work off confirmed and saved insights, usually prepared by the
    Enterprise Data Analyst or other agents.

    If the KB lacks structured findings, you defer visualization and return
    a message suggesting re-analysis via the Enterprise Data Analyst.

    You must always clearly label your visualizations, explain what they show,
    and structure your response so other agents or humans can drop them directly
    into dashboards or presentations.
    
    🎯 Your visualizations must:
    - Be accurate to the existing KB context
    - Include relevant titles, axis labels, and legends
    - Be optimized for business storytelling (e.g. highlighting trends, deltas, top performers)

    📦 All output visualizations should be saved as files and registered in the `knowledge/visuals` folder for reuse in future interactions.""",
    tools=[VisualizationTool()],
    llm=LLM(model="gpt-4o", temperature=0.3, max_tokens=4000),  # Slightly higher temperature for creativity
    knowledge=sales_knowledge,  # Shared knowledge with the analyst
    verbose=False  # Disable verbose mode to hide thought process and just show final answer
)

# 🚫 NOTE: The Business Strategy Advisor agent and related task logic have been moved to `plazza_strategy.py`
# Use: `from plazza_strategy import business_strategy_advisor` when you need to invoke strategic recommendations.

# Task creation functions - to be called on demand
def create_analysis_task(user_query=None):
    """
    Creates a dynamic analysis task based on user query.
    
    Args:
        user_query (str): Optional user query to focus the analysis on specific aspects
    
    Returns:
        Task: A task object configured with appropriate description
    """
    base_description = """
    Begin with knowledge base review, then analyze business data in the Plazza ecosystem.
    
    ## Knowledge Base First Approach - CRITICAL FIRST STEP

    Your FIRST and MOST IMPORTANT action is reviewing the existing knowledge base:
    
    1. Thoroughly examine the knowledge base for:
       - Existing schema documentation
       - Previous business analyses
       - Metrics and KPIs from prior runs
       - Historical trends and findings
    
    2. ONLY perform new database discovery if:
       - The knowledge base lacks schema information
       - Schema information appears outdated
       - The user specifically requests updated schema discovery
       - The user is asking about new tables not documented in KB
    
    3. When using KB information:
       - Cite the source timestamp when referencing KB data
       - Indicate if information might be outdated
       - Preserve all existing KB content when adding new findings
       - Use KB data preferentially over new queries
    
    ## Database Schema Discovery (ONLY IF KB LACKS THE INFO)
    
    If KB lacks schema information or the user requests schema update:
    
    1. Start with "SHOW DATABASES;" to list ALL available databases in the cluster
    
    2. For EACH database (user_transactions, defaultdb, plazza_erp, user_events, etc.), run:
       - Queries to list all tables in that specific database
       - Column structure and data types for each table
       - Relationships between tables (primary/foreign keys)
       
    3. Document findings in a dedicated "## Database Schema" section WITHOUT overwriting existing documentation
    
    ## Business Analysis (PREFER KB DATA OVER NEW QUERIES)
    
    Based on KB knowledge (preferred) or schema discovery (if needed), analyze business data focusing on:
    
    1. **Sales and Revenue Analysis**
       - Identify top-selling products and revenue drivers
       - Calculate key sales metrics (order value, frequency, etc.)
       - Look for sales patterns and trends
       
    2. **Customer Analysis**
       - Analyze customer retention and repeat purchase behavior
       - Segment customers based on behavior patterns
       - Use the RetentionAnalysisTool for specialized metrics
       
    3. **Product Analysis**
       - Evaluate product performance across categories
       - Identify inventory optimization opportunities
       - Analyze product relationships and customer preferences
    
    ## Output Format
    
    Structure your response in this order:
    
    1. **Knowledge Source** - Briefly indicate if you're using KB data, new queries, or both
    2. **Database Schema** - Reference existing KB schema or add new discoveries (never overwrite)
    3. **Business Analysis** - Your analysis of sales, customers, and products
    4. **Recommendations** - Actionable business recommendations based on your findings
    
    ## Knowledge Preservation and Response Style
    
    KNOWLEDGE MANAGEMENT:
    - NEVER overwrite existing KB content
    - ALWAYS append new findings under appropriate headers
    - When adding new data to KB, include timestamps and clear section headers
    - Preserve all historical context while adding new insights
    
    METHODOLOGY TRANSPARENCY:
    - Use the MethodologyTool for database queries only when KB data is insufficient
    - Document your methodology ONLY when specifically requested
    - Present your analysis with clear metrics and data points
    - Cite KB timestamps when referencing existing knowledge
    
    CONCISENESS RULE: Keep your final output concise and focused. Do not describe your thought process or reasoning unless specifically asked for it. Always focus on the data findings, not your methodology.
    """
    
    # Add user query focus if provided
    if user_query:
        user_focus = f"""
        ## User Query Focus
        
        The user has asked: "{user_query}"
        
        While conducting your comprehensive analysis, pay special attention to this query and ensure 
        your analysis provides specific insights related to this request. You should still perform the
        full schema discovery and analysis, but emphasize findings related to this specific question.
        """
        base_description += user_focus
    
    return Task(
        description=base_description,
        expected_output="""
        A comprehensive report including:
        
        1. Complete database schema documentation with all discovered databases and tables
        2. Highlighted new database elements not present in previous documentation
        3. Business analysis covering sales patterns, customer behavior, and product performance
        4. Data-driven recommendations for business optimization
        5. Methodology documentation ONLY if explicitly requested
        6. All findings presented in a well-structured format suitable for visualization
        """,
        agent=data_analyst
    )

# Sample visualization task function - to be called on demand
def create_visualization_task(analysis_content=None):
    """
    Creates a dynamic visualization task based on analysis content.
    
    Args:
        analysis_content (str): Optional analysis content to base visualizations on
    
    Returns:
        Task: A task object configured with appropriate description
    """
    base_description = """
    Use the Knowledge Base as your primary data source to create visualizations, adhering to Plazza brand guidelines.
    
    ## Knowledge Base Focus - CRITICAL FIRST STEP
    
    Your FIRST and MOST IMPORTANT action is to extract data from the Knowledge Base:
    
    1. Thoroughly examine the Knowledge Base for:
       - Existing business analyses
       - Key metrics and data points
       - Previous visualization approaches
       - Schema documentation and data structure information
    
    2. Extract data directly from the KB rather than triggering new database queries:
       - Parse metrics and numbers from previous analysis text
       - Use regex or pattern matching to extract structured data
       - Look for tables, lists, and formatted data in KB content
       - Reference timestamps to indicate data freshness
    
    3. ONLY request new data if:
       - The KB lacks essential metrics needed for visualization
       - The data in KB is clearly outdated
       - The specific visualization requested can't be created from KB data
    
    ## Visualization Development
    
    Create visualizations primarily using KB-extracted data:
    
    1. **Core Business Visualizations**:
       - Sales metrics visualizations from KB-extracted data
       - Customer metrics charts using KB-documented numbers
       - Product performance indicators based on KB analysis
       
    2. **Knowledge-Based Approach**:
       - Create visualizations directly from KB metrics and findings
       - Use existing schema documentation to understand data structure 
       - Preserve consistency with previous visualization approaches
       - Cite KB data source timestamps in visualization footnotes
    
    3. **Interactive Dashboard**:
       - Combine key metrics into a comprehensive dashboard
       - Organize visualizations in a logical flow
       - Include interactive elements for data exploration
       - Create insight cards summarizing key findings
       - Base all visualizations on KB-extracted data when possible
    
    ## Visualization Types
    
    Choose appropriate visualization types based on KB data:
    
    1. **Data Type Matching**:
       - Time series data → Line or area charts
       - Categorical comparisons → Bar or column charts
       - Part-to-whole relationships → Pie or donut charts
       - Distributions → Histograms or box plots
       - Geographic data → Map visualizations
       
    2. **Knowledge Extraction Approaches**:
       - Extract numerical data from KB analysis text
       - Parse tables and lists in KB for structured data
       - Use described relationships to determine chart structure
       - Maintain consistency with previous visualizations
    
    ## Plazza Brand Guidelines
    
    Apply consistent Plazza styling to all visualizations:
    
    1. **Color Palette**:
       - Primary: #FF0084 (bright pink) - Use for titles, important values, and highlights
       - Background: #fafafa (light gray) - Use for page backgrounds
       - Card Background: white - Use for cards and widget backgrounds
       - Text: Dark gray (#333) for body text, #666 for secondary text
    
    2. **UI Components**:
       - Card-based layout with rounded corners (12px radius)
       - Clean grid system for organizing content
       - Large, bold numbers for KPI values (using Plazza pink)
       - Insight cards with highlighted titles
    
    ## Output Format
    
    Generate all visualizations using the VisualizationTool, which will:
    
    1. Extract data primarily from KB content, not databases
    2. Create appropriately styled Plazza visualizations
    3. Generate an interactive dashboard with Plazza branding
    4. Save all files to the visuals directory
    
    In your final report, briefly explain your visualization approach and cite the KB sources used.
    Focus on the visualizations themselves rather than detailed methodology.
    """
    
    # Add specific analysis content reference if provided
    if analysis_content:
        content_reference = f"""
        ## Analysis Reference
        
        Base your visualizations on the following analysis:
        
        {analysis_content}
        
        Focus on creating visualizations that best represent the key insights from this analysis,
        while ensuring all data points are clearly visualized.
        """
        base_description += content_reference
    
    return Task(
        description=base_description,
        expected_output="""
        A comprehensive set of adaptive visualizations including:
        
        1. Visualizations for both standard and newly discovered data elements
        2. An interactive business metrics dashboard integrating all key insights
        3. Appropriate chart types selected based on data characteristics
        4. Clear documentation of visualization strategy for new data structures
        5. All visualizations styled according to Plazza brand guidelines
        6. Brief explanation of how visualizations adapt to the discovered schema
        """,
        agent=visualization_specialist
    )

# 🚫 NOTE: The Business Strategy Advisor agent and related task logic have been moved to `plazza_strategy.py`
# Use: `from plazza_strategy import create_strategy_task` when you need to invoke strategic recommendations.

def save_analysis_results(content, filepath=ANALYSIS_RESULTS_PATH):
    """
    Save the analysis results to a file for future reference.
    Also saves a copy to the knowledge directory for RAG, preserving history
    by appending each new analysis instead of overwriting.
    
    Args:
        content (str or CrewOutput): The analysis results to save
        filepath (str): The path to save the results to
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Add timestamp and metadata to help with retrieval
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Convert CrewOutput to string if needed
        if hasattr(content, 'raw'):
            content = content.raw
            
        # Format the content with clear section headers
        if isinstance(content, str) and not content.startswith("# "):
            content = f"# Sales Analysis Results - {timestamp}\n\n{content}"
        
        # Save to main filepath - this can still be a complete overwrite
        # as the filepath is primarily used for the current run's results
        with open(filepath, 'w') as file:
            file.write(str(content))
        print(f"Analysis results saved to {filepath}")
        
        # For the knowledge file, we want to APPEND rather than overwrite
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        knowledge_file = os.path.join(parent_dir, 'knowledge', 'sales_analysis_results.md')
        knowledge_dir = os.path.join(parent_dir, 'knowledge')
        os.makedirs(knowledge_dir, exist_ok=True)
        
        # Create a formatted header for the new content
        header = f"\n\n---\n\n## Full Analysis on {timestamp}\n\n"
        formatted_content = str(content)
        
        # If this is a new file, don't add the separator header
        if not os.path.exists(knowledge_file) or os.path.getsize(knowledge_file) == 0:
            # For new file, skip the header
            with open(knowledge_file, 'w') as file:
                file.write(formatted_content)
        else:
            # For existing file, append with header
            # First check if this exact content already exists to avoid duplication
            with open(knowledge_file, 'r') as file:
                existing_content = file.read()
                
            # Only append if the content isn't already in the file
            if formatted_content not in existing_content:
                with open(knowledge_file, 'a') as file:
                    file.write(header)
                    # Remove the header from the content if it exists to avoid duplication
                    if formatted_content.startswith("# Sales Analysis Results"):
                        # Get everything after the first line
                        content_without_header = "\n".join(formatted_content.split("\n")[1:])
                        file.write(content_without_header)
                    else:
                        file.write(formatted_content)
            else:
                print("Content already exists in knowledge file, skipping append")
                
        print(f"Analysis results appended to {knowledge_file} for RAG integration")
        
    except Exception as e:
        print(f"Error saving analysis results: {str(e)}")

# Example of how to execute tasks on demand (not executed on import)
def run_analysis(user_query=None):
    """
    Run a full analysis on demand based on optional user query.
    
    Args:
        user_query (str): Optional user query to focus the analysis
        
    Returns:
        str: The results of the analysis
    """
    # Create dynamic task based on user query
    analysis_task = create_analysis_task(user_query)
    
    # Execute analysis task
    analysis_result = data_analyst.execute_task(analysis_task)
    
    # Create visualization task based on analysis result
    visualization_task = create_visualization_task(analysis_result)
    
    # Execute visualization task
    visualization_result = visualization_specialist.execute_task(visualization_task)
    
    # Combine results
    combined_result = f"{analysis_result}\n\n## Visualizations\n\n{visualization_result}"
    
    # Save results
    save_analysis_results(combined_result)
    
    return combined_result

# For command-line usage (not executed on import)
if __name__ == "__main__":
    import sys
    from datetime import datetime
    
    # If command line argument is provided, use it as query
    user_query = None
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
        
    print(f"\n{'='*50}")
    print(f"Plazza Analytics - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")
        
    if user_query:
        print(f"Running analysis with query: {user_query}")
    else:
        print("Running full analysis without specific query focus")
        
    print("\nThis may take a few minutes. Please wait...\n")
    
    # Run analysis with optional user query
    result = run_analysis(user_query)
    
    # Display completion message
    print("\n✅ Analysis complete!")
    print(f"Results saved to: {ANALYSIS_RESULTS_PATH}")
    print(f"And to knowledge directory for future reference\n")
    
    # Display abbreviated results (first few lines)
    print("\nAnalysis Summary (first 10 lines):")
    print("\n".join(result.split("\n")[:10]))
    print("...\n")
    
    # Provide next steps
    print("Next steps:")
    print("1. Use 'python Core_Scripts/plazza_chat.py' for interactive queries")
    print("2. View full results in the files mentioned above")
    print("3. Check the visualizations directory for charts and dashboards\n")