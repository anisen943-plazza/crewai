"""
Markdown to Asana Project Creator

This tool parses a markdown document and creates an Asana project with sections,
tasks, and subtasks based on the document's structure.
"""

import os
import re
from typing import List, Dict, Any, Optional, Tuple
import requests
from crewai.tools import BaseTool

# Asana API configuration
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

# Cache for the first workspace GID found
WORKSPACE_GID = os.getenv("ASANA_WORKSPACE_GID", "1208316653297247")  # Default to the GID provided
# Cache for the first team GID found
TEAM_GID = os.getenv("ASANA_TEAM_GID")

class MarkdownChecklistItem:
    """Represents a checklist item from a markdown document."""
    def __init__(self, text: str, completed: bool = False, level: int = 0, parent=None):
        self.text = text
        self.completed = completed
        self.level = level  # 0 = section, 1 = main task, 2 = subtask, etc.
        self.parent = parent
        self.children = []
        self.asana_gid = None  # Will be populated when created in Asana
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def to_dict(self):
        return {
            "text": self.text,
            "completed": self.completed,
            "level": self.level,
            "asana_gid": self.asana_gid,
            "children": [child.to_dict() for child in self.children]
        }

class MarkdownToAsanaTool(BaseTool):
    name: str = "MarkdownToAsanaTool"
    description: str = """
    Create an Asana project from a markdown document containing implementation checklists.
    
    The markdown document should follow a specific structure with headers (using #) for sections
    and checklist items formatted as:
    - [ ] Uncompleted task
    - [x] Completed task
    
    The tool will parse this structure and create a corresponding project in Asana with:
    - Sections (from major headers like "## Section Title")
    - Tasks (from subsection headers or top-level checklist items)
    - Subtasks (from nested checklist items)
    
    This allows for automated project setup from documentation.
    """
    
    def _run(self, 
             markdown_file_path: str, 
             project_name: str, 
             workspace_gid: Optional[str] = None, 
             team_gid: Optional[str] = None) -> str:
        """
        Create an Asana project from a markdown document with implementation checklist.
        
        Args:
            markdown_file_path: Path to the markdown file containing the implementation checklist
            project_name: Name of the Asana project to create
            workspace_gid: Optional workspace GID (uses default if not provided)
            team_gid: Optional team GID (uses default if not provided)
            
        Returns:
            A summary of the created project with statistics
        """
        global WORKSPACE_GID, TEAM_GID
        
        # Validate inputs
        if not os.path.exists(markdown_file_path):
            return {"error": f"Markdown file not found: {markdown_file_path}"}
        
        # If no workspace_gid provided and WORKSPACE_GID not set, try to get workspaces
        if not workspace_gid and not WORKSPACE_GID:
            workspaces_result = self._list_workspaces()
            if isinstance(workspaces_result, dict) and 'error' in workspaces_result:
                return workspaces_result
        
        # Use provided workspace_gid or default
        workspace = workspace_gid or WORKSPACE_GID
        
        if not workspace:
            return {"error": "No workspace GID provided and no default workspace found"}
        
        # If no team_gid provided and TEAM_GID not set, try to get teams
        if not team_gid and not TEAM_GID:
            try:
                teams_result = self._list_teams(workspace_gid=workspace)
                
                # If we still don't have a team, check if there's an error in the teams response
                if not TEAM_GID and isinstance(teams_result, dict) and 'error' in teams_result:
                    print(f"Team discovery failed: {teams_result['error']}")
                    print("Trying to use personal projects. If this fails, you'll need to provide a valid team_gid.")
                    # For personal projects, sometimes we can use the user as the "team"
                    users_result = self._list_users(workspace_gid=workspace)
                    if isinstance(users_result, dict) and 'data' in users_result and len(users_result['data']) > 0:
                        # Get the current user's GID (usually the first in the list)
                        TEAM_GID = users_result['data'][0]['gid']
                        print(f"Using user GID as fallback team: {TEAM_GID}")
            except Exception as e:
                return {"error": f"Error discovering teams: {e}"}
        
        # Use provided team_gid or default
        team = team_gid or TEAM_GID
        
        if not team:
            return {"error": "No team GID provided and no default team found. Asana requires a team when creating a project."}
        
        # 1. Parse the markdown file to extract sections, tasks, and subtasks
        checklist_items = self._parse_markdown_file(markdown_file_path)
        if isinstance(checklist_items, dict) and 'error' in checklist_items:
            return checklist_items
        
        # 2. Create a new project in Asana
        project_result = self._create_project(project_name, workspace, team)
        if isinstance(project_result, dict) and 'error' in project_result:
            return project_result
        
        project_gid = project_result['data']['gid']
        
        # 3. Create sections, tasks, and subtasks in the project
        creation_result = self._create_project_structure(project_gid, checklist_items)
        if isinstance(creation_result, dict) and 'error' in creation_result:
            return creation_result
        
        # Return statistics
        stats = self._get_creation_statistics(creation_result)
        return {
            "success": True,
            "project_gid": project_gid,
            "project_name": project_name,
            "project_url": f"https://app.asana.com/0/{project_gid}",
            "statistics": stats
        }
    
    def _list_workspaces(self):
        """List all workspaces accessible to the user in Asana"""
        global WORKSPACE_GID
        
        # Real API call
        url = f"{BASE_URL}/workspaces"
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            result = response.json()
            
            # Cache the first workspace GID if available
            if not WORKSPACE_GID and 'data' in result and len(result['data']) > 0:
                WORKSPACE_GID = result['data'][0]['gid']
                print(f"Set default workspace GID to {WORKSPACE_GID}")
            
            return result
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}
    
    def _list_teams(self, workspace_gid):
        """List all teams in an Asana workspace"""
        global TEAM_GID
        
        # Real API call to get teams
        url = f"{BASE_URL}/organizations/{workspace_gid}/teams"
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            result = response.json()
            
            # Store the first team GID as a global variable if available
            if 'data' in result and len(result['data']) > 0:
                TEAM_GID = result['data'][0]['gid']
                print(f"Set default team GID to {TEAM_GID}")
                
            return result
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}
    
    def _list_users(self, workspace_gid):
        """List all users in an Asana workspace"""
        # Real API call
        url = f"{BASE_URL}/users?workspace={workspace_gid}"
        try:
            response = requests.get(url, headers=HEADERS)
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
    
    def _create_project(self, name, workspace_gid, team_gid):
        """Create a new project in Asana"""
        try:
            url = f"{BASE_URL}/projects"
            data = {
                "data": {
                    "workspace": workspace_gid,
                    "name": name,
                    "notes": "Created from markdown implementation checklist",
                    "team": team_gid
                }
            }
            
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
    
    def _create_section(self, project_gid, section_name):
        """Create a section in an Asana project"""
        try:
            url = f"{BASE_URL}/projects/{project_gid}/sections"
            data = {
                "data": {
                    "name": section_name
                }
            }
            
            response = requests.post(url, headers=HEADERS, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error creating section: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}
    
    def _create_task(self, project_gid, section_gid, name, completed=False, notes=""):
        """Create a task in an Asana project"""
        try:
            url = f"{BASE_URL}/tasks"
            data = {
                "data": {
                    "name": name,
                    "completed": completed,
                    "notes": notes,
                    "projects": [project_gid]
                }
            }
            
            # Only include section if provided (it might be null for main tasks)
            if section_gid:
                data["data"]["section"] = section_gid
                
            response = requests.post(url, headers=HEADERS, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error creating task: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}
    
    def _create_subtask(self, parent_task_gid, name, completed=False, notes=""):
        """Create a subtask in Asana"""
        try:
            url = f"{BASE_URL}/tasks/{parent_task_gid}/subtasks"
            data = {
                "data": {
                    "name": name,
                    "completed": completed,
                    "notes": notes
                }
            }
            
            response = requests.post(url, headers=HEADERS, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                return {
                    "error": f"API error creating subtask: {e}",
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            else:
                return {"error": f"Request failed: {e}"}
    
    def _parse_markdown_file(self, file_path):
        """Parse a markdown file to extract sections, tasks, and subtasks"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Extract implementation checklist section
            implementation_checklist_pattern = re.compile(r'## Implementation Checklist\s*\n(.*?)(?:\n##|$)', re.DOTALL)
            match = implementation_checklist_pattern.search(content)
            
            if not match:
                # If not found, look for any checklist items
                print("Implementation Checklist section not found. Parsing the entire document for checklist items.")
                checklist_content = content
            else:
                checklist_content = match.group(1)
            
            # Process section by section
            sections = []
            current_section = None
            current_task = None
            
            # First, identify section headers (using ###)
            section_pattern = re.compile(r'###\s+(.*?)\s*\n', re.MULTILINE)
            section_matches = section_pattern.finditer(checklist_content)
            
            for section_match in section_matches:
                section_name = section_match.group(1).strip()
                section = MarkdownChecklistItem(section_name, level=0)
                sections.append(section)
                
                # Find the content of this section (until the next section or end)
                section_start = section_match.end()
                next_section = section_pattern.search(checklist_content, section_start)
                section_end = next_section.start() if next_section else len(checklist_content)
                section_content = checklist_content[section_start:section_end]
                
                # Process all checklist items in this section
                task_pattern = re.compile(r'(?:^|\n)(?:#{4}\s+(.*?)\s*\n|\s*- \[([ x])\]\s+(.*?)(?:\n|$))', re.MULTILINE)
                task_matches = task_pattern.finditer(section_content)
                
                for task_match in task_matches:
                    if task_match.group(1):  # H4 header (#### Subsection)
                        task_name = task_match.group(1).strip()
                        task = MarkdownChecklistItem(task_name, level=1)
                        section.add_child(task)
                        current_task = task
                    else:  # Checklist item (- [ ] Task)
                        is_completed = task_match.group(2) == 'x'
                        task_name = task_match.group(3).strip()
                        
                        if current_task:
                            # This is a subtask
                            subtask = MarkdownChecklistItem(task_name, is_completed, level=2)
                            current_task.add_child(subtask)
                        else:
                            # This is a main task under the section
                            task = MarkdownChecklistItem(task_name, is_completed, level=1)
                            section.add_child(task)
            
            # If we didn't find any sections, try to parse just the checklist items
            if not sections:
                # Look for any checklist items in the document
                checklist_pattern = re.compile(r'- \[([ x])\]\s+(.*?)(?:\n|$)', re.MULTILINE)
                checklist_matches = checklist_pattern.finditer(content)
                
                # Create a default section
                default_section = MarkdownChecklistItem("Tasks", level=0)
                sections.append(default_section)
                
                for match in checklist_matches:
                    is_completed = match.group(1) == 'x'
                    task_name = match.group(2).strip()
                    task = MarkdownChecklistItem(task_name, is_completed, level=1)
                    default_section.add_child(task)
            
            return sections
        except Exception as e:
            return {"error": f"Error parsing markdown file: {str(e)}"}
    
    def _create_project_structure(self, project_gid, checklist_items):
        """Create sections, tasks, and subtasks in the Asana project"""
        result = {
            "sections": [],
            "tasks": [],
            "subtasks": []
        }
        
        try:
            # Process each section
            for section_item in checklist_items:
                # Create section
                section_result = self._create_section(project_gid, section_item.text)
                if isinstance(section_result, dict) and 'error' in section_result:
                    return section_result
                
                section_gid = section_result['data']['gid']
                section_item.asana_gid = section_gid
                result["sections"].append({
                    "name": section_item.text,
                    "gid": section_gid
                })
                
                # Process each task in this section
                for task_item in section_item.children:
                    # Create task
                    task_result = self._create_task(
                        project_gid,
                        section_gid,
                        task_item.text,
                        task_item.completed
                    )
                    if isinstance(task_result, dict) and 'error' in task_result:
                        return task_result
                    
                    task_gid = task_result['data']['gid']
                    task_item.asana_gid = task_gid
                    result["tasks"].append({
                        "name": task_item.text,
                        "gid": task_gid,
                        "completed": task_item.completed,
                        "section_gid": section_gid
                    })
                    
                    # Process each subtask for this task
                    for subtask_item in task_item.children:
                        # Create subtask
                        subtask_result = self._create_subtask(
                            task_gid,
                            subtask_item.text,
                            subtask_item.completed
                        )
                        if isinstance(subtask_result, dict) and 'error' in subtask_result:
                            return subtask_result
                        
                        subtask_gid = subtask_result['data']['gid']
                        subtask_item.asana_gid = subtask_gid
                        result["subtasks"].append({
                            "name": subtask_item.text,
                            "gid": subtask_gid,
                            "completed": subtask_item.completed,
                            "parent_task_gid": task_gid
                        })
            
            return result
        except Exception as e:
            return {"error": f"Error creating project structure: {str(e)}"}
    
    def _get_creation_statistics(self, creation_result):
        """Get statistics about the created project items"""
        sections_count = len(creation_result["sections"])
        tasks_count = len(creation_result["tasks"])
        subtasks_count = len(creation_result["subtasks"])
        
        completed_tasks = sum(1 for task in creation_result["tasks"] if task["completed"])
        completed_subtasks = sum(1 for subtask in creation_result["subtasks"] if subtask["completed"])
        
        return {
            "sections_created": sections_count,
            "tasks_created": tasks_count,
            "subtasks_created": subtasks_count,
            "total_items": sections_count + tasks_count + subtasks_count,
            "completed_tasks": completed_tasks,
            "completed_subtasks": completed_subtasks,
            "completion_rate": f"{(completed_tasks + completed_subtasks) / (tasks_count + subtasks_count) * 100:.1f}%" if (tasks_count + subtasks_count) > 0 else "0%"
        }

class CreateTemplateMdFileTool(BaseTool):
    name: str = "CreateTemplateMdFileTool"
    description: str = """
    Create a template markdown file that can be used with the MarkdownToAsanaTool.
    
    This tool generates a sample markdown file with the correct structure for creating Asana projects.
    The template includes examples of section headers, subsection headers, and checklist items
    that will properly convert to Asana sections, tasks, and subtasks.
    """
    
    def _run(self, output_path: str, project_type: str = "generic") -> str:
        """
        Generate a template markdown file for creating Asana projects.
        
        Args:
            output_path: Path where the template should be saved
            project_type: Type of project template to generate (generic, software, marketing)
            
        Returns:
            Path to the created template file
        """
        try:
            # Create the template content based on the project type
            if project_type.lower() == "software":
                template_content = self._create_software_project_template()
            elif project_type.lower() == "marketing":
                template_content = self._create_marketing_project_template()
            else:
                template_content = self._create_generic_project_template()
            
            # Ensure the directory exists
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            
            # Write the template to the output file
            with open(output_path, 'w') as f:
                f.write(template_content)
            
            return {
                "success": True,
                "file_path": output_path,
                "project_type": project_type,
                "message": f"Created {project_type} project template at {output_path}"
            }
        except Exception as e:
            return {
                "error": f"Failed to create template file: {str(e)}"
            }
    
    def _create_generic_project_template(self):
        """Create a generic project template"""
        return """# Project Implementation Checklist

## Project Overview
This is a template for creating Asana projects from markdown files.

## Implementation Checklist

### Planning Phase
- [ ] Define project scope
- [ ] Identify key stakeholders
- [ ] Set project timelines
- [ ] Establish success metrics

### Development Phase
- [ ] Create initial specifications
- [ ] Develop prototypes
- [ ] Conduct internal reviews
- [ ] Implement feedback

### Testing Phase
- [ ] Create test plans
- [ ] Execute unit tests
- [ ] Perform integration testing
- [ ] Conduct user acceptance testing

### Deployment Phase
- [ ] Prepare deployment plan
- [ ] Create backup strategy
- [ ] Execute deployment
- [ ] Monitor post-deployment

### Review Phase
- [ ] Collect user feedback
- [ ] Analyze performance metrics
- [ ] Document lessons learned
- [ ] Plan next iterations
"""
    
    def _create_software_project_template(self):
        """Create a software development project template"""
        return """# Software Project Implementation Checklist

## Project Overview
This template is designed for software development projects and includes standard phases and tasks.

## Implementation Checklist

### Project Setup
- [ ] Create project repository
- [ ] Set up development environment
- [ ] Configure version control
- [ ] Establish coding standards
- [ ] Install necessary tools and dependencies

### Design Phase
- [ ] Create architecture diagram
- [ ] Design database schema
- [ ] Define API endpoints
- [ ] Create wireframes
- [ ] Document technical requirements

### Development Phase
#### Backend Development
- [ ] Implement data models
- [ ] Create database migrations
- [ ] Develop API endpoints
- [ ] Implement business logic
- [ ] Set up authentication

#### Frontend Development
- [ ] Set up UI framework
- [ ] Implement component structure
- [ ] Develop user interface
- [ ] Connect to API endpoints
- [ ] Implement state management

### Testing Phase
- [ ] Create unit tests
- [ ] Implement integration tests
- [ ] Perform end-to-end testing
- [ ] Conduct usability testing
- [ ] Execute performance testing

### Deployment Phase
- [ ] Set up CI/CD pipeline
- [ ] Configure staging environment
- [ ] Perform load testing
- [ ] Create production environment
- [ ] Execute deployment strategy

### Documentation
- [ ] Write API documentation
- [ ] Create user guides
- [ ] Document deployment process
- [ ] Prepare maintenance documentation
- [ ] Create system architecture diagrams
"""
    
    def _create_marketing_project_template(self):
        """Create a marketing project template"""
        return """# Marketing Campaign Implementation Checklist

## Project Overview
This template is designed for marketing campaign projects and includes standard phases and tasks.

## Implementation Checklist

### Campaign Planning
- [ ] Define campaign goals and KPIs
- [ ] Identify target audience
- [ ] Determine budget allocation
- [ ] Create campaign timeline
- [ ] Establish success metrics

### Content Creation
#### Written Content
- [ ] Develop key messaging
- [ ] Create blog posts
- [ ] Draft social media copy
- [ ] Write email campaigns
- [ ] Prepare press releases

#### Visual Content
- [ ] Design campaign graphics
- [ ] Create social media images
- [ ] Develop video storyboards
- [ ] Produce campaign videos
- [ ] Create downloadable resources

### Channel Setup
- [ ] Configure social media accounts
- [ ] Set up email marketing platform
- [ ] Prepare advertising platforms
- [ ] Set up tracking and analytics
- [ ] Configure landing pages

### Campaign Execution
- [ ] Launch social media campaigns
- [ ] Deploy email sequences
- [ ] Activate paid advertising
- [ ] Publish blog content
- [ ] Release press announcements

### Monitoring & Optimization
- [ ] Track campaign metrics
- [ ] Analyze performance data
- [ ] Adjust targeting parameters
- [ ] Optimize content based on results
- [ ] Reallocate budget as needed

### Reporting & Analysis
- [ ] Compile campaign results
- [ ] Compare results to KPIs
- [ ] Document lessons learned
- [ ] Create presentation for stakeholders
- [ ] Plan follow-up campaigns
"""


# Example usage:
# markdown_to_asana = MarkdownToAsanaTool()
# result = markdown_to_asana._run(
#     markdown_file_path="/path/to/implementation-checklist.md",
#     project_name="New Project from Markdown",
#     workspace_gid="123456789",
#     team_gid="987654321"
# )
# print(result)