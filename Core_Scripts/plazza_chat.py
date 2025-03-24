"""
Plazza Analytics Chat Interface

This script creates an interactive chat interface to interact with the Plazza Analytics
multi-agent system, allowing users to ask questions and get responses dynamically.

Usage:
    python plazza_chat.py

Commands:
    - Type any question about your business data
    - Type 'viz' to generate visualizations from the last response
    - Type 'exit' or 'quit' to end the session

Note: 
    This is the interactive chat interface. For batch analysis, use batch_analysis.py.
"""

import os
import sys
import re
import time
from typing import Dict, List, Any, Optional
from datetime import datetime

from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

# Import your existing tools and agent configurations
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Core_Scripts.plazza_analytics import (
    CockroachDBTool,
    RetentionAnalysisTool,
    MethodologyTool,
    VisualizationTool,
    create_knowledge_source,
    save_analysis_results,
    create_analysis_task,
    create_visualization_task,
    run_analysis
)
from Core_Scripts.plazza_strategy import create_strategy_task, business_strategy_advisor
from Core_Scripts.sales_ai import crew as sales_ai_crew

# Make sure the crewai_visualization module is imported
try:
    from crewai_visualization import CrewAIVisualization
except ImportError:
    # Try with the Core_Scripts prefix if direct import fails
    from Core_Scripts.crewai_visualization import CrewAIVisualization

# Load environment variables
load_dotenv()

class PlazzaChat:
    """
    Chat Orchestrator for Plazza Analytics.
    
    # ROLE
    Primary conversational interface for the user, responsible for understanding business questions,
    routing queries to the right agents, and maintaining natural dialog throughout.
    
    # PRIMARY FUNCTION
    Interprets the user's request and determines whether an answer can be served directly from 
    the Knowledge Base (KB), or whether deeper analysis is needed by a specialist.
    
    # KNOWLEDGE-FIRST STRATEGY
    1. Always checks Knowledge Base first
    2. Only triggers full analysis when KB lacks content
    3. Routes visualization requests to Visualization Specialist
    4. Handles retention requests with RetentionAnalysisTool directly
    """
    
    def __init__(self):
        """Initialize the chat interface with required agents and tools."""
        self.knowledge = create_knowledge_source()
        self.setup_agents_and_tools()
        self.history = []  # Store conversation history
        self.visualizer = CrewAIVisualization()  # Direct access to visualization functions
        self.requires_full_analysis = False  # Flag to determine if full analysis is needed
        self.analysis_focus = None  # Track focused analysis area when applicable
        
        # Ensure visuals directory exists
        os.makedirs("visuals", exist_ok=True)
        
    def setup_agents_and_tools(self):
        """Set up the agents and tools for analytics."""
        # Initialize tools
        self.db_tool = CockroachDBTool()
        self.retention_tool = RetentionAnalysisTool()
        self.methodology_tool = MethodologyTool()
        self.visualization_tool = VisualizationTool()
        
        # Check knowledge base freshness
        self.kb_last_updated = self.check_kb_freshness()
        
        # Set up Data Analyst Agent (for full analysis mode)
        self.data_analyst = Agent(
            role="Enterprise Data Analyst",
            goal="Analyze business data to extract valuable insights and trends",
            backstory="""You are an expert data analyst specializing in SQL and database analysis
            for pharmaceutical retail platforms. You excel at querying complex database schemas and
            extracting meaningful business insights. You can discover database structure and analyze
            data across multiple databases to provide comprehensive analysis. You respond to user
            questions with detailed analysis and include specific data points whenever possible.""",
            verbose=True,
            allow_delegation=False,
            tools=[self.db_tool, self.retention_tool],
            knowledge=self.knowledge
        )
        
        # Set up Data Q&A Agent (for chat mode)
        self.chat_data_analyst = Agent(
            role="Data Q&A Expert",
            goal="Quickly answer user questions about sales, orders, products, and customers using business data",
            backstory="""You are the primary question-answering agent for all business intelligence tasks across the Plazza ecosystem. You operate in interactive chat mode.

# OBJECTIVE
Answer all user queries using the existing structured knowledge base if available. You only query the live CockroachDB system when required — either when the KB is empty or when explicitly instructed to refresh data.

# INPUT TYPES
You handle:
- Natural language questions about business data (sales, customers, products, etc.)
- Commands like "analyze", "viz", "refresh data"
- Retention-specific queries like "retention for February", "compare new vs repeat buyers", etc.

# TOOLS
You are equipped with:
- CockroachDBTool: SQL access across the ecosystem (defaultdb, user_transactions, plazza_erp, user_events)
- RetentionAnalysisTool: specialized tool for cohort and repeat customer insights

# DEFAULT FLOW
1. Check if the knowledge base (KB) has relevant results for the user query
   - If yes → Use it directly
   - If no → Call the `Enterprise Data Analyst` to regenerate a full analysis and refresh the KB
2. You may use the RetentionAnalysisTool directly for retention-related queries
3. Never duplicate the full schema discovery logic handled by `Enterprise Data Analyst`

# KB INTEGRATION RULE
Always assume the KB exists and is current unless told otherwise. Look in the file: `/CrewAI/knowledge/sales_analysis_results.md`

If the KB is missing or outdated, escalate the task to:
> `Enterprise Data Analyst` agent
  - Task: Run full schema + business analysis
  - Output will overwrite the KB

# RETENTION ANALYSIS
You are now responsible for **customer retention studies**.

- The `Retention Analyst` agent is deprecated.
- Its logic and capabilities are now available to you via the `RetentionAnalysisTool`.

To run a retention analysis:
- You simply call:
```python
Action: RetentionAnalysisTool
Action Input: {}
```

- The result includes:
- Repeat vs one-time customer % (filtered for test data)
- Time between repeat purchases
- Cohort-wise retention rates
- Discounts vs loyalty analysis
- CLV estimates

Always save the output of a retention analysis to the knowledge base if it provides new cohort-level insight.

# OUTPUT FORMAT (Chat Mode)
Respond conversationally with clear markdown formatting:
- Use bullet points or tables when helpful
- Include totals, dates, and comparisons
- End with suggestions like: "Type 'viz' if you want a chart" or "Would you like me to run a retention study?"

# WHAT NOT TO DO
- Do not call schema discovery queries like SHOW DATABASES; unless delegated
- Do not generate new knowledge base documents unless explicitly told
- Do not repeat Enterprise Data Analyst responsibilities

# METHODOLOGY TRANSPARENCY
When using the MethodologyTool for database queries:
1. Use the MethodologyTool for structured query execution across databases
2. Ensure queries check ALL relevant databases (defaultdb, user_transactions, plazza_erp, user_events)
3. For multi-source data (like Airtable vs regular orders), use separate independent queries
4. Always handle NULL or empty results clearly and explicitly

# RESPONSE STYLE:
- Focus on precision, speed, and clarity — your job is to serve data, not write long reports
- Answer with a single, clear statement when possible (e.g., "March sales: ₹1.5M across all channels")
- Only show query details if the user explicitly asks with keywords like "how" or "methodology"
- Use numbers, percentages, and metrics rather than general descriptions
- For numerical answers, always include the units (₹, %, items, orders, etc.)

# KNOWLEDGE MANAGEMENT:
- When you discover new information, note it for KB addition with a timestamp
- If information seems outdated, note "This is from [date] in the KB, I can refresh if needed"
- When citing KB info, briefly mention the source: "According to the KB analysis from [date]..."

You are always fast, focused, and data-driven. Minimize fluff. Maximize insight.""",
            verbose=False,  # Disable verbose mode to hide thought process and just show final answer
            allow_delegation=False,
            tools=[self.db_tool, self.retention_tool, self.methodology_tool],
            knowledge=self.knowledge
        )
        
        # Set up Visualization Specialist Agent
        self.visualization_specialist = Agent(
            role="Data Visualization Expert",
            goal="Translate analytical results and business metrics into clear, impactful charts and visual reports.",
            backstory="""You are responsible for visualizing business insights from the Plazza ecosystem.
            Your **primary data source is the Knowledge Base** (`sales_analysis_results.md`) — which contains schema, sales summaries, customer behavior, and product analytics.

            ✅ You should always begin by reading from the Knowledge Base to find existing tables, figures, or insights to visualize.
            ❌ Never initiate new database queries yourself
            🚫 You are not responsible for business analysis or full-data exploration — you visualize what's already been computed

            🎯 Your visualizations must:
            - Be accurate to the existing KB context
            - Include relevant titles, axis labels, and legends
            - Be optimized for business storytelling (e.g. highlighting trends, deltas, top performers)

            🛠️ You may request additional metrics from the Data Q&A Expert, but only if the KB is missing specific values you need.

            📦 All output visualizations should be saved as files and registered in the `knowledge/visuals` folder for reuse in future interactions.""",
            verbose=False,  # Disable verbose mode to hide thought process and just show final answer
            allow_delegation=False,
            tools=[self.visualization_tool],
            knowledge=self.knowledge
        )
        
        # Set up Business Strategy Advisor Agent
        # Note: Using the shared instance from plazza_strategy.py
        self.business_strategy_advisor = business_strategy_advisor
    
    def route_task(self, user_input: str) -> Agent:
        """Route the user query to the appropriate agent based on the Knowledge-First Strategy.
        
        # DELEGATION RULES
        - Use the Enterprise Data Analyst agent for:
          - Schema Discovery
          - Business Sales Analysis
          - Deep order/product/customer queries when KB lacks data
        
        - Use the Visualization Specialist for:
          - Graphs, charts, dashboard components
        
        - Use the RetentionAnalysisTool (via Data Q&A Expert) for:
          - Repeat purchase behavior
          - Customer lifecycle
          - Cohort analysis
        
        Args:
            user_input: The query from the user
            
        Returns:
            The appropriate agent to handle the query
        """
        # Define keyword categories
        visualization_keywords = [
            "chart", "graph", "plot", "dashboard", "visualize", "visualization",
            "display", "show me", "picture", "diagram", "visual", "image", 
            "draw", "illustrate"
        ]
        
        retention_keywords = [
            "retention", "churn", "repeat", "repeat customer", "repeat purchase",
            "loyalty", "returning", "life cycle", "lifecycle", "cohort", 
            "user retention", "customer retention"
        ]
        
        analysis_keywords = [
            "analyze", "analysis", "full analysis", "comprehensive", "discover schema",
            "schema discovery", "detailed analysis", "business analysis", "deep dive",
            "comprehensive report", "refresh data", "update analysis", "refresh"
        ]
        
        # Keywords for partial/focused analysis
        self.partial_update_keywords = {
            "airtable": ["refresh airtable", "update airtable", "airtable data", "airtable analysis"],
            "inventory": ["refresh inventory", "update inventory", "inventory data", "inventory analysis"],
            "sales": ["refresh sales", "update sales", "sales data", "sales analysis"],
            "customers": ["refresh customers", "update customers", "customer data", "customer analysis"],
            "orders": ["refresh orders", "update orders", "order data", "orders analysis"]
        }
        
        strategy_keywords = [
            "strategy", "strategic", "recommendation", "advise", "advice", "suggest",
            "business plan", "action plan", "next steps", "decision", "growth",
            "optimization", "improve", "opportunity", "initiative", "roadmap"
        ]
        
        # STEP 1: Route visualization requests
        if any(keyword in user_input.lower() for keyword in visualization_keywords):
            return self.visualization_specialist
        
        # STEP 2: Route strategy requests    
        if any(keyword in user_input.lower() for keyword in strategy_keywords):
            return self.business_strategy_advisor
        
        # STEP 3: Check for retention-specific requests
        # These go to the chat_data_analyst with RetentionAnalysisTool, not full analysis
        if any(keyword in user_input.lower() for keyword in retention_keywords):
            return self.chat_data_analyst
        
        # STEP 4: Check if this is a request for full or partial analysis
        user_input_lower = user_input.lower()
        self.requires_full_analysis = any(keyword in user_input_lower for keyword in analysis_keywords)
        
        # Check if this is a focused/partial update request
        self.analysis_focus = self.detect_focused_analysis(user_input_lower)
        
        # STEP 5: Use appropriate data analyst based on mode
        if self.requires_full_analysis:
            return self.data_analyst  # Full analysis mode when KB explicitly needs refresh
        else:
            return self.chat_data_analyst  # Knowledge-first lightweight chat mode
    
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
            
        # Only save to knowledge base if this is a full analysis result
        # to avoid polluting the knowledge base with simple Q&A
        if agent_role == "Enterprise Data Analyst" and self.requires_full_analysis:
            save_analysis_results(content)
            print(f"📝 Saved results to knowledge base for future reference")
        
        return filepath
    
    def generate_visualizations(self, content: str):
        """Explicitly generate visualizations from analysis content."""
        try:
            # Use the visualization class directly
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Generate all possible charts
            viz_results = []
            
            print(f"🎨 Generating visualizations with timestamp {timestamp}...")
            
            # Product sales chart
            try:
                # Create a temporary file with the content for visualization
                tmp_file = f"temp_viz_{timestamp}.md"
                with open(tmp_file, 'w') as f:
                    f.write(content)
                
                # Use the VisualizationTool directly
                viz_tool = VisualizationTool()
                tool_result = viz_tool._run()
                
                # Clean up temporary file
                if os.path.exists(tmp_file):
                    os.remove(tmp_file)
                
                # Parse the tool result to extract visualization paths
                if "generated" in tool_result.lower():
                    # Extract paths from result
                    viz_results = [line.strip() for line in tool_result.split("\n") 
                                  if line.strip() and ":" in line and not line.startswith("#")]
                    
                    # Print each visualization that was found
                    for viz in viz_results:
                        print(f"✅ {viz}")
                else:
                    # Fallback to direct visualization methods
                    print("Falling back to direct visualization methods...")
                    
                    # Try to create any available visualization
                    try:
                        # Try product sales chart
                        if hasattr(self.visualizer, 'create_sales_bar_chart'):
                            data = self.visualizer.parse_markdown_content(content)
                            chart_path = self.visualizer.create_sales_bar_chart(data)
                            if chart_path:
                                viz_results.append(f"Product sales chart: {os.path.basename(chart_path)}")
                                print(f"✅ Generated product sales chart")
                                
                        # Try metrics dashboard
                        if hasattr(self.visualizer, 'create_metrics_dashboard'):
                            data = self.visualizer.parse_markdown_content(content)
                            dashboard_path = self.visualizer.create_metrics_dashboard(data)
                            if dashboard_path:
                                viz_results.append(f"Business metrics dashboard: {os.path.basename(dashboard_path)}")
                                print(f"✅ Generated metrics dashboard")
                    except Exception as e:
                        print(f"⚠️ Error in fallback visualization: {str(e)}")
            except Exception as e:
                print(f"⚠️ Error generating visualizations: {str(e)}")
                
            return viz_results
        except Exception as e:
            print(f"❌ Error generating visualizations: {str(e)}")
            return []
    
    def run_chat(self):
        """
        Run the interactive chat interface with Knowledge-First Strategy.
        
        # KNOWLEDGE-FIRST STRATEGY
        1. Always checks Knowledge Base first
        2. Only triggers full analysis when KB lacks content
        3. Routes visualization requests to Visualization Specialist
        4. Handles retention requests with RetentionAnalysisTool directly
        
        # CONVERSATIONAL RULES
        - Maintains context across turns
        - Explains reasoning when routing requests
        - Is concise but helpful
        - Offers refresh options for stale KB data
        """
        print("\n" + "="*50)
        print("Welcome to Plazza Analytics Chat!")
        print("Ask questions about your business data using our Knowledge-First approach.")
        
        # System status information
        viz_count = self.count_available_visualizations()
        
        # Print KB status with freshness check
        print("\n📊 System Status:")
        if self.kb_last_updated:
            # Calculate days since last update
            days_old = (datetime.now() - self.kb_last_updated).days
            kb_date = self.kb_last_updated.strftime("%B %d, %Y")
            
            if days_old > 7:
                print(f"⚠️ Knowledge Base: Last updated {kb_date} ({days_old} days ago)")
                print(f"   Type 'refresh' or 'analyze' for fresh data analysis")
            else:
                print(f"✅ Knowledge Base: Updated recently ({kb_date})")
        else:
            print("⚠️ Knowledge Base: No existing analysis found")
            print("   Your first analysis will initialize the knowledge base")
        
        # Print visualization status
        if viz_count > 0:
            print(f"📈 Visualizations: {viz_count} charts/dashboards available")
            print("   Type 'viz' to generate visualizations from any response")
        else:
            print("📈 Visualizations: None available yet")
            print("   Run an analysis to generate visualizations")
        
        print("\nHow to use:")
        print("- For quick answers, simply ask your question (KB-first)")
        print("- For retention analysis, include words like 'retention' or 'repeat customers'")
        print("- For visualizations, include words like 'chart' or 'graph'")  
        print("- For fresh analysis, include keywords like 'analyze' or 'refresh data'")
        print("- Type 'viz' to explicitly generate visualizations from the last response")
        print("- Type 'exit' or 'quit' to end the session")
        print("="*50 + "\n")
        
        last_response = None
        
        while True:
            user_input = input("\n👤 You: ")
            
            # Handle exit commands
            if user_input.lower() in ["exit", "quit"]:
                print("\nThank you for using Plazza Analytics Chat. Goodbye!")
                break
                
            # Handle visualization command
            if user_input.lower() == "viz" and last_response:
                print("\n🎨 Generating visualizations from the last response...")
                viz_results = self.generate_visualizations(last_response)
                
                if viz_results:
                    print("\n✅ Visualizations generated successfully:")
                    for viz in viz_results:
                        print(f"  - {viz}")
                else:
                    print("\n❌ No visualizations could be generated from the last response.")
                    print("   Try asking a question that generates specific data points.")
                continue
            
            # Store in history
            self.history.append({"role": "user", "content": user_input})
            
            # Route to appropriate agent
            agent = self.route_task(user_input)
            
            # Create a dynamic task based on user input and agent type
            if agent == self.data_analyst:
                # Handle different types of analysis based on focus area
                if self.analysis_focus:
                    print(f"🔍 Running focused analysis on {self.analysis_focus.upper()} from `plazza_analytics.py`...")
                    # Create a focused query by adding specific instructions
                    focused_query = f"{user_input} (FOCUS ON {self.analysis_focus.upper()} DATA ONLY - no need for full schema discovery)"
                else:
                    print("🔍 Running full Plazza analytics from `plazza_analytics.py`...")
                    focused_query = user_input
                
                start = time.time()
                result = run_analysis(user_query=focused_query)
                duration = round(time.time() - start, 2)
                print(f"\n🧠 Analysis completed in {duration} seconds.\n")
                
                self.history.append({"role": "Data Analyst", "content": result})
                last_response = result
                
                result_path = self.save_chat_result(
                    user_input, 
                    result, 
                    "Data Analyst",
                    tools_used=["CockroachDBTool", "RetentionAnalysisTool"],
                    focus_area=self.analysis_focus
                )
                
                print(f"\n🤖 Data Analyst (responded in {duration:.1f}s):")
                print(f"{result[:500]}...\n")  # Show just a preview of the result
                
                self.requires_full_analysis = False
                
                continue  # Skip the rest of the loop since we've already handled the response
            elif agent == self.chat_data_analyst:
                # Create a lightweight chat task for simple queries using the chat agent
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

WHEN YOU MUST QUERY (only if KB info is missing):
- Use the MethodologyTool for all database queries
- Check ALL relevant databases, not just one
- Use separate queries for different data sources (never UNION them)
- Document NULL/empty results clearly

Examples:
User: How are Airtable sales this month?
Response: Airtable sales for March 2025 were ₹14.5M. Regular sales were ₹3K.

User: How did you arrive at that?
Response:
I used these queries to get the latest data:

Airtable Query:
```sql
SELECT SUM(bill_total_amount) AS total_sales FROM airtable_orders WHERE created_at >= '2025-03-01' AND created_at < '2025-04-01' AND status = 'paid'
```
Result: ₹14.5M

Regular Orders Query:
```sql
SELECT SUM(bill_total_amount) AS total_sales FROM orders WHERE created_at >= '2025-03-01' AND created_at < '2025-04-01' AND status = 'paid'
```
Result: ₹3K

KNOWLEDGE MANAGEMENT:
- Never overwrite the Knowledge Base
- When you discover new information, note it should be added to the KB
- When citing the KB, mention the source timestamp briefly
- If KB info seems outdated, offer to refresh it

Previous conversation context:
{self.format_history()}
""",
                    expected_output="A concise answer with detailed methodology explaining how the answer was derived.",
                    agent=agent
                )
            elif agent == self.visualization_specialist:
                # Use the visualization task creator for visualization specialist
                task = create_visualization_task(f"""
                The user asked: '{user_input}'.
                
                Previous conversation context:
                {self.format_history()}
                
                Create visualizations that specifically address the user's request.
                """)
            elif agent == self.business_strategy_advisor:
                print(f"\n📊 Routing to Strategic Business Consultant...")
                print(f"   Creating strategy task with knowledge-first approach.\n")

                try:
                    # Create a strategy task with the chat_data_analyst for delegation
                    strategy_task = create_strategy_task(
                        user_query=user_input,
                        data_analyst_agent=self.chat_data_analyst
                    )
                    
                    start_time = time.time()
                    answer = self.business_strategy_advisor.execute_task(strategy_task)
                    end_time = time.time()

                    self.history.append({"role": "Strategic Business Consultant", "content": answer})
                    last_response = answer

                    result_path = self.save_chat_result(
                        user_input, 
                        answer, 
                        "Strategic Business Consultant",
                        tools_used=["Knowledge", "StrategyModule"],
                        focus_area="business_strategy"
                    )

                    processing_time = end_time - start_time
                    print(f"\n🤖 Strategic Business Consultant (responded in {processing_time:.1f}s):")
                    print(f"{answer}\n")

                    self.requires_full_analysis = False

                    continue  # Skip the rest of the loop since we've already printed the result
                except Exception as e:
                    print(f"\n❌ Error generating strategy: {str(e)}")
                    print("Please try again with a more specific strategy question.")
                    continue
            else:
                # Fallback to generic task
                task = Task(
                    description=f"""The user asked: '{user_input}'. 
                    
                    Previous conversation context:
                    {self.format_history()}
                    
                    Answer in a helpful, clear, and expert manner. If you're providing analysis results,
                    include specific data points and metrics whenever possible.
                    """,
                    expected_output="A comprehensive and accurate response to the user's query.",
                    agent=agent
                )
            
            if agent == self.data_analyst:
                print(f"\n🔍 Processing your request using {agent.role} in FULL ANALYSIS mode...")
                print(f"   This will update the Knowledge Base with fresh data.")
            elif agent == self.chat_data_analyst and any(keyword in user_input.lower() for keyword in ["retention", "repeat", "churn", "cohort"]):
                print(f"\n📊 Processing your retention request using {agent.role}...")
                print(f"   Using RetentionAnalysisTool for specialized metrics.")
            elif agent == self.chat_data_analyst:
                print(f"\n🧠 Processing your request using {agent.role} in KB-FIRST mode...")
                print(f"   Checking Knowledge Base first, will only query live data if needed.")
            elif agent == self.visualization_specialist:
                print(f"\n📈 Creating visualizations with {agent.role}...")
                print(f"   Generating charts based on available Knowledge Base data.")
            else:
                print(f"\n🤖 Processing your request using {agent.role}...")
            
            try:
                # Execute the task
                start_time = time.time()
                answer = agent.execute_task(task)
                end_time = time.time()
                
                # Store response in history
                self.history.append({"role": agent.role, "content": answer})
                last_response = answer
                
                # Determine tools used
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
                
                # Save result for persistence with enhanced metadata
                result_path = self.save_chat_result(
                    user_input, 
                    answer, 
                    agent.role,
                    tools_used=tools_used,
                    focus_area=self.analysis_focus
                )
                
                # Check if this is a visualization request and automate visualization
                if agent == self.visualization_specialist:
                    viz_results = self.generate_visualizations(answer)
                    if viz_results:
                        answer += "\n\nVisualizations have been created and saved to:"
                        for viz in viz_results:
                            answer += f"\n- {viz}"
                
                # Print response with timing info
                processing_time = end_time - start_time
                print(f"\n🤖 {agent.role} (responded in {processing_time:.1f}s):")
                print(f"{answer}\n")
                
                # Reset the full analysis flag
                self.requires_full_analysis = False
                
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                print("Please try asking your question differently.")
    
    def detect_focused_analysis(self, user_input_lower):
        """Detect if the user is requesting a focused analysis on a specific area."""
        for focus_area, keywords in self.partial_update_keywords.items():
            if any(keyword in user_input_lower for keyword in keywords):
                return focus_area
        return None
        
    def check_kb_freshness(self):
        """Check when the knowledge base was last updated."""
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        knowledge_file = os.path.join(parent_dir, 'knowledge', 'sales_analysis_results.md')
        
        if not os.path.exists(knowledge_file):
            return None
            
        try:
            # Get modification time of the knowledge file
            mod_time = os.path.getmtime(knowledge_file)
            mod_date = datetime.fromtimestamp(mod_time)
            
            # Check the content for timestamps
            with open(knowledge_file, 'r') as file:
                content = file.read()
                
            # Look for analysis timestamps in the content
            import re
            timestamp_matches = re.findall(r'## Full Analysis on (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', content)
            
            if timestamp_matches:
                # Use the most recent timestamp from the content
                latest_timestamp = max(timestamp_matches)
                return datetime.strptime(latest_timestamp, '%Y-%m-%d %H:%M:%S')
            
            # Fall back to file modification time if no timestamps found
            return mod_date
            
        except Exception as e:
            print(f"Error checking KB freshness: {str(e)}")
            return None
    
    def count_available_visualizations(self):
        """Count the number of visualizations available in the visuals directory."""
        visuals_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "visuals")
        if not os.path.exists(visuals_dir):
            return 0
            
        # Count HTML and PNG files
        viz_count = len([f for f in os.listdir(visuals_dir) 
                        if f.endswith(('.html', '.png')) and 
                        os.path.isfile(os.path.join(visuals_dir, f))])
        return viz_count
            
    def format_history(self, max_entries=3):
        """Format chat history for context in prompts."""
        if not self.history:
            return "No previous conversation."
            
        # Only include the last few exchanges to avoid context length issues
        recent_history = self.history[-max_entries*2:] if len(self.history) > max_entries*2 else self.history
        
        formatted = []
        for entry in recent_history:
            formatted.append(f"{entry['role']}: {entry['content']}")
            
        return "\n\n".join(formatted)

if __name__ == "__main__":
    chat = PlazzaChat()
    chat.run_chat()