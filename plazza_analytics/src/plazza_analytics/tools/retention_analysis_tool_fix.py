import os
import psycopg2
import psycopg2.extras
import json
import re
from datetime import datetime
from typing import Literal, Optional, Dict, Any, List
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Version History
# 2025-03-26: Updated for CrewAI v0.108.0+ compatibility
#   - Added parameter validation with proper type hints
#   - Updated run method to use **kwargs pattern for compatibility
#   - Added enhanced error handling and debug logging
#   - Added parameter validation for query_intent and limit
#   - Added proper fallback mechanisms for invalid parameter values
#   - Enhanced documentation with comprehensive docstrings
# 2025-03-27: Fixed Pydantic compatibility issues
#   - Modified to work properly with CrewAI v0.108.0 
#   - Used approach similar to other working tools in the project
#   - Removed custom schema classes
#   - Enhanced parameter validation with defensive coding
#   - Simplified implementation while maintaining functionality
# 2025-03-28: Fixed recurring issues
#   - Added consistent type casting for contact_id fields
#   - Enhanced test data filtering with phone/email patterns
#   - Fixed contact details retrieval with proper joins
#   - Added better error handling and troubleshooting guidance
#   - Added helper to detect and exclude test users

# Module-level caches for performance
_retention_cache = None  # Cached results for reuse
_schema_cache = {}  # Schema information for each table

# Database connection configuration (moved to module level for reuse)
DB_CONNECTION_VARS = {
    "user_transactions": "DATABASE_URL_USER_TRANSACTIONS",
    "defaultdb": "DATABASE_URL",
    "plazza_erp": "DATABASE_URL_ERP",
    "user_events": "DATABASE_URL_USER"
}

# Known test data patterns
TEST_PHONE_NUMBERS = {'8850959517', '9999999999', '9876543210', '0000000000'}
TEST_EMAIL_PATTERNS = ['test', 'example.com', 'noreply', 'nowhere']
TEST_ORDER_PATTERNS = ['TEST', 'POD-WEBHOOK', 'POD-TEST']

# Schema-level cache and DB_SCHEMA_CACHE for caching schema info across runs
DB_SCHEMA_CACHE = {}

# Create Pydantic schema for tool parameters
class RetentionAnalysisArgs(BaseModel):
    generate_visuals: bool = Field(
        default=True, 
        description="Whether to generate visualizations"
    )
    force_refresh: bool = Field(
        default=False, 
        description="Force a refresh of the analysis, ignoring the cache"
    )
    query_intent: Literal["general", "repeat_customers"] = Field(
        default="general", 
        description="Type of analysis to perform ('general' or 'repeat_customers')"
    )
    limit: int = Field(
        default=10, 
        description="Maximum number of results to return for detailed queries",
        ge=1,
        le=100
    )
    include_contact_details: bool = Field(
        default=False, 
        description="Whether to include customer names and contact information"
    )

class RetentionAnalysisTool(BaseTool):
    """Retention Analysis Tool for CrewAI.
    
    This tool performs comprehensive retention analysis across regular and Airtable data sources.
    """
    name: str = "RetentionAnalysisTool"
    description: str = """Perform comprehensive customer retention analysis across ALL data sources in the Plazza ecosystem.
    Analyzes BOTH regular tables AND Airtable tables to provide a complete view of customer behavior.
    Calculates repeat rates, time between purchases, top products, and discount impact.
    NOW FEATURES:
    1. Automatic schema discovery to adapt to different table structures
    2. Safe fallback mechanisms for missing columns
    3. Complete integration of both regular tables AND Airtable tables
    4. Indian Rupee (₹) formatting for all monetary values
    5. Robust error handling with clear explanations
    
    USAGE OPTIONS:
    - generate_visuals: Whether to generate visualizations (default: True)
    - query_intent: Type of analysis ("general" or "repeat_customers")
    - include_contact_details: Include customer names and contact information (with repeat_customers intent)
    - limit: Maximum number of results to return (default: 10)
    
    EXAMPLES:
    - Standard retention metrics: retention_analysis_tool.run()
    - Find repeat customers: retention_analysis_tool.run(query_intent="repeat_customers")
    - Customer details: retention_analysis_tool.run(query_intent="repeat_customers", include_contact_details=True)
    - Limit results: retention_analysis_tool.run(query_intent="repeat_customers", limit=5)"""
    
    # Important: define args_schema for CrewAI v0.108.0+ compatibility
    # Make sure it's properly annotated to avoid Pydantic errors
    args_schema: type[RetentionAnalysisArgs] = RetentionAnalysisArgs
    
    def run(self, 
            generate_visuals: bool = True, 
            force_refresh: bool = False,
            query_intent: str = "general",
            limit: int = 10,
            include_contact_details: bool = False,
            **kwargs):
        """Run comprehensive retention analysis on the user_transactions database.
        
        Args:
            generate_visuals: Whether to generate visualizations (default: True)
            force_refresh: Force a refresh of the analysis, ignoring the cache (default: False)
            query_intent: Type of analysis to perform ("general", "repeat_customers", etc.)
            limit: Maximum number of results to return for detailed queries (default: 10)
            include_contact_details: Whether to include customer names and contact information (default: False)
        
        Returns:
            str: Formatted retention analysis results.
        """
        global _retention_cache, _schema_cache
        
        try:
            print(f"RetentionAnalysisTool called with parameters: generate_visuals={generate_visuals}, "
                  f"force_refresh={force_refresh}, query_intent={query_intent}, "
                  f"limit={limit}, include_contact_details={include_contact_details}")
            
            # Parameter validation
            # Validate query_intent
            if query_intent not in ["general", "repeat_customers"]:
                print(f"WARNING: Invalid query_intent '{query_intent}'. Falling back to 'general'.")
                query_intent = "general"
                
            # Validate limit
            try:
                limit = int(limit)
                if limit < 1:
                    print(f"WARNING: limit {limit} is too small. Setting to 1.")
                    limit = 1
                elif limit > 100:
                    print(f"WARNING: limit {limit} is too large. Setting to 100.")
                    limit = 100
            except (ValueError, TypeError):
                print(f"WARNING: Invalid limit '{limit}'. Falling back to default (10).")
                limit = 10
                
            # Reset cache if forcing refresh or changing analysis type
            if force_refresh or query_intent != "general":
                _retention_cache = None
                print("Cache reset due to force_refresh or non-general query_intent")
            else:
                print("Using standard cache policy")
                
            # Use cache only for general analysis
            if query_intent == "general" and not force_refresh and _retention_cache:
                print("Returning cached results")
                return _retention_cache
            
            print("Executing _run with extracted parameters")
            return self._run(
                generate_visuals=generate_visuals,
                force_refresh=force_refresh,
                query_intent=query_intent,
                limit=limit,
                include_contact_details=include_contact_details
            )
        except Exception as e:
            error_message = f"ERROR in RetentionAnalysisTool.run: {str(e)}"
            print(error_message)
            import traceback
            print(traceback.format_exc())
            return error_message

    def _run(self, generate_visuals: bool = True, force_refresh: bool = False, 
             query_intent: str = "general", limit: int = 10, include_contact_details: bool = False) -> str:
        """Run comprehensive retention analysis on the user_transactions database.
        
        This is the internal implementation method called by run() after parameter processing.
        
        Args:
            generate_visuals (bool): Whether to generate visualizations (default: True)
            force_refresh (bool): Force a refresh of the analysis, ignoring the cache (default: False)
            query_intent (str): Type of analysis to perform ("general", "repeat_customers")
            limit (int): Maximum number of results to return for detailed queries (default: 10)
            include_contact_details (bool): Whether to include customer names and contact information (default: False)
        
        Returns:
            str: Formatted retention analysis results
        
        Raises:
            Exception: If database connection fails or analysis encounters an error
        """
        global _retention_cache, _schema_cache
        conn = None
        
        try:
            # Parameter validation
            if query_intent not in ["general", "repeat_customers"]:
                return f"""❌ Error: Invalid query_intent: '{query_intent}'
                
Please use one of the following supported values:
- "general": Standard retention metrics (repeat rate, time between purchases, etc.)
- "repeat_customers": Detailed list of repeat customers with purchase history

Example usage:
retention_analysis_tool.run(query_intent="repeat_customers", include_contact_details=True, limit=10)
"""
            
            print(f"RetentionAnalysisTool._run started with: query_intent={query_intent}, "
                  f"include_contact_details={include_contact_details}, limit={limit}")
            
            # Start building results
            results = []
            
            # Get database connection
            conn_str = os.getenv(DB_CONNECTION_VARS["user_transactions"])
            if not conn_str:
                return "❌ DATABASE_URL_USER_TRANSACTIONS not set"

            print("Connecting to database...")
            conn = psycopg2.connect(conn_str)
            
            # STEP 1: Schema Discovery - this is always needed
            print("Beginning schema discovery...")
            schema_info = self._discover_schema(conn)
            if "error" in schema_info:
                return f"❌ Schema discovery failed: {schema_info['error']}"
            
            print(f"Schema discovery completed. Found {len(schema_info['tables'])} tables.")
            
            # Build the schema graph for relationship analysis    
            print("Building schema relationship graph...")
            graph = self._build_schema_graph(schema_info)
            print(f"Relationship graph built with {len(graph)} nodes.")
                
            # Check the query intent to determine what to do
            if query_intent == "repeat_customers":
                # Special case: Repeat customers with details
                print(f"Processing repeat customers query with include_contact_details={include_contact_details}, limit={limit}")
                return self._process_repeat_customers_query(conn, schema_info, limit, include_contact_details)
            else:
                # Default behavior: Full retention analysis
                print("Processing general retention query")
                result = self._process_general_retention_query(conn, schema_info)
                
                # Cache the result for future use (only for general analysis)
                _retention_cache = result
                return result
                
        except Exception as e:
            detailed_error = f"""❌ Retention analysis failed: {str(e)}

## Troubleshooting Information
- Error type: {type(e).__name__}
- Error details: {str(e)}
- Query intent: {query_intent}
- Include contact details: {include_contact_details}
- Limit: {limit}
- Occurred during comprehensive retention analysis
- The tool attempted schema discovery but encountered an error during query execution

### Recommendation
This is likely due to one of the following issues:
1. Schema differences between regular and Airtable tables
2. Missing tables or columns required for the analysis
3. Type compatibility issues in SQL UNION operations
4. Parameter validation issues with the CrewAI tool schema

Please try running individual SQL queries via the CockroachDBTool to identify specific schema issues."""
            print(f"ERROR in _run method: {str(e)}")
            import traceback
            print(traceback.format_exc())
            return detailed_error
        finally:
            if conn:
                try:
                    conn.close()
                    print("Database connection closed.")
                except Exception as close_error:
                    print(f"Warning: Error closing database connection: {str(close_error)}")

    def _discover_schema(self, conn):
        """Discover and cache the schema for relevant tables in user_transactions database.
        
        This enhanced version:
        1. Discovers all tables in the public schema
        2. Extracts column information for each table
        3. Detects relationships between tables based on naming conventions and PK/FK
        4. Builds a schema graph for finding optimal join paths
        5. Counts records to provide volume metrics
        
        Returns:
            Dictionary with schema information and relationships
        """
        import re
        
        # Store both schema info and relationship graph
        schema_info = {
            "tables": {},
            "relationships": [],
            "counts": {}
        }
        
        try:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                # Get all tables in the public schema
                cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                  AND table_type = 'BASE TABLE'
                ORDER BY table_name
                """)
                existing_tables = [row['table_name'] for row in cursor.fetchall()]
                
                # For each existing table, get its column structure
                for table in existing_tables:
                    cursor.execute(f"""
                    SELECT column_name, data_type, is_nullable
                    FROM information_schema.columns
                    WHERE table_schema = 'public' AND table_name = '{table}'
                    ORDER BY ordinal_position
                    """)
                    columns = {row['column_name']: {
                        'data_type': row['data_type'],
                        'is_nullable': row['is_nullable']
                    } for row in cursor.fetchall()}
                    
                    # Check primary key if possible
                    try:
                        cursor.execute(f"""
                        SELECT a.attname
                        FROM pg_index i
                        JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
                        WHERE i.indrelid = '{table}'::regclass AND i.indisprimary;
                        """)
                        pk_rows = cursor.fetchall()
                        if pk_rows:
                            primary_keys = [row[0] for row in pk_rows]
                            columns['__primary_key__'] = primary_keys
                    except Exception:
                        # If we can't determine PK, just continue
                        pass
                    
                    schema_info["tables"][table] = columns
                
                # Get record counts for important tables
                for table in existing_tables:
                    if any(pattern in table for pattern in ['orders', 'contact', 'customer', 'product']):
                        try:
                            # For orders tables, count paid orders
                            if 'orders' in table:
                                cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE status = 'paid'")
                            else:
                                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                            row = cursor.fetchone()
                            if row:
                                schema_info["counts"][table] = row[0]
                        except Exception:
                            schema_info["counts"][table] = "unknown"
                
                # Discover relationships based on naming conventions (since CockroachDB doesn't expose FK constraints well)
                for table in existing_tables:
                    table_cols = schema_info["tables"][table].keys()
                    
                    # Look for columns that might be foreign keys (ending with _id)
                    for col in table_cols:
                        if col.endswith('_id') and col != 'id':
                            # Extract the target table name (remove _id suffix)
                            target_table_name = col[:-3]  # Remove _id
                            
                            # Handle plural to singular conversion for common tables
                            singular_name = target_table_name
                            if target_table_name.endswith('s'):
                                singular_name = target_table_name[:-1]
                            
                            # Check both singular and plural forms
                            for potential_table in [target_table_name, singular_name, target_table_name + 's']:
                                if potential_table in existing_tables:
                                    # Found a potential relationship
                                    schema_info["relationships"].append({
                                        "source_table": table,
                                        "source_column": col,
                                        "target_table": potential_table,
                                        "target_column": "id",  # Assume the target column is 'id'
                                        "relationship_type": "foreign_key"
                                    })
                                    break
                
                # Special handling for pairs like 'contact' and 'contact_phones'
                # For tables like contact_phones, contact_addresses, etc.
                for table in existing_tables:
                    parts = table.split('_')
                    if len(parts) > 1:
                        base_table = parts[0]
                        if base_table in existing_tables:
                            # Check if this table has a column matching base_table_id
                            fk_col = f"{base_table}_id"
                            if fk_col in schema_info["tables"][table]:
                                schema_info["relationships"].append({
                                    "source_table": table,
                                    "source_column": fk_col,
                                    "target_table": base_table,
                                    "target_column": "id",
                                    "relationship_type": "foreign_key"
                                })
                
                # Add special relationships for common table pairs we know about
                known_relationships = [
                    # Order items relationship
                    {"source_table": "order_items", "source_column": "order_id", 
                     "target_table": "orders", "target_column": "order_id"},
                    {"source_table": "airtable_order_items", "source_column": "order_id", 
                     "target_table": "airtable_orders", "target_column": "order_id"},
                    
                    # Contact relationships
                    {"source_table": "orders", "source_column": "contact_id", 
                     "target_table": "contacts", "target_column": "id"},
                    {"source_table": "airtable_orders", "source_column": "contact_id", 
                     "target_table": "airtable_contacts", "target_column": "id"},
                    
                    # Product relationships
                    {"source_table": "order_items", "source_column": "product_id", 
                     "target_table": "products", "target_column": "product_id"},
                    {"source_table": "airtable_order_items", "source_column": "product_id", 
                     "target_table": "airtable_products", "target_column": "product_id"},
                     
                    # Contact phone relationships
                    {"source_table": "contact_phones", "source_column": "contact_id", 
                     "target_table": "contacts", "target_column": "id"},
                    {"source_table": "airtable_contact_phones", "source_column": "contact_id", 
                     "target_table": "airtable_contacts", "target_column": "id"}
                ]
                
                # Add the known relationships if both tables exist
                for rel in known_relationships:
                    if (rel["source_table"] in existing_tables and 
                        rel["target_table"] in existing_tables):
                        schema_info["relationships"].append({
                            **rel,
                            "relationship_type": "known_relation"
                        })
            
            # Cache the schema information
            global _schema_cache
            _schema_cache = schema_info
            return schema_info
            
        except Exception as e:
            return {"error": str(e)}

    def _build_schema_graph(self, schema_info):
        """Build a directed graph from the schema relationships for join path inference."""
        # This is a simplified version that doesn't require networkx
        # For a production system, consider using networkx for more advanced graph algorithms
        
        # Create a graph data structure {node: [neighbors]}
        graph = {}
        
        # Initialize all tables as nodes
        for table in schema_info["tables"].keys():
            graph[table] = []
        
        # Add edges based on relationships
        for relation in schema_info["relationships"]:
            source = relation["source_table"]
            target = relation["target_table"]
            
            # Add bidirectional edges - we can traverse relationships in both directions
            # In a real graph implementation, we'd store edge attributes
            if source in graph:
                graph[source].append({
                    "table": target,
                    "join_condition": f"{source}.{relation['source_column']} = {target}.{relation['target_column']}"
                })
            else:
                graph[source] = [{
                    "table": target,
                    "join_condition": f"{source}.{relation['source_column']} = {target}.{relation['target_column']}"
                }]
                
            # Add the reverse direction too for simpler path finding
            if target in graph:
                graph[target].append({
                    "table": source,
                    "join_condition": f"{target}.{relation['target_column']} = {source}.{relation['source_column']}"
                })
            else:
                graph[target] = [{
                    "table": source,
                    "join_condition": f"{target}.{relation['target_column']} = {source}.{relation['source_column']}"
                }]
        
        return graph
        
    def _find_join_path(self, graph, start_table, end_table):
        """Find a path between two tables for generating JOINs."""
        # Simple BFS implementation to find shortest path
        if start_table not in graph or end_table not in graph:
            return None
            
        visited = {start_table}
        queue = [(start_table, [])]  # (node, path_so_far)
        
        while queue:
            (node, path) = queue.pop(0)
            
            # Check all neighbors
            for neighbor in graph[node]:
                next_table = neighbor["table"]
                join_condition = neighbor["join_condition"]
                
                if next_table == end_table:
                    # Found our destination
                    return path + [{"from": node, "to": next_table, "condition": join_condition}]
                    
                if next_table not in visited:
                    visited.add(next_table)
                    queue.append((next_table, path + [{"from": node, "to": next_table, "condition": join_condition}]))
        
        # No path found
        return None

    def _is_test_data(self, data, field_name, test_patterns):
        """Check if a field contains test data patterns."""
        if field_name not in data or data[field_name] is None:
            return False
            
        value = str(data[field_name]).lower()
        return any(pattern.lower() in value for pattern in test_patterns)
        
    def _is_test_user(self, row):
        """Check if a user record is test data based on various indicators."""
        # Check known test phone numbers
        phone = str(row.get('phone_number', '')) if row.get('phone_number') else ""
        if phone in TEST_PHONE_NUMBERS:
            return True
            
        # Check email for test patterns
        email = str(row.get('email', '')) if row.get('email') else ""
        if any(pattern in email.lower() for pattern in TEST_EMAIL_PATTERNS):
            return True
            
        # Check order patterns
        order_id = str(row.get('order_id', '')) if row.get('order_id') else ""
        if any(pattern in order_id for pattern in TEST_ORDER_PATTERNS):
            return True
            
        # Additional test user detection - check for common test names
        first_name = str(row.get('first_name', '')).lower() if row.get('first_name') else ""
        last_name = str(row.get('last_name', '')).lower() if row.get('last_name') else ""
        if first_name in ['test', 'dummy', 'example'] or last_name in ['test', 'dummy', 'example']:
            return True
            
        return False

    def _generate_safe_discount_query(self, schema_info):
        """Generate a discount query that safely handles missing columns."""
        # Check if item_total exists in both tables
        tables_info = schema_info.get("tables", {})
        orders_has_item_total = 'item_total' in tables_info.get('orders', {})
        airtable_has_item_total = 'item_total' in tables_info.get('airtable_orders', {})
        
        regular_orders_cte = """
        -- Regular orders discount data
        SELECT 
            CAST(contact_id AS text) AS contact_id,
            CASE 
                WHEN item_total > 0 THEN (1 - bill_total_amount / NULLIF(item_total, 0)) * 100
                ELSE 0 
            END as discount_pct
        FROM orders o
        LEFT JOIN contacts c ON o.contact_id = c.id
        WHERE o.status = 'paid'
          AND o.order_id NOT LIKE '%TEST%'
          AND o.order_id NOT LIKE 'POD-WEBHOOK%'
          AND (c.phone IS NULL OR c.phone NOT IN ('8850959517', '9999999999', '9876543210'))
          AND (c.email IS NULL OR c.email NOT ILIKE '%test%')
        """
        
        # For Airtable, we need to adapt to the possibility that item_total doesn't exist
        if not airtable_has_item_total:
            # If no item_total in Airtable, need to calculate it from order_items
            airtable_orders_cte = """
            -- Airtable orders discount data with calculated item_total
            SELECT 
                CAST(ao.contact_id AS text) AS contact_id,
                CASE 
                    WHEN calculated_total > 0 THEN (1 - ao.bill_total_amount / NULLIF(calculated_total, 0)) * 100
                    ELSE 0 
                END as discount_pct
            FROM airtable_orders ao
            LEFT JOIN airtable_contacts ac ON ao.contact_id = ac.id
            LEFT JOIN (
                SELECT order_id, SUM(COALESCE(selling_price * quantity, 0)) as calculated_total
                FROM airtable_order_items
                GROUP BY order_id
            ) items ON ao.order_id = items.order_id
            WHERE ao.status = 'paid'
              AND ao.order_id NOT LIKE '%TEST%'
              AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
              AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
              AND items.calculated_total IS NOT NULL
            """
        else:
            # If item_total exists in Airtable, use it directly
            airtable_orders_cte = """
            -- Airtable orders discount data
            SELECT 
                CAST(ao.contact_id AS text) AS contact_id,
                CASE 
                    WHEN item_total > 0 THEN (1 - bill_total_amount / NULLIF(item_total, 0)) * 100
                    ELSE 0 
                END as discount_pct
            FROM airtable_orders ao
            LEFT JOIN airtable_contacts ac ON ao.contact_id = ac.id
            WHERE ao.status = 'paid'
              AND ao.order_id NOT LIKE '%TEST%'
              AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
              AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
              AND item_total IS NOT NULL
            """
        
        # Build the complete query with both CTEs
        if orders_has_item_total:
            regular_part = regular_orders_cte
        else:
            regular_part = """-- Regular orders skipped due to missing item_total column
    SELECT NULL as contact_id, NULL as discount_pct WHERE 1=0"""
            
        combined_discount_query = f"""
        WITH combined_discount_data AS (
            {regular_part}
            
            UNION ALL
            
            {airtable_orders_cte}
        )
        
        -- Aggregate by discount bracket
        SELECT 
            ROUND(discount_pct, -1) as bracket,
            COUNT(DISTINCT contact_id) as customers
        FROM combined_discount_data
        WHERE discount_pct BETWEEN 0 AND 100
        GROUP BY ROUND(discount_pct, -1)
        ORDER BY bracket
        """
        
        return combined_discount_query

    def _generate_data_volume_report(self, schema_info):
        """Generate a report on data volume for each table."""
        results = ["## Data Volume Report"]
        
        # Extract regular and airtable table counts
        counts = schema_info.get("counts", {})
        orders_count = counts.get('orders', 0)
        airtable_orders_count = counts.get('airtable_orders', 0)
        
        results.append(f"- Regular orders table: {orders_count:,} paid orders")
        results.append(f"- Airtable orders table: {airtable_orders_count:,} paid orders")
        
        # Calculate total and percentages
        total_orders = orders_count + airtable_orders_count
        if total_orders > 0:
            regular_percent = (orders_count / total_orders) * 100
            airtable_percent = (airtable_orders_count / total_orders) * 100
            results.append(f"- Total orders across all sources: {total_orders:,}")
            results.append(f"- Regular orders represent: {regular_percent:.1f}% of total")
            results.append(f"- Airtable orders represent: {airtable_percent:.1f}% of total")
            results.append("")  # Empty line
        
        results.append("⚠️ *Including both data sources is critical for accurate analysis*")
        results.append("")  # Empty line
        return "\n".join(results)

    def _execute_total_sales_query(self, conn):
        """Execute a query to get total sales from both regular and Airtable tables."""
        try:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                -- CTE for regular orders sales
                WITH regular_sales AS (
                    SELECT SUM(bill_total_amount) as total_sales
                    FROM orders o
                    LEFT JOIN contacts c ON o.contact_id = c.id
                    WHERE o.status = 'paid'
                    AND o.order_id NOT LIKE '%TEST%'
                    AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                    AND (c.phone IS NULL OR c.phone NOT IN ('8850959517', '9999999999', '9876543210'))
                    AND (c.email IS NULL OR c.email NOT ILIKE '%test%')
                ),
                -- CTE for airtable orders sales
                airtable_sales AS (
                    SELECT SUM(bill_total_amount) as total_sales
                    FROM airtable_orders ao
                    LEFT JOIN airtable_contacts ac ON ao.contact_id = ac.id
                    WHERE ao.status = 'paid'
                    AND ao.order_id NOT LIKE '%TEST%'
                    AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
                    AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
                )
                -- Combine the results
                SELECT 
                    COALESCE((SELECT total_sales FROM regular_sales), 0) as regular_sales,
                    COALESCE((SELECT total_sales FROM airtable_sales), 0) as airtable_sales
                """)
                row = cursor.fetchone()
                if row:
                    regular_sales = float(row["regular_sales"] or 0)
                    airtable_sales = float(row["airtable_sales"] or 0)
                    total_sales = regular_sales + airtable_sales
                    
                    # Format as rupees with commas
                    regular_sales_formatted = f"₹{regular_sales:,.2f}"
                    airtable_sales_formatted = f"₹{airtable_sales:,.2f}"
                    total_sales_formatted = f"₹{total_sales:,.2f}"
                    
                    return {
                        "regular_sales": regular_sales,
                        "airtable_sales": airtable_sales,
                        "total_sales": total_sales,
                        "regular_sales_formatted": regular_sales_formatted,
                        "airtable_sales_formatted": airtable_sales_formatted,
                        "total_sales_formatted": total_sales_formatted
                    }
                return None
        except Exception as e:
            return {"error": str(e)}

    def _format_schema_report(self, schema_info):
        """Format schema discovery results into a readable report."""
        results = ["## Schema Discovery Results"]
        
        # Format tables
        for table, columns in schema_info["tables"].items():
            table_desc = f"### {table.capitalize()}"
            results.append(table_desc)
            
            # Get primary key info if available
            if "__primary_key__" in columns:
                pk_cols = ", ".join(columns["__primary_key__"])
                results.append(f"Primary key: {pk_cols}")
                
            for col_name, col_info in columns.items():
                if col_name != "__primary_key__" and isinstance(col_info, dict):
                    data_type = col_info.get('data_type', 'unknown')
                    nullable = "NULL" if col_info.get('is_nullable', 'YES') == 'YES' else "NOT NULL"
                    results.append(f"- {col_name}: {data_type} {nullable}")
            
            results.append("")  # Add a blank line between tables
        
        # Format relationships
        results.append("### Discovered Relationships")
        for rel in schema_info["relationships"]:
            results.append(f"- {rel['source_table']}.{rel['source_column']} → {rel['target_table']}.{rel['target_column']}")
        
        results.append("")  # Add a blank line
        
        # Format counts
        results.append("### Table Counts")
        for table, count in schema_info["counts"].items():
            results.append(f"- {table}: {count}")
        
        return "\n".join(results)
        
    def _generate_repeat_customers_query(self, schema_info, include_contact_details=True, limit=10):
        """Generate a query to find repeat customers with their contact details and purchase history."""
        # Build the schema graph
        graph = self._build_schema_graph(schema_info)
        
        # Define the base tables and their aliases
        base_tables = []
        
        # Check which order tables exist
        tables = schema_info["tables"].keys()
        if "orders" in tables:
            base_tables.append({"table": "orders", "alias": "o", "condition": "o.status = 'paid'"})
        if "airtable_orders" in tables:
            base_tables.append({"table": "airtable_orders", "alias": "ao", "condition": "ao.status = 'paid'"})
            
        if not base_tables:
            return None, "No order tables found in schema."
        
        # Create explicit JOIN clauses with proper aliases
        contact_joins_regular = []
        contact_joins_airtable = []
        phone_joins_regular = []
        phone_joins_airtable = []
        
        # Check for contacts tables and related tables
        has_contacts = "contacts" in tables
        has_airtable_contacts = "airtable_contacts" in tables
        has_contact_phones = "contact_phones" in tables
        has_airtable_contact_phones = "airtable_contact_phones" in tables
        
        # For standard contacts and orders - with explicit aliases
        if has_contacts:
            contact_joins_regular.append("LEFT JOIN contacts c ON CAST(o.contact_id AS text) = CAST(c.id AS text)")
            
            # Add join for contact_phones if it exists
            if has_contact_phones:
                phone_joins_regular.append("LEFT JOIN contact_phones cp ON CAST(c.id AS text) = CAST(cp.contact_id AS text)")
                
        # For airtable contacts and orders - with explicit aliases
        if has_airtable_contacts:
            contact_joins_airtable.append("LEFT JOIN airtable_contacts ac ON CAST(ao.contact_id AS text) = CAST(ac.id AS text)")
            
            # Add join for airtable_contact_phones if it exists
            if has_airtable_contact_phones:
                phone_joins_airtable.append("LEFT JOIN airtable_contact_phones acp ON CAST(ac.id AS text) = CAST(acp.contact_id AS text)")
        
        # Start building the query
        query_parts = []
        
        # For the REGULAR orders CTE
        if "orders" in tables:
            regular_fields = ["CAST(o.contact_id AS text) AS contact_id", 
                            "o.order_id", "CAST(o.created_at AS timestamp) AS created_at", "o.bill_total_amount"]
            
            # Add contact info if available
            if has_contacts:
                for field in ["first_name", "last_name", "email", "phone"]:
                    if field in schema_info["tables"].get("contacts", {}):
                        regular_fields.append(f"c.{field}")
                
                # Add phone number from contact_phones if available
                if has_contact_phones and "phone_number" in schema_info["tables"].get("contact_phones", {}):
                    regular_fields.append("cp.phone_number")
            
            regular_cte = f"""
            -- Regular orders with customer information
            WITH regular_orders AS (
                SELECT {', '.join(regular_fields)}
                FROM orders o
                {" ".join(contact_joins_regular)}
                {" ".join(phone_joins_regular)}
                WHERE o.status = 'paid'
                AND o.order_id NOT LIKE '%TEST%'
                AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                AND (c.phone IS NULL OR c.phone NOT IN ('8850959517', '9999999999', '9876543210'))
                AND (c.email IS NULL OR c.email NOT ILIKE '%test%')
            )"""
            query_parts.append(regular_cte)
        
        # For the AIRTABLE orders CTE
        if "airtable_orders" in tables:
            airtable_fields = ["CAST(ao.contact_id AS text) AS contact_id", "ao.order_id", 
                            "CAST(ao.created_at AS timestamp) AS created_at", 
                            "ao.bill_total_amount"]
            
            # Add contact info if available
            if has_airtable_contacts:
                for field in ["first_name", "last_name", "email"]:
                    if field in schema_info["tables"].get("airtable_contacts", {}):
                        airtable_fields.append(f"ac.{field}")
                
                # Add phone number from airtable_contact_phones if available
                if has_airtable_contact_phones and "phone_number" in schema_info["tables"].get("airtable_contact_phones", {}):
                    airtable_fields.append("acp.phone_number")
                                
            airtable_cte = f"""
            -- Airtable orders with customer information
            {', ' if 'orders' in tables else ''}airtable_orders AS (
                SELECT {', '.join(airtable_fields)}
                FROM airtable_orders ao
                {" ".join(contact_joins_airtable)}
                {" ".join(phone_joins_airtable)}
                WHERE ao.status = 'paid'
                AND ao.order_id NOT LIKE '%TEST%'
                AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
                AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
            )"""
            query_parts.append(airtable_cte)
        
        # COMBINED orders CTE (union of both sources)
        combined_cte = """
        -- Combined orders from both sources
        , combined_orders AS (
            SELECT * FROM regular_orders
            UNION ALL
            SELECT * FROM airtable_orders
        )"""
        
        # Add the combined CTE if we have both regular and airtable tables
        if "orders" in tables and "airtable_orders" in tables:
            query_parts.append(combined_cte)
        
        # Add the order count CTE
        order_count_cte = """
        -- Count orders per customer
        , customer_orders AS (
            SELECT
                contact_id,
                COUNT(DISTINCT order_id) AS order_count,
                SUM(bill_total_amount) AS total_spent,
                MAX(created_at) AS latest_order_date,
                MIN(created_at) AS first_order_date
            FROM combined_orders
            GROUP BY contact_id
            HAVING COUNT(DISTINCT order_id) > 1
            ORDER BY order_count DESC, total_spent DESC
            LIMIT {limit}
        )"""
        
        # Adjust the customer_orders CTE to use the right source
        if "orders" in tables and "airtable_orders" in tables:
            # Use the combined_orders CTE
            query_parts.append(order_count_cte)
        elif "orders" in tables:
            # Use just regular_orders
            order_count_cte = order_count_cte.replace("combined_orders", "regular_orders")
            query_parts.append(order_count_cte)
        elif "airtable_orders" in tables:
            # Use just airtable_orders
            order_count_cte = order_count_cte.replace("combined_orders", "airtable_orders")
            query_parts.append(order_count_cte)
        
        # Add the final SELECT statement with proper COALESCE for contact details
        if include_contact_details:
            # Build fields list based on what's available in the schema
            contact_fields = []
            
            # Add basic fields that are commonly available
            contact_fields.extend([
                "cu.contact_id",
                "cu.order_count AS purchase_frequency",
                "cu.total_spent",
                "cu.latest_order_date",
                "cu.first_order_date"
            ])
            
            # Add name fields with COALESCE if available
            if (has_contacts and "first_name" in schema_info["tables"].get("contacts", {})) or \
               (has_airtable_contacts and "first_name" in schema_info["tables"].get("airtable_contacts", {})):
                if has_contacts and has_airtable_contacts:
                    contact_fields.append("COALESCE(c.first_name, ac.first_name) AS first_name")
                elif has_contacts:
                    contact_fields.append("c.first_name")
                else:
                    contact_fields.append("ac.first_name")
                    
            if (has_contacts and "last_name" in schema_info["tables"].get("contacts", {})) or \
               (has_airtable_contacts and "last_name" in schema_info["tables"].get("airtable_contacts", {})):
                if has_contacts and has_airtable_contacts:
                    contact_fields.append("COALESCE(c.last_name, ac.last_name) AS last_name")
                elif has_contacts:
                    contact_fields.append("c.last_name")
                else:
                    contact_fields.append("ac.last_name")
            
            # Add email if available
            if (has_contacts and "email" in schema_info["tables"].get("contacts", {})) or \
               (has_airtable_contacts and "email" in schema_info["tables"].get("airtable_contacts", {})):
                if has_contacts and has_airtable_contacts:
                    contact_fields.append("COALESCE(c.email, ac.email) AS email")
                elif has_contacts:
                    contact_fields.append("c.email")
                else:
                    contact_fields.append("ac.email")
            
            # Add phone number if available (either from contacts table or contact_phones)
            phone_fields = []
            if has_contacts and "phone" in schema_info["tables"].get("contacts", {}):
                phone_fields.append("c.phone")
                
            if has_contact_phones and "phone_number" in schema_info["tables"].get("contact_phones", {}):
                phone_fields.append("cp.phone_number")
                
            if has_airtable_contact_phones and "phone_number" in schema_info["tables"].get("airtable_contact_phones", {}):
                phone_fields.append("acp.phone_number")
                
            if phone_fields:
                phone_coalesce = f"COALESCE({', '.join(phone_fields)}) AS phone_number"
                contact_fields.append(phone_coalesce)
            
            # Determine which tables to join based on what's available
            from_clause = ""
            if "orders" in tables and "airtable_orders" in tables:
                from_clause = "combined_orders co"
            elif "orders" in tables:
                from_clause = "regular_orders co"
            else:
                from_clause = "airtable_orders co"
                
            # Build GROUP BY clause based on selected fields
            group_by_fields = ["cu.contact_id", "cu.order_count", "cu.total_spent", "cu.latest_order_date", "cu.first_order_date"]
            
            # Add contact fields to GROUP BY if they're in the SELECT
            for field in ["first_name", "last_name", "email"]:
                if f"c.{field}" in contact_fields or f"ac.{field}" in contact_fields or f"COALESCE(c.{field}, ac.{field})" in contact_fields:
                    if has_contacts and has_airtable_contacts:
                        group_by_fields.append(f"c.{field}")
                        group_by_fields.append(f"ac.{field}")
                    elif has_contacts:
                        group_by_fields.append(f"c.{field}")
                    else:
                        group_by_fields.append(f"ac.{field}")
            
            # Add phone fields to GROUP BY if they're in the SELECT
            for field in phone_fields:
                group_by_fields.append(field)
                
            final_select = f"""
            -- Final query with customer details
            SELECT
                {', '.join(contact_fields)}
            FROM customer_orders cu
            LEFT JOIN {from_clause}
                ON cu.contact_id = co.contact_id
            {' '.join(contact_joins_regular) if has_contacts else ''}
            {' '.join(contact_joins_airtable) if has_airtable_contacts else ''}
            {' '.join(phone_joins_regular) if has_contact_phones else ''}
            {' '.join(phone_joins_airtable) if has_airtable_contact_phones else ''}
            GROUP BY
                {', '.join(group_by_fields)}
            ORDER BY
                cu.order_count DESC,
                cu.total_spent DESC
            """
        else:
            # Simpler version without contact details
            final_select = """
            -- Final query with just order counts
            SELECT
                cu.contact_id,
                cu.order_count AS purchase_frequency,
                cu.total_spent,
                cu.latest_order_date,
                cu.first_order_date
            FROM customer_orders cu
            ORDER BY
                cu.order_count DESC,
                cu.total_spent DESC
            """
        
        query_parts.append(final_select)
        
        # Combine all parts into a single query
        full_query = "\n".join(query_parts)
        
        # Replace limit placeholder
        full_query = full_query.replace("{limit}", str(limit))
        
        return full_query, None

    def _process_repeat_customers_query(self, conn, schema_info, limit=10, include_contact_details=False):
        """Process a query specifically for getting repeat customer details."""
        try:
            # Generate a query for finding repeat customers with their details
            query, error = self._generate_repeat_customers_query(
                schema_info, 
                include_contact_details=include_contact_details,
                limit=limit
            )
            
            if error:
                return f"❌ Error generating repeat customers query: {error}"
                
            if not query:
                return "❌ Could not generate a valid query for repeat customers. Schema may be missing required tables."
                
            # Execute the query
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                
                if not rows:
                    return "No repeat customers found in the database."
                
                # Filter out test data
                filtered_rows = []
                for row in rows:
                    if not self._is_test_user(row):
                        filtered_rows.append(row)
                
                # Format the results
                results = []
                results.append("# Repeat Customers Analysis")
                results.append(f"Found {len(filtered_rows)} non-test repeat customers across regular and Airtable data sources.\n")
                
                # Include a data volume report for context
                results.append(self._generate_data_volume_report(schema_info))
                
                # Format customer details
                results.append("## Customer Details")
                for i, row in enumerate(filtered_rows, 1):
                    # Create a nicely formatted customer card
                    customer_name = f"{row.get('first_name', '')} {row.get('last_name', '')}"
                    if not customer_name.strip():
                        customer_name = "Customer"
                        
                    results.append(f"### {i}. {customer_name}")
                    
                    # Contact information section
                    results.append("**Contact Information:**")
                    if 'email' in row and row['email']:
                        results.append(f"- Email: {row['email']}")
                    if 'phone_number' in row and row['phone_number']:
                        results.append(f"- Phone: {row['phone_number']}")
                    if 'contact_id' in row and row['contact_id']:
                        results.append(f"- Contact ID: {row['contact_id']}")
                        
                    # Purchase history section
                    results.append("**Purchase History:**")
                    results.append(f"- Total Orders: {row.get('purchase_frequency', 0)}")
                    
                    # Format total spent as rupees
                    if 'total_spent' in row and row['total_spent']:
                        total_spent = float(row['total_spent'])
                        results.append(f"- Total Spent: ₹{total_spent:,.2f}")
                        
                    # Format dates nicely
                    if 'first_order_date' in row and row['first_order_date']:
                        first_date = row['first_order_date']
                        if isinstance(first_date, (datetime, str)):
                            if isinstance(first_date, str):
                                # Try to parse the date string
                                try:
                                    first_date = datetime.strptime(first_date, "%Y-%m-%d %H:%M:%S")
                                except:
                                    pass
                            results.append(f"- First Purchase: {first_date.strftime('%Y-%m-%d') if isinstance(first_date, datetime) else first_date}")
                            
                    if 'latest_order_date' in row and row['latest_order_date']:
                        latest_date = row['latest_order_date']
                        if isinstance(latest_date, (datetime, str)):
                            if isinstance(latest_date, str):
                                # Try to parse the date string
                                try:
                                    latest_date = datetime.strptime(latest_date, "%Y-%m-%d %H:%M:%S")
                                except:
                                    pass
                            results.append(f"- Latest Purchase: {latest_date.strftime('%Y-%m-%d') if isinstance(latest_date, datetime) else latest_date}")
                    
                    # Add empty line between customers
                    results.append("")
                
                # Add timestamp
                results.append("")
                results.append(f"*Analysis generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} using RetentionAnalysisTool with schema-aware query generation.*")
                
                # Return the formatted result
                return "\n".join(results)
                
        except Exception as e:
            return f"""❌ Error processing repeat customers query: {str(e)}
            
## Troubleshooting Information

👇 Most likely a schema mismatch or bad JOIN condition.
👉 Contact IDs may not align properly between CTEs or contact tables.

## Detailed SQL Query That Was Attempted:

```sql
{query if 'query' in locals() else 'Query generation failed'}
```

This error might indicate schema mismatches or missing data in the tables. Please check the database structure and try again."""
                
    def _process_general_retention_query(self, conn, schema_info):
        """Process a general retention analysis query with standard metrics."""
        try:
            results = []
            
            # Add data volume report
            results.append(self._generate_data_volume_report(schema_info))
                
            # Get total sales data for summary
            sales_data = self._execute_total_sales_query(conn)
            if sales_data and "error" not in sales_data:
                results.append("## Sales Summary")
                results.append(f"- Regular orders total: {sales_data['regular_sales_formatted']}")
                results.append(f"- Airtable orders total: {sales_data['airtable_sales_formatted']}")
                results.append(f"- Combined total sales: {sales_data['total_sales_formatted']}")
                results.append("")  # Empty line

            # QUERY 1: Repeat customer % - COMBINED from both regular and airtable tables
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                -- Common Table Expression (CTE) for regular orders with type casting for UUID compatibility
                WITH regular_orders AS (
                    SELECT CAST(o.contact_id AS text) AS contact_id, COUNT(*) as order_count
                    FROM orders o
                    LEFT JOIN contacts c ON o.contact_id = c.id
                    WHERE o.status = 'paid'
                    AND o.order_id NOT LIKE '%TEST%'
                    AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                    AND (c.phone IS NULL OR c.phone NOT IN ('8850959517', '9999999999', '9876543210'))
                    AND (c.email IS NULL OR c.email NOT ILIKE '%test%')
                    GROUP BY CAST(o.contact_id AS text)
                ),
                -- CTE for airtable orders
                airtable_orders AS (
                    SELECT CAST(ao.contact_id AS text) AS contact_id, COUNT(*) as order_count
                    FROM airtable_orders ao
                    LEFT JOIN airtable_contacts ac ON ao.contact_id = ac.id
                    WHERE ao.status = 'paid'
                    AND ao.order_id NOT LIKE '%TEST%'
                    AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
                    AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
                    GROUP BY CAST(ao.contact_id AS text)
                ),
                -- Combined customers view
                combined_customers AS (
                    SELECT contact_id, order_count FROM regular_orders
                    UNION ALL
                    SELECT contact_id, order_count FROM airtable_orders
                ),
                -- Get total orders per customer across both systems
                aggregated_counts AS (
                    SELECT contact_id, SUM(order_count) as total_order_count
                    FROM combined_customers
                    GROUP BY contact_id
                )
                -- Calculate retention metrics
                SELECT 
                    COUNT(DISTINCT contact_id) as total_customers,
                    COUNT(DISTINCT CASE WHEN total_order_count > 1 THEN contact_id END) as repeat_customers
                FROM aggregated_counts
                """)
                row = cursor.fetchone()
                if row:
                    total = row["total_customers"]
                    repeat = row["repeat_customers"]
                    results.append("## Retention Summary")
                    results.append(f"- Total customers: {total:,}")
                    results.append(f"- Repeat customers: {repeat:,}")
                    results.append(f"- One-time customers: {(total - repeat):,}")
                    results.append(f"- Repeat rate: {round((repeat / total) * 100, 1) if total else 0}%")
                    results.append("")  # Empty line

            # QUERY 2: Avg time between purchases - COMBINED from both regular and airtable tables
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                -- Combine orders from both tables with type casting for UUID and timestamp compatibility
                WITH combined_orders AS (
                    SELECT 
                        CAST(o.contact_id AS text) AS contact_id, 
                        CAST(o.created_at AS timestamp) AS created_at,
                        o.order_id
                    FROM orders o
                    LEFT JOIN contacts c ON o.contact_id = c.id
                    WHERE o.status = 'paid'
                      AND o.order_id NOT LIKE '%TEST%'
                      AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                      AND (c.phone IS NULL OR c.phone NOT IN ('8850959517', '9999999999', '9876543210'))
                      AND (c.email IS NULL OR c.email NOT ILIKE '%test%')
                    UNION ALL
                    SELECT 
                        CAST(ao.contact_id AS text) AS contact_id, 
                        CAST(ao.created_at AS timestamp) AS created_at,
                        ao.order_id
                    FROM airtable_orders ao
                    LEFT JOIN airtable_contacts ac ON ao.contact_id = ac.id
                    WHERE ao.status = 'paid'
                      AND ao.order_id NOT LIKE '%TEST%'
                      AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
                      AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
                ),
                -- Rank orders by created_at for each customer
                ranked_orders AS (
                    SELECT contact_id, created_at,
                           ROW_NUMBER() OVER (PARTITION BY contact_id ORDER BY created_at) AS rn
                    FROM combined_orders
                )
                -- Calculate average days between first and second order
                SELECT 
                    AVG(
                        EXTRACT(
                            DAY FROM 
                            (r2.created_at - r1.created_at)
                        )
                    ) as avg_days
                FROM ranked_orders r1
                JOIN ranked_orders r2 
                  ON r1.contact_id = r2.contact_id AND r1.rn = 1 AND r2.rn = 2
                """)
                row = cursor.fetchone()
                if row and row["avg_days"]:
                    results.append("## Time Between Purchases")
                    results.append(f"- Average days between 1st and 2nd order: {round(row['avg_days'], 1)} days")
                    results.append("")  # Empty line

            # QUERY 3: Discount impact - using schema-aware query generation
            try:
                discount_query = self._generate_safe_discount_query(schema_info)
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                    cursor.execute(discount_query)
                    rows = cursor.fetchall()
                    if rows:
                        results.append("## Discount Impact")
                        for row in rows:
                            results.append(f"- {int(row['bracket'])}% discount bracket: {row['customers']:,} customers")
                        results.append("")  # Empty line
            except Exception as e:
                results.append("## Discount Impact")
                results.append(f"⚠️ Could not analyze discount impact: {str(e)}")
                results.append("This is likely due to schema differences between tables.")
                results.append("")  # Empty line
            
            # QUERY 4: Latest customer cohort performance
            try:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                    cursor.execute("""
                    -- Common Table Expression (CTE) for combined orders with casting
                    WITH combined_orders AS (
                        SELECT 
                            CAST(o.contact_id AS text) AS contact_id,
                            CAST(o.created_at AS timestamp) AS created_at,
                            o.bill_total_amount
                        FROM orders o
                        LEFT JOIN contacts c ON o.contact_id = c.id
                        WHERE o.status = 'paid'
                          AND o.order_id NOT LIKE '%TEST%'
                          AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                          AND (c.phone IS NULL OR c.phone NOT IN ('8850959517', '9999999999', '9876543210'))
                          AND (c.email IS NULL OR c.email NOT ILIKE '%test%')
                        UNION ALL
                        SELECT 
                            CAST(ao.contact_id AS text) AS contact_id,
                            CAST(ao.created_at AS timestamp) AS created_at,
                            ao.bill_total_amount
                        FROM airtable_orders ao
                        LEFT JOIN airtable_contacts ac ON ao.contact_id = ac.id
                        WHERE ao.status = 'paid'
                          AND ao.order_id NOT LIKE '%TEST%'
                          AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
                          AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
                        ),
                    -- First purchase date for each customer
                    first_purchase AS (
                        SELECT 
                            contact_id,
                            MIN(created_at) AS first_order_date,
                            DATE_TRUNC('month', MIN(created_at)) AS cohort_month
                        FROM combined_orders
                        GROUP BY contact_id
                    ),
                    -- Get 3 most recent cohorts with at least 10 customers
                    recent_cohorts AS (
                        SELECT 
                            cohort_month,
                            COUNT(DISTINCT contact_id) AS cohort_size
                        FROM first_purchase
                        GROUP BY cohort_month
                        HAVING COUNT(DISTINCT contact_id) >= 10
                        ORDER BY cohort_month DESC
                        LIMIT 3
                    ),
                    -- Calculate repeat rates for these cohorts
                    cohort_performance AS (
                        SELECT 
                            rc.cohort_month,
                            rc.cohort_size,
                            COUNT(DISTINCT CASE WHEN 
                                (SELECT COUNT(*) FROM combined_orders co 
                                 WHERE co.contact_id = fp.contact_id) > 1 
                                THEN fp.contact_id END) AS repeat_customers
                        FROM recent_cohorts rc
                        JOIN first_purchase fp ON rc.cohort_month = fp.cohort_month
                        GROUP BY rc.cohort_month, rc.cohort_size
                    )
                    -- Final output with formatted dates and percentages
                    SELECT 
                        TO_CHAR(cohort_month, 'Month YYYY') AS cohort,
                        cohort_size,
                        repeat_customers,
                        ROUND((repeat_customers::numeric / cohort_size) * 100, 1) AS repeat_rate
                    FROM cohort_performance
                    ORDER BY cohort_month DESC
                    """)
                    rows = cursor.fetchall()
                    if rows:
                        results.append("## Recent Cohort Performance")
                        for row in rows:
                            cohort = row["cohort"].strip()  # Remove trailing spaces
                            results.append(f"- {cohort}: {row['cohort_size']:,} customers, {row['repeat_rate']}% repeat rate")
                        results.append("")  # Empty line
            except Exception as e:
                results.append("## Recent Cohort Performance")
                results.append(f"⚠️ Could not analyze cohort performance: {str(e)}")
            
            # QUERY 5: Repeat Purchase Categories
            try:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                    # First check if relevant tables and columns exist
                    tables_info = schema_info.get("tables", {})
                    if ('order_items' in tables_info and 'airtable_order_items' in tables_info and
                        'product_id' in tables_info.get('order_items', {}) and 
                        'product_id' in tables_info.get('airtable_order_items', {})):
                        
                        cursor.execute("""
                        WITH combined_orders AS (
                            SELECT 
                                CAST(o.contact_id AS text) AS contact_id,
                                o.order_id,
                                'regular' AS source
                            FROM orders o
                            LEFT JOIN contacts c ON o.contact_id = c.id
                            WHERE o.status = 'paid'
                              AND o.order_id NOT LIKE '%TEST%'
                              AND o.order_id NOT LIKE 'POD-WEBHOOK%'
                              AND (c.phone IS NULL OR c.phone NOT IN ('8850959517', '9999999999', '9876543210'))
                              AND (c.email IS NULL OR c.email NOT ILIKE '%test%')
                            UNION ALL
                            SELECT 
                                CAST(ao.contact_id AS text) AS contact_id,
                                ao.order_id,
                                'airtable' AS source
                            FROM airtable_orders ao
                            LEFT JOIN airtable_contacts ac ON ao.contact_id = ac.id
                            WHERE ao.status = 'paid'
                              AND ao.order_id NOT LIKE '%TEST%'
                              AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
                              AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
                        ),
                        combined_items AS (
                            SELECT 
                                co.contact_id,
                                CASE 
                                    WHEN co.source = 'regular' THEN oi.product_id
                                    ELSE aoi.product_id
                                END AS product_id,
                                CASE
                                    WHEN co.source = 'regular' THEN oi.medicine_name
                                    ELSE aoi.medicine_name
                                END AS medicine_name,
                                co.order_id
                            FROM combined_orders co
                            LEFT JOIN order_items oi ON co.order_id = oi.order_id AND co.source = 'regular'
                            LEFT JOIN airtable_order_items aoi ON co.order_id = aoi.order_id AND co.source = 'airtable'
                            WHERE (oi.product_id IS NOT NULL OR aoi.product_id IS NOT NULL)
                        ),
                        -- Get customers with multiple orders
                        repeat_customers AS (
                            SELECT contact_id
                            FROM combined_orders
                            GROUP BY contact_id
                            HAVING COUNT(DISTINCT order_id) > 1
                        ),
                        -- Get repeat purchase products
                        repeat_products AS (
                            SELECT 
                                product_id,
                                medicine_name,
                                COUNT(DISTINCT ci.contact_id) AS repeat_customers,
                                COUNT(DISTINCT ci.order_id) AS times_purchased
                            FROM combined_items ci
                            JOIN repeat_customers rc ON ci.contact_id = rc.contact_id
                            GROUP BY product_id, medicine_name
                            HAVING COUNT(DISTINCT ci.contact_id) >= 5
                        )
                        -- Get top repeat purchase products
                        SELECT 
                            product_id,
                            medicine_name,
                            repeat_customers,
                            times_purchased
                        FROM repeat_products
                        ORDER BY repeat_customers DESC, times_purchased DESC
                        LIMIT 10
                        """)
                        rows = cursor.fetchall()
                        if rows:
                            results.append("## Top Repeat Purchase Products")
                            for row in rows:
                                product_name = row["medicine_name"] or "Unknown"
                                results.append(f"- {product_name} (ID: {row['product_id']}): Purchased by {row['repeat_customers']} repeat customers")
                            results.append("")  # Empty line
            except Exception as e:
                results.append("## Top Repeat Purchase Products")
                results.append(f"⚠️ Could not analyze repeat purchase products: {str(e)}")
            
            # Format the final result with a timestamp
            # Add a timestamp to the results
            results.append("")  # Empty line 
            results.append(f"*Analysis generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} using RetentionAnalysisTool with schema discovery.*")
            
            # Join all results into a single string
            formatted_result = "\n".join(results)
            
            # Cache the result for future use
            global _retention_cache
            _retention_cache = formatted_result
            return formatted_result
        except Exception as e:
            return f"""❌ Error in general retention analysis: {str(e)}

## Troubleshooting Information
- Error type: {type(e).__name__}
- Error details: {str(e)}
- This error occurred during the general retention analysis
- It may be related to database schema or query execution issues

Please check the database configuration and schema structure."""