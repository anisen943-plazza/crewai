# CrewAI Project Documentation

## Project Overview

### System Enhancements (March 24-26)

#### Agent Memory and Enhanced Logging Implementation (March 24)

1. **Agent Memory Activation**:
   - Updated all agents to use `memory=True` parameter
   - Enabled short-term memory for Data Q&A Expert to maintain context of SQL queries
   - Added memory to Enterprise Data Analyst for continuous analysis building
   - Implemented memory for Visualization Specialist to ensure style consistency
   - Added memory to Strategic Business Consultant for tracking recommendation implementation
   - Enhanced backstories to include memory-specific responsibilities
   - Improved cross-session coherence with persistent context

2. **Enhanced Task Logging with Metadata**:
   - Added comprehensive metadata to all chat outputs
   - Created tool attribution tracking to record which tools contributed to responses
   - Implemented automatic tool usage detection based on response content patterns
   - Added analysis type classification (Full Analysis vs. Quick Answer)
   - Enhanced timestamp and processing record information 
   - Added KB access tracking and age calculation
   - Added focus area tracking for specialized analyses
   - Implemented execution duration tracking for performance monitoring
   - Created standardized metadata format for consistency across outputs

3. **JSON Summary Output**:
   - Implemented parallel JSON export alongside markdown outputs
   - Created structured format for easier dashboard integration
   - Added tool usage data for analytics on system performance
   - Included KB metadata for freshness tracking
   - Preserved query-response pairs in machine-readable format
   - Enabled programmatic access to chat history
   - Used consistent timestamp formatting for time-series analysis
   - Added boolean flags for quick filtering in dashboards

4. **Memory System Implementation**:
   ```python
   # Memory activation in agent definitions
   def get_data_analyst():
       return Agent(
           role="Enterprise Data Analyst",
           goal="Analyze business data to extract valuable insights and trends",
           backstory="""You are an expert data analyst specializing in SQL and database analysis
           for pharmaceutical retail platforms. You query complex database schemas and extract
           meaningful insights. You perform full schema discovery and in-depth business analysis.
           You maintain memory of previous analyses and build upon your findings over time.""",
           verbose=True,
           allow_delegation=False,
           tools=[db_tool, retention_tool],
           knowledge=knowledge,
           memory=True  # Enable memory for context retention
       )
   
   def get_chat_data_analyst():
       return Agent(
           role="Data Q&A Expert",
           goal="Quickly answer user questions about sales, orders, products, and customers",
           backstory="""You are the primary Q&A agent in chat mode. You rely on the Knowledge Base
   first. You query live data only when required or told to refresh. You now handle retention too.
   
   Tools:
   - CockroachDBTool
   - RetentionAnalysisTool
   - MethodologyTool
   
   Your job is to:
   1. Use the KB when possible
   2. Run queries only when needed
   3. Handle retention requests directly via the RetentionAnalysisTool
   4. Maintain memory of recent SQL queries and results for efficiency
   
   When citing KB info, mention the timestamp. Never overwrite the KB yourself.""",
           verbose=False,
           allow_delegation=False,
           tools=[db_tool, retention_tool, methodology_tool],
           knowledge=knowledge,
           memory=True
       )
   ```

5. **Enhanced Logging Implementation**:
   ```python
   def save_chat_result(self, query: str, response: str, agent_role: str, tools_used=None, focus_area=None):
       """Save chat results for persistence and visualization with enhanced metadata."""
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       filename = f"chat_result_{timestamp}.md"
       
       # Determine which tools were used (if not provided)
       if tools_used is None:
           tools_used = []
           # Check for indicators of specific tool usage in the response
           if "SQL Query:" in response or "```sql" in response:
               tools_used.append("CockroachDBTool")
           if "## Customer Retention Analysis" in response:
               tools_used.append("RetentionAnalysisTool")
           if "## Methodology" in response:
               tools_used.append("MethodologyTool")
           if "generated" in response.lower() and ("chart" in response.lower() or "dashboard" in response.lower()):
               tools_used.append("VisualizationTool")
       
       # Add focus area metadata if applicable
       focus_metadata = ""
       if focus_area:
           focus_metadata = f"\n## Focus Area\n{focus_area}"
       
       # Create the content with enhanced metadata
       content = f"""# Plazza Analytics Chat Result

   ## Query
   {query}

   ## Response from {agent_role}
   {response}

   ## Metadata
   - **Timestamp**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
   - **Agent**: {agent_role}
   - **Tools Used**: {', '.join(tools_used) if tools_used else 'None'}
   - **Analysis Type**: {"Full Analysis" if self.requires_full_analysis else "Quick Answer"}
   - **Memory Enabled**: True{focus_metadata}

   ## Processing Record
   - **Request Time**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
   - **KB Access**: {"Yes" if self.kb_last_updated else "No"}
   - **KB Age**: {f"{(datetime.now() - self.kb_last_updated).days} days" if self.kb_last_updated else "N/A"}
   """
       
       # Save to file for potential visualization
       filepath = os.path.join("Run_Results", filename)
       os.makedirs(os.path.dirname(filepath), exist_ok=True)
       
       with open(filepath, "w") as f:
           f.write(content)
   ```

6. **JSON Output Implementation**:
   ```python
   # Generate JSON summary alongside markdown for easier reuse
   json_filepath = os.path.join("Run_Results", f"chat_result_{timestamp}.json")
   json_content = {
       "query": query,
       "response": response,
       "agent": agent_role,
       "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
       "tools_used": tools_used,
       "analysis_type": "Full Analysis" if self.requires_full_analysis else "Quick Answer",
       "memory_enabled": True,
       "focus_area": focus_area,
       "kb_accessed": self.kb_last_updated is not None,
       "kb_age_days": (datetime.now() - self.kb_last_updated).days if self.kb_last_updated else None
   }
   
   import json
   with open(json_filepath, "w") as f:
       json.dump(json_content, f, indent=2)
   ```

7. **Tool Attribution Tracking**:
   ```python
   # Determine tools used based on response content
   tools_used = []
   if agent == self.visualization_specialist:
       tools_used = ["VisualizationTool"]
       if "product sales chart" in answer.lower():
           tools_used.append("TopProductsChartTool")
       if "customer retention" in answer.lower():
           tools_used.append("CustomerRetentionChartTool")
       if "metrics dashboard" in answer.lower():
           tools_used.append("MetricsDashboardTool")
   elif agent == self.chat_data_analyst:
       if "SQL Query:" in answer or "```sql" in answer:
           tools_used.append("CockroachDBTool")
       if "## Customer Retention Analysis" in answer:
           tools_used.append("RetentionAnalysisTool")
       if "## Methodology" in answer:
           tools_used.append("MethodologyTool")
   ```

8. **Benefits**:
   - **Improved Conversation Coherence**: Agents maintain context across multiple turns
   - **Enhanced SQL Efficiency**: Data Q&A Expert remembers recent queries and results
   - **Analysis Continuity**: Enterprise Data Analyst builds upon previous findings
   - **Visualization Consistency**: Visualization Specialist maintains consistent styling
   - **Strategic Follow-Through**: Strategy Advisor tracks recommendation implementation
   - **Superior Debugging**: Detailed logging with tool attribution and execution metadata
   - **Dashboard Integration**: Structured JSON enables automatic visualization updates
   - **Performance Monitoring**: Execution timing and tool usage analytics
   - **Knowledge Tracking**: KB access and age metrics for freshness monitoring
   - **Specialized Analysis**: Focus area tracking for domain-specific insights

9. **Files Modified**:
   - `/Core_Scripts/agent_registry.py`: Added memory=True to all agent definitions and enhanced backstories
   - `/Core_Scripts/plazza_chat.py`: Implemented enhanced save_chat_result with metadata and JSON output
   - `/CLAUDE.md`: Updated documentation with implementation details

## Project Overview

This project combines CrewAI with CockroachDB to create an AI-powered data analysis system for the Plazza ecosystem (a retail/pharmaceutical platform). The system includes database schema documentation generation, AI-driven data analysis, and API documentation tools.

## Recent Enhancements (March 2025)

### System Overview (Updated March 25)

This system now implements a fully modular, tool-based architecture with clearly separated responsibilities:

#### Core Modules
- **agent_registry.py**: Centralized factory for all agents and tools
- **plazza_analytics.py**: Data analysis and visualization functionality
- **plazza_strategy.py**: Business strategy recommendations
- **plazza_chat.py**: User interface and query routing
- **crewai_visualization.py**: Enhanced visualization capabilities

#### Agent Hierarchy
- **Data Q&A Expert** (Primary chat agent): KB-first approach with specialized tools
- **Enterprise Data Analyst**: Deep analysis with database discovery
- **Visualization Specialist**: Creates charts and dashboards from KB data
- **Business Strategy Advisor**: Strategic recommendations based on KB insights

#### Tool Composition
- **CockroachDBTool**: SQL query execution across databases
- **RetentionAnalysisTool**: Customer retention metrics calculation
- **MethodologyTool**: Structured query execution with documentation
- **VisualizationTool**: Visual representation of analysis results
- **Specialized Chart Tools**: TopProductsChartTool, CustomerRetentionChartTool, etc.

#### Knowledge Flow
1. User input → Chat orchestrator (plazza_chat.py)
2. Intent routing → Appropriate agent
3. KB-first approach → Check knowledge before querying
4. Tool execution → Specialized functionality
5. Response + visualization → Enhanced user experience
6. Knowledge preservation → Updated KB for future use

This architecture now follows modern software engineering principles including:
- **Separation of concerns**: Each module has a single responsibility
- **Dependency injection**: Tools and knowledge passed to agents
- **Factory pattern**: Agent creation centralized in registry
- **Modular composition**: Specialized tools composed into workflows
- **Knowledge-first design**: Prioritizing existing knowledge over fresh computation

### Path Standardization and File Organization (March 26)

1. **Path Standardization**:
   - Fixed inconsistent file paths across the codebase
   - Moved output files from `/Core_Scripts/` to proper `/Run_Results/` directory
   - Updated all file references to use standardized locations
   - Ensured all components consistently use the correct directory structure
   - Added robust fallback path resolution for missing files

2. **Environment Variable Configuration**:
   - Replaced hardcoded paths with environment variable support
   - Added fallback mechanisms for consistent behavior
   - Added `VISUALIZATION_OUTPUT_DIR` environment variable support
   - Added `DEFAULT_ANALYSIS_FILE` environment variable for default input
   - Ensured all tool wrappers respect environment settings
   - Added centralized path resolution logic for consistency

3. **Clean Separation of Concerns**:
   - Established clear boundaries between code and output directories
   - Implemented proper directory structure following software engineering best practices
   - Enhanced documentation with comprehensive file organization guidelines
   - Created centralized path resolution mechanisms in each module
   - Added explicit checks for directory existence with automatic creation

### Visualization System Enhancements (March 25-26)

1. **Flexible Input Handling**:
   - Updated visualization module to accept direct content or file paths
   - Added `content` parameter to `visualize_analysis_results()` function
   - Modified `VisualizationTool` to accept optional `input_data` parameter
   - Created dedicated chart-specific tools for more granular control

3. **Enhanced Data Persistence**:
   - Added automatic JSON export of parsed markdown data
   - Created timestamped filenames for better tracking
   - Implemented automatic directory creation when needed
   - Added data reusability for agent chaining scenarios

4. **Specialized Visualization Tools**:
   - Added `TopProductsChartTool` for creating product sales charts
   - Added `CustomerRetentionChartTool` for retention analysis
   - Added `MetricsDashboardTool` for comprehensive dashboards
   - Each tool accepts direct markdown content as input
   - Integrated specialized tools with agent registry

5. **Bundling and Portability**:
   - Added ZIP export functionality for visualization bundles
   - Implemented `export_visualizations_as_zip()` utility function
   - Added ZIP option to command-line interface
   - Created automatic bundling in visualization tools

6. **Event Logging for Traceability**:
   - Added visualization event logging to `visualization_log.md`
   - Captured source, timestamp, and output details
   - Implemented logging in both CLI and tool interfaces
   - Enhanced debugging capabilities with detailed logs

7. **Standardized Tool Naming and References**:
   - Ensured consistent naming between class names and tool names
   - Updated tool descriptions to reference other specialized tools
   - Added clear cross-references between general and specialized tools
   - Enhanced Visualization Specialist agent with access to all visualization tools

8. **Testing and Validation**:
   - Added test suite for CLI entry point validation
   - Implemented test cases for file and content arguments
   - Added tests for ZIP bundle functionality
   - Created mock systems for isolated testing

9. **Implementation Examples**:
   ```python
   # Direct content visualization
   from crewai_visualization import visualize_analysis_results
   
   # Pass content directly
   result = crew.kickoff()
   viz_results = visualize_analysis_results(content=result)
   
   # Agent using visualization tool with input_data
   visualization_tool = VisualizationTool()
   viz_results = visualization_tool._run(input_data=analysis_text)
   
   # Specialized chart tool usage
   product_chart_tool = TopProductsChartTool()
   chart_path = product_chart_tool._run(input_data=analysis_text)
   
   # Using default input from environment
   viz_results = visualize_analysis_results()  # uses DEFAULT_ANALYSIS_FILE
   ```

10. **Command-Line Interface Improvement**:
    ```bash
    # Visualize from file
    python crewai_visualization.py --file analysis.md --output-dir visuals
    
    # Visualize from direct content
    python crewai_visualization.py --content "## Analysis..." --output-dir visuals
    
    # Read from stdin
    cat analysis.md | python crewai_visualization.py --content - --zip
    
    # Use environment defaults (DEFAULT_ANALYSIS_FILE and VISUALIZATION_OUTPUT_DIR)
    python crewai_visualization.py
    ```

11. **Benefits**:
    - More flexible integration options for CrewAI workflows
    - Better support for direct agent-to-agent chaining
    - Improved data persistence for downstream consumption
    - Granular control over visualization types
    - Enhanced traceability through logging
    - More modular and reusable visualization components
    - Standardized naming and references across the system
    - Comprehensive test coverage for CLI functionality

12. **Files Modified**:
    - Updated: `/Core_Scripts/crewai_visualization.py`
    - Updated: `/Core_Scripts/agent_registry.py`
    - Updated: `/Core_Scripts/plazza_analytics.py`
    - Created: `/Core_Scripts/tests/test_visualization_cli.py`
    - Updated: `/.env`
    - Updated: `/CLAUDE.md`
    - Moved: `sales_ai_run_result.md` from `/Core_Scripts/` to `/Run_Results/`

### Optional Enhancements Implementation (March 24, 2025)

1. **Connection Reuse Optimization**:
   - Centralized database connection mapping at the module level for sharing
   - Implemented connection pooling in MethodologyTool to reuse connections across queries for the same database
   - Enhanced RetentionAnalysisTool to execute multiple queries with a single connection instead of creating multiple
   - Added query grouping by database to minimize connection creation
   - Created robust connection cleanup with explicit try/finally blocks
   - Added global DB_SCHEMA_CACHE for storing schema information in memory-enabled agents

2. **Agent Memory Integration with Caching**:
   - Enhanced _list_all_databases method to cache results for memory-enabled agents
   - Added class-level caching for RetentionAnalysisTool to avoid redundant expensive queries
   - Implemented memory-aware functions that check for cached results before executing
   - Added knowledge preservation to minimize database load for memory-enabled agents
   - Ensured proper cache handling with consistent data structures
   - Set up memory system to properly honor the memory=True parameter in agent definitions

3. **Visualization Hooks in RetentionAnalysisTool**:
   - Added automatic visualization generation in RetentionAnalysisTool
   - Implemented _generate_visualizations() helper method to create charts
   - Added integration with both specialized and general visualization tools
   - Enhanced tool description to document visualization capabilities
   - Added visualization file references in analysis results
   - Implemented error handling to ensure analysis works even if visualization fails
   - Created parameter to optionally disable visualizations when needed

4. **JSON Output for Dashboard Integration**:
   - Added JSON parallel output alongside Markdown in visualization module
   - Implemented _save_json_data method to export structured data for dashboards
   - Added timestamp-based filenames for JSON exports (matching HTML/PNG)
   - Enhanced result object to include JSON path in return values
   - Added enable_json_output parameter with default=True setting
   - Maintained backward compatibility with existing visualization functions

5. **Future Module Separation**:
   - Prepared for eventual tool separation by centralizing connection logic
   - Maintained clear component boundaries using class variables and proper scoping
   - Organized complex tools with clear method responsibilities
   - Added comments suggesting eventual file organization improvements
   - Ensured loosely coupled implementations to facilitate future refactoring

6. **Implementation Benefits**:
   - **Performance**: Significant reduction in database connections through pooling and reuse
   - **Memory**: Better utilization of agent memory for caching expensive computations
   - **Integration**: JSON output enables programmatic dashboard integration
   - **Visualization**: Automated chart generation directly from analysis tools
   - **Development**: Modular implementation that could be extended to separate files
   - **Robustness**: Enhanced error handling and connection cleanup
   - **User Experience**: Faster response times with cached data for memory-enabled agents

7. **Technical Details**:
   ```python
   # Database connection mapping - moved to module level for reuse
   DB_CONNECTION_VARS = {
       "user_transactions": "DATABASE_URL_USER_TRANSACTIONS",
       "defaultdb": "DATABASE_URL",
       "plazza_erp": "DATABASE_URL_ERP",
       "user_events": "DATABASE_URL_USER"
   }
   
   # Cache for database schema information to optimize memory-enabled agents
   DB_SCHEMA_CACHE = {}
   
   def _list_all_databases(self):
       # Return cached result if available for memory-enabled agents
       global DB_SCHEMA_CACHE
       if 'all_databases' in DB_SCHEMA_CACHE:
           return DB_SCHEMA_CACHE['all_databases']
           
       # Use just one connection to discover all databases
       conn = None
       for db_name, env_var in DB_CONNECTION_VARS.items():
           connection_string = os.getenv(env_var)
           if connection_string:
               try:
                   conn = psycopg2.connect(connection_string)
                   break
               except Exception:
                   continue
                   
       # Cache the result for future use
       output = "\n".join(result)
       DB_SCHEMA_CACHE['all_databases'] = output
       return output
       
   # MethodologyTool connection optimization with query grouping
   def _run(self, queries: list) -> str:
       # Group queries by database to minimize connection creation
       queries_by_db = {}
       for i, query_obj in enumerate(queries):
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
           # Create a single connection for all queries to this database
           try:
               conn = psycopg2.connect(connection_string)
               # Execute each query using the same connection...
               
   # RetentionAnalysisTool with visualization hooks and caching
   class RetentionAnalysisTool(BaseTool):
       # Class-level cache for expensive retention analysis results
       _retention_cache = None
       
       def _run(self, generate_visuals=True) -> str:
           """
           Execute comprehensive retention analysis across databases
           
           Args:
               generate_visuals (bool): Whether to generate visualizations (default: True)
           """
           # For memory-enabled agents, we can cache the expensive retention analysis
           if RetentionAnalysisTool._retention_cache:
               return RetentionAnalysisTool._retention_cache
               
           # Multiple queries with single connection
           conn = psycopg2.connect(connection_string)
           try:
               # Process each query...
               
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
           finally:
               conn.close()
       
       def _generate_visualizations(self, analysis_results):
           """Generate visualizations from retention analysis results"""
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
           
   # JSON output for dashboard integration
   def _save_json_data(self, markdown_data, output_dir, filename_prefix):
       # Parse the data if it's a string
       if isinstance(markdown_data, str):
           sections = self.parse_markdown_content(markdown_data)
       else:
           sections = markdown_data
           
       # Create timestamp filename matching HTML/PNG outputs
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       json_filename = f"{filename_prefix}_{timestamp}.json"
       json_path = os.path.join(output_dir, json_filename)
       
       # Store parsed markdown data in JSON format
       with open(json_path, 'w') as f:
           json.dump(sections, f, indent=2)
   ```

8. **Files Modified**:
   - `/Core_Scripts/plazza_analytics.py`: Enhanced database connection handling with centralized mapping and visualization hooks
   - `/Core_Scripts/crewai_visualization.py`: Added JSON output capabilities and improved integration
   - `/CLAUDE.md`: Updated documentation with implementation details
   
9. **Testing Considerations**:
   - Connection pooling improvements require database availability for full testing
   - Memory integration benefits will be most apparent in long-running agent sessions
   - JSON output provides new integration possibilities with external dashboards
   - Future unit tests could mock database connections to verify optimizations
   - Visualization hooks should be tested with various retention analysis patterns
   - Test with and without generate_visuals=False to ensure parameter works correctly
   - Verify visualization error handling doesn't impact core analysis functionality

### UX Polishing Enhancements (March 28)

1. **Knowledge Base Freshness Check**:
   - Added automatic detection and display of KB age at startup
   - Implemented warning for outdated KB (older than 7 days)
   - Added suggestion to run 'refresh' for fresh data
   - Included timestamp extraction from KB content with regex
   - Enhanced console output with colored status indicators

2. **System Status Information**:
   - Added visualization count display at startup
   - Implemented KB status reporting with color indicators
   - Created helpful messages based on system state
   - Added methods to check file timestamps and content
   - Improved onboarding experience for new users

3. **Focused Analysis Support**:
   - Added support for partial/focused analysis updates
   - Implemented domain-specific keyword detection for different data types
   - Created focused query creation for targeted analysis
   - Added support for refreshing specific areas like:
     - Airtable data analysis
     - Inventory analysis
     - Sales metrics
     - Customer data
     - Order processing
   - Reduced analysis time by limiting schema discovery when focus is known

4. **Implementation Details**:
   ```python
   # Freshness check implementation
   def check_kb_freshness(self):
       """Check when the knowledge base was last updated."""
       # Find and extract timestamps from KB content
       import re
       timestamp_matches = re.findall(r'## Full Analysis on (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', content)
       
       if timestamp_matches:
           # Use the most recent timestamp
           latest_timestamp = max(timestamp_matches)
           return datetime.strptime(latest_timestamp, '%Y-%m-%d %H:%M:%S')
       
       # Fall back to file modification time
       return mod_date
   
   # Focused analysis detection
   def detect_focused_analysis(self, user_input_lower):
       """Detect if the user is requesting a focused analysis on a specific area."""
       for focus_area, keywords in self.partial_update_keywords.items():
           if any(keyword in user_input_lower for keyword in keywords):
               return focus_area
       return None
   ```

5. **Benefits**:
   - Better transparency about KB freshness
   - More efficient focused analysis without full schema rediscovery
   - Enhanced user experience with status indicators
   - Clearer guidance for users on available commands
   - Faster analysis for specific data domains

6. **Files Modified**:
   - `/Core_Scripts/plazza_chat.py`: Added freshness check and focused analysis
   - `/CLAUDE.md`: Updated documentation

### Analytics & Sales AI Integration with PlazzaChat (March 27)

1. **Plazza Analytics Integration**:
   - Updated `plazza_chat.py` to directly use the `run_analysis()` function from `plazza_analytics.py`
   - Added import: `from Core_Scripts.plazza_analytics import run_analysis`
   - Modified data_analyst handler in run_chat() to call run_analysis() directly
   - Bypassed task creation for more efficient processing of full analysis requests
   - Added clear console output with timing information
   - Ensured proper history tracking and result saving
   - Displayed a preview of the analysis result for better user experience

2. **Sales AI Module Integration**:
   - Updated `plazza_chat.py` to integrate with `sales_ai.py` for strategic recommendations
   - Added direct import of the sales_ai crew: `from Core_Scripts.sales_ai import crew as sales_ai_crew`
   - Implemented specialized routing logic in the run_chat() function for strategic queries
   - Added error handling for sales_ai.py execution failures
   - Enhanced the user experience with clear messaging about strategy processing

3. **Implementation Details**:
   ```python
   # Import the Sales AI crew at the top of the file
   from Core_Scripts.sales_ai import crew as sales_ai_crew
   
   # Inside the run_chat() function
   elif agent == self.business_strategy_advisor:
       print(f"\n📊 Routing to Sales Strategist Agent (sales_ai.py)...")
       print(f"   Running the sales AI crew for strategic recommendations.\n")

       try:
           start_time = time.time()
           answer = sales_ai_crew.kickoff()
           end_time = time.time()

           self.history.append({"role": "Sales Strategist", "content": answer})
           last_response = answer

           result_path = self.save_chat_result(user_input, answer, "Sales Strategist")

           processing_time = end_time - start_time
           print(f"\n🤖 Sales Strategist (responded in {processing_time:.1f}s):")
           print(f"{answer}\n")

           self.requires_full_analysis = False

           continue  # Skip the rest of the loop since we've already printed the result
       except Exception as e:
           print(f"\n❌ Error running sales_ai.py: {str(e)}")
           print("Please try again or check the sales_ai.py module.")
           continue
   ```

3. **Benefits**:
   - Enables direct access to the sales_ai.py functionality from the chat interface
   - Preserves full context and history across interactions
   - Provides consistent user experience with timing information
   - Maintains knowledge persistence by saving results to the chat history
   - Handles errors gracefully with meaningful error messages

4. **Files Modified**:
   - `/Core_Scripts/plazza_chat.py`: Added sales_ai_crew import and routing implementation
   - `/CLAUDE.md`: Updated documentation about the integration

### System Architecture Modularization (March 25)

1. **Agent Registry Centralization**:
   - Created `agent_registry.py` as a central module for agent creation/configuration
   - Moved all agent definitions from `plazza_chat.py` into factory functions
   - Implemented shared tool instances to avoid duplication
   - Added global knowledge source with proper initialization
   - Provided clean interface for accessing agent instances

2. **Strategy Module Extraction**:
   - Created dedicated `plazza_strategy.py` for all strategy-related functionality
   - Moved `business_strategy_advisor` agent from `plazza_analytics.py` to `plazza_strategy.py`
   - Moved `create_strategy_task()` function to the strategy module
   - Added clear redirection comments in the original locations
   - Updated `plazza_chat.py` to import from the new module

3. **Module Responsibility Boundaries**:
   - `plazza_analytics.py`: Now focused solely on data analysis and visualization
   - `plazza_strategy.py`: Handles all business strategy recommendations
   - `agent_registry.py`: Centralizes agent definitions and configurations
   - `plazza_chat.py`: User interface and orchestration only, imports from specialized modules

4. **Implementation Details**:
   ```python
   # Agent registry pattern (agent_registry.py)
   def get_data_analyst():
       return Agent(
           role="Enterprise Data Analyst",
           goal="Analyze business data to extract valuable insights and trends",
           backstory="""You are an expert data analyst specializing in SQL...""",
           tools=[db_tool, retention_tool],
           knowledge=knowledge
       )
       
   # Usage in other modules
   from Core_Scripts.agent_registry import get_chat_data_analyst
   analyst = get_chat_data_analyst()
   ```

5. **Module Extraction Pattern (plazza_strategy.py)**:
   ```python
   # In plazza_analytics.py (original file)
   # 🚫 NOTE: The Business Strategy Advisor agent and related task logic 
   # have been moved to `plazza_strategy.py`
   
   # In plazza_chat.py (consumer)
   from Core_Scripts.plazza_strategy import create_strategy_task, business_strategy_advisor
   ```

6. **Benefits**:
   - Cleaner, more maintainable codebase with clear component boundaries
   - Easier testing and component replacement
   - Better separation of concerns between analysis, strategy, and visualization
   - Simplified agent lifecycle management
   - Enhanced modularity for future extensions

7. **Template Reusability Enhancements**:
   - Extracted strategy description into `STRATEGY_TASK_TEMPLATE` constant
   - Extracted expected output into `EXPECTED_OUTPUT_TEMPLATE` constant
   - Made templates available at module level for reuse in other scripts
   ```python
   # In plazza_strategy.py
   STRATEGY_TASK_TEMPLATE = """
   Develop actionable business strategies based on existing insights...
   """
   
   # Usage in create_strategy_task()
   base_description = STRATEGY_TASK_TEMPLATE
   ```

8. **Files Modified**:
   - Created: `/Core_Scripts/agent_registry.py`
   - Created: `/Core_Scripts/plazza_strategy.py`
   - Modified: `/Core_Scripts/plazza_analytics.py`
   - Modified: `/Core_Scripts/plazza_chat.py`
   - Updated: `/CLAUDE.md`

### Strategy Module Enhancement (March 24, 2025)

1. **Automated Strategy Logging**:
   - Added `save_strategy_output()` function to archive all generated strategies
   - Implemented automatic timestamping for strategy filenames
   - Added metadata section with generation details (timestamp, model, file reference)
   - Created dedicated `/Run_Results/strategies/` directory for strategy persistence
   - Added proper formatting and structure to saved strategy files

2. **Delegation Framework Integration**:
   - Enhanced `create_strategy_task()` with optional data analyst agent parameter
   - Added conditional delegation instructions when analyst agent is available
   - Implemented task configuration with `allow_delegation=True` when appropriate
   - Provided detailed knowledge gap handling guidelines in task description
   - Preserved Knowledge-First approach by prioritizing existing insights

3. **Automated Output Processing**:
   - Added `callback` parameter to task creation for automatic logging
   - Implemented lambda function to process output immediately after generation
   - Created automatic directory structure management with `Path` handling
   - Enhanced error handling with formatting fallbacks for malformed outputs

4. **Implementation Details**:
   ```python
   # Improved directory structure with Path objects
   BASE_DIR = Path(__file__).resolve().parent.parent
   KNOWLEDGE_DIR = BASE_DIR / "knowledge"
   STRATEGY_DIR = BASE_DIR / "Run_Results" / "strategies"
   
   # Ensure directories exist
   STRATEGY_DIR.mkdir(parents=True, exist_ok=True)
   
   # Strategy logging function
   def save_strategy_output(output, filename_prefix="strategy"):
       ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
       filename = f"{filename_prefix}_{ts}.md"
       filepath = STRATEGY_DIR / filename
       
       # [Content formatting logic...]
       
       with open(filepath, "w") as f:
           f.write(output)
       
       print(f"Strategy saved to {filepath}")
       return str(filepath)
   
   # Enhanced task factory with delegation support
   def create_strategy_task(user_query=None, analysis_content=None, data_analyst_agent=None):
       # [Base task creation logic...]
       
       # Add delegation if analyst is provided
       if data_analyst_agent:
           # [Delegation instructions...]
           
           return Task(
               description=base_description,
               expected_output=EXPECTED_OUTPUT_TEMPLATE,
               agent=business_strategy_advisor,
               async_execution=False,
               callback=lambda output: save_strategy_output(output),
               allow_delegation=True
           )
   ```

5. **Enhanced Chat Integration**:
   - Modified `plazza_chat.py` to use the enhanced strategy task creation
   - Added data analyst agent reference for potential delegation
   - Replaced direct `sales_ai_crew.kickoff()` with more modular `business_strategy_advisor.execute_task()`
   - Enhanced output handling with better messaging and error reporting
   - Updated tool tags for improved tracking in chat history
   
   ```python
   # Updated routing in plazza_chat.py
   elif agent == self.business_strategy_advisor:
       print(f"\n📊 Routing to Strategic Business Consultant...")
       
       try:
           # Create a strategy task with the chat_data_analyst for delegation
           strategy_task = create_strategy_task(
               user_query=user_input,
               data_analyst_agent=self.chat_data_analyst
           )
           
           answer = self.business_strategy_advisor.execute_task(strategy_task)
           # [Result handling...]
       except Exception as e:
           print(f"\n❌ Error generating strategy: {str(e)}")
   ```

6. **Enhanced Usability**:
   - Added clear path structure using `pathlib.Path` for cross-platform compatibility
   - Implemented directory creation with `exist_ok=True` for fault tolerance
   - Added metadata enrichment for better traceability and history tracking
   - Enhanced content structure with conditional formatting
   - Added intelligent content parsing to preserve document structure

7. **Benefits**:
   - **Enhanced Traceability**: All strategies are now automatically logged with timestamps
   - **Better Knowledge Management**: Dedicated directory structure for strategy outputs
   - **Improved Debugging**: Metadata enrichment provides better context for troubleshooting
   - **Future-Proof Design**: Optional delegation support enables multi-agent workflows
   - **Consistent Structure**: Standardized output formatting across all strategy generation
   - **Audit Capabilities**: Complete history of all generated strategies maintained automatically
   - **Simplified Chat Integration**: Direct integration with strategy module without using sales_ai_crew
   - **Improved Error Handling**: Better error reporting with clear messages to the user

8. **Files Modified**:
   - Updated: `/Core_Scripts/plazza_strategy.py` with logging and delegation enhancements
   - Updated: `/Core_Scripts/plazza_chat.py` to use the enhanced strategy module
   - Updated: `/CLAUDE.md` with comprehensive documentation of strategy improvements

### Batch Analysis Enhancement with Testing Implementation (March 24-26)

1. **Complete Batch Analysis Overhaul**:
   - Refactored `batch_analysis.py` to reuse `run_analysis()` from `plazza_analytics.py`
   - Integrated visualization generation with direct `crewai_visualization` module linkage
   - Added Knowledge Base freshness check before running analysis 
   - Implemented flexible command-line options with multiple operational modes
   - Enhanced path handling with environment variable support
   - Added ZIP bundle creation for easy visualization sharing
   - Implemented comprehensive test suite with unittest framework
   - Added argument validation to prevent conflicting flags
   - Created detailed documentation with usage examples

2. **Knowledge Base Freshness Check**:
   - Improved `check_kb_freshness()` function with detailed output 
   - Enhanced timestamp extraction from KB content with better regex
   - Added display of hours/days since last update for better context
   - Implemented tuple return (is_fresh, last_updated) for more flexibility
   - Added robust error handling with informative messages
   - Enhanced logging with emoji indicators for better readability

3. **Unit Test Implementation**:
   - Added comprehensive test suite in `/Core_Scripts/tests/test_batch_analysis.py`
   - Implemented tests for all command-line options and combinations
   - Added tests for KB freshness detection with various timestamps
   - Created test cases for conflicting flag validation
   - Implemented mock-based tests for argument validation logic
   - Enhanced test architecture with proper setup and teardown

4. **Smart File Discovery Logic**:
   - Added `get_latest_analysis_file()` function for finding most recent analysis
   - Implemented glob pattern matching for timestamped files
   - Created sorting by modification time to prioritize newest files
   - Enhanced file path handling with standardized approaches
   - Added fallback mechanisms for missing files
   - Improved robustness with multi-location checking

5. **Operational Modes**:
   - **Full Analysis Mode**: Complete analysis with visualizations
   - **Visualization-Only Mode**: Refresh visuals from existing analysis
   - **Analysis-Only Mode**: Skip visualization generation
   - **Force Mode**: Override KB freshness check
   - Added mode-specific error handling and user guidance
   - Implemented dedicated output formatting for each mode

6. **Command-Line Validation**:
   - Added validation for conflicting flags (`--no-viz` and `--viz-only`)
   - Implemented warning for illogical combinations (`--force` with `--viz-only`)
   - Added descriptive error messages with usage examples
   - Enhanced CLI with consistent argument naming and descriptions
   - Improved user experience with progress indicators and next steps
   - Added validation with sys.exit(1) for critical errors

7. **Documentation Improvements**:
   - Created comprehensive `batch_analysis_README.md` with detailed usage guide
   - Updated `Core_Scripts/README.md` with CLI options and testing info
   - Enhanced CLAUDE.md with implementation details and usage examples
   - Added troubleshooting section for common issues
   - Updated testing documentation with instructions for all test files
   - Added example commands for all operational modes
8. **Benefits**:
   - **Efficiency**: Avoids redundant analysis when Knowledge Base is recent
   - **Resource Conservation**: Reduces computational load and database queries
   - **Flexibility**: Multiple CLI options for different use cases
   - **Reliability**: Better error handling prevents system crashes
   - **Maintainability**: Comprehensive test suite ensures stability
   - **Automation-Friendly**: Designed for automated scheduled execution via CRON
   - **User Experience**: Enhanced progress indicators and next steps guidance
   - **Portability**: Improved path handling with environment variables

9. **Files Modified**:
   - `/Core_Scripts/batch_analysis.py`: Complete refactoring with enhanced features
   - `/Core_Scripts/tests/test_batch_analysis.py`: New unit test implementation
   - `/Core_Scripts/tests/test_batch_analysis_mock.py`: Mock test for validation logic
   - `/Core_Scripts/batch_analysis_README.md`: Comprehensive usage documentation
   - `/Core_Scripts/README.md`: Updated with batch analysis details and testing info
   - `/CLAUDE.md`: Enhanced documentation

10. **Usage Examples**:
    ```bash
    # Normal run (skips if KB is fresh)
    python Core_Scripts/batch_analysis.py
    
    # Force run (ignores KB freshness)
    python Core_Scripts/batch_analysis.py --force
    
    # Skip visualization generation
    python Core_Scripts/batch_analysis.py --no-viz
    
    # Custom output directory
    python Core_Scripts/batch_analysis.py --output-dir /path/to/visuals
    
    # Visualization only (no analysis)
    python Core_Scripts/batch_analysis.py --viz-only
    
    # Run tests
    python -m unittest Core_Scripts/tests/test_batch_analysis.py
    ```

### Knowledge Base-First Architecture & Methodology Transparency (March 24)

1. **Knowledge Retention Improvements**:
   - Modified `save_analysis_results()` to append new analysis rather than overwriting
   - Added timestamped headers and markdown dividers between analyses
   - Implemented duplicate content checking to avoid repetition
   - Preserved KB history for better knowledge accumulation over time

2. **Agent Knowledge-First Approach**:
   - Updated all agents to prioritize Knowledge Base before querying databases
   - Added explicit "check KB first" instructions in all agent backstories
   - Implemented KB citation with timestamps to track knowledge freshness
   - Created rules against overwriting existing KB content

3. **Methodology Transparency Enhancements**:
   - Added MethodologyTool for structured query execution and documentation
   - Implemented concise response format with option for detailed methodology
   - Created intelligent detection of methodology requests based on keywords
   - Balanced transparency with clean output through conditional formatting

4. **F-String Curly Braces Fix**:
   - Fixed ValueError when using JSON examples inside f-strings
   - Updated plazza_chat.py to use double curly braces `{{` and `}}` to escape them in f-strings
   - Prevented "invalid format specifier" errors when executing SQL queries

5. **Implementation Details**:
   ```python
   # Knowledge preservation with append-only updates
   def save_analysis_results(content, filepath=ANALYSIS_RESULTS_PATH):
       # Save to main filepath (overwrite allowed for main file)
       with open(filepath, 'w') as file:
           file.write(str(content))
       
       # For knowledge file, APPEND rather than overwrite
       knowledge_file = os.path.join(parent_dir, 'knowledge', 'sales_analysis_results.md')
       
       # Create a formatted header for the new content
       header = f"\n\n---\n\n## Full Analysis on {timestamp}\n\n"
       
       # Check for existing content to avoid duplication
       if os.path.exists(knowledge_file):
           with open(knowledge_file, 'r') as file:
               existing_content = file.read()
               
           # Only append if content isn't already in the file
           if formatted_content not in existing_content:
               with open(knowledge_file, 'a') as file:
                   file.write(header)
                   file.write(formatted_content)
   ```

6. **Knowledge Base-First Agent Design**:
   ```python
   self.data_analyst = Agent(
       role="Enterprise Data Analyst",
       goal="Provide business analysis, insights, and metrics using data across the Plazza ecosystem",
       backstory="""You are a senior data analyst with deep access to all databases in the Plazza ecosystem.
       
       **Your First Action Always**: Consult the Knowledge Base.
       If the user's question can be answered using existing knowledge, do not run SQL queries.
       Only run database queries if information is missing, outdated, or never previously documented.
       
       When updating the knowledge base:
       - Do NOT overwrite existing content.
       - Append new findings under correct sections
       - If content already exists, enrich it without deleting prior context.
       """
   )
   ```

7. **Concise Output with Optional Methodology**:
   ```python
   # Format the query results into a methodology section
   def _format_methodology(self, query_results):
       # Create a concise summary for direct answers
       concise_summary = []
       
       # Generate concise summary first (1-2 lines)
       if summary_values:
           results_str = ", ".join([f"{desc.split('(')[0].strip()}: {val}" 
                           for desc, val in summary_values.items()])
           concise_summary.append(f"{results_str}")
       
       # Flag to identify if this is a methodology request
       methodology_requested = any(key.lower() in ['how', 'methodology', 'explain', 'detail'] 
                              for result in query_results 
                              for key in result.get('description', '').lower().split())
       
       # Return just the concise summary if methodology not requested
       if not methodology_requested and concise_summary:
           return "\n".join(concise_summary)
           
       # Otherwise return the full methodology
       return "\n".join(methodology)
   ```

8. **Enhanced Chat Agent Task Description**:
   ```python
   task = Task(
       description=f"""The user has asked: '{user_input}'

   KNOWLEDGE BASE FIRST ALWAYS:
   - Your FIRST action must be to check the Knowledge Base for existing answers
   - Only run new queries if the KB lacks the requested information or if info is outdated
   - When using KB info, cite the source: "According to analysis from [date]..."

   RESPONSE STYLE:
   - Provide a concise, direct answer in 1-2 sentences
   - Include specific metrics with units (₹, %, items)
   - Only show methodology if the user explicitly asks with words like "how" or "explain"
   """
   ```

9. **Benefits**:
   - Significant knowledge retention improvements over time
   - Reduced database queries by prioritizing KB usage
   - Better insights through accumulation of historical knowledge
   - Concise responses with option for detailed methodology
   - Consistent knowledge management across all agents

10. **Files Modified**:
    - `/Core_Scripts/plazza_analytics.py`: Updated `save_analysis_results()`, agent definitions, task creation, and MethodologyTool
    - `/Core_Scripts/plazza_chat.py`: Fixed f-string format issue, updated agent backstories and task descriptions
    - `/CLAUDE.md`: Added documentation about the enhancements

### Multi-Database Schema Discovery Fix (March 23)

1. **Fixed Database Discovery Across All Databases**:
   - Updated CockroachDBTool to properly list all databases with SHOW DATABASES
   - Enhanced querying logic to check all databases, not just defaultdb
   - Added explicit prompting to search across all available databases 
   - Fixed issue where only defaultdb was being checked for tables
   - Improved discovery of Airtable and other integration data

2. **Implementation Details**:
   ```python
   # Added proper database discovery
   def _list_all_databases(self, db_connection_vars):
       """List all available databases in the CockroachDB cluster."""
       result = ["Available databases in CockroachDB cluster:"]
       
       # Add the known databases from our mapping
       for db_name in db_connection_vars.keys():
           result.append(f"- {db_name}")
           
       # Also try to discover additional databases
       additional_dbs = set()
       # ... discovery logic to find all databases
       
       return "\n".join(result)
   ```

3. **Selective Knowledge Base Updates**:
   - Limited knowledge base updates to full analysis results only
   - Prevented chat queries from polluting the knowledge base
   - Added check for agent role and analysis mode before saving
   - Improved RAG quality by only storing comprehensive analyses

4. **Technical Background**:
   - Previously, schema discovery was only checking defaultdb
   - SHOW DATABASES was not properly handled by the CockroachDBTool
   - Chat queries were polluting the knowledge base with low-value content
   - Chat queries about data existence weren't checking all databases

5. **Files Modified**:
   - `/Core_Scripts/plazza_analytics.py`: Enhanced CockroachDBTool with proper database discovery
   - `/Core_Scripts/plazza_chat.py`: Added multi-database check instructions and selective knowledge saving
   - `/CLAUDE.md`: Added documentation about the fixes

6. **Benefits**:
   - Complete visibility across all databases in the CockroachDB cluster
   - Better answers to questions about data existence and availability
   - Cleaner knowledge base with only high-value full analyses
   - More accurate schema discovery in analysis mode

### Chat Mode Enhancement (March 23)

1. **Lightweight Chat vs Full Analysis Mode**:
   - Added dual-mode operation in the chat interface
   - Implemented distinction between quick questions and full analysis
   - Created specialized "Data Q&A Expert" agent for lightweight chat mode
   - Reduced unnecessary database schema discovery for simple queries
   - Fixed performance issues with chat responses

2. **Implementation Details**:
   ```python
   # Added detection of analysis keywords
   analysis_keywords = [
       "analyze", "analysis", "full analysis", "comprehensive", "discover schema",
       "schema discovery", "detailed analysis", "business analysis", "deep dive",
       "comprehensive report"
   ]
   
   # Mode detection based on user input
   self.requires_full_analysis = any(keyword in user_input.lower() for keyword in analysis_keywords)
   
   # Agent selection based on mode
   if self.requires_full_analysis:
       return self.data_analyst  # Full analysis mode
   else:
       return self.chat_data_analyst  # Lightweight chat mode
   ```

3. **Benefits**:
   - Significantly faster responses for simple queries
   - Avoids unnecessary database schema discovery for every question
   - Reduces database load by minimizing exploratory queries
   - Provides more focused answers to specific questions
   - Better user experience with mode-specific prompting

4. **Technical Background**:
   - Previous implementation triggered full schema discovery for every query
   - Each user question would launch comprehensive database exploration
   - This caused long wait times even for simple questions
   - The fix separates chat Q&A from comprehensive analysis

5. **Files Modified**:
   - `/Core_Scripts/plazza_chat.py`: Added mode detection and specialized agents
   - `/CLAUDE.md`: Added documentation about the enhancement

6. **New Components**:
   - Added `chat_data_analyst` agent with focused Q&A backstory
   - Implemented keyword detection for analysis requests
   - Created mode-specific task descriptions
   - Added visual indicators to show which mode is active
   - Updated welcome message to explain the two modes

### CrewAI Compatibility Fix (March 23)

1. **Fixed Knowledge Source Path Handling**:
   - Modified `create_knowledge_source()` to remove dependency on `crewai.utils` module
   - Replaced `crewai.utils.constants.KNOWLEDGE_DIRECTORY` import with direct path construction
   - Fixed path handling to be version-agnostic and work with any CrewAI version
   - Enhanced error handling in knowledge creation logic

2. **Implementation Details**:
   ```python
   # Before (problematic code):
   from crewai.utils.constants import KNOWLEDGE_DIRECTORY
   knowledge_dir = os.path.join(os.getcwd(), KNOWLEDGE_DIRECTORY)
   
   # After (fixed version):
   parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   knowledge_dir = os.path.join(parent_dir, 'knowledge')
   ```

3. **Benefits**:
   - Ensures proper initialization of the RAG knowledge system
   - Works across different CrewAI versions
   - No dependency on internal CrewAI module structure
   - Graceful fallback if knowledge file doesn't exist
   - Better error handling with informative messages

4. **Technical Background**:
   - The issue appeared after updating to a newer version of CrewAI
   - The package structure changed, moving or removing the `utils` module
   - This caused a `ModuleNotFoundError: No module named 'crewai.utils'` error when initializing
   - Our fix avoids referring to internal CrewAI package structure entirely
   - Instead, we use standard Python path manipulation that works regardless of CrewAI version

5. **Files Modified**:
   - `/Core_Scripts/plazza_analytics.py`: Updated `create_knowledge_source()` function
   - `/Core_Scripts/README.md`: Added troubleshooting section about this issue
   - `/CLAUDE.md`: Added documentation about the fix

6. **Testing**:
   - Verified that both `plazza_chat.py` and `plazza_analytics.py` initialize successfully
   - Confirmed that the knowledge file is properly found and loaded
   - Knowledge persistence now works correctly regardless of CrewAI version

### Visualization Styling Update (March 20)

1. **Plazza Branding Integration**:
   - Enhanced all visualizations with Plazza brand colors and styling
   - Created consistent visual language across charts and dashboards
   - Implemented card-based UI with proper spacing and typography
   - Added interactive elements with Plazza-style tooltips

2. **Technical Improvements**:
   - Migrated from Matplotlib to Plotly for interactive visualizations
   - Implemented custom HTML templates with embedded CSS
   - Created color gradient generators for consistent styling
   - Optimized chart rendering for better performance
   - Added insight cards to summarize key metrics

3. **Architecture Improvements**:
   - Enhanced visualization agent with Plazza brand knowledge
   - Updated visualization module to support multiple output formats
   - Fixed import paths for better code organization
   - Created standalone visualization demo script for testing
   - Ensured all visualizations use consistent styling

## Project Structure

The project has been reorganized into the following structure:

- **/Core_Scripts/**: Main application scripts (core system)
  - `agent_registry.py` - Centralized repository of agent definitions and tools
  - `crewai_visualization.py` - Core visualization module with chart generation
  - `plazza_analytics.py` - Main analysis script with database tools and tasks
  - `plazza_chat.py` - Interactive chat interface for database queries
  - `plazza_strategy.py` - Business strategy generation module
  - `tests/` - Test suite for Core_Scripts functionality

- **/Claude_Scripts/**: Contains helper scripts, debugging tools, and experimental implementations
  - `RAG_README.md` - Documentation on RAG integration
  - `explore_db_schema.py` - Generates database schema documentation
  - `explore_db_schema_focused.py` - Focused database documentation generation
  - `fix_rag_integration.py` - Script to fix RAG integration issues
  - `requirements_db_doc.txt` - Requirements for database documentation tools
  - `sales_ai_debug.py` - Debug version of the sales analysis system
  - `visualization_agent_demo.py` - Simple demo of the visualization agent
  - Various Metabase integration files and documentation

- **/Ref_documents/**: Reference materials and API documentation
  - `Sample_Dashboard.md` - Dashboard template with Plazza styling
  - Various API documentation files
  - Database schema JSON files

- **/Run_Results/**: Storage for analysis outputs
  - `sales_ai_run_result.md` - Latest analysis results
  - Chat history and analysis outputs with timestamped filenames

- **/knowledge/**: RAG knowledge store
  - `sales_analysis_results.md` - Persistent storage of analysis for RAG
  - Used by CrewAI's knowledge retrieval system

- **/visuals/**: Visualization outputs
  - HTML dashboards with interactive elements
  - PNG exports for embedding in documentation
  - Each visualization named with timestamp for tracking

## File Organization Guidelines

To maintain consistency and organization in the project:

1. **Output Files**: 
   - All analysis results should be saved to `/Run_Results/`
   - Never save output files to `/Core_Scripts/` or other code directories

2. **Visualizations**:
   - All visualization outputs should go to `/visuals/`
   - Use timestamped filenames to track generation time

3. **Knowledge Management**:
   - Knowledge Base files should be stored in `/knowledge/`
   - Use append-only updates with timestamps for history preservation

4. **Code Organization**:
   - Core functionality should be in `/Core_Scripts/`
   - Experimental scripts should go in `/Claude_Scripts/`
   - Helper function libraries should be imported from main modules

5. **Path Resolution**:
   - Always use absolute paths calculated from the module location
   - Prefer environment variables for configurable paths
   - Use `os.path.join()` for cross-platform compatibility

6. **Environment Configuration**:
   - Store configuration in `.env` file (loaded via dotenv)
   - Never hardcode sensitive information or paths
   - Use variables like `DEFAULT_ANALYSIS_FILE` for common locations

## RAG Knowledge Integration

The system has been enhanced with RAG (Retrieval-Augmented Generation) capabilities to provide knowledge persistence across analysis runs.

### Implementation Status
- **Fully Implemented**: Fixed in both sales_ai.py and sales_ai_debug.py
- **Directory Structure**: Added /knowledge directory at project root 
- **Fixed Path Issue**: Now using relative paths that work with CrewAI's expectations
- **Dual Persistence**: Results saved to both main file and knowledge directory
- **Fault Tolerant**: Falls back to direct file access if RAG encounters issues
- **CrewOutput Handling**: Fixed error when saving CrewOutput objects

### Root Cause Analysis
The issue was in CrewAI's knowledge system path handling:

1. `KNOWLEDGE_DIRECTORY` constant is set to "knowledge" in CrewAI's constants.py
2. In BaseFileKnowledgeSource.convert_to_path() method:
   ```python
   return Path(KNOWLEDGE_DIRECTORY + "/" + path) if isinstance(path, str) else path
   ```
3. This prepends "knowledge/" to any string path, even absolute paths
4. Our temporary file path became "knowledge/var/folders/..." which is invalid
5. Path objects don't get this prefix applied, creating inconsistent behavior

### Solution Implemented

We chose option #1 from our analysis: Create a knowledge directory and use relative paths. The implemented solution:

1. **Created Knowledge Directory**: 
   - Added "knowledge" directory at project root
   - Copy analysis results to knowledge/sales_analysis_results.md

2. **Fixed Path References**:
   - Use simple filenames ('sales_analysis_results.md') for TextFileKnowledgeSource
   - Let CrewAI prepend the "knowledge/" as expected

3. **Enhanced save_analysis_results()**:
   - Saves to both the main file and knowledge directory
   - Maintains timestamps and history preservation
   - Added error handling to gracefully recover
   - Properly handles CrewOutput objects by extracting their raw content
   - Uses type checking with isinstance() before calling string methods
   - Explicitly converts content to string when writing to files

4. **Improved Knowledge Creation Logic**:
   - Extracted to create_knowledge_source() function
   - Better error handling and logging
   - Falls back to empty Knowledge object if file not found
   
5. **Agent Initialization Fix**:
   - Updated knowledge parameter to accept a single Knowledge object, not a list
   - Changed from `knowledge=[sales_knowledge] if sales_knowledge else None` to `knowledge=sales_knowledge`
   - This resolves Pydantic validation errors during Agent initialization

### Code Structure Changes

1. **New Helper Functions**:
   - create_knowledge_source() to handle Knowledge object creation
   - Improved save_analysis_results() for dual file saving

2. **New/Modified Files**:
   - Updated sales_ai.py and sales_ai_debug.py
   - Added knowledge/sales_analysis_results.md
   - Created fix_rag_integration.py helper script
   - Updated CLAUDE.md documentation

3. **New Imports**:
   - Added 'import shutil' for file operations

### Key Insights Learned

1. **CrewAI Knowledge System Expectations**:
   - Expects files to be in a project-relative "knowledge/" directory
   - Requires relative paths (or Path objects) for proper handling
   - Automatically prefixes "knowledge/" to string paths
   - Agent expects a single Knowledge object, not a list of Knowledge objects

2. **Best Practices for CrewAI RAG**:
   - Use simple filenames, not absolute paths
   - Keep knowledge files in the project-relative knowledge directory
   - Implement fallbacks for robustness
   - Ensure content has clear sections for better chunking
   - Convert CrewOutput objects to strings before using string methods
   - Use type checking with isinstance() before calling string methods
   - Handle raw content extraction from CrewOutput objects

## Database Schema Discovery Methodology

The system now includes a methodology for discovering and documenting new database schemas without code changes, using only prompt engineering. We have implemented this in the plazza_analytics.py script.

### Implementation Strategy

1. **Dynamic Schema Discovery**:
   - Uses agents' existing CockroachDBTool to execute information_schema queries
   - Leverages the knowledge persistence system to update schema documentation
   - Works with any newly added tables or databases in the cluster
   - Requires no code modifications, only task prompt adjustments

2. **Generic System Prompts**:
   - All system prompts have been made generic to enable true exploration
   - Removed hardcoded database and table references from CockroachDBTool description
   - Added schema discovery instructions directly in the tool description
   - Made agent backstories focus on exploration rather than specific tables

3. **Information Schema Queries**:
   - Standard SQL queries to discover database structure:
   ```sql
   -- List all schemas (databases)
   SELECT schema_name 
   FROM information_schema.schemata 
   WHERE schema_name NOT IN ('pg_catalog', 'information_schema', 'crdb_internal', 'pg_extension')

   -- List all tables in schema 
   SELECT table_name
   FROM information_schema.tables
   WHERE table_schema = 'public' AND table_type = 'BASE TABLE'

   -- Get column details
   SELECT column_name, data_type, is_nullable
   FROM information_schema.columns
   WHERE table_schema = 'public' AND table_name = 'table_name'
   ORDER BY ordinal_position
   ```

4. **Knowledge Base Updates**:
   - New schema information is added to the "Database Schema" section
   - Structured in hierarchical format for better chunking
   - Includes relationship mapping between tables
   - Preserves existing schema documentation while adding new entries

### Specific Changes Made

1. **CockroachDBTool Description**:
   - Removed hardcoded table and database listings
   - Added schema discovery query examples
   - Made the database parameter description more generic
   - Added instructions to document any discoveries

2. **Data Analyst Agent Backstory**:
   - Added explicit schema discovery responsibility
   - Made database references generic
   - Emphasized the dual responsibility of schema discovery and business analysis
   - Instructed to always begin with schema discovery
   - **Given exclusive responsibility for updating the knowledge base with schema information**

3. **Analysis Task Description**:
   - Made schema discovery the explicit first step
   - Added detailed instructions for documenting schema
   - Structured expected output to include schema documentation
   - Made business analysis follow schema discovery

4. **Visualization Specialist**:
   - Updated to focus on adapting to discovered schemas
   - Added schema-specific visualization strategies
   - Included guidance on selecting visualization types based on data structure
   - Emphasized knowledge integration with new schema discoveries
   - **Instructed only to read from knowledge base, not update schema information**
   - **Role limited to visualization creation based on Data Analyst's discoveries**

### Benefits

1. **Self-Updating Documentation**:
   - System stays current with database schema changes
   - No need to manually update schema documentation
   - Ensures visualizations can adapt to new data structures

2. **Improved Adaptability**:
   - Works with any new tables added to the cluster
   - Handles structural changes to existing tables
   - Can identify and visualize data from new sources

3. **Consistent Methodology**:
   - Standardized approach for schema discovery and documentation
   - Clear documentation format ensures consistent knowledge structure
   - Visualization follows consistent patterns for new data types
   - Only the Data Analyst agent updates the knowledge base with schema information

### Usage

To run the system with schema discovery capabilities, simply use:

```bash
python Core_Scripts/plazza_analytics.py
```

No special parameters are needed - the system is now designed to always begin with schema discovery as its first step, followed by business analysis based on the discovered schema.

You can also enhance the schema discovery focus with a specific prompt:

```bash
python Core_Scripts/plazza_analytics.py "Focus on discovering any new tables or databases that have been added to the cluster recently. Document all schema elements thoroughly before proceeding with business analysis."
```

This schema discovery methodology ensures the system remains adaptable to database changes without requiring code modifications, following the principle of using prompts rather than code changes to guide agent behavior.

## Visualization System

### Architecture Evolution

The project now supports multiple visualization approaches:

1. **Single-Agent with VisualizationTool**:
   - Uses `crewai_visualization.py` as a tool within data analyst agent
   - Integrated in `sales_ai.py`
   - Simpler architecture but limited specialization

2. **Multi-Agent Architecture**:
   - Implemented in `sales_ai_visualization.py`
   - Dedicated agents for analysis and visualization
   - Enhanced visualizations with specialized focus
   - Uses Process.sequential to ensure proper task ordering
   - Shared knowledge base between agents

3. **Standalone Visualization Demo**:
   - `visualization_agent_demo.py` for focused testing
   - Can generate visualizations from existing analysis results
   - Useful for testing/debugging visualization capabilities

### Visualization Capabilities

The visualization system includes:

1. **Chart Types**:
   - Product sales bar charts showing top products by quantity
   - Customer retention pie charts with repeat vs. one-time percentages
   - Interactive business metrics dashboard with combined KPIs
   - All visualizations saved to the "visuals" directory

2. **Implementation Components**:
   - `CrewAIVisualization` class for chart generation
   - `parse_markdown_content()` function to extract structured data
   - Product name resolution via database lookups
   - Interactive Plotly-based dashboards
   - Static image generation for embedding

3. **Integration Methods**:
   - Agent-triggered: Agent can call `VisualizationTool` as part of analysis
   - Auto-generated: Script generates visualizations automatically after analysis
   - Embedded: Visualizations linked directly in enhanced markdown output

### Dashboard Enhancement Implementation

The dashboards have been enhanced with Plazza styling:

1. **Plazza Brand Colors Implementation**:
   - Primary: #FF0084 (bright pink) - Used for headings, KPI values, and chart elements
   - Background: #fafafa (light gray) - Applied to page backgrounds
   - Card background: white - Used for visualization containers
   - Card shadow: rgba(0,0,0,0.1) - Applied as subtle shadow for depth

2. **UI Components Implementation**:
   - Card-based layout with rounded corners (12px radius)
   - Grid system for flexible layouts using CSS Grid
   - KPI boxes with large value display in Plazza pink
   - Insight cards with highlighted titles and summary text

3. **Chart Styling Implementation**:
   - Created custom color palette based on Plazza primary color
   - Enhanced tooltips with formatted data and clear labels
   - Added hover effects to all interactive elements
   - Improved spacing and margins for better readability
   - Implemented gradient effects for bar charts based on Plazza pink

4. **Visualization Code Updates**:
   - Modified `crewai_visualization.py` with Plazza styling constants
   - Updated all chart generation functions with brand-compliant styling
   - Replaced Matplotlib charts with Plotly for better interactivity
   - Added custom HTML templates with Plazza CSS
   - Implemented responsive layout with flexbox and grid

5. **Technical Implementation Details**:
   - Defined Plazza color constants in visualization module
   - Created gradient generator based on Plazza primary color
   - Enhanced chart generation with consistent styling
   - Redesigned HTML output with embedded CSS
   - Added insight cards to dashboard layout
   - Updated visualization agent task description with brand guidelines

### Recent Bugfixes

1. **CrewOutput Object Handling**:
   - Fixed error: `'CrewOutput' object has no attribute 'startswith'`
   - Added content type checking with `isinstance(content, str)` before using string methods
   - Added extraction of raw content from CrewOutput objects using `content.raw`
   - Used explicit string conversion with `str(content)` when writing to files

2. **Agent Initialization**:
   - Fixed Pydantic validation error: `Input should be a valid dictionary or instance of Knowledge`
   - Changed from providing a list `[sales_knowledge]` to providing the single object `sales_knowledge`
   - This aligns with CrewAI's expected parameter format for Agents

3. **Visualization Dependencies**:
   - Added kaleido package for Plotly image export
   - Fixed path handling for visualization outputs
   - Improved error handling in visualization generation

### Recent Enhancements (March 21)

1. **Enhanced Content Processing**:
   - Implemented multiple regex patterns for more robust data extraction
   - Added support for extracting structured data from markdown tables
   - Improved time series and geographical data detection
   - Enhanced error handling with graceful fallbacks

2. **RAG Knowledge Optimization**:
   - Added rich metadata with domain-specific attributes
   - Enhanced document structure for better semantic chunking
   - Improved history preservation logic
   - Added robust error handling with fallback mechanisms
   - Implemented structured content formatting with explicit section markers

3. **Extended Visualization Capabilities**:
   - Added time-series chart for trend analysis showing period-to-period changes
   - Added geographic distribution visualization for regional analysis
   - Implemented period-over-period comparative visualization
   - Enhanced markdown embedding with better organization and layout
   - Added automatic insight summaries for visualizations

## Advanced Features

### Visualization Capabilities

The system now includes comprehensive visualization capabilities that transform data analysis into visual insights:

1. **Visualization Module**: Added `crewai_visualization.py` with the following components:
   - `CrewAIVisualization` class for generating multiple chart types
   - Automatic extraction of data points from analysis text
   - Integration with CrewAI workflow through `VisualizationTool`
   - Support for bar charts, pie charts, and interactive dashboards

2. **Chart Types**:
   - Product sales bar charts showing top products by quantity
   - Customer retention pie charts with repeat vs. one-time percentages
   - Interactive business metrics dashboard with combined KPIs
   - All visualizations saved to the "visuals" directory

3. **Multi-Agent Architecture**:
   - Data Analyst agent (specializes in SQL and data analysis) 
   - Visualization Specialist agent (specializes in creating dashboards)
   - Communication via shared knowledge and sequential task execution
   - Specialized LLM configuration with tailored temperature settings:
     - Data Analyst: temperature=0.2 for precise analysis
     - Visualization Specialist: temperature=0.3 for creative designs

### Product Name Enhancement

Product references now include both names and IDs for better readability:
   - Query enhancement in `CockroachDBTool` to include product names
   - Results formatted as "Product: NAME (ID)" for clear identification
   - Improved JOIN logic to retrieve product names from appropriate tables

### Test Data Filtering

Comprehensive test data filtering implemented at multiple levels:
   - SQL query filtering with expanded test patterns
   - Display-level filtering for any test data that bypasses query filters
   - Enhanced `RetentionAnalysisTool` with aggressive test data exclusion
   - Filtering patterns for:
     - Products with IDs containing 'TEST', 'test', 'p'
     - Specific test IDs like 'MED001', 'TEST-MED-001'
     - Orders with test identifiers
     - Transactions below $10 (likely test data)

## Database Connection Information

### CockroachDB Connection Variables
- **DATABASE_URL**: Connects to the defaultdb database (core product catalog)
- **DATABASE_URL_USER_TRANSACTIONS**: Connects to the user_transactions database (customer orders)
- **DATABASE_URL_ERP**: Connects to the plazza_erp database (business operations)
- **DATABASE_URL_USER**: Connects to the user_events database (activity tracking)

### Connection Format
```
postgresql://username:password@hostname:port/database?sslmode=verify-full
```

### Connection Parameters
- **Hostname:** plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud
- **Port:** 26257
- **SSL Mode:** verify-full

## Database Schema

### 1. user_transactions Database (Customer and Order Management)
- **contacts**: Customer information (id, first_name, last_name, email, etc.)
- **contact_addresses**: Customer addresses (address_id, house_number, locality, state, pincode)
- **contact_phones**: Customer phone numbers (phone_number, is_primary)
- **orders**: Order information (order_id, contact_id, status, bill_total_amount, created_at)
- **order_items**: Individual items in orders (product_id, medicine_name, quantity, mrp, selling_price)
- **payments**: Payment details with enhanced QR code support (payment_id, customer_id, order_amount, payment_status, payment_method)
- **products**: Product catalog (product_id, medicine_name, medicine_type, mrp, quantity_available)
- **stores**: Store information (name, address, city, state, pincode, gst_number)
- **tookan_jobs**: Delivery tracking (job_id, agent_id, job_status, tracking_url)
- **whatsapp_messages**: Message history (message_id, order_id, status)
- **whatsapp_notifications**: Notification tracking (message_id, order_id, phone_number, status)
- **zoho_config**: Zoho integration settings (organization_id, tax_settings)
- **zoho_tokens**: Authentication tokens for Zoho API

### 2. defaultdb Database (Core Product Catalog)
- **all_products**: Complete product catalog (product_id, name, manufacturers, salt_composition, medicine_type)
- **inventory_products**: Inventory tracking (product_id, vendor_id, batch_number, expiry_date, stock_qty)
- **plazza_price_table**: Pricing information (product_id, mrp, selling_price, discount_percentage)
- **validated_matches**: Validated product matches between systems (product_id, vendor_product_id, confidence)
- **matching_logs**: Product matching tracking (match_id, product_id, confidence_score, matching_method)

### 3. plazza_erp Database (ERP system for business operations)
- **inventory_transactions**: Inventory movement (transaction_id, product_id, quantity, transaction_type)
- **promotional_coupons**: Promo codes (coupon_code, discount_type, discount_value, valid_from, valid_to)
- **one_time_coupons**: Single-use codes (coupon_code, used, used_by, used_at)
- **conversations**: Customer chat history (conversation_id, customer_id, conversation_text)

### 4. user_events Database (User activity tracking)
- **session_events**: User session data (session_id, user_id, event_type, timestamp)
- **user_searches**: Search history (search_id, user_id, search_term, results_count)
- **page_views**: Page view tracking (page_id, user_id, page_name, time_spent)
- **conversion_events**: Purchase funnel events (event_id, user_id, event_type, product_id)

## CrewAI Implementation

### Custom Tools
- **CockroachDBTool**: Executes SQL queries against CockroachDB databases
  - Takes a query parameter and database parameter
  - Returns formatted query results
  - Handles connection management and error reporting
- **RetentionAnalysisTool**: Specialized tool for customer retention metrics
  - Performs multi-query analysis with aggressive test data filtering
  - Calculates repeat vs. one-time percentages, time between purchases, and more
- **PreviousAnalysisTool**: Retrieves historical analysis results
  - Complements RAG integration with direct file access
  - Formats results for better readability
- **VisualizationTool**: Creates visualizations from analysis results
  - Integrated with CrewAIVisualization class
  - Generates charts, dashboards, and enhanced markdown

### Agents
1. **Enterprise Data Analyst**:
   - Specializes in SQL generation and multi-database analysis
   - Uses CockroachDBTool to execute queries
   - Configured with GPT-4o (temperature=0.2, max_tokens=4000)
   - Focuses on extracting business insights from raw data

2. **Data Visualization Specialist**:
   - Specializes in creating visual representations of data
   - Uses VisualizationTool to generate charts and dashboards
   - Configured with GPT-4o (temperature=0.3, max_tokens=4000)
   - Focuses on creating compelling, interactive visualizations
   - Formats and enhances raw analysis with visual elements

### Task Examples
- Inventory-Sales Gap Analysis: Identify products with high inventory but low sales
- Data Consistency Analysis: Find products in inventory but missing from catalog
- Cross-database Analysis: Correlate data across multiple Plazza databases
- Customer Retention Analysis: Calculate repeat purchase metrics and cohort analysis
- Dashboard Creation: Transform analysis into interactive visualizations

## Scripts and Utilities

### Core System

#### Business Analysis
- `sales_ai.py`: Main CrewAI implementation for database analysis (single agent)
- `sales_ai_visualization.py`: Multi-agent implementation with visualization specialist

#### Visualization System
- `crewai_visualization.py`: Core visualization module with chart generation

#### Website Scraping
- `website_scraper.py`: Uses Firecrawl API to generate API documentation from websites

### Support Scripts

#### Database Schema Documentation
- `explore_db_schema.py`: Documents schemas for all databases
- `explore_db_schema_focused.py`: Documents schema for a specific database

#### Debugging and Testing
- `sales_ai_debug.py`: Debug version with timeout handling and simplified tasks
- `visualization_agent_demo.py`: Simple demo of visualization capabilities
- `fix_rag_integration.py`: Script to fix RAG integration issues

### Experimental Features

#### Metabase Integration (Alternative Visualization in Claude_Scripts)
- `metabase_tool.py`: Alternative visualization tool using Metabase API
- `test_metabase_tool.py`: Test suite for Metabase integration
- `direct_metabase_test.py`: Direct API testing without CrewAI
- `sales_ai_metabase.py`: CrewAI with Metabase visualization integration
- `sales_ai_metabase_sample.py`: Sample implementation without database dependencies
- `dashboard.html`: Custom dashboard prototype with Plazza styling
- `METABASE_INTEGRATION.md`: Comprehensive documentation of Metabase integration
- `METABASE_SUMMARY.md`: Executive summary of Metabase implementation

## API Documentation
- Generated markdown files in the API_documents directory
- Database schemas in JSON format
- Connection code examples for Python

## Useful Commands

### Running Schema Documentation
```bash
python explore_db_schema.py  # Document all databases
python explore_db_schema_focused.py  # Focus on user_transactions database
```

### Running AI Analysis
```bash
python sales_ai.py  # Full business analysis with single agent
python sales_ai_debug.py  # Debugging version with timeouts
python sales_ai_visualization.py  # Multi-agent version with visualization specialist
```

### Visualization Demo
```bash
python visualization_agent_demo.py  # Run standalone visualization demo
```

### Website Scraping
```bash
python website_scraper.py  # Scrape API documentation websites
```

### Required Environment Variables
- OPENAI_API_KEY: For CrewAI agent (GPT-4o)
- DATABASE_URL: CockroachDB connection string for defaultdb
- DATABASE_URL_USER_TRANSACTIONS: Connection string for user_transactions
- DATABASE_URL_ERP: Connection string for plazza_erp database
- DATABASE_URL_USER: Connection string for user_events database
- FC_API_KEY: Firecrawl API key for website scraping

## Next Steps

1. **Enhanced Dashboard Styling ✅**:
   - ✅ Implemented Plazza brand color scheme (#FF0084) across visualizations
   - ✅ Created consistent card-based UI with rounded corners (12px)
   - ✅ Improved layout with proper grid system and flexible containers
   - ✅ Added interactive elements, tooltips, and hover effects

2. **Enhanced Content Processing ✅**:
   - ✅ Improved section extraction with multiple pattern matching
   - ✅ Implemented robust metadata for better retrieval
   - ✅ Added structured data extraction from tables
   - ✅ Enhanced error handling with fallback mechanisms

3. **Optimized RAG Parameters ✅**:
   - ✅ Maintained optimal chunk size (800) and overlap (200)
   - ✅ Enhanced metadata with domain-specific attributes
   - ✅ Improved content structuring for better semantic chunking
   - ✅ Added robust error handling and fallbacks

4. **Extended Visualization Capabilities ✅**:
   - ✅ Added time-series visualizations for trend analysis
   - ✅ Added geographic visualizations for regional analysis
   - ✅ Implemented comparative visualizations for period-over-period metrics
   - ✅ Enhanced chart embedding in markdown with better organization

5. **Database Schema Discovery ✅**:
   - ✅ Implemented schema discovery through agent prompting
   - ✅ Added information_schema query patterns to agent guidance
   - ✅ Enabled self-updating knowledge base for schema changes
   - ✅ Created methodology for maintaining schema documentation

6. **Add Multiple Knowledge Sources**:
   - Explore adding domain-specific knowledge sources
   - Integrate external documentation

7. **Implement Metrics and Evaluation**:
   - Track how often RAG knowledge is used
   - Evaluate retrieval quality
   - Measure impact on analysis quality

8. **Future Visualization Enhancement**:
   - Create downloadable PDF reports with embedded visualizations
   - Add interactive dashboard filters
   - Implement user preferences for visualization styles

## Multi-Agent System Enhancement Plan

The multi-agent system for automated dashboard generation has been streamlined to rely solely on the Plotly-based visualization system. This enhancement plan addresses current issues and sets a path for more robust visualization capabilities.

### Current Issues

1. **Data Extraction Limitations**:
   - The `parse_markdown_content()` function in `crewai_visualization.py` struggles to reliably extract structured data from markdown analysis
   - Regex patterns need improvement to handle diverse data formats
   - Table extraction from markdown is inconsistent

2. **Database Connectivity**:
   - Intermittent failures in database connections affect data retrieval
   - The visualization module fails gracefully but produces empty dashboards
   - Error handling needs enhancement to provide better feedback

3. **Visualization Dependencies**:
   - The `kaleido` package is required for Plotly image export but may not be installed
   - PNG generation for dashboard embedding fails without proper dependencies
   - Environment setup needs to be more robust

### Implementation Plan

1. **Enhanced Data Extraction**:
   - Improve regex patterns for more robust extraction from different markdown formats
   - Add additional extraction methods beyond regex (e.g., markdown parsers)
   - Implement fallback mechanisms when extraction fails
   - Add better error reporting for data extraction issues

2. **Robust Database Connectivity**:
   - Implement connection pooling to improve reliability
   - Add comprehensive error handling with meaningful error messages
   - Create mock data generation for testing without database access
   - Implement timeout and retry logic for database operations

3. **Dependency Management**:
   - Add explicit dependency checking at runtime
   - Implement automatic installation of missing packages via pip
   - Create a complete requirements.txt file for visualization dependencies
   - Add clear documentation about required packages

4. **Enhanced Visualization Types**:
   - Implement time-series charts showing trends over time
   - Add geographic visualizations for regional analysis
   - Create comparative visualizations for period-over-period metrics
   - Design specialized visualizations for pharmaceutical industry metrics

### Technical Implementation Details

1. **Data Extraction Enhancements**:
   - Replace simple regex with a combined approach using Python-Markdown parser
   - Create specialized extractors for different data types (tables, lists, KPIs)
   - Implement a structured data validation system to ensure completeness
   - Add logging for extraction process to aid debugging

2. **Visualization Module Improvements**:
   - Enhance the `CrewAIVisualization` class with more robust error handling
   - Create dedicated chart type classes for better organization
   - Implement a template system for consistent dashboard layouts
   - Add customization options for Plazza styling

3. **Multi-Agent Framework Optimization**:
   - Refine the communication between Data Analyst and Visualization Specialist
   - Improve knowledge sharing with more structured data formats
   - Add explicit validation steps before visualization generation
   - Create a feedback loop for visualization quality assessment

### Integration Testing Framework

1. **Test Cases**:
   - Empty database scenario
   - Partial data availability
   - Malformed analysis text
   - Missing visualization dependencies
   - Various data formats and structures

2. **Mock Data Generator**:
   - Create synthetic pharmaceutical sales data
   - Generate mock customer retention metrics
   - Produce artificial time-series data
   - Develop regional distribution test data

3. **Validation Metrics**:
   - Dashboard completeness score
   - Data extraction accuracy
   - Visual quality assessment
   - Performance benchmarks for generation time

## User-Driven Architecture Update (March 2025)

The system has been redesigned to be fully user-driven rather than automatically running analysis on startup:

### Key Architectural Changes

1. **Removed Static Task Execution**:
   - Eliminated hardcoded tasks that ran automatically on import
   - Removed automatic `crew.kickoff()` execution
   - Converted to a reactive system that only analyzes when requested

2. **Dynamic Task Creation**:
   - Added `create_analysis_task()` and `create_visualization_task()` functions
   - Tasks are now created on-demand based on user input
   - All processing happens only in response to user queries

3. **Improved Path Handling for Knowledge**:
   - Fixed CrewAI knowledge system path expectations
   - Added robust handling of knowledge file locations
   - Implemented automatic knowledge file creation when missing
   - Used Path objects to avoid CrewAI's internal path manipulation

4. **Enhanced Chat Interface**:
   - Updated to use the new dynamic task creation
   - Improved visualization handling with VisualizationTool integration
   - Added better error handling and fallbacks
   - Enhanced user experience with more descriptive feedback

5. **Command-Line Improvements**:
   - Added better command-line interface with progress information
   - Improved feedback during analysis execution
   - Enhanced error handling to provide useful error messages
   - Added guidance for next steps after analysis

### Usage Models

The system now offers two distinct usage models:

1. **Interactive Chat Interface** (`plazza_chat.py`):
   - Ask questions about your business data in two different modes:
     - **Chat Mode**: For quick, specific questions (default)
     - **Analysis Mode**: For comprehensive database discovery and analysis
   - Trigger full analysis by including keywords like "analyze" or "full analysis"
   - Request visualizations with natural language
   - Generate visualizations explicitly with the "viz" command
   - Fully reactive - only processes when explicitly requested

2. **Command-Line Analysis** (`plazza_analytics.py`):
   - Run targeted analysis with `python Core_Scripts/plazza_analytics.py "your query"`
   - Execute full analysis without arguments for comprehensive results
   - Output saved to knowledge base for future reference
   - Visualizations generated automatically as part of analysis

### Implementation Details

1. **Knowledge System Improvements**:
   - Uses CrewAI's `KNOWLEDGE_DIRECTORY` constant for proper path handling
   - Checks multiple possible source locations for knowledge files
   - Creates starter file when no knowledge exists
   - Uses Path objects to avoid CrewAI's path manipulation with strings
   - Implements fallback to empty knowledge object for robustness

2. **Visualization Integration**:
   - Chat interface now uses VisualizationTool directly
   - Implements fallback visualization methods
   - Supports multiple visualization types
   - Better error handling for visualization generation

3. **More Robust Error Handling**:
   - Graceful handling of missing files and directories
   - Better feedback during execution
   - Enhanced fallback mechanisms for resilience
   - Clear error messages for troubleshooting

## Methodology Transparency Enhancement (March 23, 2025)

### Problem Addressed

1. **Inconsistent Query Results**:
   - Users reported inconsistent answers from the Data Q&A agent
   - The agent wasn't documenting the SQL queries used to derive answers
   - Multi-source queries (e.g., checking Airtable + regular orders) were inconsistent
   - NULL or empty results weren't handled correctly in summaries

2. **Lack of Methodology Transparency**:
   - Users couldn't verify how answers were derived
   - No insight into which databases or tables were checked
   - No explanation when certain data sources had no data
   - No documentation of query failure or empty result sets

3. **Inconsistent SQL Approach**:
   - Sometimes used UNION to combine data from different tables
   - Other times executed separate queries but didn't document them
   - No consistent pattern for multi-source aggregate queries

### Solution Implemented

1. **New MethodologyTool**:
   - Created specialized tool for executing and documenting SQL queries
   - Automatically formats queries, results, and summaries in markdown
   - Handles NULL/None results explicitly
   - Groups aggregate results into a clear summary
   - Documents when tables return no results

2. **Enhanced Data Q&A Agent**:
   - Updated agent backstory to emphasize methodology transparency
   - Required the agent to document all queries and results
   - Added specific instructions for handling multi-source queries
   - Provided example query structure for common scenarios
   - Required the agent to use the MethodologyTool for all SQL execution

3. **Structured Response Format**:
   - Implemented a standard response format:
     * Direct answer to user's question
     * Methodology section showing queries and results
     * Summary of findings explaining the data
   - Clear separation between raw query results and interpretation
   - Better error handling and NULL result reporting

### Benefits

1. **Methodology Transparency**:
   - Users can now see exactly how answers were derived
   - All SQL queries are documented with their results
   - Clear indication when tables have no data
   - Better education on database structure through query visibility

2. **Consistent Multi-Source Queries**:
   - Separate queries for different data sources
   - Better handling of NULL/None results
   - Clear aggregation in the summary section
   - Explicit documentation of which tables were checked

3. **Better Troubleshooting**:
   - Easier to identify query problems
   - Clear visibility into data structure
   - Transparent reporting of empty result sets
   - Consistent error handling and reporting

### Implementation Details

1. **MethodologyTool Class**:
   - Takes a list of query objects (query, database, description)
   - Executes each query independently
   - Formats results in a consistent markdown structure
   - Creates a summary section with aggregate results
   - Handles error cases and empty result sets

2. **Updated Agent Task Prompting**:
   - Added detailed instructions for methodology documentation
   - Provided example query structure for common scenarios
   - Emphasized separate queries for different data sources
   - Required use of the MethodologyTool for all SQL execution

3. **Agent Backstory Enhancement**:
   - Emphasized transparency and methodology documentation
   - Required clear documentation of all data sources checked
   - Specified consistent response format
   
4. **Agent Verbosity Control**:
   - Disabled verbose mode (verbose=False) in all agents
   - Prevents thought/action/observation logs from appearing in output
   - Shows only the final answer to the user
   - Creates cleaner, more professional responses while maintaining methodology transparency

### Usage Example

When a user asks a question like "What is the total sales across Airtable and non-Airtable data in March?", the system will now:

1. First provide a direct answer:
   ```
   The total sales across all data sources in March 2025 is Rs. 3,089.34.
   ```

2. Then include a detailed methodology section:
   ```
   ## Methodology

   I executed the following queries to answer your question:

   ### 1. Calculate March 2025 sales from regular orders

   **Database:** `user_transactions`
   **SQL Query:**
   ```sql
   SELECT SUM(bill_total_amount) AS total_sales 
   FROM orders 
   WHERE created_at >= '2025-03-01' AND created_at < '2025-04-01' AND status = 'paid';
   ```

   **Results:**
   ```
   total_sales: 3089.34
   ```

   ### 2. Calculate March 2025 sales from Airtable orders

   **Database:** `user_transactions`
   **SQL Query:**
   ```sql
   SELECT SUM(bill_total_amount) AS total_sales 
   FROM airtable_orders 
   WHERE created_at >= '2025-03-01' AND created_at < '2025-04-01' AND status = 'paid';
   ```

   **Results:**
   ℹ️ This query returned no results (NULL or empty set)

   ## Summary of Findings

   Based on the queries executed:
   - Calculate March 2025 sales from regular orders (total_sales): 3089.34
   - Calculate March 2025 sales from Airtable orders (total_sales): No data
   ```

3. The output is clean, professional, and structured without showing any internal thought process, just the final answer and methodology.

### Technical Implementation

The MethodologyTool works by:

1. Accepting a list of query objects with:
   - `query`: The SQL to execute
   - `database`: The database to query 
   - `description`: What the query is checking

2. Executing each query independently and in parallel when possible

3. Handling results processing:
   - Detecting aggregate queries (containing SUM, COUNT, etc.)
   - Processing tabular results with proper formatting
   - Explicitly marking NULL or empty result sets
   - Generating a comprehensive summary of all results

4. Creating a structured markdown output with:
   - Each query clearly documented with its SQL
   - Results properly formatted based on query type
   - A summary section that combines all findings

By using this approach, we ensure consistency, transparency, and clean output all at once, providing both the technical detail users need for verification while maintaining a professional presentation.

### Agent Architecture Refactor (March 25)

1. **AgentRole Consolidation and Knowledge-First Strategy**:
   - Deprecated the standalone Retention Analyst agent
   - Integrated retention analysis capabilities into the Data Q&A Expert agent
   - Implemented clearer responsibility boundaries between agents
   - Enhanced all agents with explicit Knowledge-First strategy

2. **System Prompt Refactoring**:
   - Refactored Chat Orchestrator (PlazzaChat) with KB-First routing logic
   - Updated Enterprise Data Analyst to focus on deep analysis and KB maintenance
   - Enhanced Data Q&A Expert with RetentionAnalysisTool capabilities
   - Refactored Visualization Specialist to work exclusively with KB data

3. **Data Q&A Expert Enhancement**:
   ```python
   self.chat_data_analyst = Agent(
       role="Data Q&A Expert",
       goal="Quickly answer user questions about sales, orders, products, and customers using business data",
       backstory="""You are the primary question-answering agent for all business intelligence tasks across the Plazza ecosystem. You operate in interactive chat mode.

   # OBJECTIVE
   Answer all user queries using the existing structured knowledge base if available. You only query the live CockroachDB system when required — either when the KB is empty or when explicitly instructed to refresh data.

   # RETENTION ANALYSIS
   You are now responsible for **customer retention studies**.
   - The `Retention Analyst` agent is deprecated.
   - Its logic and capabilities are now available to you via the `RetentionAnalysisTool`.
   
   # DEFAULT FLOW
   1. Check if the knowledge base (KB) has relevant results for the user query
      - If yes → Use it directly
      - If no → Call the `Enterprise Data Analyst` to regenerate a full analysis and refresh the KB
   """
   )
   ```

4. **Enterprise Data Analyst Refactor**:
   ```python
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
       """
   )
   ```

5. **Visualization Specialist Refactor**:
   ```python
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
       """
   )
   ```

6. **Chat Orchestrator Refactor**:
   - Enhanced query routing with specific retention keyword detection
   - Updated route_task() method to implement Knowledge-First strategy
   - Added clear console feedback with agent-specific action explanations
   - Updated welcome message to explain the Knowledge-First approach

7. **Benefits**:
   - Clearer agent responsibilities with less duplication
   - More focused agents with specialized expertise
   - Reduced complexity in the agent architecture
   - Improved error handling and user feedback
   - Better separation between chat Q&A and deep analysis
   - Explicit retention analysis integration in the Data Q&A Expert
   - Clear Knowledge-First strategy across all agents

8. **Files Modified**:
   - `/Core_Scripts/plazza_chat.py`: Updated Chat Orchestrator and Data Q&A Expert
   - `/Core_Scripts/plazza_analytics.py`: Updated Enterprise Data Analyst and Visualization Specialist
   - `/CLAUDE.md`: Added documentation about the refactoring

## System Integration Guide

### Using the Agent Registry

To access predefined agents in your scripts:

```python
from Core_Scripts.agent_registry import get_data_analyst, get_chat_data_analyst, get_visualization_specialist

# Get a configured agent with all tools and knowledge
analyst = get_data_analyst()

# Create a task for the agent
task = Task(
    description="Analyze March 2025 sales data",
    expected_output="Comprehensive sales analysis with trends",
    agent=analyst
)

# Execute the task
result = analyst.execute_task(task)
```

### Using Specialized Strategy Module

For business strategy recommendations:

```python
from Core_Scripts.plazza_strategy import create_strategy_task, business_strategy_advisor

# Create a strategy task with user query
strategy_task = create_strategy_task(
    user_query="What pricing strategy should we adopt for our top products?",
    analysis_content=analysis_results
)

# Execute the strategy task
strategy_result = business_strategy_advisor.execute_task(strategy_task)
```

### Using Enhanced Visualization Tools

Multiple options for visualization:

```python
# Option 1: Direct function call with content
from crewai_visualization import visualize_analysis_results

results = visualize_analysis_results(content=analysis_text)

# Option 2: Using the general-purpose visualization tool
from Core_Scripts.crewai_visualization import VisualizationTool

viz_tool = VisualizationTool()
viz_results = viz_tool._run(input_data=analysis_text)

# Option 3: Using specialized chart tools
from Core_Scripts.crewai_visualization import TopProductsChartTool, MetricsDashboardTool

product_chart = TopProductsChartTool()._run(input_data=analysis_text)
dashboard = MetricsDashboardTool()._run(input_data=analysis_text)
```

### Environment Configuration

Add to your .env file:

```
# Database connections
DATABASE_URL=postgresql://username:password@hostname:port/defaultdb?sslmode=verify-full
DATABASE_URL_USER_TRANSACTIONS=postgresql://username:password@hostname:port/user_transactions?sslmode=verify-full

# Visualization settings
VISUALIZATION_OUTPUT_DIR=/path/to/custom/visuals/directory

# OpenAI API Key
OPENAI_API_KEY=your-api-key
```

### Self-Evaluating Router Enhancement (March 30, 2025)

1. **Self-Evaluation Capability**:
   - Added response quality self-evaluation to the router agent
   - Implemented routing effectiveness assessment
   - Added quality metrics assessment (completeness, accuracy, follow-up needs)
   - Created hidden HTML comments for self-evaluation metadata
   - Enhanced logging to capture evaluation details separately from user response

2. **Agent Reflection System**:
   - Added quality criteria assessment for each delegation
   - Implemented agent selection reasoning documentation
   - Created feedback loop for potential re-routing
   - Added detailed analytics on routing decisions
   - Enhanced debugging capabilities with transparent decision documentation

3. **Enhanced Logging Functionality**:
   - Added structured self-evaluation section in log files
   - Created separate display for routing decisions vs. actual response
   - Implemented error handling with detailed diagnostic information
   - Added richer metadata for troubleshooting and improvement

4. **Implementation Details**:
   ```python
   # Enhanced task description with self-evaluation instructions
   router_task = Task(
       description=f"""
   # ...task instructions...
   
   5. Evaluate the response quality:
      - Does it directly answer the user's question?
      - Is the information complete and accurate?
      - Would the user need to ask follow-up questions?
      - If unsatisfactory, consider delegating to a different agent.
   
   Your final output should include:
   1. The result of the delegated task
   2. A brief hidden self-evaluation note in HTML comment format <!-- Self-evaluation: ... -->
      indicating which agent was selected, why, and your assessment of the quality.
   """,
   # ...other parameters...
   )
   
   # Extract self-evaluation while hiding it from the user
   eval_match = re.search(r'<!--\s*(Self-evaluation:.*?)-->', result, re.DOTALL)
   if eval_match:
       self_evaluation = eval_match.group(1).strip()
       # Remove the evaluation from user-facing response
       user_response = re.sub(r'<!--\s*Self-evaluation:.*?-->', '', result, flags=re.DOTALL).strip()
   ```

5. **Benefits**:
   - **Improved Routing Quality**: System can learn from its own assessments
   - **Better Debugging**: Clear documentation of why specific agents were selected
   - **Enhanced Analytics**: Valuable metadata for system improvement
   - **Response Validation**: Built-in quality check for every response
   - **Transparency**: Clear documentation of routing decisions without cluttering user responses
   - **Continuous Improvement**: Foundation for future self-improving capabilities

6. **Files Modified**:
   - Enhanced `/Core_Scripts/advanced_router.py` with self-evaluation capabilities
   - Updated `/CLAUDE.md` with implementation documentation

### Advanced Routing Implementation (March 29, 2025)

1. **Intelligent Query Routing System**:
   - Added `get_routing_agent()` to agent_registry.py as a centralized orchestrator
   - Created `advanced_router.py` with dynamic task delegation capabilities
   - Implemented intent-based classification of user queries
   - Added automatic routing to appropriate specialist agents
   - Created conversation logging with metadata tracking
   - Enhanced user experience with interactive CLI

2. **Advanced Routing Architecture**:
   - **Central Orchestrator**: AI Orchestrator agent with routing intelligence
   - **Dynamic Task Construction**: Creates specialized tasks based on query intent
   - **Delegation Framework**: Uses CrewAI's delegation system to pass tasks to specialists
   - **Specialist Agents**: Data Q&A Expert, Enterprise Data Analyst, Visualization Specialist, Strategy Advisor
   - **Transparent Output Handling**: Only returns the final specialist response without orchestration details
   - **Conversational Memory**: Implements agent memory for context retention

3. **Routing Capabilities**:
   - **Q&A Routing**: Directs quick database questions to the Data Q&A Expert
   - **Analysis Routing**: Sends deep analysis requests to the Enterprise Data Analyst
   - **Visualization Routing**: Directs chart and dashboard requests to the Visualization Specialist
   - **Strategy Routing**: Sends business strategy queries to the Strategy Advisor
   - **Hybrid Request Handling**: Intelligently decomposes complex multi-part requests

4. **Implementation Details**:
   ```python
   # Router agent definition in agent_registry.py
   def get_routing_agent():
       return Agent(
           role="AI Orchestrator",
           goal="Understand user intent and delegate it to the correct AI specialist.",
           backstory="""
   You are the central coordinator of the Plazza AI system. When a user submits a request, 
   you must analyze it, determine its type (Q&A, full analysis, visualization, strategy), 
   and assign it to the most appropriate specialist agent.
   
   You are capable of delegating tasks dynamically using CrewAI's delegation feature. 
   You understand the strengths and tools of each agent.
   
   Agents available:
   - Data Q&A Expert: for quick answers from the knowledge base or DB
   - Enterprise Data Analyst: for deep analysis
   - Visualization Specialist: for visual dashboards
   - Strategy Advisor: for business strategy based on insights
   
   Only return the final output from the delegated task.
   """,
           allow_delegation=True,
           verbose=True,
           memory=True
       )
   ```

5. **Enhanced Error Handling**:
   - Added robust exception handling for routing errors
   - Implemented clear error messaging for users
   - Created fallback mechanisms for failed delegations
   - Added complete conversation logging for debugging

6. **Usage**:
   ```bash
   # Run the advanced router interface
   python Core_Scripts/advanced_router.py
   
   # Example queries:
   # "What are the top-selling products this quarter?"
   # "Give me a dashboard showing repeat customers."
   # "What strategy should we use to reduce churn?"
   ```

7. **Files Modified**:
   - Added routing agent to `/Core_Scripts/agent_registry.py`
   - Created new `/Core_Scripts/advanced_router.py`
   - Added router logs directory `/Run_Results/router_logs/`
   - Updated `/CLAUDE.md` with documentation

8. **Benefits**:
   - **Improved User Experience**: Single entry point for all query types
   - **Reduced Cognitive Load**: Users don't need to know which agent to use
   - **More Accurate Agent Selection**: AI-powered routing based on intent
   - **Better Debugging**: Complete conversation logging for troubleshooting
   - **Extensible Architecture**: Easy to add new specialist agents
   - **Enhanced Context Retention**: Memory implementation for conversation history

### System Enhancement Summary (March 28, 2025)

This section provides a comprehensive overview of all major enhancements implemented across the system in March 2025, with integration details and architectural patterns.

1. **Architecture Highlights**:
   - **Modular Design Pattern**: Complete separation of concerns with centralized agent registry
   - **Knowledge-First Approach**: RAG-powered knowledge retrieval prioritized over database queries
   - **Agent Delegation Framework**: Enhanced inter-agent communication with CrewAI's delegation system
   - **Tool Composition Pattern**: Specialized tools composed into cohesive workflows
   - **Factory Pattern Implementation**: Centralized agent and task creation through factory functions
   - **Event-Driven Callbacks**: Automatic post-processing through task callback functions
   - **Metadata-Rich Persistence**: All outputs saved with comprehensive metadata for traceability

2. **Integration Patterns**:
   - **Chat Orchestration**: Central orchestrator with intent-based routing to specialized agents
   - **Strategy Generation**: Automatic logging and delegation support for business recommendations
   - **Visualization System**: Flexible deployment options with direct content or file input
   - **Batch Analysis**: Knowledge freshness checking with override capability for scheduled execution
   - **Output Management**: Standardized directory structure with timestamped file naming
   - **Path Resolution**: Environment-variable driven path configuration with automatic directory creation
   - **Error Handling**: Consistent patterns for graceful failure and user-friendly messaging

3. **System-Wide Improvements**:
   - **Enhanced Documentation**: Comprehensive documentation with usage examples
   - **Standardized Directory Structure**: Clean separation between code and output directories
   - **Test Suite Implementation**: Unit tests for core components with mock systems
   - **Environment Variable Support**: Flexible configuration through environment variables
   - **Cross-Platform Compatibility**: Path handling with pathlib.Path for platform independence
   - **Consistent Error Handling**: User-friendly error messages with clear guidance
   - **Security Enhancements**: Improved handling of sensitive connection information

4. **Technical Debt Reduction**:
   - **Path Standardization**: Eliminated inconsistent path handling across codebase
   - **Code Duplication Elimination**: Centralized core functionality in shared modules
   - **Module Responsibility Boundaries**: Clear separation between module responsibilities
   - **Parameter Naming Consistency**: Standardized parameter names across functions
   - **Fallback Mechanisms**: Added graceful degradation for missing files or configuration
   - **Version Compatibility**: Enhanced compatibility with different CrewAI versions
   - **Performance Optimization**: Reduced unnecessary database queries through KB caching

### Streamlit Frontend Enhancement (April 1, 2025)

1. **Streamlined User Interface**:
   - Replaced tab-based layout with unified radio selector interface
   - Implemented form-based input with Enter key submission support
   - Added session state management for persistent results
   - Enhanced error handling with comprehensive feedback
   - Created consistent visual styling across all components
   - Improved router log display in collapsible sidebar sections

2. **Error Handling Improvements**:
   - Added comprehensive try-except blocks for all operations
   - Implemented detailed traceback display for debugging
   - Added specific error messages for import issues
   - Enhanced visualization error handling with graceful degradation
   - Improved file access error handling with helpful guidance
   - Added Python path debugging for troubleshooting

3. **Implementation Details**:
   ```python
   # Chat mode selection with radio buttons
   chat_mode = st.radio("Select Chat Mode:", ["🧠 AI Orchestrator", "⚡ Fast Chat (Standard)"])
   
   # Form-based input for Enter key submission
   with st.form("chat_form"):
       user_input = st.text_input("Ask a question:")
       submitted = st.form_submit_button("Submit")
   
   # Session state for persistent results
   if submitted and user_input:
       # Process the request...
       st.session_state["last_input"] = user_input
       st.session_state["last_result"] = result
   
   # Display result from session state
   if submitted and "last_result" in st.session_state:
       st.markdown("### 🧠 Chat Result")
       st.markdown(st.session_state["last_result"])
   ```

4. **Path Resolution and Module Imports**:
   - Added robust path resolution for Core_Scripts directory
   - Implemented module availability checking with helpful error messages
   - Added import error handling with guidance for troubleshooting
   - Enhanced visualization module import with fallback behavior
   - Created debug output for Python path configuration
   - Added flexible directory structure support

5. **Performance Optimizations**:
   - Lazy loading of modules only when needed
   - Improved file reading with proper error handling
   - Enhanced visualization rendering with better error recovery
   - Added caching of repeated operations to reduce load times
   - Implemented efficient log file processing with pagination

6. **Files Modified**:
   - `/Streamlit_Frontend/streamlit_app.py`: Complete UI redesign with better error handling
   - `/Streamlit_Frontend/dashboard.py`: Updated styling to match main interface
   - `/CLAUDE.md`: Updated documentation with UI enhancement details

### Streamlit Frontend Implementation (March 31, 2025)

1. **Web Interface for Plazza AI**:
   - Created dedicated Streamlit frontend in `/Streamlit_Frontend` directory
   - Implemented dual chat interface for both standard and advanced router
   - Added system status dashboard with knowledge base monitoring
   - Created visualization display for generated charts and dashboards
   - Implemented router logs and performance metrics tracking
   - Built comprehensive dashboard for system analytics

2. **Architecture Components**:
   - **streamlit_app.py**: Main application with tabs for different chat modes
   - **dashboard.py**: Advanced analytics dashboard with charts and metrics
   - **utils.py**: Shared utility functions for file handling and data extraction
   - **requirements.txt**: Dependency management for the frontend

3. **Integration with Core System**:
   - Direct integration with `plazza_chat.py` for standard chat interface
   - Integration with `advanced_router.py` for orchestrated routing
   - Access to knowledge base for freshness monitoring
   - Display of visualizations generated by the system
   - Analysis of router logs for performance metrics

4. **Dashboard Features**:
   - System overview cards with key metrics
   - Router performance statistics
   - Agent usage distribution chart
   - Time-based analysis of system usage
   - Query distribution by hour of day
   - System analytics with derived metrics

5. **Accessibility Improvements**:
   - Web-based UI for non-technical users
   - Clear visual indicators for system status
   - Interactive components for better user experience
   - Mobile-friendly responsive design
   - Tabbed interface for different functionality

6. **Implementation Details**:
   ```python
   # Streamlit app structure
   st.set_page_config(
       page_title="Plazza AI Chat",
       layout="wide",
       initial_sidebar_state="expanded"
   )

   st.title("💬 Plazza AI — Intelligent Chat & Analytics")

   # Tabs for different chat modes
   tab1, tab2 = st.tabs(["Standard Chat", "Advanced Router"])

   with tab1:
       # Standard chat interface implementation
       from Core_Scripts.plazza_chat import PlazzaChat
       
   with tab2:
       # Advanced router interface implementation
       from Core_Scripts.advanced_router import run_advanced_router
   ```

7. **Router Log Analysis**:
   ```python
   # Extract metadata from router logs
   def extract_metadata_from_log(log_path):
       content = log_path.read_text()
       
       # Extract self-evaluation using regex
       eval_match = re.search(r'## Router Self-Evaluation\n```\n(.*?)\n```', content, re.DOTALL)
       if eval_match:
           self_evaluation = eval_match.group(1).strip()
           
       # Extract other metadata...
       return metadata
   ```

8. **Benefits**:
   - **Enhanced Accessibility**: Web interface for non-technical users
   - **Centralized Access**: Single point of entry for all system features
   - **Visual Analytics**: Clear visualization of system performance
   - **Improved UX**: Intuitive interface for complex AI interactions
   - **Agent Transparency**: Visibility into AI routing decisions
   - **System Monitoring**: Real-time status of knowledge base and components

9. **Files Created**:
   - `/Streamlit_Frontend/streamlit_app.py`: Main Streamlit application
   - `/Streamlit_Frontend/dashboard.py`: System analytics dashboard
   - `/Streamlit_Frontend/utils.py`: Shared utility functions
   - `/Streamlit_Frontend/requirements.txt`: Python dependencies
   - `/Streamlit_Frontend/README.md`: Documentation for frontend

## Future Development Roadmap (Updated April 1, 2025)

1. **Q2 2025**:
   - ✅ Implement modular system architecture (Completed March 25)
   - ✅ Extract business strategy module (Completed March 25)
   - ✅ Enhance visualization module (Completed March 25)
   - ✅ Implement agent delegation framework (Completed March 24)
   - ✅ Add automatic logging for strategy outputs (Completed March 24)
   - ✅ Create comprehensive documentation (Completed March 28)
   - ✅ Implement Advanced Router with self-evaluation (Completed March 30)
   - ✅ Create Streamlit web interface (Completed March 31)
   - ✅ Enhance Streamlit UI with streamlined interface (Completed April 1)
   - ✅ Fix import and path issues in web interface (Completed April 1)
   - Develop multi-agent test harness (Week 4-6)
   - Add task dependency resolution for multi-stage analysis (Week 7-8)

2. **Q3 2025**:
   - Implement REST API for remote querying (Week 1-3)
   - Create scheduled batch job system for regular analyses (Week 4-5)
   - Develop cross-DB insights with federation logic (Week 6-8)
   - Add notification system for analysis completion (Week 9-10)

3. **Q4 2025**:
   - Build custom dashboard composer interface (Week 1-3)
   - Develop executive summaries with prioritized insights (Week 4-6)
   - Implement alert system for anomaly detection (Week 7-9)
   - Create collaborative annotation system for insights (Week 10-12)