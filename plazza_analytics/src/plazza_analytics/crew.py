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
    
    # Initialize tools
    from plazza_analytics.tools.cockroach_db_tool import CockroachDBTool
    
    try:
        from plazza_analytics.tools.methodology_tool import MethodologyTool
        from plazza_analytics.tools.retention_analysis_tool import RetentionAnalysisTool
        from plazza_analytics.tools.previous_analysis_tool import PreviousAnalysisTool
        from plazza_analytics.tools.general_visualization_tool import GeneralVisualizationTool
        
        # Create the tools
        cockroach_db_tool = CockroachDBTool()
        methodology_tool = MethodologyTool()
        retention_analysis_tool = RetentionAnalysisTool()
        previous_analysis_tool = PreviousAnalysisTool()
        general_visualization_tool = GeneralVisualizationTool()
        
        # Tool mapping for each agent
        agent_tools = {
            "data_analyst": [cockroach_db_tool, retention_analysis_tool],
            "chat_data_analyst": [cockroach_db_tool, methodology_tool, retention_analysis_tool, previous_analysis_tool],
            "visualization_specialist": [general_visualization_tool]
        }
    except ImportError as e:
        print(f"Warning: Could not import all tools: {e}")
        # Create fallback version with just the CockroachDBTool
        cockroach_db_tool = CockroachDBTool()
        
        # Minimal tool mapping for each agent
        agent_tools = {
            "data_analyst": [cockroach_db_tool],
            "chat_data_analyst": [cockroach_db_tool],
            "visualization_specialist": []
        }
    
    # Create agent instances with appropriate tools
    agents = {}
    for agent_name, agent_data in agent_config.items():
        tools_for_agent = agent_tools.get(agent_name.lower().replace(" ", "_"), [])
        
        agents[agent_name] = Agent(
            role=agent_data.get("role", ""),
            goal=agent_data.get("goal", ""),
            backstory=agent_data.get("backstory", ""),
            verbose=True,
            allow_delegation=agent_name == "conversation_orchestrator",
            tools=tools_for_agent
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