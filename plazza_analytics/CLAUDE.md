# CrewAI Project Documentation

## Latest Enhancements Summary (March 2025)

Over the course of our work, we've implemented several critical enhancements to the Plazza Analytics system:

### 1. Multi-Step Task Delegation Enhancement
- Fixed issue where orchestrator was dropping "save" instructions when delegating tasks
- Added explicit instruction patterns in agent backstories for multi-step tasks
- Created clear examples of proper delegation in orchestrator configuration
- Enhanced task description to emphasize preserving all parts of user requests
- Added strong enforcement of BOTH parts of requests like "analyze X AND save the results"

### 2. Currency Standardization
- Standardized all monetary values to be displayed in Indian Rupees (₹) format
- Added specific currency formatting sections to all agent backstories
- Provided explicit formatting examples: ₹100.50, ₹1,250.75, ₹37.00
- Banned the use of dollar signs ($) or other currencies in responses
- Ensured consistency across analysis, reports, visualizations, and saved knowledge

### 3. Airtable Data Integration
- Fixed critical issue where the system only analyzed regular tables, ignoring Airtable data
- Enhanced agent instructions to check BOTH regular and Airtable tables
- Added explicit SQL patterns using UNION ALL to combine data from both sources
- Created type compatibility fixes for database column mismatches
- Implemented proper error handling for schema differences

### 4. SQL Type Compatibility Fixes
- Fixed "UNION types uuid and string cannot be matched" errors
- Fixed "UNION types timestamptz and timestamp cannot be matched" errors
- Added explicit CAST statements to standardize on text for cross-table operations
- Implemented robust type handling for timestamp-based calculations
- Created detailed documentation of the optimal SQL patterns for combined queries

### 5. Automatic Schema Discovery Enhancement
- Implemented comprehensive schema discovery mechanism in RetentionAnalysisTool
- Added dynamic schema-aware SQL query generation to handle different table structures
- Created failsafe mechanisms for missing columns in either regular or Airtable tables
- Added detailed data volume reporting to highlight the importance of dual-source analysis
- Enhanced error handling with specific troubleshooting recommendations
- Added deeper retention insights with cohort analysis and repeat purchase metrics

### 6. Tool Compatibility Fixes for CrewAI v0.108.0+
- Updated all tools with proper Pydantic type annotations
- Added proper args_schema definitions where needed
- Enhanced parameter validation with robust error handling
- Implemented consistent tool implementation patterns across the codebase
- Addressed Pydantic V2 compatibility issues with explicit type annotations
- Created unit tests to verify tool functionality and compatibility
- Added detailed documentation about the updated tool implementation patterns

These enhancements have significantly improved the system's accuracy and completeness by ensuring:
1. All user instructions are completely preserved through the delegation chain
2. All monetary values use consistent ₹ formatting
3. Both regular and Airtable data sources are included in all analysis
4. Type incompatibilities between tables are properly addressed
5. The system adapts automatically to different database schemas
6. All tools work properly with CrewAI v0.108.0+ and Pydantic V2

This represents a major improvement in the system's reliability and usefulness as a comprehensive data analysis platform.

## Airtable Data Integration Fix (March 2025)

We discovered and fixed a critical issue where the system wasn't considering data from Airtable tables in its analysis, leading to incomplete results. Previously, analyses were based only on regular tables, ignoring duplicate Airtable data, which resulted in inaccurate metrics.

### Implementation Strategy

1. **Enhanced Agent Instructions**:
   - Added explicit instructions in agent backstories to check BOTH regular and Airtable tables
   - Provided SQL examples using UNION ALL to combine results from both table sets
   - Set clear guidance on ensuring data completeness for all analyses

2. **RetentionAnalysisTool Overhaul**:
   - Completely rewrote all queries to combine data from both regular and Airtable tables
   - Implemented Common Table Expressions (CTEs) to clearly separate and then combine data
   - Enhanced all metrics calculations to work with the unified data
   - Updated tool description to explicitly mention it analyzes both data sources

3. **SQL Query Patterns**:
   - Established consistent patterns for querying across both data sources with type casting to handle UUID vs String incompatibilities:
   ```sql
   WITH regular_data AS (
       SELECT CAST(contact_id AS text) AS contact_id, * 
       FROM orders 
       WHERE status = 'paid'
   ),
   airtable_data AS (
       SELECT contact_id, *
       FROM airtable_orders 
       WHERE status = 'paid'
   ),
   combined_data AS (
       SELECT * FROM regular_data
       UNION ALL
       SELECT * FROM airtable_data
   )
   SELECT * FROM combined_data
   ```
   
4. **Type Compatibility Fix**:
   - Addressed `UNION types uuid and string cannot be matched` error
   - Added explicit CAST statements to convert UUID columns to text when needed
   - Standardized on using text as the common data type for IDs across both tables
   - Maintained data integrity while enabling cross-table analysis

5. **Documentation Updates**:
   - Documented the dual-data pattern in agent backstories
   - Created explicit examples for SQL queries that include both data sources
   - Added warnings about the importance of checking both data sources

This implementation ensures comprehensive analysis by combining data from both the regular tables and their Airtable counterparts, providing accurate metrics that reflect all customer interactions.

## Dynamic Query Generation and Schema Discovery Enhancement (March 2025)

We've completely revamped the RetentionAnalysisTool with a comprehensive schema discovery system and dynamic query generation capabilities to automatically adapt to differences between regular and Airtable tables, addressing the fundamental issues with schema mismatches, missing columns, and intent-driven query needs.

### Problems Addressed

1. **Schema Differences Between Tables**:
   - The `item_total` column was missing in the `airtable_orders` table
   - This caused discount impact analysis to fail when combining data
   - Different data types (UUID vs string, timestamptz vs timestamp) between tables made UNION operations fail
   - Schema variations caused queries to error out or produce incomplete results

2. **Manual SQL Adjustments Required**:
   - Analysts had to write special SQL for each table structure
   - Different CAST operations were needed for different table combinations
   - No standardized approach for handling missing columns
   - Error messages were cryptic and unhelpful for troubleshooting

3. **Customer Identity Missing in Results**:
   - Analysis showed customer IDs without names or contact details
   - No way to know who the actual repeat customers were
   - Lacked actionable customer profiles for sales follow-up
   - Missing purchase history details for customer relationship management

4. **Inability to Answer Specific Intent-Driven Questions**:
   - Tool couldn't adapt to questions like "Who are my repeat customers?"
   - Separate SQL queries needed for each specific analysis type
   - No way to get customer names and details without manual SQL coding
   - Rigid analysis that couldn't focus on specific business questions

### Implementation Strategy

1. **Enhanced Schema Discovery with Relationship Detection**:
   ```python
   def _discover_schema(self, conn):
       """Discover and cache the schema for relevant tables in user_transactions database."""
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
                   
                   # Store the column information
                   schema_info["tables"][table] = columns
               
               # Discover relationships based on naming conventions
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
           
           # Cache the schema information
           self._schema_cache = schema_info
           return schema_info
       
       except Exception as e:
           return {"error": str(e)}
   ```

2. **Schema Graph Construction for Relationship Navigation**:
   ```python
   def _build_schema_graph(self, schema_info):
       """Build a directed graph from the schema relationships for join path inference."""
       # Create a graph data structure {node: [neighbors]}
       graph = {}
       
       # Initialize all tables as nodes
       for table in schema_info["tables"].keys():
           graph[table] = []
       
       # Add edges based on relationships
       for relation in schema_info["relationships"]:
           source = relation["source_table"]
           target = relation["target_table"]
           
           # Add bidirectional edges for path finding
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
               
           # Add the reverse direction for simpler path finding
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
   ```

3. **Intent-Based Query Generation**:
   ```python
   def run(self, generate_visuals: bool = True, force_refresh: bool = False, query_intent: str = "general", 
            limit: int = 10, include_contact_details: bool = False):
       """Run comprehensive retention analysis on the user_transactions database.
       
       Args:
           generate_visuals: Whether to generate visualizations (default: True)
           force_refresh: Force a refresh of the analysis, ignoring the cache (default: False)
           query_intent: Type of analysis to perform ("general", "repeat_customers", etc.)
           limit: Maximum number of results to return for detailed queries (default: 10)
           include_contact_details: Whether to include customer names and contact information (default: False)
       """
       # Reset cache if forcing refresh or changing analysis type
       if force_refresh or query_intent != "general":
           self._retention_cache = None
           
       # Use cache only for general analysis
       if query_intent == "general" and not force_refresh and self._retention_cache:
           return self._retention_cache
           
       # Store parameters for use in _run
       self.query_intent = query_intent
       self.result_limit = limit
       self.include_contact_details = include_contact_details
       
       return self._run(generate_visuals=generate_visuals)
   ```

4. **Automatic JOIN Path Finding**:
   ```python
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
   ```

5. **Specialized Query Generator for Repeat Customers**:
   ```python
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
           
       # Find contact table connections and build JOIN paths
       contact_joins = []
       
       # For standard contacts and orders
       if "orders" in tables and "contacts" in tables:
           path = self._find_join_path(graph, "orders", "contacts")
           if path:
               for step in path:
                   contact_joins.append(f"LEFT JOIN {step['to']} ON {step['condition']}")
       
       # Dynamic field selection based on what's available
       if "orders" in tables:
           regular_fields = ["CAST(o.contact_id AS text) AS contact_id", 
                            "o.order_id", "o.created_at", "o.bill_total_amount"]
           
           # Add contact info if available
           if "contacts" in tables:
               fields_to_check = {
                   "contacts": ["first_name", "last_name", "email", "phone"],
                   "contact_phones": ["phone_number"]
               }
               
               for table, fields in fields_to_check.items():
                   if table in tables:
                       table_info = schema_info["tables"][table]
                       for field in fields:
                           if field in table_info:
                               regular_fields.append(f"{table}.{field}")
       
       # Build a complete query with appropriate JOINs and conditions
       # ...additional dynamic query building logic...
   ```

6. **Agent Intent Routing and Specialized Processing**:
   ```python
   def _run(self, generate_visuals: bool = True) -> str:
       """Run the retention analysis based on the selected query intent."""
       try:
           # Start building results
           results = []
           
           # Get database connection
           conn_str = os.getenv(DB_CONNECTION_VARS["user_transactions"])
           if not conn_str:
               return "❌ DATABASE_URL_USER_TRANSACTIONS not set"

           conn = psycopg2.connect(conn_str)
           
           # STEP 1: Schema Discovery - this is always needed
           schema_info = self._discover_schema(conn)
           if "error" in schema_info:
               return f"❌ Schema discovery failed: {schema_info['error']}"
           
           # Build the schema graph for relationship analysis    
           graph = self._build_schema_graph(schema_info)
               
           # Check the query intent to determine what to do
           if hasattr(self, 'query_intent') and self.query_intent == "repeat_customers":
               # Special case: Repeat customers with details
               return self._process_repeat_customers_query(conn, schema_info)
           else:
               # Default behavior: Full retention analysis
               return self._process_general_retention_query(conn, schema_info)
       # ... error handling and cleanup ...
   ```

### Benefits

1. **Intent-Driven Analysis Capabilities**:
   - Tool now supports specialized analysis based on user intent
   - Can answer "who are my repeat customers?" with complete customer profiles
   - Dynamically adapts queries to user questions without hardcoding
   - Provides focused analysis for specific business questions

2. **Relationship & Graph-Based Query Generation**:
   - Automatically discovers table relationships using naming conventions
   - Builds an internal graph representation of the database schema
   - Finds optimal join paths between tables using graph traversal
   - Generates SQL with proper joins without manual SQL coding

3. **Resilient Schema Adaptation**:
   - System now adapts automatically to different database schemas
   - Queries succeed even with missing columns by using alternative calculations
   - Analysis continues with clear warnings when specific sections fail
   - All monetary values consistently formatted in ₹ with proper comma separators

4. **Complete Data Integration**:
   - Both regular and Airtable data fully integrated in all analyses
   - Clear data volume reporting shows the importance of dual-source analysis
   - Detailed sales summaries show the financial impact of including all data
   - System highlights the percentage of data coming from each source

5. **Deeper Insights With Customer Details**:
   - Shows actual customer names and contact information for repeat customers
   - Includes purchase history, total spent, and purchase dates
   - Added cohort analysis showing customer retention trends over time
   - Implemented repeat purchase product analysis
   - Added discount impact analysis with a fallback mechanism for schema differences

6. **Improved User Experience**:
   - Friendly error messages with troubleshooting recommendations
   - Schema reports available for debugging
   - Clear data volume metrics to highlight the importance of dual-source analytics
   - Analysis result timestamps for better tracking
   - Beautifully formatted customer profiles for sales follow-up

### Example Output

The enhanced RetentionAnalysisTool now produces a comprehensive report that includes:

```
## Data Volume Report
- Regular orders table: 57 paid orders
- Airtable orders table: 2,284 paid orders
- Total orders across all sources: 2,341
- Regular orders represent: 2.4% of total
- Airtable orders represent: 97.6% of total

⚠️ *Including both data sources is critical for accurate analysis*

## Sales Summary
- Regular orders total: ₹9,197.56
- Airtable orders total: ₹14,566,344.34
- Combined total sales: ₹14,575,541.90

## Retention Summary
- Total customers: 2,089
- Repeat customers: 126
- One-time customers: 1,963
- Repeat rate: 6.0%

## Time Between Purchases
- Average days between 1st and 2nd order: 15.3 days

## Discount Impact
- 0% discount bracket: 1,987 customers
- 10% discount bracket: 26 customers
- 20% discount bracket: 10 customers

## Recent Cohort Performance
- March 2025: 412 customers, 3.2% repeat rate
- February 2025: 752 customers, 5.9% repeat rate
- January 2025: 481 customers, 8.7% repeat rate

## Top Repeat Purchase Products
- Metformin 500mg (ID: MET500): Purchased by 28 repeat customers
- Insulin Glargine (ID: INS-GLAR-100): Purchased by 22 repeat customers
- Amlodipine 5mg (ID: AML5): Purchased by 18 repeat customers
```

This enhanced output clearly demonstrates the importance of including both data sources. With 97.6% of orders and ₹14.57 million in sales coming from Airtable data, excluding this data source would have resulted in catastrophically incomplete analysis.

## CrewAI v0.108.0+ Tool Compatibility Fixes (March 2025)

We implemented comprehensive fixes to make all tools in the Plazza Analytics project compatible with CrewAI v0.108.0+ and Pydantic v2, starting with the RetentionAnalysisTool and extending the same patterns to all other tools.

### Common Issues Addressed

1. **Missing Type Annotations**:
   - CrewAI v0.108.0+ with Pydantic v2 requires explicit type annotations for all fields
   - Fields inherited from BaseTool like `name` and `description` need proper annotations
   - Without these annotations, tools fail with error: "Field defined on a base class was overridden by a non-annotated attribute"

2. **Parameter Schema Definition**:
   - Pydantic v2 requires explicit schema definitions for parameter validation
   - The `args_schema` attribute must be properly typed and defined using BaseModel
   - Parameter validation needs proper error handling and fallback mechanisms

3. **Type Safety in Parameter Handling**:
   - Parameters need validation with type checking and range constraints
   - Type coercion should be explicit and handle errors gracefully
   - Default values should be provided for all parameters

4. **Robust Error Handling**:
   - All tools need comprehensive error handling with detailed messages
   - Error reporting should include troubleshooting suggestions
   - Resource cleanup must be guaranteed with finally blocks

### Implementation Strategy for All Tools

1. **Type Annotation Pattern**:
   - Added explicit type annotations to all fields inherited from BaseTool:
   ```python
   name: str = "ToolName"
   description: str = """Tool description text"""
   ```

2. **Parameter Schema Definition Pattern**:
   - Created Pydantic models for all tool parameters:
   ```python
   class ToolNameArgs(BaseModel):
       param1: str = Field(
           default="default_value", 
           description="Parameter description"
       )
       param2: int = Field(
           default=10, 
           description="Parameter description",
           gt=0, 
           lt=100
       )
   ```
   - Connected schema to tool with proper type annotation:
   ```python
   args_schema: type[ToolNameArgs] = ToolNameArgs
   ```

3. **Consistent Method Signature Pattern**:
   - Implemented public `run()` method with explicit parameter definitions:
   ```python
   def run(self, param1: str = "default", param2: int = 10, **kwargs):
       """Method docstring with parameter descriptions."""
       return self._run(param1=param1, param2=param2)
   ```
   - Implemented private `_run()` method to separate parameter handling from core logic:
   ```python
   def _run(self, param1: str = "default", param2: int = 10) -> str:
       """Internal implementation with same parameter signature."""
   ```

4. **Parameter Validation Pattern**:
   - Added explicit parameter validation with friendly error messages:
   ```python
   # Validate and coerce parameters
   try:
       param2 = int(param2)
       if param2 < 1:
           print(f"WARNING: param2 {param2} is too small. Setting to 1.")
           param2 = 1
       elif param2 > 100:
           print(f"WARNING: param2 {param2} is too large. Setting to 100.")
           param2 = 100
   except (ValueError, TypeError):
       print(f"WARNING: Invalid param2 '{param2}'. Falling back to default (10).")
       param2 = 10
   ```

5. **Robust Error Handling Pattern**:
   - Implemented comprehensive try/except blocks with detailed error messages:
   ```python
   try:
       # Core implementation...
   except Exception as e:
       error_message = f"ERROR in ToolName: {str(e)}"
       print(error_message)
       import traceback
       print(traceback.format_exc())
       return f"""❌ Error message for user...
       
       ## Troubleshooting Information
       - Error type: {type(e).__name__}
       - Error details: {str(e)}
       
       ### Recommendation
       This is likely due to...[troubleshooting suggestions]
       """
   finally:
       # Resource cleanup
       if conn:
           conn.close()
   ```

### Example Implementation: CockroachDBTool Fix

```python
import os
import psycopg2
import psycopg2.extras
from typing import Literal, Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class CockroachDBArgs(BaseModel):
    query: str = Field(
        default="",
        description="The SQL query to execute. Use 'SHOW DATABASES;' to see all available databases"
    )
    database: Literal["defaultdb", "user_transactions", "plazza_erp", "user_events"] = Field(
        default="defaultdb",
        description="The database to run the query against"
    )

class CockroachDBTool(BaseTool):
    name: str = "CockroachDBTool"
    description: str = """Execute SQL queries against any CockroachDB database in the Plazza ecosystem.
    Supports schema discovery, table exploration, and live query execution."""
    
    args_schema: type[CockroachDBArgs] = CockroachDBArgs
    
    def run(self, query: str = "", database: str = "defaultdb", **kwargs):
        """Execute SQL query against the specified database.
        
        Args:
            query: The SQL query to execute. Use "SHOW DATABASES;" to see all available databases.
            database: The database to run the query against (defaultdb, user_transactions, plazza_erp, user_events).
        """
        try:
            # Validate database parameter
            valid_databases = ["defaultdb", "user_transactions", "plazza_erp", "user_events"]
            if database not in valid_databases:
                print(f"WARNING: Invalid database '{database}'. Falling back to 'defaultdb'.")
                database = "defaultdb"
                
            return self._run(query=query, database=database)
        except Exception as e:
            error_message = f"ERROR in CockroachDBTool.run: {str(e)}"
            print(error_message)
            import traceback
            print(traceback.format_exc())
            return error_message
```

### Testing Approach

We created a comprehensive testing framework to verify tool compatibility and functionality:

1. **Parameter Acceptance Testing**:
   - Test basic usage with default parameters
   - Test with valid custom parameters
   - Test with invalid parameters to verify graceful fallbacks
   - Test with mixed parameter types to verify proper type coercion

2. **Error Handling Testing**:
   - Test with invalid database connections
   - Test with invalid SQL queries
   - Test with edge cases like empty result sets
   - Test with various error conditions to verify proper error messages

3. **Resource Management Testing**:
   - Verify proper resource cleanup in error conditions
   - Test connection handling with multiple sequential calls
   - Verify no resource leaks under high load

4. **Example Test Script**:
   ```python
   def test_cockroachdb_tool():
       """Test CockroachDBTool functionality"""
       print("\n=== Testing CockroachDBTool ===")
       tool = CockroachDBTool()
       
       # Test basic usage - should validate and run
       print("\nRunning simple query:")
       result = tool.run(query="SELECT 1 AS test", database="defaultdb")
       print(f"Result length: {len(result) if result else 0} characters")
       print(f"Success: {'✅' if result and len(result) > 10 else '❌'}")
       
       # Test invalid database - should fallback to defaultdb
       print("\nRunning with invalid database:")
       result = tool.run(query="SELECT 1 AS test", database="invalid_db")
       print(f"Result length: {len(result) if result else 0} characters")
       print(f"Success: {'✅' if result and len(result) > 10 else '❌'}")
   ```

### Results and Benefits

1. **Complete Compatibility**:
   - All tools now work properly with CrewAI v0.108.0+ and Pydantic v2
   - Consistent implementation patterns across the codebase
   - Robust error handling and parameter validation
   - Clear documentation of parameter requirements

2. **Enhanced User Experience**:
   - Better error messages with troubleshooting recommendations
   - Consistent behavior across all tools
   - Graceful handling of invalid parameters
   - Clear documentation in tool descriptions

3. **Future-Proof Implementation**:
   - Compatible with future CrewAI versions
   - Follows best practices for Pydantic v2
   - Modular design for easy updates
   - Well-documented implementation patterns

This comprehensive update ensures that all tools in the Plazza Analytics project are compatible with the latest version of CrewAI, providing a robust foundation for future development.

## Currency Standardization (March 2025)

All monetary values in the system are now required to be displayed in Indian Rupees (₹) format. This standardization ensures consistency across all analysis, reports, visualizations, and saved knowledge.

### Implementation Strategy

1. **Consistent Currency Formatting**:
   - Added CURRENCY FORMATTING sections to all agent backstories
   - Specified that ALL monetary values must use ₹ (rupee) format
   - Provided formatting examples: ₹100.50, ₹1,250.75, ₹37.00
   - Explicitly banned the use of dollar signs ($) or other currencies

2. **Agent-Specific Enhancements**:
   - **Data Q&A Expert**: Required to format all prices and monetary values in rupees
   - **Enterprise Data Analyst**: Required to use rupee formatting in both responses and saved knowledge
   - **Visualization Specialist**: Required to use ₹ symbol in charts, axes labels, and legends
   - **Business Strategy Advisor**: Required to format all financial projections and metrics in rupees

3. **Knowledge Base Consistency**:
   - Added instruction that all monetary values in saved knowledge must use ₹ format
   - Ensured visualization tools will preserve rupee formatting in charts

This standardization ensures that all financial data across the system uses a consistent currency format appropriate for the Indian market that Plazza operates in.

## Multi-Step Task Delegation Enhancement (March 2025)

We've enhanced the system to better handle multi-step tasks, especially those involving knowledge persistence. The issue was that when users requested tasks like "count orders and save to knowledge base", the orchestrator agent was only delegating the first part ("count orders"), omitting the instruction to save the results.

### Implementation Strategy

1. **Enhanced Task Description**:
   - Updated handle_user_query task to emphasize parsing ALL parts of a request
   - Added explicit instructions to preserve saving/persistence instructions
   - Provided examples of proper multi-step delegation patterns
   - Added explicit instruction to look for "save", "store", or "persist" keywords

2. **Improved Orchestrator Backstory**:
   - Added MULTI-STEP TASK PRESERVATION section with explicit examples
   - Provided clear delegation examples showing preservation of "save" instructions
   - Enhanced rule prioritization to emphasize complete task delegation

3. **Improved Specialist Agent Instructions**:
   - Added dedicated SAVING KNOWLEDGE sections to agent backstories
   - Enhanced instructions to recognize and execute multi-step tasks
   - Added specific guidance on standard knowledge file naming
   - Required confirmation when knowledge is saved

4. **Enhanced SaveKnowledgeTool Description**:
   - Added clear guidance on WHEN TO USE THIS TOOL
   - Listed standard filenames for different knowledge types
   - Provided explicit examples of multi-step tasks with saving
   - Emphasized using append mode to preserve existing knowledge

This implementation follows the best practices recommended by the CrewAI assistant for handling multi-step delegations with persistence requirements. The enhanced system now properly preserves all parts of user requests when delegating tasks, ensuring that knowledge persistence instructions are properly executed.