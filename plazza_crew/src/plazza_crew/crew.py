import os
import sys
import yaml
from crewai import Crew, Process, Agent, Task

# Add the project directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# Import with the corrected path
from src.plazza_crew.tools.custom_postgres_tool import query_postgres

# Directory where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load agents configuration from YAML file
with open(os.path.join(current_dir, "config/agents.yaml"), "r") as f:
    agents_config = yaml.safe_load(f)

# Load tasks configuration from YAML file
with open(os.path.join(current_dir, "config/tasks.yaml"), "r") as f:
    tasks_config = yaml.safe_load(f)

# Initialize agents
user_query_handler = Agent(
    role=agents_config["user_query_handler"]["role"],
    goal=agents_config["user_query_handler"]["goal"],
    backstory=agents_config["user_query_handler"]["backstory"],
    allow_delegation=True,
    verbose=True,
)

postgres_query_agent = Agent(
    role=agents_config["postgres_query_agent"]["role"],
    goal=agents_config["postgres_query_agent"]["goal"],
    backstory=agents_config["postgres_query_agent"]["backstory"],
    tools=[query_postgres],
    verbose=True,
)

# Initialize tasks
handle_user_query_task = Task(
    description=tasks_config["handle_user_query_task"]["description"],
    expected_output=tasks_config["handle_user_query_task"]["expected_output"],
    agent=user_query_handler
)

answer_from_db_task = Task(
    description=tasks_config["answer_from_db_task"]["description"],
    expected_output=tasks_config["answer_from_db_task"]["expected_output"],
    agent=postgres_query_agent
)

# Define crew
crew = Crew(
    agents=[user_query_handler, postgres_query_agent],
    tasks=[handle_user_query_task, answer_from_db_task],
    process=Process.sequential,
    verbose=True
)