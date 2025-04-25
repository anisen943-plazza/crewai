import requests
import datetime
from typing import Optional
from crewai.tools import BaseTool

# Asana API configuration
import os
from dotenv import load_dotenv

# Try to load environment variables from the Master_ENV directory
master_env_path = "/Users/aniruddhasen/Projects/Master_ENV/.env"
if os.path.exists(master_env_path):
    load_dotenv(master_env_path)
else:
    # Fall back to local .env file if it exists
    load_dotenv()

# Get Asana API token from environment variables
ASANA_API_TOKEN = os.getenv("ASANA_API_TOKEN")
if not ASANA_API_TOKEN:
    raise ValueError("ASANA_API_TOKEN not found in environment variables")

HEADERS = {
    "Authorization": f"Bearer {ASANA_API_TOKEN}",
    "Content-Type": "application/json"
}
BASE_URL = "https://app.asana.com/api/1.0"

# For the workspace GID, we'll need to get it from the API
# We'll use this as a cache for the first workspace GID found
# Use the provided GID as a fallback if no workspace is found
WORKSPACE_GID = "1208316653297247"  # Using the GID provided by the user
# We'll also cache the first team GID found
TEAM_GID = None

class CreateProjectTool(BaseTool):
    name: str = "CreateProjectTool"
    description: str = "Create a new project in Asana. If workspace_gid is not provided, uses the default workspace. Requires a team_gid."
    
    def _run(self, name: str, notes: str = "", workspace_gid: Optional[str] = None, team_gid: Optional[str] = None) -> str:
        """
        Create a new project in Asana.
        
        Args:
            name: The name of the project
            notes: Optional notes for the project
            workspace_gid: Optional workspace GID (uses default if not provided)
            team_gid: Optional team GID. If not provided, will use the default team.
            
        Returns:
            Project information in JSON format
        """
        global WORKSPACE_GID, TEAM_GID
        
        # If no workspace_gid provided and WORKSPACE_GID not set, try to get workspaces
        if not workspace_gid and not WORKSPACE_GID:
            workspaces_tool = ListWorkspacesTool()
            workspaces_tool._run()
        
        # Use provided workspace_gid or default
        workspace = workspace_gid or WORKSPACE_GID
        
        if not workspace:
            return {"error": "No workspace GID provided and no default workspace found"}
        
        # If no team_gid provided and TEAM_GID not set, try to get teams
        if not team_gid and not TEAM_GID:
            try:
                teams_tool = ListTeamsTool()
                teams_result = teams_tool._run(workspace_gid=workspace)
                
                # If we still don't have a team, check if there's an error in the teams response
                if not TEAM_GID and isinstance(teams_result, dict) and 'error' in teams_result:
                    print(f"Team discovery failed: {teams_result['error']}")
                    print("Trying to use personal projects. If this fails, you'll need to provide a valid team_gid.")
                    # For personal projects, sometimes we can use the user as the "team"
                    users_tool = ListUsersTool()
                    users_result = users_tool._run(workspace_gid=workspace)
                    if isinstance(users_result, dict) and 'data' in users_result and len(users_result['data']) > 0:
                        # Get the current user's GID (usually the first in the list)
                        TEAM_GID = users_result['data'][0]['gid']
                        print(f"Using user GID as fallback team: {TEAM_GID}")
            except Exception as e:
                print(f"Error discovering teams: {e}")
        
        # Use provided team_gid or default
        team = team_gid or TEAM_GID
        
        if not team:
            return {"error": "No team GID provided and no default team found. Asana requires a team when creating a project."}
        
        # Make the actual API call
        try:
            url = f"{BASE_URL}/projects"
            data = {
                "data": {
                    "workspace": workspace,
                    "name": name,
                    "notes": notes,
                    "team": team
                }
            }
            
            response = requests.post(url, headers=HEADERS, json=data)
            response.raise_for_status()  # Raise an exception for 4XX/5XX responses
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}

class CreateTaskTool(BaseTool):
    name: str = "CreateTaskTool"
    description: str = "Create a new task in an Asana project"
    
    def _run(self, project_gid: str, name: str, notes: str = "", assignee: Optional[str] = None) -> str:
        """Create a new task in an Asana project"""
        try:
            url = f"{BASE_URL}/tasks"
            data = {
                "data": {
                    "name": name,
                    "notes": notes,
                    "projects": [project_gid]
                }
            }
            
            # Only include assignee if provided
            if assignee:
                data["data"]["assignee"] = assignee
                
            response = requests.post(url, headers=HEADERS, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}

class AssignTaskTool(BaseTool):
    name: str = "AssignTaskTool"
    description: str = "Assign a task to a user in Asana"
    
    def _run(self, task_gid: str, assignee: str) -> str:
        """Assign a task to a user in Asana"""
        try:
            url = f"{BASE_URL}/tasks/{task_gid}"
            data = {"data": {"assignee": assignee}}
            response = requests.put(url, headers=HEADERS, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}

class SetDueDateTool(BaseTool):
    name: str = "SetDueDateTool"
    description: str = "Set the due date for an Asana task"
    
    def _run(self, task_gid: str, due_date: str) -> str:
        """Set the due date for an Asana task"""
        try:
            url = f"{BASE_URL}/tasks/{task_gid}"
            data = {"data": {"due_on": due_date}}
            response = requests.put(url, headers=HEADERS, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}

class BrowseProjectTool(BaseTool):
    name: str = "BrowseProjectTool"
    description: str = "Browse a project and its tasks in Asana"
    
    def _run(self, project_gid: str) -> str:
        """Browse a project and its tasks in Asana"""
        try:
            # Get project details
            project_url = f"{BASE_URL}/projects/{project_gid}"
            project_response = requests.get(project_url, headers=HEADERS)
            project_response.raise_for_status()
            project = project_response.json()
            
            # Get project sections
            sections_url = f"{BASE_URL}/projects/{project_gid}/sections"
            sections_response = requests.get(sections_url, headers=HEADERS)
            sections_response.raise_for_status()
            sections = sections_response.json()
            
            # Get project tasks
            tasks_url = f"{BASE_URL}/projects/{project_gid}/tasks"
            tasks_response = requests.get(tasks_url, headers=HEADERS)
            tasks_response.raise_for_status()
            tasks = tasks_response.json()
            
            # Enhance tasks with section names
            if 'data' in tasks and isinstance(tasks['data'], list) and 'data' in sections:
                section_map = {section['gid']: section['name'] for section in sections['data']}
                
                for task in tasks['data']:
                    # If task has a section, add section name
                    if 'section' in task and task['section'] in section_map:
                        task['section_name'] = section_map[task['section']]
                    else:
                        task['section_name'] = "No Section"
            
            return {"project": project, "sections": sections, "tasks": tasks}
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}

class FindProjectByNameTool(BaseTool):
    name: str = "FindProjectByNameTool"
    description: str = "Find an Asana project by name"
    
    def _run(self, project_name: str, workspace_gid: Optional[str] = None) -> str:
        """Find an Asana project by name in the workspace"""
        global WORKSPACE_GID
        
        # If no workspace_gid provided and WORKSPACE_GID not set, try to get workspaces
        if not workspace_gid and not WORKSPACE_GID:
            workspaces_tool = ListWorkspacesTool()
            workspaces_tool._run()
        
        # Use provided workspace_gid or default
        workspace = workspace_gid or WORKSPACE_GID
        
        if not workspace:
            return {"error": "No workspace GID provided and no default workspace found"}
        
        try:
            # Get all projects in the workspace
            url = f"{BASE_URL}/projects?workspace={workspace}&limit=100"
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            result = response.json()
            
            # Find the project with the matching name
            matching_projects = []
            
            if 'data' in result:
                for project in result['data']:
                    if project_name.lower() in project['name'].lower():
                        matching_projects.append(project)
            
            if matching_projects:
                return {"matching_projects": matching_projects}
            else:
                return {"error": f"No projects found matching '{project_name}'"}
                
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}

class ListWorkspacesTool(BaseTool):
    name: str = "ListWorkspacesTool"
    description: str = "List all workspaces accessible to the user in Asana"
    
    def _run(self) -> str:
        """List all workspaces accessible to the user in Asana"""
        global WORKSPACE_GID
        
        # Real API call
        url = f"{BASE_URL}/workspaces"
        response = requests.get(url, headers=HEADERS)
        result = response.json()
        
        # Cache the first workspace GID if available
        if not WORKSPACE_GID and 'data' in result and len(result['data']) > 0:
            WORKSPACE_GID = result['data'][0]['gid']
            print(f"Set default workspace GID to {WORKSPACE_GID}")
        
        return result

class ListTeamsTool(BaseTool):
    name: str = "ListTeamsTool"
    description: str = "List all teams in an Asana workspace. If no workspace_gid is provided, uses the default workspace."
    
    def _run(self, workspace_gid: Optional[str] = None) -> str:
        """List all teams in an Asana workspace"""
        global WORKSPACE_GID
        
        # If no workspace_gid provided and WORKSPACE_GID not set, try to get workspaces
        if not workspace_gid and not WORKSPACE_GID:
            workspaces_tool = ListWorkspacesTool()
            workspaces_tool._run()
        
        # Use provided workspace_gid or default
        workspace = workspace_gid or WORKSPACE_GID
        
        if not workspace:
            return {"error": "No workspace GID provided and no default workspace found"}
        
        # Real API call to get teams
        url = f"{BASE_URL}/organizations/{workspace}/teams"
        response = requests.get(url, headers=HEADERS)
        result = response.json()
        
        # Store the first team GID as a global variable if available
        if 'data' in result and len(result['data']) > 0:
            global TEAM_GID
            TEAM_GID = result['data'][0]['gid']
            print(f"Set default team GID to {TEAM_GID}")
            
        return result

class ListUsersTool(BaseTool):
    name: str = "ListUsersTool"
    description: str = "List all users in an Asana workspace. If no workspace_gid is provided, uses the default workspace."
    
    def _run(self, workspace_gid: Optional[str] = None) -> str:
        """List all users in an Asana workspace"""
        global WORKSPACE_GID
        
        # If no workspace_gid provided and WORKSPACE_GID not set, try to get workspaces
        if not workspace_gid and not WORKSPACE_GID:
            workspaces_tool = ListWorkspacesTool()
            workspaces_tool._run()
        
        # Use provided workspace_gid or default
        workspace = workspace_gid or WORKSPACE_GID
        
        if not workspace:
            return {"error": "No workspace GID provided and no default workspace found"}
        
        # Real API call
        url = f"{BASE_URL}/users?workspace={workspace}"
        response = requests.get(url, headers=HEADERS)
        return response.json()

class CompareTasksWithDocumentationTool(BaseTool):
    name: str = "CompareTasksWithDocumentationTool"
    description: str = """Compare an Asana project's tasks with implementation checklist in a markdown document.
    
    Supports various markdown formats through template specification:
    - standard: The default format with "- [ ] Task" and "- [x] Completed task"
    - headings: Extract tasks from headings (### Task Name)
    - custom: Use a custom regex pattern to extract tasks
    
    Examples:
    - Standard: compare_tool._run(project_gid, markdown_file, template="standard")
    - Headings: compare_tool._run(project_gid, markdown_file, template="headings", heading_level=3)
    - Custom: compare_tool._run(project_gid, markdown_file, template="custom", pattern=r'Task: (.+?) \| Status: (.+?)$')
    """
    
    def _run(self, project_gid: str, markdown_file_path: str, template: str = "standard", 
            heading_level: int = None, pattern: str = None, section_filter: str = None) -> str:
        """
        Compare tasks in an Asana project with implementation checklist items in a markdown document.
        
        Args:
            project_gid: The GID of the Asana project to check
            markdown_file_path: Path to the markdown file containing implementation checklist
            template: The template format to use for parsing the markdown:
                - "standard": Default format with "- [ ] Task" and "- [x] Completed task"
                - "headings": Extract tasks from headings (e.g., ### Task Name)
                - "custom": Use a custom regex pattern to extract tasks
            heading_level: For "headings" template, specify the heading level (e.g., 3 for ###)
            pattern: For "custom" template, provide a regex pattern with groups for task text and completion status
            section_filter: Only look at tasks under a specific section (e.g., "Implementation Checklist")
            
        Returns:
            A comparison summary showing which tasks exist in Asana but are missing in the document,
            and which checklist items exist in the document but are missing in Asana.
        """
        try:
            # First, get all tasks from the Asana project
            tasks_url = f"{BASE_URL}/projects/{project_gid}/tasks"
            tasks_response = requests.get(tasks_url, headers=HEADERS)
            tasks_response.raise_for_status()
            tasks_data = tasks_response.json()
            
            asana_tasks = []
            if 'data' in tasks_data:
                # For each task, get its details to access the name
                for task_ref in tasks_data['data']:
                    task_id = task_ref['gid']
                    task_url = f"{BASE_URL}/tasks/{task_id}"
                    task_response = requests.get(task_url, headers=HEADERS)
                    task_response.raise_for_status()
                    task_detail = task_response.json()
                    
                    if 'data' in task_detail:
                        asana_tasks.append({
                            'gid': task_id,
                            'name': task_detail['data'].get('name', ''),
                            'completed': task_detail['data'].get('completed', False)
                        })
            
            # Read the markdown file
            with open(markdown_file_path, 'r') as f:
                markdown_content = f.read()
            
            # If section_filter is provided, extract only that section
            if section_filter:
                import re
                section_pattern = re.compile(f'## {re.escape(section_filter)}.*?(?=^##|\Z)', re.MULTILINE | re.DOTALL)
                section_match = section_pattern.search(markdown_content)
                if section_match:
                    markdown_content = section_match.group(0)
                else:
                    return {"error": f"Section '{section_filter}' not found in markdown document"}
            
            # Extract checklist items based on the selected template
            checklist_items = self._extract_checklist_items(markdown_content, template, heading_level, pattern)
            
            if not checklist_items:
                return {"error": f"No checklist items found using template '{template}'. Check if the format matches or try a different template."}
            
            # Compare the two sets
            missing_in_asana = []
            missing_in_doc = []
            matches = []
            
            # Check which checklist items are missing in Asana
            for doc_item in checklist_items:
                found = False
                best_match = None
                best_similarity = 0
                
                for asana_task in asana_tasks:
                    # Calculate similarity between the two task names
                    similarity = self._calculate_similarity(doc_item['text'], asana_task['name'])
                    
                    # If similarity is above threshold, consider it a match
                    if similarity >= 0.5:
                        found = True
                        if similarity > best_similarity:
                            best_similarity = similarity
                            best_match = asana_task
                
                if found and best_match:
                    matches.append({
                        'doc_item': doc_item,
                        'asana_task': best_match,
                        'similarity': best_similarity
                    })
                else:
                    missing_in_asana.append(doc_item)
            
            # Check which Asana tasks are missing in the checklist
            # Use a set to track asana tasks that already matched
            matched_tasks = set(match['asana_task']['gid'] for match in matches)
            
            for asana_task in asana_tasks:
                if asana_task['gid'] in matched_tasks:
                    continue  # Skip tasks that already matched
                    
                found = False
                for doc_item in checklist_items:
                    # Calculate similarity
                    similarity = self._calculate_similarity(doc_item['text'], asana_task['name'])
                    
                    # If similarity is above threshold, consider it a match
                    if similarity >= 0.5:
                        found = True
                        break
                
                if not found:
                    missing_in_doc.append(asana_task)
            
            # Prepare the comparison summary
            return {
                "template_used": template,
                "asana_tasks_count": len(asana_tasks),
                "checklist_items_count": len(checklist_items),
                "missing_in_asana": missing_in_asana,
                "missing_in_doc": missing_in_doc,
                "matches": matches,
                "complete_in_asana": [task for task in asana_tasks if task['completed']],
                "incomplete_in_asana": [task for task in asana_tasks if not task['completed']],
                "checked_in_doc": [item for item in checklist_items if item['completed']],
                "unchecked_in_doc": [item for item in checklist_items if not item['completed']]
            }
        
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"Error processing comparison: {str(e)}"}
    
    def _extract_checklist_items(self, markdown_content, template, heading_level=None, pattern=None):
        """Extract checklist items from markdown based on the selected template"""
        import re
        checklist_items = []
        
        if template == "standard":
            # Standard format: "- [ ] Task description" or "- [x] Task description"
            checklist_pattern = re.compile(r'- \[([ x])\] (.+?)$', re.MULTILINE)
            
            for match in checklist_pattern.finditer(markdown_content):
                is_checked = match.group(1) == 'x'
                task_text = match.group(2).strip()
                checklist_items.append({
                    'text': task_text,
                    'completed': is_checked
                })
                
        elif template == "headings":
            # Extract tasks from headings (e.g., ### Task Name)
            if not heading_level:
                heading_level = 3  # Default to H3 (###)
                
            heading_prefix = '#' * heading_level
            heading_pattern = re.compile(f'{heading_prefix} (.+?)$', re.MULTILINE)
            
            for match in heading_pattern.finditer(markdown_content):
                task_text = match.group(1).strip()
                # For headings, we can't determine completion status automatically
                # We'll assume uncompleted unless there's explicit "DONE" or similar marker
                is_checked = any(marker in task_text.upper() for marker in ["DONE", "COMPLETED", "FINISHED", "✓", "✅"])
                checklist_items.append({
                    'text': task_text,
                    'completed': is_checked
                })
                
        elif template == "custom" and pattern:
            # Use a custom regex pattern with groups for task text and completion status
            custom_pattern = re.compile(pattern, re.MULTILINE)
            
            for match in custom_pattern.finditer(markdown_content):
                if len(match.groups()) >= 2:
                    # Assume first group is task text, second is completion status
                    task_text = match.group(1).strip()
                    status_text = match.group(2).strip().upper()
                    is_checked = any(marker in status_text for marker in ["DONE", "COMPLETED", "FINISHED", "YES", "Y", "TRUE", "✓", "✅"])
                    checklist_items.append({
                        'text': task_text,
                        'completed': is_checked
                    })
                elif len(match.groups()) == 1:
                    # If only one group, assume it's the task text and status is unknown
                    task_text = match.group(1).strip()
                    checklist_items.append({
                        'text': task_text,
                        'completed': False  # Default to not completed
                    })
                    
        else:
            # Fallback to standard format if template isn't recognized
            return self._extract_checklist_items(markdown_content, "standard")
            
        return checklist_items
    
    def _calculate_similarity(self, str1, str2):
        """Calculate similarity between two strings"""
        # Convert to lowercase for comparison
        s1 = str1.lower()
        s2 = str2.lower()
        
        # Check for containment (one string being a subset of the other)
        if s1 in s2:
            # If str1 is smaller and is contained within str2, it's highly similar
            return len(s1) / len(s2) if len(s2) > 0 else 0.0
        elif s2 in s1:
            # If str2 is smaller and is contained within str1, it's highly similar
            return len(s2) / len(s1) if len(s1) > 0 else 0.0
        
        # For more complex cases, use common words approach
        words1 = set(s1.split())
        words2 = set(s2.split())
        
        # Count common words
        common_words = words1.intersection(words2)
        
        # Calculate similarity based on common words
        total_words = len(words1.union(words2))
        return len(common_words) / total_words if total_words > 0 else 0.0