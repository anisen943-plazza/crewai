import yaml
import os
from crewai import Crew, Process, Agent, Task

def load_yaml_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def create_plazza_crew():
    # Load agents and tasks from YAML
    agents_yaml_path = os.path.join(os.path.dirname(__file__), "config", "agents.yaml")
    tasks_yaml_path = os.path.join(os.path.dirname(__file__), "config", "tasks.yaml")
    
    agent_config = load_yaml_config(agents_yaml_path)
    task_config = load_yaml_config(tasks_yaml_path)
    
    # Set up knowledge sources with optimized parameters
    try:
        # In newer versions of CrewAI, the Knowledge class is imported directly from crewai
        from crewai import Knowledge
        # The TextFileKnowledgeSource is still in a similar location
        try:
            # Try the new import path first
            from crewai.knowledge_source.text_file_knowledge_source import TextFileKnowledgeSource
        except ImportError:
            # Fall back to old import path
            from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
        
        # Create knowledge sources with optimal chunking parameters
        # Use relative paths for CrewAI's knowledge system
        knowledge_files = [
            {"file": "sales_analysis.md", "domain": "sales", "type": "business_intelligence"},
            {"file": "database_schemas.md", "domain": "technical", "type": "database_schema"},
            {"file": "customer_insights.md", "domain": "customer", "type": "retention_analysis"}
        ]
        
        # Create sources
        knowledge_sources = []
        for kf in knowledge_files:
            try:
                source = TextFileKnowledgeSource(
                    file_paths=[kf["file"]],
                    chunk_size=800,
                    chunk_overlap=200,
                    metadata={"domain": kf["domain"], "type": kf["type"]}
                )
                knowledge_sources.append(source)
            except Exception as e:
                print(f"Warning: Could not create knowledge source for {kf['file']}: {e}")
        
        # Create knowledge collection
        knowledge = Knowledge(
            collection_name="plazza_knowledge",
            sources=knowledge_sources
        ) if knowledge_sources else None
    
    except ImportError as e:
        print(f"Warning: Could not set up knowledge: {e}")
        knowledge = None
    
    # Initialize tools with names that match YAML references
    from crewai.tools import BaseTool
    from plazza_analytics.tools.cockroach_db_tool import CockroachDBTool
    
    try:
        from plazza_analytics.tools.methodology_tool import MethodologyTool
        from plazza_analytics.tools.retention_analysis_tool import RetentionAnalysisTool
        from plazza_analytics.tools.previous_analysis_tool import PreviousAnalysisTool
        from plazza_analytics.tools.general_visualization_tool import GeneralVisualizationTool
        from plazza_analytics.tools.save_knowledge_tool import SaveKnowledgeTool
        
        # Create tool instances with variable names matching those in YAML
        # These names must exactly match the strings in the agents.yaml file
        cockroach_db_tool = CockroachDBTool()
        methodology_tool = MethodologyTool()
        retention_analysis_tool = RetentionAnalysisTool()
        previous_analysis_tool = PreviousAnalysisTool()
        save_knowledge_tool = SaveKnowledgeTool()
        # Import the class and initialize it with a different name first to avoid name collision
        GeneralVisualizationToolClass = GeneralVisualizationTool
        GeneralVisualizationTool = GeneralVisualizationToolClass()  # Name matches case in YAML
        
    except ImportError as e:
        print(f"Warning: Could not import all tools: {e}")
    
    # Create a mapping of tool names to tool instances
    tool_mapping = {
        "cockroach_db_tool": cockroach_db_tool,
        "methodology_tool": methodology_tool,
        "retention_analysis_tool": retention_analysis_tool,
        "previous_analysis_tool": previous_analysis_tool,
        "save_knowledge_tool": save_knowledge_tool,
        "GeneralVisualizationTool": GeneralVisualizationTool
    }
    
    # Create agent instances directly from YAML config
    agents = {}
    for agent_name, agent_data in agent_config.items():
        # Fetch tool names from YAML and resolve to actual tool instances
        tool_names = agent_data.get("tools", [])
        agent_tools = []
        
        for name in tool_names:
            if name in tool_mapping:
                agent_tools.append(tool_mapping[name])
            else:
                print(f"⚠️ Warning: Tool '{name}' is not defined in crew.py")
        
        agents[agent_name] = Agent(
            role=agent_data.get("role", ""),
            goal=agent_data.get("goal", ""),
            backstory=agent_data.get("backstory", ""),
            verbose=True,
            allow_delegation=agent_name == "conversation_orchestrator",
            tools=agent_tools,  # Pass resolved tools here
            knowledge=knowledge,  # Add the knowledge source
            memory=True  # Enable memory for context
        )
    
    # Initialize tasks with agents
    tasks = []
    for task_name, task_data in task_config.items():
        agent_name = "conversation_orchestrator"  # Default agent for tasks
        tasks.append(Task(
            description=task_data.get("description", ""),
            expected_output=task_data.get("expected_output", ""),
            agent=agents[agent_name]
        ))
    
    # Define crew
    # In CrewAI v0.30.0, hierarchical process requires a manager agent
    # We'll use the Conversation Orchestrator as the manager
    return Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,  # Change to sequential to avoid needing a manager
        verbose=True
    )

# Create a single crew instance
crew = create_plazza_crew()