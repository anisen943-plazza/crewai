import yaml
import importlib
import sys
import os
from pathlib import Path
from crewai import Agent, Task, Crew, Process

# Add the proper paths to sys.path to make imports work
current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
src_dir = current_dir.parent.parent  # Navigate up to src directory
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

# Import tool classes
from src.asana_manager.tools.asana_tools import (
    ListWorkspacesTool, ListTeamsTool, CreateProjectTool, CreateTaskTool, AssignTaskTool, 
    SetDueDateTool, BrowseProjectTool, ListUsersTool, FindProjectByNameTool, 
    CompareTasksWithDocumentationTool, WORKSPACE_GID, TEAM_GID
)

# Create instances of our tool classes
list_workspaces_tool = ListWorkspacesTool()
list_teams_tool = ListTeamsTool()
create_project_tool = CreateProjectTool()
create_task_tool = CreateTaskTool()
assign_task_tool = AssignTaskTool()
set_due_date_tool = SetDueDateTool()
browse_project_tool = BrowseProjectTool()
list_users_tool = ListUsersTool()
find_project_tool = FindProjectByNameTool()
compare_tasks_tool = CompareTasksWithDocumentationTool()

# Create a dict of available tools
available_tools = {
    "asana_tools.ListWorkspacesTool": list_workspaces_tool,
    "asana_tools.ListTeamsTool": list_teams_tool,
    "asana_tools.CreateProjectTool": create_project_tool,
    "asana_tools.CreateTaskTool": create_task_tool,
    "asana_tools.AssignTaskTool": assign_task_tool,
    "asana_tools.SetDueDateTool": set_due_date_tool,
    "asana_tools.BrowseProjectTool": browse_project_tool,
    "asana_tools.ListUsersTool": list_users_tool,
    "asana_tools.FindProjectByNameTool": find_project_tool,
    "asana_tools.CompareTasksWithDocumentationTool": compare_tasks_tool
}

# 1. Load your YAML configs as dicts
with open("src/asana_manager/config/agents.yaml") as f:
    agents_dict = yaml.safe_load(f)
with open("src/asana_manager/config/tasks.yaml") as f:
    tasks_dict = yaml.safe_load(f)

# Create a dictionary to store agent objects by name
agent_lookup = {}

# 2. Build Agent objects with proper tool instantiation
for name, cfg in agents_dict.items():
    # Extract tools from config and replace with actual tool objects
    if 'tools' in cfg:
        tool_names = cfg.pop('tools', [])
        tools = []
        for tool_name in tool_names:
            if tool_name in available_tools:
                tools.append(available_tools[tool_name])
            else:
                print(f"Warning: Tool {tool_name} not found")
        
        # Add the tools to the config
        if tools:
            cfg['tools'] = tools
    
    # Create the agent with a name parameter
    agent = Agent(
        name=name,
        role=cfg.get('role', ''),
        goal=cfg.get('goal', ''),
        backstory=cfg.get('backstory', ''),
        tools=cfg.get('tools', []),
        verbose=True
    )
    
    # Store in lookup dictionary
    agent_lookup[name] = agent

# 3. Create tasks with reference to agent objects
tasks = []
for name, cfg in tasks_dict.items():
    # Get the agent reference
    agent_name = cfg.get('agent')
    agent = agent_lookup.get(agent_name)
    
    if not agent:
        print(f"Warning: Agent '{agent_name}' not found for task '{name}'")
        continue
    
    # Create task with properly formatted parameters
    task = Task(
        name=name,
        description=cfg.get('description', ''),
        expected_output=cfg.get('expected_output', ''),
        agent=agent
    )
    
    tasks.append(task)

# 3. Instantiate your Crew
crew = Crew(
    agents=list(agent_lookup.values()),
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

# 4. Kick it off
print("Starting AsanaManager crew...")
print(f"Using Asana workspace GID: {WORKSPACE_GID}")

try:
    # First, try to list workspaces and teams to ensure API connectivity
    print("Testing Asana API connectivity...")
    workspaces = list_workspaces_tool._run()
    if 'data' in workspaces:
        print(f"✓ Successfully connected to Asana - found {len(workspaces['data'])} workspace(s)")
        
        # Try to list teams in the first workspace
        if len(workspaces['data']) > 0:
            workspace_gid = workspaces['data'][0]['gid']
            print(f"Testing team discovery in workspace: {workspace_gid}")
            teams = list_teams_tool._run(workspace_gid=workspace_gid)
            if 'data' in teams and len(teams['data']) > 0:
                print(f"✓ Found {len(teams['data'])} team(s) in workspace")
            else:
                print("⚠️ No teams found. Using fallback mechanism for team discovery.")
    else:
        print("⚠️ Could not list workspaces. Using provided GID as fallback.")
    
    # Choose which task to run
    print("\nAvailable tasks:")
    print("1. Create a new Asana project using CrewAI workflow")
    print("2. Compare Pharmacist Operations Module with documentation") 
    print("3. List all projects across all workspaces")
    print("4. Find a project by name")
    print("5. Browse project details")
    print("6. List workspaces and teams")
    print("7. Create project (direct tool)")
    print("8. Create project from markdown file")
    task_choice = input("\nEnter task number (1-8): ")
    
    if task_choice == "1":
        # Create project inputs
        project_name = input("\nEnter project name: ")
        task1 = input("Enter first task name: ")
        task2 = input("Enter second task name: ")
        task3 = input("Enter third task name: ")
        
        print("\nStarting CrewAI workflow to create project...")
        result = crew.kickoff(
            task_name="initialize_asana_project",
            inputs={
                "project_name": project_name or "Q2 Launch Plan",
                "task1": task1 or "Planning",
                "task2": task2 or "Execution",
                "task3": task3 or "Review"
            }
        )
    elif task_choice == "2":
        print("\nStarting CrewAI workflow to compare Pharmacist Operations Module with documentation...")
        result = crew.kickoff(task_name="compare_project_with_documentation")
    elif task_choice == "3":
        # Import the project listing tool directly
        from src.asana_manager.tools.list_all_projects import ListAllProjectsTool
        
        print("\nListing all projects across workspaces...")
        list_tool = ListAllProjectsTool()
        result = list_tool.run()
        
        # Don't print the result again since the tool already displays output
        result = None
    elif task_choice == "4":
        # Find project by name
        project_name = input("\nEnter project name to find: ")
        
        print(f"\nSearching for projects matching: '{project_name}'...")
        result = find_project_tool._run(name=project_name)
        
        # Handle the result
        if isinstance(result, dict) and "matches" in result:
            matches = result["matches"]
            if not matches:
                print("No matching projects found.")
            else:
                print(f"\nFound {len(matches)} matching project(s):\n")
                for i, project in enumerate(matches, 1):
                    print(f"{i}. Project: {project['name']}")
                    print(f"   GID: {project['gid']}")
                    print(f"   Workspace: {project['workspace']['name']}")
                    if "team" in project and project["team"]:
                        print(f"   Team: {project['team']['name']}")
                    print(f"   URL: https://app.asana.com/0/{project['gid']}")
                    print()
        
        # Don't print the result again
        result = None
    elif task_choice == "5":
        # Browse project
        project_gid = input("\nEnter project GID to browse: ")
        
        print(f"\nBrowsing project with GID: {project_gid}...")
        result = browse_project_tool._run(project_gid=project_gid)
        
        # Handle the result
        if isinstance(result, dict) and "project" in result:
            project_data = result["project"]
            sections_data = result.get("sections", {})
            tasks_data = result.get("tasks", {})
            
            # Handle potential Asana API nested structure
            project = project_data.get('data', project_data)
            
            # Handle sections with 'data' wrapper
            section_items = []
            if isinstance(sections_data, dict) and 'data' in sections_data:
                section_items = sections_data['data']
            else:
                section_items = sections_data
                
            # Handle tasks with 'data' wrapper    
            task_items = []
            if isinstance(tasks_data, dict) and 'data' in tasks_data:
                task_items = tasks_data['data']
            else:
                task_items = tasks_data
            
            print(f"\nProject Details:")
            # Access project attributes safely
            if 'name' in project:
                print(f"   Name: {project['name']}")
            else:
                print(f"   Name: Unknown (name not found in response)")
                
            if 'gid' in project:
                project_gid = project['gid']
                print(f"   GID: {project_gid}")
                print(f"   URL: https://app.asana.com/0/{project_gid}")
            else:
                print(f"   GID: {project_gid} (from input)")
                
            if "notes" in project and project["notes"]:
                print(f"   Notes: {project['notes']}")
            
            print(f"\nSections ({len(section_items)}):")
            for i, section_data in enumerate(section_items, 1):
                # Handle possible 'data' wrapper for each section
                section = section_data.get('data', section_data)
                if 'name' in section and 'gid' in section:
                    print(f"{i}. {section['name']} (GID: {section['gid']})")
                else:
                    print(f"{i}. Section name/gid not found")
            
            print(f"\nTasks ({len(task_items)}):")
            for i, task_data in enumerate(task_items, 1):
                # Handle possible 'data' wrapper for each task
                task = task_data.get('data', task_data)
                
                # Extract task attributes safely
                status = "✅" if task.get("completed", False) else "⬜"
                section_name = task.get("section_name", "No Section")
                
                # Handle assignee which might be nested
                assignee = task.get("assignee", {})
                assignee_name = "Unassigned"
                if isinstance(assignee, dict) and 'name' in assignee:
                    assignee_name = assignee['name']
                
                due_date = task.get("due_on", "No due date")
                
                # Access task name and gid safely
                if 'name' in task:
                    task_name = task['name']
                    print(f"{i}. {status} {task_name}")
                else:
                    print(f"{i}. {status} Task name not found")
                    
                if 'gid' in task:
                    print(f"   GID: {task['gid']}")
                
                print(f"   Section: {section_name}")
                print(f"   Assignee: {assignee_name}")
                print(f"   Due Date: {due_date}")
                print()
        
        # Don't print the result again
        result = None
    elif task_choice == "6":
        # List workspaces and teams
        print("\nListing workspaces and teams...")
        
        # List workspaces
        workspaces_result = list_workspaces_tool._run()
        if isinstance(workspaces_result, dict) and "data" in workspaces_result:
            workspaces = workspaces_result["data"]
            print(f"\nWorkspaces ({len(workspaces)}):")
            for i, workspace in enumerate(workspaces, 1):
                print(f"{i}. {workspace['name']} (GID: {workspace['gid']})")
                
                # List teams for this workspace
                teams_result = list_teams_tool._run(workspace_gid=workspace['gid'])
                if isinstance(teams_result, dict) and "data" in teams_result:
                    teams = teams_result["data"]
                    print(f"   Teams ({len(teams)}):")
                    if not teams:
                        print("      No teams found in this workspace")
                    for j, team in enumerate(teams, 1):
                        print(f"      {j}. {team['name']} (GID: {team['gid']})")
                print()
        
        # Don't print the result again
        result = None
    elif task_choice == "7":
        # Create a project directly
        project_name = input("\nEnter project name: ")
        project_notes = input("Enter project notes (optional): ")
        
        print(f"\nCreating project: '{project_name}'...")
        result = create_project_tool._run(
            name=project_name,
            notes=project_notes
        )
        
        # Handle the result
        if isinstance(result, dict) and "data" in result:
            project = result["data"]
            print(f"\nProject created successfully!")
            print(f"   Name: {project['name']}")
            print(f"   GID: {project['gid']}")
            print(f"   URL: https://app.asana.com/0/{project['gid']}")
        
        # Don't print the result again
        result = None
    elif task_choice == "8":
        # Create project from markdown
        from src.asana_manager.tools.markdown_to_asana import MarkdownToAsanaTool
        
        markdown_file = input("\nEnter path to markdown file: ")
        project_name = input("Enter project name: ")
        
        print(f"\nCreating project from markdown file: {markdown_file}...")
        
        # Create the tool instance
        md_tool = MarkdownToAsanaTool()
        result = md_tool._run(
            markdown_file_path=markdown_file,
            project_name=project_name
        )
        
        # Handle the result
        if isinstance(result, dict) and "success" in result and result["success"]:
            print(f"\nProject created successfully!")
            print(f"   Name: {result['project_name']}")
            print(f"   URL: {result['project_url']}")
            print(f"\nStatistics:")
            for key, value in result['statistics'].items():
                print(f"   - {key.replace('_', ' ').title()}: {value}")
        
        # Don't print the result again
        result = None
    else:
        print("\n❌ Invalid choice. Please enter a number between 1 and 8.")
        result = None
    
    if result is not None:
        print("\nResult:", result)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTroubleshooting suggestions:")
    print("1. Check that your ASANA_API_TOKEN is valid")
    print("2. Make sure you have access to at least one workspace in Asana")
    print("3. Verify that you have at least one team in your workspace")
    print("4. Check for detailed error messages above to understand the API issue")