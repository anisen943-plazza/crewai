# File: Core_Scripts/agent_registry.py

import os
from crewai import Agent
from Core_Scripts.plazza_analytics import (
    CockroachDBTool,
    RetentionAnalysisTool,
    MethodologyTool,
    VisualizationTool,
    create_knowledge_source
)
from Core_Scripts.crewai_visualization import CrewAIVisualization

# Load .env if needed
from dotenv import load_dotenv
load_dotenv()

# Global Knowledge Base
knowledge = create_knowledge_source()

# Import specialized visualization tools
from Core_Scripts.crewai_visualization import (
    TopProductsChartTool,
    CustomerRetentionChartTool,
    MetricsDashboardTool
)

# Shared tools
db_tool = CockroachDBTool()
retention_tool = RetentionAnalysisTool()
methodology_tool = MethodologyTool()
visualization_tool = VisualizationTool()

# Specialized visualization tools
top_products_tool = TopProductsChartTool()
customer_retention_tool = CustomerRetentionChartTool()
metrics_dashboard_tool = MetricsDashboardTool()

# Agent definitions

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
        memory=True
    )

def get_chat_data_analyst():
    return Agent(
        role="Data Q&A Expert",
        goal="Quickly answer user questions about sales, orders, products, and customers using business data",
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

def get_visualization_specialist():
    return Agent(
        role="Data Visualization Expert",
        goal="Create clear, impactful visual reports from the KB.",
        backstory="""You turn business data into compelling visualizations. You never run queries.
You rely entirely on the KB and produce charts/dashboards from its data.

You can access specialized visualization tools for specific use cases:
- VisualizationTool: For creating all chart types at once
- TopProductsChartTool: For product sales visualizations only
- CustomerRetentionChartTool: For customer retention analysis only
- MetricsDashboardTool: For business metrics dashboards only

You maintain memory of recent visualization requests to optimize chart generation
and ensure consistency in visualization styles across sessions.

You do not analyze or update data — just visualize what exists.""",
        verbose=False,
        allow_delegation=False,
        tools=[visualization_tool, top_products_tool, customer_retention_tool, metrics_dashboard_tool],
        knowledge=knowledge,
        memory=True
    )

def get_strategy_advisor():
    return Agent(
        role="Strategic Business Consultant",
        goal="Advise business strategy using sales, retention and product data from the KB",
        backstory="""You give strategic business advice based on KB data. You suggest concrete next steps
but never query data yourself. You may ask the Data Q&A Expert for specific metrics if needed.
You maintain memory of previous strategy discussions to provide continuous strategic guidance
and follow up on previous recommendations to track their implementation and success.""",
        verbose=False,
        allow_delegation=False,
        tools=[],
        knowledge=knowledge,
        memory=True
    )

def get_visualizer_instance():
    return CrewAIVisualization()

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