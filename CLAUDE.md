# CrewAI Project Documentation

## AI Agent Guide to Asana Manager Tools (April 2024)

This guide is designed for AI agents working with the CrewAI Asana Manager tools, providing detailed instructions on how to effectively use the various tools for Asana project management and documentation integration.

### Quick Start for AI Agents: One Command to Rule Them All

For AI agents, the easiest way to use the Asana Manager tools is through the main menu system. This single command provides access to all tools:

```bash
# Step 1: Activate the virtual environment
source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate

# Step 2: Change to the project directory
cd /Users/aniruddhasen/Projects/CrewAI/asana_manager

# Step 3: Run the main menu
python -m src.asana_manager.main
```

Then select the appropriate option (1-8) from the menu for your task. This is the recommended approach for most interactions with the Asana Manager.

For more detailed instructions, specific tool usage, or advanced operations, see the relevant sections below.

### ⚠️ IMPORTANT: Virtual Environment Setup ⚠️

**Before using ANY tool or command in this guide, you MUST first activate the virtual environment:**

```bash
# REQUIRED FIRST STEP: Activate the virtual environment
source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate
```

Without activating the virtual environment first, you will encounter errors like:
```
ModuleNotFoundError: No module named 'crewai'
```

All commands in this guide assume you have already activated the virtual environment. The virtual environment contains all necessary dependencies including CrewAI, Python-dotenv, PyYAML, and the Asana API libraries.

### Key Prerequisites Checklist

Before attempting to use any tools:

1. ✅ **ALWAYS activate the virtual environment first**:
   ```bash
   source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate
   ```

2. ✅ **Verify Asana API token is available**:
   ```bash
   echo $ASANA_API_TOKEN
   # Should display your token
   ```

3. ✅ **Run all commands from the project root directory**:
   ```bash
   cd /Users/aniruddhasen/Projects/CrewAI/asana_manager
   ```

Skip any of these steps and the tools will not work!

### Overview of Asana Manager Tools

The Asana Manager project provides a comprehensive suite of tools to bridge the gap between documentation and Asana project management. These tools enable:

1. **Project Creation from Markdown**: Generate complete Asana projects directly from structured markdown documents
2. **Project Comparison**: Compare existing Asana projects with documentation to identify misalignment
3. **Two-Way Synchronization**: Keep Asana projects and documentation in sync
4. **Template Generation**: Create markdown templates as starting points for project documentation
5. **Flexible Format Support**: Work with various markdown formats through template specifications

### Tool Selection Guide

Choose the appropriate tool based on your task:

| Task | Tool to Use | Key Features |
|------|-------------|-------------|
| Create a project from markdown | `MarkdownToAsanaTool` or standalone script | Hierarchical task creation, automatic section handling |
| Compare project vs. documentation | `CompareTasksWithDocumentationTool` or standalone script | Using project GID for direct access, smart task matching, various template formats |
| Generate project template | `CreateTemplateMdFileTool` or standalone script | Different project types (generic, software, marketing) |
| Find projects by name | `FindProjectByNameTool` or `find_project.py` | Fuzzy matching across workspaces |
| Browse project details | `BrowseProjectTool` or `browse_project.py` | View sections, tasks, and project information |
| List available workspaces | `ListWorkspacesTool` or `list_workspaces_and_teams.py` | Automatic discovery and caching |
| Task management | `CreateTaskTool`, `AssignTaskTool`, `SetDueDateTool` | Core Asana operations |
| List all projects | `list_projects.py` or main.py option 3 | Shows all projects across all workspaces |

### Markdown Format Templates and Document Preparation

The comparison tool supports three markdown format templates for maximum flexibility. Proper document preparation is crucial for effective comparison.

#### 1. Standard Format (default)
```markdown
## Section Name
- [ ] Uncompleted task
- [x] Completed task
```

#### 2. Headings Format
```markdown
## Section Name
### Task 1
### Task 2 (COMPLETED)
#### Subtask 1
```

#### 3. Custom Format (with regex pattern)
```markdown
Task: Do something | Status: Incomplete
Task: Another thing | Status: Complete
```

#### Document Preparation Guidelines

For optimal task matching between Asana and markdown, follow these guidelines:

1. **Choose the Right Template**: 
   - **Standard Format**: Best for GitHub-style task lists with checkboxes
   - **Headings Format**: Ideal for hierarchical documents with heading levels
   - **Custom Format**: For custom notation or specialized formats

2. **Structure Your Document**:
   - Use clear section headings with `##` (level 2 headings)
   - Group related tasks under appropriate sections
   - Use consistent terminology between Asana tasks and markdown
   - Keep task descriptions concise and focused

3. **Section Filtering**: 
   - Organize tasks under a dedicated section like `## Implementation Checklist`
   - Use the `--section` parameter to focus only on relevant parts
   - Sections are identified by `##` level headings (not `###` or `####`)

4. **Example Well-Structured Document**:
```markdown
# Project Documentation

## Overview
(Project overview text here)

## Implementation Checklist
This section contains tasks to be completed.

- [ ] Configure user authentication
- [ ] Implement dashboard UI
- [ ] Create database schema
- [x] Set up CI/CD pipeline
- [ ] Write test cases

## Timeline
(Timeline information here)
```

Use this with: `--section "Implementation Checklist"`

5. **Task Matching Optimization**:
   - Use identical or very similar wording between Asana and markdown
   - Be consistent with capitalization and terminology
   - Include key identifiers or IDs in both systems
   - Add task context for better similarity matching
   - Adjust similarity threshold with `--similarity` parameter (default: 0.5)

6. **Troubleshooting Tips**:
   - If tasks aren't matching: Check for wording differences
   - If no tasks found: Verify template format matches document structure
   - If multiple matches for one task: Make task descriptions more specific
   - If section not found: Check heading level (must be `##`)
   - Use `--verbose` flag to see detailed matching information

#### Advanced Topics and Limitations

1. **Subtask Handling and Visibility**:
   - **Current Limitation**: The `compare_project.py` and `browse_project.py` tools only work with top-level tasks by default
   - **Missing Feature**: There is currently no parameter or flag to display subtasks in the standard output
   - **Technical Reason**: The Asana API separates subtasks from their parent tasks, requiring additional API calls to fetch them
   - **Manual Solution**: Add a `--show-subtasks` parameter to browse_project.py (implementation instructions below)
   - **Hierarchical Fix**: For proper subtask integration, modify both comparison and browsing tools to make additional API calls

   **Adding Subtask Support to browse_project.py**:
   ```python
   # Add to browse_project.py argument parser:
   parser.add_argument(
       "--show-subtasks",
       action="store_true",
       help="Include subtasks in the output"
   )
   
   # Add after retrieving each task (around line 146):
   if args.show_subtasks:
       print(f"   Subtasks:")
       subtask_url = f"{BASE_URL}/tasks/{task['gid']}/subtasks"
       try:
           subtask_response = requests.get(subtask_url, headers=HEADERS)
           subtask_response.raise_for_status()
           subtasks = subtask_response.json().get('data', [])
           
           if subtasks:
               for i, subtask in enumerate(subtasks, 1):
                   subtask_status = "✅" if subtask.get("completed", False) else "⬜"
                   print(f"   {i}. {subtask_status} {subtask['name']} (GID: {subtask['gid']})")
           else:
               print("   No subtasks found")
       except Exception as e:
           print(f"   Error retrieving subtasks: {e}")
   ```

2. **Direct Subtask Access via API**:
   ```bash
   # First get the parent task GID
   python -m src.asana_manager.main
   # Select option 5 (Browse project) to find task GIDs
   
   # Then use Asana API directly to get subtasks
   curl -H "Authorization: Bearer $ASANA_API_TOKEN" \
        https://app.asana.com/api/1.0/tasks/[TASK_GID]/subtasks
   
   # For detailed information about a specific subtask
   curl -H "Authorization: Bearer $ASANA_API_TOKEN" \
        https://app.asana.com/api/1.0/tasks/[SUBTASK_GID]
   ```

3. **Section Extraction Clarification**:
   - **Why Section Filtering May Fail**: Section filtering uses regex patterns that depend on specific markdown structures
   - **Common Issues**:
     1. **Inconsistent Heading Levels**: Make sure your section uses the exact heading level specified in `--heading-level`
     2. **Extra Whitespace**: Extra lines or spaces can break pattern matching
     3. **Special Characters**: Some special characters may interfere with regex patterns
     4. **Missing Boundary Markers**: Sections need clear boundaries (either a new section or end of file)
   
   **Debugging Section Extraction**:
   ```bash
   # Analyze markdown structure with this command
   python -c "import re; f=open('your_document.md', 'r'); content=f.read(); print(re.findall(r'#{3} (.*?)$', content, re.MULTILINE))"
   
   # Test section extraction with different heading levels
   python compare_project.py --project-gid "1234567890" "your_document.md" --template headings --heading-level 2
   python compare_project.py --project-gid "1234567890" "your_document.md" --template headings --heading-level 3
   ```

4. **Hierarchical Comparison Details**:
   - **Structural Mismatch**: Asana's hierarchy (workspace→project→section→task→subtask) doesn't perfectly match markdown's structure
   - **Document Preparation Solutions**:
     1. **Depth-First Structure**: Create a document that fully represents hierarchy by indentation level
     ```markdown
     ## Project Name
     ### Section One
     - [ ] Parent Task A
         - [ ] Subtask A1
             - [ ] Sub-subtask A1.1
         - [ ] Subtask A2
     - [ ] Parent Task B
     
     ### Section Two
     - [ ] Parent Task C
     ```
     
     2. **Multi-Stage Comparison**: Compare at each hierarchy level separately
     ```bash
     # First compare top-level structure
     python compare_project.py --project-gid "1234567890" "overview.md" --template headings
     
     # Then compare specific sections
     python compare_project.py --project-gid "1234567890" "section_one_details.md" --section-filter "Section One"
     
     # Finally compare specific tasks and subtasks
     python compare_project.py --project-gid "1234567890" "task_a_details.md" --task-filter "Parent Task A"
     ```
     
     3. **Custom Task-Subtask Matching**: Implement a custom script for hierarchical comparison
     ```python
     # Sample code to recursively match tasks and subtasks
     def compare_with_hierarchy(project_gid, markdown_file):
         # Get all tasks with their subtasks
         all_tasks = get_project_tasks_with_subtasks(project_gid)
         
         # Parse markdown with hierarchical structure
         md_items = parse_markdown_with_hierarchy(markdown_file)
         
         # Perform hierarchical matching
         matches = match_hierarchical_items(all_tasks, md_items)
         
         return matches
     ```

5. **Fixing Structure Mismatches**:
   - **Enhanced API Integration**: Implement a specialized hierarchical comparison tool
   ```bash
   # Create a new script for hierarchical comparison
   python compare_hierarchical.py --project-gid "1234567890" "your_document.md" --recursion-depth 3
   ```
   
   - **Document Structure Standardization**: Enforce consistent document structure with templates
   ```bash
   # Generate a hierarchical template
   python create_project_from_markdown.py --create-template --template-output hierarchical_template.md --template-type hierarchical
   ```
   
   - **Asana-Markdown Bridge**: Create a bidirectional sync tool to keep structures aligned
   ```bash
   # Sync from Asana to markdown (keeping hierarchy)
   python sync_asana_to_markdown.py --project-gid "1234567890" --output hierarchical_doc.md --preserve-hierarchy
   ```

6. **Non-Interactive Usage of main.py**:
   When running main.py in scripts or non-interactive environments, the `input()` function can cause an EOF error. To work around this:
   ```bash
   # Provide input via echo and pipe
   echo "5" | python -m src.asana_manager.main
   
   # Or use expect script for more complex interactions
   pip install pexpect
   python -c 'import pexpect; p=pexpect.spawn("python -m src.asana_manager.main"); p.expect("Enter task number"); p.sendline("5"); p.interact()'
   
   # Best practice: Use standalone scripts directly instead
   # Example: Instead of selecting menu option 4
   python find_project.py --project-name "Project Name"
   ```

### Running the Tools

#### As CrewAI Tools

Use these tools directly in your CrewAI agent workflows:

```python
from src.asana_manager.tools.asana_tools import CompareTasksWithDocumentationTool
from src.asana_manager.tools.markdown_to_asana import MarkdownToAsanaTool, CreateTemplateMdFileTool

# Initialize the tools
comparison_tool = CompareTasksWithDocumentationTool()
markdown_to_asana = MarkdownToAsanaTool()
template_creator = CreateTemplateMdFileTool()

# Example: Compare project with documentation (with template options)
result = comparison_tool._run(
    project_gid="1234567890",
    markdown_file_path="/path/to/documentation.md",
    template="headings",
    heading_level=3,
    section_filter="Implementation Checklist"
)

# Example: Create project from markdown
project = markdown_to_asana._run(
    markdown_file_path="/path/to/project.md",
    project_name="New Project from Documentation"
)

# Example: Generate template markdown file
template = template_creator._run(
    output_path="/path/to/output.md",
    project_type="software"  # options: generic, software, marketing
)
```

#### As Standalone Scripts

For direct command-line usage:

```bash
# Create project from markdown
python create_project_from_markdown.py --create-project --markdown-file project.md --project-name "New Project"

# Create template file
python create_project_from_markdown.py --create-template --template-output template.md --template-type software

# Compare project using project GID (recommended method)
python compare_project.py --project-gid "1234567890123456" documentation.md

# Compare using headings format with project GID
python compare_project.py --project-gid "1234567890123456" documentation.md --template headings --heading-level 3

# Compare using custom format with project GID
python compare_project.py --project-gid "1234567890123456" documentation.md --template custom --pattern "Task: (.+?) \| Status: (.+?)$"

# Only compare a specific section with project GID
python compare_project.py --project-gid "1234567890123456" documentation.md --section "Implementation Checklist"

# Generate JSON for missing tasks with project GID
python compare_project.py --project-gid "1234567890123456" documentation.md --generate-json

# Add missing tasks to Asana with project GID
python compare_project.py --project-gid "1234567890123456" documentation.md --update-asana

# Alternative using project name (slower, searches across workspaces)
python compare_project.py --project-name "Project Name" documentation.md
```

### Advanced Configuration

#### Environment Variables Setup

The tools use environment variables for API configuration:

```
ASANA_API_TOKEN=your_personal_access_token
ASANA_WORKSPACE_GID=optional_default_workspace_id
ASANA_TEAM_GID=optional_default_team_id
```

These can be stored in either:
1. `/Users/aniruddhasen/Projects/Master_ENV/.env` (preferred)
2. Local `.env` file in the project directory
3. System environment variables

#### Template Creation Recommendations

For optimal results when creating templates:

1. **For Section-Based Projects**: Use H2 (`##`) for sections and H3 (`###`) for subsections
2. **For Timeline-Based Projects**: Include explicit phase names in section headers
3. **For Task Dependencies**: Create a clear hierarchy with proper heading levels
4. **For Multiple Assignees**: Indicate ownership in task descriptions

#### Template Locations

Default templates are available at:
- `/Users/aniruddhasen/Projects/CrewAI/asana_manager/templates/generic.md`
- `/Users/aniruddhasen/Projects/CrewAI/asana_manager/templates/software.md`
- `/Users/aniruddhasen/Projects/CrewAI/asana_manager/templates/marketing.md`

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| No workspaces found | Check API token validity and permissions |
| No teams found | Some personal Asana accounts may not have teams; system will use personal projects |
| Template parsing errors | Validate markdown format against expected template |
| No tasks extracted | Try different template format or check section names |
| Low similarity matches | Adjust similarity threshold with `--similarity 0.6` |
| KeyError accessing API data | The Asana API uses a nested structure with 'data' keys. Use `.get("data", default)` when accessing data |
| Project/Task not found | Verify the GID is correct using `list_projects.py` or main.py option 3 |
| API structure changes | Use the debug output in tools to see the actual data structure returned |
| Main menu import error | Make sure you're running `python -m src.asana_manager.main` from the asana_manager directory |
| Option 5 (Browse Project) KeyError | This is fixed in the latest version. If you encounter it, update your code |
| Input validation errors | Make sure to provide valid GIDs when prompted by main.py options |

### Asana API Response Format

Understanding the Asana API response structure is critical when working with these tools:

1. **Nested Data Structure**: The Asana API wraps most responses in a `data` field:
   ```json
   {
     "data": {
       "gid": "1234567890",
       "name": "Project Name",
       "notes": "Project Description"
     }
   }
   ```

2. **Collections as Arrays**: Lists of items are arrays inside the `data` field:
   ```json
   {
     "data": [
       { "gid": "1111", "name": "Item 1" },
       { "gid": "2222", "name": "Item 2" }
     ]
   }
   ```

3. **Nested Objects**: Some fields like `assignee` are nested objects:
   ```json
   {
     "assignee": {
       "gid": "3456789",
       "name": "User Name"
     }
   }
   ```

All tools in this repository have been updated to handle this structure, but you should be aware of it when processing results.

### Implementation Details for AI Integration

For agents needing deeper integration with the tools:

1. **Workspace and Team Discovery**: The tools automatically discover and cache workspace/team GIDs
2. **Smart Task Matching**: Uses a combination of substring containment and word overlap algorithms
3. **Hierarchical Parsing**: Creates proper parent-child relationships between tasks and subtasks
4. **Error Resilience**: Implements comprehensive fallbacks for API and parsing errors
5. **Format Flexibility**: Adapts to different markdown structures with pluggable templates
6. **API Response Handling**: All tools properly handle Asana's nested data structure

By using these tools effectively, AI agents can bridge documentation and project management seamlessly, ensuring alignment between project plans and execution.

### Detailed Tool Usage Instructions

#### Environment Variables

After activating the virtual environment (which is a required first step), check that your Asana API token is properly set:

```bash
# Check if Asana API token is set
echo $ASANA_API_TOKEN

# If not set, set it temporarily
# export ASANA_API_TOKEN="your_personal_access_token"
```

The tools will automatically use this environment variable for API authentication.

#### FindProjectByNameTool: Detailed Usage

This tool finds projects by name across all your Asana workspaces.

```python
from src.asana_manager.tools.asana_tools import FindProjectByNameTool

# Create the tool instance
find_project_tool = FindProjectByNameTool()

# Find projects matching a name (case-insensitive, partial matches work)
result = find_project_tool._run(
    project_name="Marketing Campaign",  # Required: The name to search for
    workspace_gid=None  # Optional: Specific workspace to search in
)

# Process the results
if "matching_projects" in result:
    projects = result["matching_projects"]
    print(f"Found {len(projects)} matching projects:")
    for i, project in enumerate(projects):
        print(f"{i+1}. {project['name']} (GID: {project['gid']})")
        
        # If you need a specific project GID for other operations
        project_gid = projects[0]["gid"]
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

#### ListWorkspacesTool: Detailed Usage

Get all workspaces accessible to your Asana account.

```python
from src.asana_manager.tools.asana_tools import ListWorkspacesTool

# Create the tool instance
workspaces_tool = ListWorkspacesTool()

# List all accessible workspaces
result = workspaces_tool._run()

# Process the results
if "data" in result:
    workspaces = result["data"]
    print(f"Found {len(workspaces)} workspaces:")
    for i, workspace in enumerate(workspaces):
        print(f"{i+1}. {workspace['name']} (GID: {workspace['gid']})")
        
        # Remember the first workspace GID for other operations
        if i == 0:
            first_workspace_gid = workspace["gid"]
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

#### ListTeamsTool: Detailed Usage

Get all teams in a workspace.

```python
from src.asana_manager.tools.asana_tools import ListTeamsTool

# Create the tool instance
teams_tool = ListTeamsTool()

# List teams in a workspace
result = teams_tool._run(
    workspace_gid="1234567890"  # Optional: Uses default if not provided
)

# Process the results
if "data" in result:
    teams = result["data"]
    print(f"Found {len(teams)} teams:")
    for i, team in enumerate(teams):
        print(f"{i+1}. {team['name']} (GID: {team['gid']})")
        
        # Remember the first team GID for project creation
        if i == 0:
            first_team_gid = team["gid"]
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

#### CreateProjectTool: Detailed Usage

Create a new project in Asana.

```python
from src.asana_manager.tools.asana_tools import CreateProjectTool

# Create the tool instance
create_project_tool = CreateProjectTool()

# Create a new project
result = create_project_tool._run(
    name="New Project",  # Required: Project name
    notes="Project created via API",  # Optional: Project description
    workspace_gid=None,  # Optional: Uses default if not provided
    team_gid=None  # Optional: Uses default if not provided
)

# Process the results
if "data" in result:
    project = result["data"]
    print(f"Created project: {project['name']} (GID: {project['gid']})")
    
    # Remember the project GID for adding tasks
    project_gid = project["gid"]
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

#### CreateTaskTool: Detailed Usage

Add a task to an existing project.

```python
from src.asana_manager.tools.asana_tools import CreateTaskTool

# Create the tool instance
create_task_tool = CreateTaskTool()

# Add a task to a project
result = create_task_tool._run(
    project_gid="1234567890",  # Required: Project GID
    name="Implement feature X",  # Required: Task name
    notes="This is a high priority task",  # Optional: Task description
    assignee=None  # Optional: User GID to assign task
)

# Process the results
if "data" in result:
    task = result["data"]
    print(f"Created task: {task['name']} (GID: {task['gid']})")
    
    # Remember the task GID for subtasks or setting due dates
    task_gid = task["gid"]
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

#### AssignTaskTool: Detailed Usage

Assign a task to a user.

```python
from src.asana_manager.tools.asana_tools import AssignTaskTool, ListUsersTool

# First, get users to find the assignee
users_tool = ListUsersTool()
users_result = users_tool._run(workspace_gid="1234567890")

# Find the user to assign to
user_gid = None
if "data" in users_result:
    for user in users_result["data"]:
        if "John Doe" in user["name"]:
            user_gid = user["gid"]
            break

# Now assign the task
if user_gid:
    assign_tool = AssignTaskTool()
    result = assign_tool._run(
        task_gid="1234567890",  # Required: Task GID
        assignee=user_gid  # Required: User GID
    )
    
    # Process the results
    if "data" in result:
        print(f"Task assigned successfully to user {user_gid}")
    else:
        print(f"Error: {result.get('error', 'Unknown error')}")
```

#### SetDueDateTool: Detailed Usage

Set a due date for a task.

```python
from src.asana_manager.tools.asana_tools import SetDueDateTool
import datetime

# Create the tool instance
due_date_tool = SetDueDateTool()

# Calculate due date (2 weeks from now)
today = datetime.datetime.now()
due_date = today + datetime.timedelta(days=14)
due_date_str = due_date.strftime("%Y-%m-%d")

# Set the due date
result = due_date_tool._run(
    task_gid="1234567890",  # Required: Task GID
    due_date=due_date_str  # Required: Due date in YYYY-MM-DD format
)

# Process the results
if "data" in result:
    task = result["data"]
    print(f"Set due date for task '{task['name']}' to {task['due_on']}")
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

#### BrowseProjectTool: Detailed Usage

View complete project details including sections and tasks.

```python
from src.asana_manager.tools.asana_tools import BrowseProjectTool

# Create the tool instance
browse_tool = BrowseProjectTool()

# Get project details, sections, and tasks
result = browse_tool._run(
    project_gid="1234567890"  # Required: Project GID
)

# Process the results (with proper handling of Asana API response structure)
if "project" in result and "tasks" in result:
    # Handle nested 'data' field in Asana API responses
    project = result["project"].get("data", result["project"])
    sections = result["sections"].get("data", [])
    tasks = result["tasks"].get("data", [])
    
    print(f"Project: {project['name']}")
    print(f"Description: {project.get('notes', 'No description')}")
    print(f"Tasks ({len(tasks)}):")
    
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']} (GID: {task['gid']})")
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

#### CompareTasksWithDocumentationTool: Detailed Usage

This powerful tool compares tasks in an Asana project with items in a markdown document.

```python
from src.asana_manager.tools.asana_tools import CompareTasksWithDocumentationTool

# Create the tool instance
comparison_tool = CompareTasksWithDocumentationTool()

# Compare project with documentation (multiple template options)
result = comparison_tool._run(
    project_gid="1234567890",  # Required: Project GID (recommended method for direct access)
    markdown_file_path="/path/to/doc.md",  # Required: Path to markdown file
    template="standard",  # Optional: "standard", "headings", or "custom"
    heading_level=3,  # Optional: For "headings" template, which level to use
    pattern=r"Task: (.+?) \| Status: (.+?)$",  # Optional: For "custom" template
    section_filter="Implementation Checklist"  # Optional: Only look at specific section
)

# Process the results - this has many properties
if "error" not in result:
    # Statistics
    print(f"Asana tasks: {result['asana_tasks_count']}")
    print(f"Document items: {result['checklist_items_count']}")
    
    # Missing items
    print(f"\nMissing in Asana ({len(result['missing_in_asana'])}):")
    for item in result['missing_in_asana']:
        print(f"- {item['text']} (Completed: {item['completed']})")
    
    print(f"\nMissing in documentation ({len(result['missing_in_doc'])}):")
    for task in result['missing_in_doc']:
        print(f"- {task['name']} (Completed: {task['completed']})")
    
    # Matching items
    print(f"\nMatches ({len(result['matches'])}):")
    for match in result['matches']:
        print(f"- Asana: '{match['asana_task']['name']}' ↔ Doc: '{match['doc_item']['text']}'")
        print(f"  Similarity: {match['similarity']:.2f}")
else:
    print(f"Error: {result['error']}")
```

#### MarkdownToAsanaTool: Detailed Usage

This tool creates an Asana project from a markdown file with sections and tasks.

```python
from src.asana_manager.tools.markdown_to_asana import MarkdownToAsanaTool

# Create the tool instance
md_to_asana_tool = MarkdownToAsanaTool()

# Create project from markdown
result = md_to_asana_tool._run(
    markdown_file_path="/path/to/project.md",  # Required: Markdown file path
    project_name="Project from Documentation",  # Required: Name for the new project
    workspace_gid=None,  # Optional: Uses default if not provided
    team_gid=None  # Optional: Uses default if not provided
)

# Process the results
if "success" in result and result["success"]:
    print(f"Created project: {result['project_name']}")
    print(f"Project URL: {result['project_url']}")
    print("\nStatistics:")
    for key, value in result["statistics"].items():
        print(f"- {key.replace('_', ' ').title()}: {value}")
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

#### CreateTemplateMdFileTool: Detailed Usage

This tool generates template markdown files for Asana projects.

```python
from src.asana_manager.tools.markdown_to_asana import CreateTemplateMdFileTool

# Create the tool instance
template_tool = CreateTemplateMdFileTool()

# Generate template file
result = template_tool._run(
    output_path="/path/to/output.md",  # Required: Where to save template
    project_type="software"  # Optional: "generic", "software", or "marketing"
)

# Process the results
if "success" in result and result["success"]:
    print(f"Created template at: {result['file_path']}")
    print(f"Project type: {result['project_type']}")
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

### Error Handling and Debugging Tips

When using these tools, here are some common errors and solutions:

1. **ModuleNotFoundError: No module named 'crewai'**:
   ```
   ModuleNotFoundError: No module named 'crewai'
   ```
   **Solution**: You forgot to activate the virtual environment! This is the most common error.
   ```bash
   source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate
   ```
   ALWAYS run this command first before ANY operation with these tools.

2. **API Token Errors**:
   ```
   {"errors":[{"message":"Not Authorized"}]}
   ```
   **Solution**: Your Asana API token is not set or is invalid:
   ```bash
   # Check if token is set
   echo $ASANA_API_TOKEN
   
   # Set it if needed
   export ASANA_API_TOKEN="your_personal_access_token"
   ```

3. **Project/Workspace Not Found**:
   ```
   {"errors":[{"message":"project: Unknown object"}]}
   ```
   **Solution**: Verify the GID exists and you have access to it. Use `list_projects.py` to see available projects.

4. **Path Errors**:
   ```
   FileNotFoundError: [Errno 2] No such file or directory
   ```
   **Solution**: Make sure you're in the correct directory. Change to the project root:
   ```bash
   cd /Users/aniruddhasen/Projects/CrewAI/asana_manager
   ```

5. **Import Errors in Your Own Scripts**:
   ```
   ImportError: attempted relative import with no known parent package
   ```
   **Solution**: Include the proper Python path in your scripts:
   ```python
   import sys
   from pathlib import Path
   sys.path.append(str(Path(__file__).parent.parent))
   ```

#### ListAllProjectsTool: Detailed Usage

This tool lists all projects across all your Asana workspaces with a single command.

```python
from src.asana_manager.tools.list_all_projects import ListAllProjectsTool

# Create the tool instance
list_tool = ListAllProjectsTool()

# List all projects across all workspaces
result = list_tool.run()

# Optionally, specify a workspace and output format
result = list_tool.run(
    workspace_gid="1234567890",  # Optional: Only list projects in this workspace
    output_format="json"  # Optional: "text" (default) or "json"
)

# If using json format, you can process the results programmatically
if result.get("format") == "json":
    workspaces = result.get("workspaces", [])
    for workspace in workspaces:
        print(f"Workspace: {workspace['name']}")
        for project in workspace.get('projects', []):
            print(f"  - {project['name']} (GID: {project['gid']})")
```

#### ListAllProjectsTool: Standalone Usage

The standalone script provides a simple command-line interface to list all Asana projects.

```bash
# REQUIRED FIRST STEP: Activate the virtual environment
source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate

# List all projects across all workspaces
python list_projects.py

# List projects in a specific workspace
python list_projects.py --workspace 1234567890

# Get JSON output
python list_projects.py --format json
```

#### FindProjectByNameTool: Standalone Usage

The standalone script provides a simple command-line interface to find Asana projects by name.

```bash
# REQUIRED FIRST STEP: Activate the virtual environment
source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate

# Find projects by name
python find_project.py --project-name "Marketing Campaign"

# Find in a specific workspace
python find_project.py --project-name "Marketing Campaign" --workspace-gid 1234567890

# Get JSON output
python find_project.py --project-name "Marketing Campaign" --output-format json
```

#### BrowseProjectTool: Standalone Usage

The standalone script lets you browse project details including sections and tasks. It includes robust error handling and supports the Asana API response structure.

```bash
# REQUIRED FIRST STEP: Activate the virtual environment
source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate

# Browse a project (provide the project GID)
python browse_project.py --project-gid 1234567890

# Get JSON output
python browse_project.py --project-gid 1234567890 --output-format json
```

The script will show:
- Project details (name, GID, notes)
- All sections in the project
- All tasks organized by section
- Task details including completion status, assignee, and due date

The script handles Asana's nested data structure and provides detailed debug output if there are any issues with the API response format.

#### ListWorkspacesAndTeamsTool: Standalone Usage

This script provides a simple way to list all workspaces and teams.

```bash
# REQUIRED FIRST STEP: Activate the virtual environment
source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate

# List all workspaces and teams
python list_workspaces_and_teams.py

# List teams in a specific workspace
python list_workspaces_and_teams.py --workspace-gid 1234567890

# List only workspaces
python list_workspaces_and_teams.py --list-type workspaces

# List only teams
python list_workspaces_and_teams.py --list-type teams --workspace-gid 1234567890

# Get JSON output
python list_workspaces_and_teams.py --output-format json
```

#### CreateProjectTool: Standalone Usage

Create a new Asana project using the command-line interface.

```bash
# REQUIRED FIRST STEP: Activate the virtual environment
source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate

# Create a new project
python create_project.py --name "New Project"

# Create with notes
python create_project.py --name "New Project" --notes "Project description"

# Create in specific workspace and team
python create_project.py --name "New Project" --workspace-gid 1234567890 --team-gid 0987654321

# Get JSON output
python create_project.py --name "New Project" --output-format json
```

#### Using the Main Menu

The main.py script provides a comprehensive menu interface to access all Asana Manager tools from a single command. This is the recommended way for AI agents to interact with the Asana Manager tools:

```bash
# REQUIRED FIRST STEP: Activate the virtual environment
source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate

# Change to the project directory
cd /Users/aniruddhasen/Projects/CrewAI/asana_manager

# Run the main menu
python -m src.asana_manager.main
```

The menu offers the following options:

```
Menu options:
1. Create a new Asana project using CrewAI workflow
2. Compare Pharmacist Operations Module with documentation
3. List all projects across all workspaces
4. Find a project by name
5. Browse project details
6. List workspaces and teams
7. Create project (direct tool)
8. Create project from markdown file
```

**Detailed Menu Option Descriptions:**

1. **Create a new Asana project using CrewAI workflow**
   - Uses the full CrewAI workflow to interactively create a project with tasks
   - Prompts for project name and three initial tasks
   - Handles all Asana API interactions automatically
   - Optimal for creating structured projects quickly

2. **Compare Pharmacist Operations Module with documentation**
   - Compares an existing Asana project with a markdown checklist
   - Shows missing tasks and completion status
   - Specifically configured for the Pharmacist Operations Module
   - Equivalent to running `compare_project.py` with preset parameters

3. **List all projects across all workspaces**
   - Shows all Asana projects in all accessible workspaces
   - Displays project names, GIDs, and workspace information
   - Same functionality as running `list_projects.py` directly
   - Useful for finding project GIDs needed by other tools

4. **Find a project by name**
   - Searches for projects by name in all workspaces
   - Similar to running `find_project.py` directly
   - Displays matching projects with GIDs and workspace details
   - Use when you need to find a specific project by its name

5. **Browse project details**
   - Shows detailed information about a specific project
   - Requires the project GID (get it from options 3 or 4 first)
   - Displays sections, tasks, assignees, due dates, and completion status
   - Same functionality as running `browse_project.py` directly

6. **List workspaces and teams**
   - Shows all Asana workspaces and teams you have access to
   - Displays GIDs for both workspaces and teams
   - Useful for getting the workspace/team GIDs needed for project creation
   - Same functionality as running `list_workspaces_and_teams.py` directly

7. **Create project (direct tool)**
   - Creates a new project using the direct Asana API tool
   - Simple project creation without additional tasks or workflow
   - Same functionality as running `create_project.py` directly
   - Good for quickly creating an empty project

8. **Create project from markdown file**
   - Converts a markdown document into an Asana project
   - Creates tasks, subtasks, and sections based on markdown structure
   - Same functionality as running `create_project_from_markdown.py` directly
   - Great for turning documentation into actionable projects

To use the menu, simply enter the number of the desired option when prompted. The menu will then guide you through any additional inputs needed for the selected action.

**Recommended Main Menu Workflow for AI Agents:**

1. For most tasks, start by accessing the main menu system:
   ```bash
   source /Users/aniruddhasen/Projects/CrewAI/venv/bin/activate
   cd /Users/aniruddhasen/Projects/CrewAI/asana_manager
   python -m src.asana_manager.main
   ```

2. For project exploration, follow this sequence:
   - First use option 3 (List all projects) to see available projects and their GIDs
   - Then use option 5 (Browse project details) with a specific GID to examine tasks

3. For creating new projects:
   - If you need a sophisticated project with tasks/sections, use option 1
   - If you already have a markdown document, use option 8 
   - For a simple empty project, use option 7

4. Remember that option 2 is specifically configured for the Pharmacist Operations Module and uses a hardcoded path for documentation

### Combining Multiple Tools

For complex workflows, you can combine multiple tools:

```python
# Example: Find a project, add tasks, and compare with documentation
from src.asana_manager.tools.asana_tools import (
    FindProjectByNameTool, CreateTaskTool, CompareTasksWithDocumentationTool
)

# 1. Find the project
find_tool = FindProjectByNameTool()
projects = find_tool._run("Marketing Campaign")

if "matching_projects" in projects and len(projects["matching_projects"]) > 0:
    project_gid = projects["matching_projects"][0]["gid"]
    
    # 2. Add a task to the project
    task_tool = CreateTaskTool()
    task = task_tool._run(
        project_gid=project_gid,
        name="Review campaign metrics",
        notes="Compare with Q3 baseline"
    )
    
    # 3. Compare with documentation
    compare_tool = CompareTasksWithDocumentationTool()
    comparison = compare_tool._run(
        project_gid=project_gid,
        markdown_file_path="/path/to/marketing_plan.md"
    )
    
    # Process the comparison results
    # ...
```

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

These enhancements have significantly improved the system's accuracy and completeness by ensuring:
1. All user instructions are completely preserved through the delegation chain
2. All monetary values use consistent ₹ formatting
3. Both regular and Airtable data sources are included in all analysis
4. Type incompatibilities between tables are properly addressed
5. The system adapts automatically to different database schemas

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
           query_intent: Type of analysis to perform ("general", "repeat_customers", "retention_rate", etc.)
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

# CrewAI Project Documentation

## IMPORTANT FINDINGS: Preventing AI Hallucination in CrewAI

This documentation explains a significant issue discovered in the Plazza Analytics project that caused AI agents to fabricate data rather than admit uncertainty. The issue stemmed from subtle instruction wording that prioritized "completeness" over truthfulness.

**Key Observation**: Without specific truthfulness instructions, AI agents defaulted to providing "helpful" but fabricated answers. This has significant implications for multi-agent systems where truthfulness should be a primary constraint.

### Key Issues Discovered

1. **Instruction-Induced Hallucination**: The system was generating completely fictional product sales data rather than admitting lack of information.

2. **Root Causes**: 
   - Task instructions emphasizing "complete" responses without emphasizing truthfulness
   - Agent backstories directing agents to "evaluate response quality" without clear truthfulness guidelines
   - The phrase "Did it fully answer the user?" implicitly encouraged fabrication over admitting uncertainty

3. **Misleading Agent Instructions**: Phrases like "you delegate to the right expert and return their answer" were being interpreted as permission to modify or enhance responses that seemed incomplete.

### Solutions Implemented

1. **Explicit Truthfulness Prioritization**: Modified agent backstories to explicitly forbid fabrication:
   ```yaml
   YOUR MOST IMPORTANT RULE: You must NEVER modify, enhance, or fabricate data in the expert's response.
   ```

2. **Clear Instructions Against Fabrication**: Added explicit instructions:
   ```yaml
   TRUTHFULNESS IS ESSENTIAL:
   1. Never make up data, products, or numbers
   2. If you can't find information, simply state "I don't have that information"
   3. Be honest about database query failures or knowledge base limitations
   4. Do not create fictional data even if it seems helpful
   ```

3. **Removed Completion Pressure**: Eliminated instructions that encouraged "complete" responses:
   ```yaml
   # Removed text
   Evaluate the response quality:
   - Did it fully answer the user?
   - If not, consider rerouting or rephrasing.
   ```

4. **Clear Response Passing Instructions**: Changed how the Orchestrator handles responses:
   ```yaml
   # Changed from
   You never respond directly to the user — you delegate to the right expert and return their answer.
   
   # To
   You route user queries to the right agent and return ONLY their exact response.
   ```

### Testing Results

We tested the system before and after these changes:

**Before**: The system claimed to find specific products with sales figures:
```
The top selling products based on the latest sales data are:
1. Product A - $500,000
2. Product B - $450,000
3. Product C - $400,000
4. Product D - $350,000
5. Product E - $300,000
```

**After**: The system honestly admitted its limitations:
```
I don't have that information.
```

This transformation from fabrication to honesty was achieved solely through prompt engineering changes, without any modifications to the underlying code or database connections.

### Implications for AI System Design

This case study provides important insights into AI system design:

1. **Truthfulness Requirements**: AI systems need explicit instructions prioritizing truthfulness over helpfulness
2. **Instruction Auditing**: Review all agent instructions for subtle language that might encourage fabrication
3. **Completeness vs. Accuracy**: Remove pressure to provide "complete" answers when data is unavailable
4. **Clear Boundaries**: Provide unambiguous instructions about response modification and data fabrication

These findings are especially critical in multi-agent systems where responses pass through multiple AI agents before reaching the user, as the orchestrating agent may feel compelled to "complete" or "improve" responses from specialist agents.

## CrewAI YAML-Based Tool Configuration

### Correct Tool Assignment Pattern

The Plazza Analytics project revealed a critical issue with tool assignment in CrewAI v0.108.0. The problem involved how tools are referenced in YAML configuration and instantiated in Python code.

#### Issue: Hardcoded vs. YAML Tool Assignment

The system was using a hardcoded approach in crew.py:

```python
# Hardcoded tool mapping (PROBLEMATIC)
agent_tools = {
    "data_analyst": [cockroach_db_tool, retention_analysis_tool],
    "chat_data_analyst": [cockroach_db_tool, methodology_tool, retention_analysis_tool, previous_analysis_tool],
    "visualization_specialist": [general_visualization_tool]
}
```

This ignored the tools specified in agents.yaml:

```yaml
visualization_specialist:
  tools:
    - GeneralVisualizationTool
```

#### Solution: YAML-Driven Tool Assignment

The correct pattern according to CrewAI documentation:

1. **In agents.yaml** - Define tool names as strings:
   ```yaml
   tools:
     - cockroach_db_tool
     - methodology_tool
   ```

2. **In crew.py** - Create tool instances with matching variable names:
   ```python
   # Variable names MUST match the tool names in YAML
   cockroach_db_tool = CockroachDBTool()
   methodology_tool = MethodologyTool()
   
   # Then create agents without explicitly passing tools
   # CrewAI will automatically match tool names from YAML
   agent = Agent(
       role=agent_data.get("role", ""),
       backstory=agent_data.get("backstory", ""),
       # No tools parameter - tools come from YAML
   )
   ```

3. **Remove Tool Mapping Logic**:
   - Delete the hardcoded tool mapping dictionary
   - Let CrewAI handle tool assignment based on YAML names

This approach ensures tools are assigned based on declarative YAML configuration rather than imperative Python code.

#### Implementation in Plazza Analytics

We implemented this fix by:

1. Adding proper tool entries to agents.yaml:
   ```yaml
   chat_data_analyst:
     # Other fields...
     tools:
       - cockroach_db_tool 
       - methodology_tool
       - retention_analysis_tool
       - previous_analysis_tool
   ```

2. Creating tool instances with matching names in crew.py:
   ```python
   # Create tool instances with variable names matching those in YAML
   cockroach_db_tool = CockroachDBTool()
   methodology_tool = MethodologyTool()
   retention_analysis_tool = RetentionAnalysisTool()
   previous_analysis_tool = PreviousAnalysisTool()
   ```

3. Removing the hardcoded tool mapping:
   ```python
   # Removed this code
   agent_tools = {
       "data_analyst": [cockroach_db_tool, retention_analysis_tool],
       "chat_data_analyst": [cockroach_db_tool, methodology_tool, retention_analysis_tool, previous_analysis_tool],
       "visualization_specialist": [general_visualization_tool]
   }
   
   # Removed this from agent creation
   tools=tools_for_agent
   ```

This allowed the declarative YAML configuration to drive tool assignment, making the system more maintainable and following proper CrewAI patterns.

## Other Technical Fixes

### 1. Knowledge Paths

CrewAI knowledge system expects knowledge files to be in a directory named "knowledge" at the project root. When using TextFileKnowledgeSource:

- Use relative paths (e.g., "sales_analysis.md") not absolute paths
- CrewAI will automatically prepend "knowledge/" to find files

In our testing, we discovered that using absolute paths causes problems because CrewAI still prepends "knowledge/", resulting in errors like:

```
File not found: knowledge/Users/aniruddhasen/Projects/CrewAI/plazza_analytics/knowledge/sales_analysis.md
```

The correct approach is to use simple filenames and let CrewAI handle the path resolution:

```python
knowledge_files = [
    {"file": "sales_analysis.md", "domain": "sales", "type": "business_intelligence"},
    {"file": "database_schemas.md", "domain": "technical", "type": "database_schema"}
]
```

### 2. Type Annotations for Tools

All tool classes must use type annotations for tool attributes:

```python
# Incorrect
name = "ToolName"

# Correct 
name: str = "ToolName"
description: str = "Tool description"
```

### 3. BaseTool Import

Always import BaseTool from CrewAI, not LangChain:

```python
# Incorrect
from langchain.tools import BaseTool

# Correct
from crewai.tools import BaseTool
```

## Virtual Environment Setup (March 2025)

### Environment Creation and Dependencies Installation

Created a compatible virtual environment for plazza_analytics:

```bash
# Create a Python 3.11 virtual environment
cd /Users/aniruddhasen/Projects/CrewAI/plazza_analytics
python3 -m venv venv_py311

# Activate virtual environment and update pip
source venv_py311/bin/activate
pip install -U pip

# Install CrewAI and dependencies
pip install "crewai[tools]>=0.105.0,<1.0.0" pyyaml>=6.0 psycopg2-binary

# Install plazza_analytics in development mode
pip install -e .
```

### Installed Packages

The virtual environment includes:
- CrewAI 0.108.0 with tools support
- CrewAI Tools 0.38.1
- PyYAML 6.0.2
- psycopg2-binary 2.9.10
- All necessary dependencies for LangChain, OpenAI, and other required libraries

### Environment Configuration

Created a .env template with required environment variables:

```
# OpenAI API key
OPENAI_API_KEY=your-api-key-here

# Database connections
DATABASE_URL="postgresql://username:password@plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
DATABASE_URL_USER_TRANSACTIONS="postgresql://username:password@plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud:26257/user_transactions?sslmode=verify-full"
DATABASE_URL_ERP="postgresql://username:password@plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud:26257/plazza_erp?sslmode=verify-full"
DATABASE_URL_USER="postgresql://username:password@plazza-catalogue-3852.jxf.gcp-us-central1.cockroachlabs.cloud:26257/user_events?sslmode=verify-full"

# Visualization settings
VISUALIZATION_OUTPUT_DIR="/Users/aniruddhasen/Projects/CrewAI/plazza_analytics/visuals"

# Knowledge Base settings
DEFAULT_KNOWLEDGE_BASE="/Users/aniruddhasen/Projects/CrewAI/plazza_analytics/knowledge"
```

### Directory Structure

Ensured the required directories exist:
```bash
mkdir -p /Users/aniruddhasen/Projects/CrewAI/plazza_analytics/visuals
```

The knowledge directory already exists with well-structured markdown files for CrewAI's RAG capabilities:
- sales_analysis.md
- database_schemas.md
- customer_insights.md

### Package Structure

The plazza_analytics package has been installed in development mode with the following structure:
- pyproject.toml for package configuration
- src/plazza_analytics/ for the core code
- knowledge/ for the knowledge base files
- Tools implementation in src/plazza_analytics/tools/

### Compatibility Notes

When testing the application, encountered a Pydantic error related to BaseTool implementations:
- Issue: "Field 'name' defined on a base class was overridden by a non-annotated attribute"
- This is due to Pydantic v2 requiring type annotations for fields overridden from a base class
- To resolve this would require adding type annotations to tool classes

Additionally, there may be compatibility issues with the current knowledge integration approach:
- Error: "cannot import name 'Knowledge' from 'crewai.knowledge'"
- This suggests the CrewAI API for knowledge handling has changed

These issues would require code modifications to resolve, which should only be done with explicit permission.

## Project Overview

### System Integration and Robustness Improvements (March 24)

#### Combined AI Orchestration and Frontend Enhancements

The system has been significantly enhanced with robust error handling, streamlined UI, and improved agent orchestration:

1. **Complete AI Orchestration Flow Implementation**:
   - Fixed CrewOutput handling in advanced_router.py
   - Enhanced task delegation with proper field validation
   - Implemented robust self-evaluation extraction
   - Added comprehensive logging for router decisions
   - Ensured proper error propagation across the system

2. **Streamlined Streamlit Frontend**:
   - Implemented proper form handling with callback-based input clearing
   - Enhanced user session state management
   - Added robust error handling with detailed tracebacks
   - Created smooth chat experience with proper UI feedback
   - Ensured proper module importing with graceful degradation

3. **End-to-End System Testing**:
   - Verified router-to-agent delegation path
   - Tested frontend-to-router integration
   - Validated self-evaluation persistence in logs
   - Ensured robust error handling across the stack
   - Confirmed proper clearing of input fields after submission

4. **Technical Implementation Highlights**:
   - Enhanced router-to-agent delegation with complete JSON schema requirements
   - Fixed session state manipulation with proper Streamlit lifecycle hooks
   - Implemented robust type checking for CrewOutput objects
   - Used callback functions for cleaner state management
   - Added graceful error handling at all levels of the stack

5. **Documentation Enhanced**:
   - Added detailed explanations of all enhancements
   - Provided example code snippets for key implementations
   - Documented technical background for each fix
   - Included troubleshooting guidance for common issues
   - Updated implementation notes for future developers

The system now provides a robust, user-friendly interface with intelligent query routing, proper agent delegation, and comprehensive error handling, making it suitable for production use.

### System Enhancements (March 24-26)

#### Streamlit Frontend and Router Bugfixes (March 24)

1. **Form Submission Fix**:
   - Fixed issue with Enter key submission not working
   - Simplified the form handling approach for better reliability
   - Fixed template variable error in advanced_router.py
   - Added proper f-string escaping for JSON examples in router task
   - Ensured both "user_input" and "task" variables are passed to the crew

2. **Implementation Details**:
   ```python
   # Fixed form handling for Enter key support
   with st.form(key="chat_form"):
       query = st.text_input("Ask a question:")
       submit_button = st.form_submit_button("Submit")
   
   # Fixed JSON example escaping in f-strings
   description=f"""
   ...
   "input **MUST** be a complete JSON object like this:
   {{{{
     "task": "Do something specific",
     "context": "Everything they need to know in detail",
     "coworker": "Data Q&A Expert" 
   }}}}
   """
   
   # Fixed missing template variable
   result = crew.kickoff(inputs={"user_input": user_query, "task": user_query})
   ```

3. **Benefits**:
   - Restored Enter key submission in Streamlit interface
   - Fixed "Missing required template variable" error
   - Improved reliability of the advanced router
   - Enhanced user experience with more intuitive form handling
   - Prevented common f-string escaping errors in router tasks

4. **Technical Background**:
   - Streamlit forms enable Enter key submission by default
   - CrewAI requires proper escaping of curly braces in f-strings
   - When using CrewAI's kickoff method, all template variables need to be provided
   - Double curly braces are needed in f-strings to render actual curly braces
   - Form submission handling requires careful state management

5. **Files Modified**:
   - `/Streamlit_Frontend/streamlit_app.py`: Fixed form handling for Enter key support
   - `/Core_Scripts/advanced_router.py`: Fixed f-string escaping and template variables

#### Router JSON Format Fix (March 24)

1. **JSON Format Standardization**:
   - Fixed error with JSON formatting in delegation
   - Replaced escaped f-string JSON example with properly formatted code block
   - Properly delimited JSON code with markdown code block syntax
   - Ensured consistent JSON format in both router and agent registry
   - Eliminated confusing escaping that led to improper JSON parsing

2. **Implementation Details**:
   ```python
   # Original problematic formatting (in f-string):
   description=f"""
   ...
   When you use the delegation tool, the input **MUST** be a complete JSON object like this:
   {{{{
     "task": "Do something specific",
     "context": "Everything they need to know in detail",
     "coworker": "Data Q&A Expert" 
   }}}}
   """
   
   # Fixed version with clear code block formatting:
   description=f"""
   ...
   When you use the delegation tool, the input **MUST** be a valid JSON object that includes all three required fields:
   
   ```json
   {{
     "task": "Do something specific",
     "context": "Everything they need to know in detail",
     "coworker": "Data Q&A Expert" 
   }}
   ```
   """
   ```

3. **Benefits**:
   - Fixed "'\n  "task"'" error in delegation tool
   - More readable prompt for the router agent
   - Better communication of expected JSON format
   - Eliminated confusing double-escape sequences
   - More consistent example format across the codebase
   - Improved reliability of the delegation mechanism

4. **Technical Background**:
   - Using explicit code blocks with ``` syntax helps LLMs format JSON properly
   - Multiple levels of escaping in f-strings can be confusing
   - Markdown code blocks provide clearer visual boundaries for JSON examples
   - Consistent JSON formatting between prompts and actual implementation
   - Properly delimited code blocks improve readability and parsing

5. **Files Modified**:
   - `/Core_Scripts/advanced_router.py`: Updated JSON example with code block syntax
   - `/Core_Scripts/agent_registry.py`: Applied the same code block pattern for consistency

#### Router Template Variable Fix (March 24)

1. **Template Variable Standardization**:
   - Fixed "Missing required template variable" error in router task
   - Converted f-string to regular triple-quoted string
   - Changed placeholders from `{user_query}` to `{user_input}`
   - Removed double curly braces from JSON examples
   - Eliminated nested template substitution issues

2. **Implementation Details**:
   ```python
   # Original problematic f-string with user_query:
   router_task = Task(
       description=f"""
       You are given the following user request:
       
       "{user_query}"
       ...
       """,
       ...
   )
   
   # Fixed version with standard template and user_input:
   router_task = Task(
       description="""
       You are given the following user request:
       
       "{user_input}"
       ...
       """,
       ...
   )
   ```

3. **Benefits**:
   - Fixed "Missing required template variable" error
   - Eliminated confusion between template variables and literal text
   - Standardized on CrewAI's expected template format
   - More consistent with CrewAI's input parameter naming
   - Improved reliability of the routing system
   - Simplified the template structure for better maintainability

4. **Technical Background**:
   - CrewAI expects template variables in a specific format
   - The system uses `user_input` as the standard variable name 
   - Mixing f-strings with template variables can cause conflicts
   - Multiple levels of string substitution create complexity
   - Using standard template strings simplifies the implementation

5. **Files Modified**:
   - `/Core_Scripts/advanced_router.py`: Changed router task to use standard template with user_input variable

#### Streamlit Frontend Enhancement: Input Field Auto-Clear (March 24)

1. **Input Field Clearing**:
   - Added automatic clearing of input field after form submission
   - Enhanced user experience by removing the need to manually clear the field
   - Implemented proper callback-based session state management for form inputs
   - Used Streamlit's on_click parameter for clean state handling
   - Created a smoother, more intuitive chat experience that respects Streamlit's widget lifecycle

2. **Implementation Details**:
   ```python
   # Define a callback function to clear input
   def clear_chat_input():
       st.session_state["chat_input"] = ""
   
   # Use callback with on_click parameter
   with st.form("chat_form"):
       user_input = st.text_input("Ask a question:", key="chat_input")
       submitted = st.form_submit_button("Submit", on_click=clear_chat_input)

   # Handle form submission with proper state management
   if submitted:
       # Get input before it's cleared by the callback
       query = user_input or st.session_state.get("chat_input", "")
       if query:
           # Process the query
           result = run_advanced_router(query)
   ```

3. **Benefits**:
   - Improves user experience by clearing the input field after submission
   - Follows Streamlit's recommended pattern for session state manipulation
   - Prevents the "You can't mutate session_state directly after widget creation" error
   - Reduces user friction when asking multiple questions
   - Creates a more natural chat interface workflow
   - Properly respects Streamlit's widget lifecycle and state management

4. **Technical Background**:
   - Streamlit's session state has specific mutation rules
   - Direct mutation after widget creation is not allowed
   - The on_click parameter provides the correct lifecycle hook for state changes
   - Callback functions run at the proper time in Streamlit's execution flow
   - This pattern follows Streamlit's best practices for form handling

5. **Files Modified**:
   - `/Streamlit_Frontend/streamlit_app.py`: Enhanced form handling with proper callback-based session state management

#### Advanced Router Enhancement: Task Delegation and CrewOutput Handling Fix (March 24)

1. **CrewOutput Object Handling**:
   - Fixed a critical type error in the advanced router when handling CrewOutput objects
   - Added proper type detection and conversion to ensure string operations work correctly
   - Implemented robust fallback to str() when raw_output property is not available
   - Enhanced error handling for regex operations on response content
   - Fixed "expected string or bytes-like object, got 'CrewOutput'" error in Streamlit frontend

2. **Delegation Format Standardization**:
   - Added explicit formatting requirements for the delegation tool
   - Fixed potential "Field required" validation errors with coworker field
   - Enhanced routing agent and task instructions with proper delegation format
   - Added example JSON format with all required fields (task, context, coworker)
   - Updated agent names to ensure exact matching between registry and delegation calls
   - Added explicit warnings about field requirements to prevent delegation failures

3. **Implementation Details: CrewOutput Handling**:
   ```python
   # Advanced Router CrewOutput handling
   def run_advanced_router(user_query):
       # ... existing code ...
       
       result = crew.kickoff(inputs={"user_input": user_query})
       
       # Convert CrewOutput to string if needed
       if hasattr(result, "raw_output"):
           result_str = result.raw_output
       else:
           result_str = str(result)
       
       # Use string version for regex operations
       eval_match = re.search(r'<!--\s*(Self-evaluation:.*?)-->', result_str, re.DOTALL)
       # ... remaining code ...
   ```

4. **Implementation Details: Delegation Format**:
   ```python
   # Updated routing agent backstory with delegation format requirements
   backstory="""
   ...
   DELEGATION FORMAT REQUIREMENTS:
   When using the "Delegate work to coworker" tool, you MUST include all 3 required fields:
   1. "task": Clear instructions on what they need to do
   2. "context": All relevant background information they need
   3. "coworker": EXACT agent name from the list above

   Example of correct delegation format:
   {
     "task": "Answer the user's question about top-selling products",
     "context": "The user is asking about sales performance and needs metrics",
     "coworker": "Data Q&A Expert"
   }

   IMPORTANT: If you forget even one of these fields, the delegation will fail completely.
   ...
   """
   ```

5. **Benefits**:
   - Eliminates type errors when processing agent responses
   - Prevents delegation failures due to missing required fields
   - Ensures proper extraction of self-evaluation metadata
   - Maintains compatibility with CrewAI's output structure changes
   - Enhances stability of the Streamlit frontend
   - Preserves router logs with proper formatting and evaluation data
   - Creates more reliable agent-to-agent delegation

6. **Technical Background**:
   - Recent versions of CrewAI return CrewOutput objects instead of plain strings
   - CrewAI's DelegateWorkToolSchema requires three specific fields: task, context, and coworker
   - Missing any required field in the delegation tool causes a validation error
   - LLMs sometimes omit required fields if not explicitly instructed
   - Explicit format examples significantly increase success rate for delegations

7. **Files Modified**:
   - `/Core_Scripts/advanced_router.py`: Updated response handling and task instructions
   - `/Core_Scripts/agent_registry.py`: Enhanced routing agent with delegation format requirements

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

### Intent-Driven Customer Retention Analysis (March 26)

1. **Enhanced RetentionAnalysisTool Implementation**:
   - Implemented dynamic, intent-based query processing for customer retention analysis
   - Added specialized query_intent parameter with "general" and "repeat_customers" modes
   - Created graph-based schema discovery for relationship detection between tables
   - Added automatic JOIN path finding for optimal query construction
   - Implemented customer detail retrieval with complete contact information
   - Added flexible parameterization for number of results and detail level

2. **Agent Integration for Retention Analysis**:
   - Updated Data Q&A Expert agent with enhanced RetentionAnalysisTool capabilities
   - Added specialized retention analysis examples in agent backstory
   - Implemented customer detail processing with proper Indian Rupee (₹) formatting
   - Created dedicated task templates for repeat customer identification
   - Enhanced the orchestration router to recognize retention-related queries

3. **Task Routing and Parameter Selection**:
   - Added retention-specific intent detection in the orchestration layer
   - Implemented automatic parameter selection based on query type
   - Created specialized task templates for retention metrics and customer profiling
   - Added comprehensive parameter passing examples in agent descriptions
   - Improved router to recognize customer-specific query patterns

4. **Implementation Details**:
   ```python
   # Intent-based RetentionAnalysisTool usage
   # Simple retention metrics
   retention_analysis_tool.run(query_intent="general")
   
   # Detailed customer profiles
   retention_analysis_tool.run(
       query_intent="repeat_customers",
       include_contact_details=True,
       limit=10
   )
   
   # Dynamic schema discovery implementation
   def _discover_schema(self, conn):
       """Discover and cache the schema for relevant tables with relationships."""
       # Schema discovery implementation that detects relationships
       # between tables based on naming conventions and foreign keys
       
   def _build_schema_graph(self, schema_info):
       """Build a directed graph from schema relationships for JOIN path inference."""
       # Create a graph representation of table relationships
       
   def _find_join_path(self, graph, start_table, end_table):
       """Find optimal JOIN path between tables using BFS."""
       # Breadth-first search to find shortest join paths
   ```

5. **Benefits**:
   - **Improved User Experience**: Users can now request specific customer details with simple queries
   - **Unified Data Source**: Both regular tables and Airtable tables are automatically combined
   - **Enhanced Adaptability**: System automatically adapts to schema changes and differences
   - **Richer Insights**: Complete customer profiles with contact information and purchase history
   - **Dynamic Query Generation**: No more hardcoded queries that break with schema changes
   - **Optimal JOIN Paths**: Graph-based approach ensures most efficient query construction
   - **Structured Customer Information**: Properly formatted outputs with all contact details

6. **Example Usage Patterns**:
   - "Who are my repeat customers?" → Shows complete list with basic information
   - "Show me detailed profiles of my top 5 repeat customers" → Includes contact details with limit=5
   - "What's the purchase history of my most loyal customers?" → Detailed purchase timeline
   - "What percentage of customers are repeat buyers?" → General retention metrics

7. **Specialized Intent Types**:
   - **"general"**: Comprehensive retention metrics focusing on percentages, time between purchases, cohort analysis
   - **"repeat_customers"**: Detailed customer list with complete profiles including:
     * Customer names and contact information
     * Complete purchase history with order dates
     * Total spent formatted in Indian Rupees (₹)
     * First and most recent purchase dates
     * Purchase frequency counts

8. **Enterprise Data Analyst Enhancement**:
   - Added specialized section on Enhanced Customer Analysis Capabilities
   - Highlighted the graph-based schema discovery for deeper customer insights
   - Added detailed examples of the new intent-based analysis capabilities
   - Enhanced examples to cover complete customer profiling use-cases
   - Emphasized the ability to adapt to schema differences between tables

9. **Files Modified**:
   - Updated: `/src/plazza_analytics/tools/retention_analysis_tool.py` with graph-based schema discovery
   - Updated: `/src/plazza_analytics/config/agents.yaml` with enhanced tool descriptions
   - Updated: `/src/plazza_analytics/config/tasks.yaml` with specialized retention tasks
   - Updated: `/CLAUDE.md` with documentation of the enhancements

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

### Knowledge Persistence Implementation (March 26, 2025)

1. **Knowledge Persistence Tools**:
   - Created SaveKnowledgeTool to persist agent discoveries to knowledge files
   - Enhanced PreviousAnalysisTool for more robust path finding
   - Added knowledge persistence capabilities to Data Q&A Expert and Enterprise Data Analyst
   - Implemented knowledge file timestamping and structured format
   - Solved knowledge directory path issues for CrewAI compatibility

2. **Implementation Strategy**:
   - Tool-based approach for flexible knowledge persistence
   - Agents invoke SaveKnowledgeTool directly after making discoveries
   - Added detailed tool usage instructions to agent backstories
   - Fixed tool mapping in crew.py to properly associate YAML tool names with instances

3. **Knowledge Directory Structure**:
   - Ensured knowledge files are at project root level for CrewAI compatibility
   - Properly structured knowledge files with timestamps and metadata
   - Enhanced agent instructions to include specific file targets for different knowledge types
   - Fixed path handling for both knowledge files and previous analysis results

4. **CrewAI Assistant Integration**:
   - Added workflow for consulting CrewAI Assistant through the user interface
   - Leveraged CrewAI Assistant for resolving tool-to-agent mapping issues
   - Used CrewAI Assistant documentation to understand knowledge directory expectations
   - Documented proper knowledge persistence patterns from CrewAI Assistant for future reference
   - Enhanced agent prompt patterns based on CrewAI Assistant recommendations

   **How to Use CrewAI Assistant**:
   - When you need help with CrewAI-specific issues, ask Claude Code to relay questions to CrewAI Assistant
   - Reference file `/Users/aniruddhasen/Projects/CrewAI/Ref_documents/CrewAI_assistant_chat.md` for previous interactions
   - For implementation questions, provide code snippets from your project to get more specific advice
   - CrewAI Assistant can help with:
     - Agent and tool configuration best practices
     - YAML configuration patterns
     - Tool mapping and assignment
     - File path handling for knowledge files
     - Handling multi-step tasks and complex delegations
     - Proper prompt engineering for specialist agents

5. **Challenges and Improvements Needed**:
   - Multi-step task handling in orchestrator needs enhancement
   - Orchestrator doesn't always include all parts of instructions when delegating
   - Knowledge saving needs to be automated rather than requiring explicit instructions
   - Complex instructions with multiple tool steps need better parsing

## CrewAI Assistant Query - RetentionAnalysisTool Issue (March 26, 2025)

The following is a query that was prepared for CrewAI Assistant to help troubleshoot issues with the RetentionAnalysisTool:

```
I'm having an issue with my CrewAI project where the RetentionAnalysisTool is causing the process to hang. I've updated the tool to accept new parameters (query_intent, include_contact_details, limit), but now when an agent tries to use it, the execution gets stuck.

Here's my modified RetentionAnalysisTool implementation:

```python
import os
import psycopg2
import psycopg2.extras
import json
import re
from datetime import datetime
from crewai.tools import BaseTool
from typing import Optional, Literal, Dict, Any, Annotated
from plazza_analytics.tools.config import DB_CONNECTION_VARS, DB_SCHEMA_CACHE

class RetentionAnalysisTool(BaseTool):
    name: str = "RetentionAnalysisTool"
    description: str = """Perform comprehensive customer retention analysis across ALL data sources in the Plazza ecosystem.
    Analyzes BOTH regular tables AND Airtable tables to provide a complete view of customer behavior.
    Calculates repeat rates, time between purchases, top products, and discount impact.
    NOW FEATURES:
    1. Automatic schema discovery to adapt to different table structures
    2. Safe fallback mechanisms for missing columns
    3. Complete integration of both regular tables AND Airtable tables
    4. Indian Rupee (₹) formatting for all monetary values
    5. Robust error handling with clear explanations
    
    USAGE OPTIONS:
    - generate_visuals: Whether to generate visualizations (default: True)
    - query_intent: Type of analysis ("general" or "repeat_customers")
    - include_contact_details: Include customer names and contact information (with repeat_customers intent)
    - limit: Maximum number of results to return (default: 10)
    
    EXAMPLES:
    - Standard retention metrics: retention_analysis_tool.run()
    - Find repeat customers: retention_analysis_tool.run(query_intent="repeat_customers")
    - Customer details: retention_analysis_tool.run(query_intent="repeat_customers", include_contact_details=True)
    - Limit results: retention_analysis_tool.run(query_intent="repeat_customers", limit=5)"""

    # Class-level caches for performance
    _retention_cache = None  # Cached results for reuse
    _schema_cache = {}  # Schema information for each table
    
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

    def _run(self, generate_visuals: bool = True) -> str:
        """Execute the actual retention analysis."""
        # Implementation details...
```

And here's the agent definition in the YAML file:

```yaml
chat_data_analyst:
  role: >
    Data Q&A Expert
  goal: >
    Quickly answer user questions by first checking the knowledge base, then using tools only when necessary.
  backstory: >
    You are the primary agent for answering user queries using the existing knowledge base.
    
    # SECTION ON RETENTION TOOL
    RetentionAnalysisTool - For customer retention metrics with ENHANCED CAPABILITIES
       - NEW FEATURE: Intent-based query processing with specialized analysis types
       - Usage: retention_analysis_tool.run(query_intent="repeat_customers", include_contact_details=True)
       - Possible query_intent values:
         * "general" - Standard retention metrics (repeat rate, time between purchases, etc.)
         * "repeat_customers" - Detailed list of repeat customers with contact info and purchase history
       - NEW FEATURE: Dynamic schema discovery adapts to database changes automatically
       - NEW FEATURE: Relationship detection finds connections between tables based on naming patterns
       - NEW FEATURE: Graph-based query generation finds optimal JOIN paths between tables
       - Include customer NAMES and CONTACT DETAILS with include_contact_details=True
  tools:
    - cockroach_db_tool 
    - methodology_tool
    - retention_analysis_tool
    - previous_analysis_tool
    - save_knowledge_tool
```

Here's what happens in the log when the process hangs:

```
🚀 Crew: crew
└── 📋 Task: d6e14f61-d27f-4234-a8a9-9e4c8f55fc34
       Status: Executing Task...
    ├── 🤖 Agent: Conversation Orchestrator
    │   
    │       Status: In Progress
    │   └── 🔧 Using Delegate work to coworker (1)
    └── 🤖 Agent: Data Q&A Expert
        
            Status: In Progress
        └── 🔧 Failed RetentionAnalysisTool (2)

╭─────────────────────────────────────────────────────────────────────────── Tool Error ────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                    │
│  Tool Usage Failed                                                                                                                                                 │
│  Name: RetentionAnalysisTool                                                                                                                                       │
│  Error: Arguments validation failed: 1 validation error for RetentionAnalysisToolSchema                                                                            │
│  generate_visuals                                                                                                                                                  │
│    Field required [type=missing, input_value={'query_intent': 'repeat_..._contact_details': True}, input_type=dict]                                                │
│      For further information visit https://errors.pydantic.dev/2.10/v/missing                                                                                      │
│                                                                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

I tried modifying the tool to use an `args_schema` like this:

```python
args_schema: Dict[str, Dict[str, Any]] = {
    "generate_visuals": {
        "type": "bool",
        "description": "Whether to generate visualizations",
        "default": True
    },
    "query_intent": {
        "type": "str",
        "description": "Type of analysis to perform ('general' or 'repeat_customers')",
        "default": "general"
    },
    "include_contact_details": {
        "type": "bool",
        "description": "Include customer names and contact information with repeat_customers intent",
        "default": False
    },
    "limit": {
        "type": "int",
        "description": "Maximum number of results to return",
        "default": 10
    },
    "force_refresh": {
        "type": "bool",
        "description": "Force a refresh of the analysis, ignoring cache",
        "default": False
    }
}
```

Could you help me with:
1. The correct way to define tool parameters in CrewAI v0.108.0+
2. How to handle multiple parameters in a BaseTool implementation 
3. An example of a working tool with complex parameters
4. How to debug tool execution issues

I'm using Python 3.11 and the latest CrewAI version. Thank you!
```

### CrewAI Assistant Response

[Awaiting response from CrewAI Assistant]

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
   - ✅ Fix CrewOutput handling in advanced router (Completed April 1)
   - ✅ Enhance delegation format with proper field validation (Completed April 1)
   - ✅ Implement proper Streamlit form handling with callbacks (Completed April 1)
   - ✅ Implement knowledge persistence with SaveKnowledgeTool (Completed March 26)
   - ✅ Implement automatic schema discovery in RetentionAnalysisTool (Completed March 26)
   - ✅ Add dynamic SQL generation for schema differences (Completed March 26)
   - ✅ Create comprehensive data volume reporting (Completed March 26)
   - Develop multi-agent test harness (Week 4-6)
   - Add task dependency resolution for multi-stage analysis (Week 7-8)
   - Enhance orchestrator for better multi-step task handling (Week 5-6)

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

## Plazza Analytics - CrewAI Project Setup Guide

### CrewAI Version Compatibility Issue

The Plazza Analytics project is built using an older version of CrewAI that has API differences with the current version. Specifically:

1. **API Changes**: 
   - The project is trying to import `AgentConfig` and `TaskConfig` from `crewai.config`, which doesn't exist in newer versions
   - The YAML configuration loading mechanism has been removed or significantly changed in newer versions

2. **Required Modifications**:
   ```python
   # Original imports in crew.py
   from crewai import Crew, Process
   from crewai.config import AgentConfig, TaskConfig  # This no longer exists
   
   # Modified imports for newer CrewAI versions
   import yaml
   from crewai import Crew, Process, Agent, Task
   ```

3. **Agent & Task Creation**:
   - Original: Used `AgentConfig` and `TaskConfig` classes to load from YAML
   - Modified: Need to load YAML directly and manually instantiate Agent and Task objects

### Proposed Modification (Without Changing Structure)

To make the project compatible with current CrewAI versions while maintaining the same structure:

```python
# Modified version of crew.py
import yaml
from crewai import Crew, Process, Agent, Task

def create_plazza_crew():
    # Load agents configuration from YAML file
    with open("src/plazza_analytics/config/agents.yaml", "r") as f:
        agents_config = yaml.safe_load(f)
    
    # Load tasks configuration from YAML file
    with open("src/plazza_analytics/config/tasks.yaml", "r") as f:
        tasks_config = yaml.safe_load(f)
    
    # Initialize agents
    conversation_orchestrator = Agent(
        role=agents_config["conversation_orchestrator"]["role"],
        goal=agents_config["conversation_orchestrator"]["goal"],
        backstory=agents_config["conversation_orchestrator"]["backstory"],
        allow_delegation=True,
        verbose=True
    )
    
    data_analyst = Agent(
        role=agents_config["data_analyst"]["role"],
        goal=agents_config["data_analyst"]["goal"],
        backstory=agents_config["data_analyst"]["backstory"],
        verbose=True
    )
    
    chat_data_analyst = Agent(
        role=agents_config["chat_data_analyst"]["role"],
        goal=agents_config["chat_data_analyst"]["goal"],
        backstory=agents_config["chat_data_analyst"]["backstory"],
        verbose=True
    )
    
    visualization_specialist = Agent(
        role=agents_config["visualization_specialist"]["role"],
        goal=agents_config["visualization_specialist"]["goal"],
        backstory=agents_config["visualization_specialist"]["backstory"],
        # Note: actual tool instances would need to be implemented
        tools=["GeneralVisualizationTool"],
        verbose=True
    )
    
    business_strategy_advisor = Agent(
        role=agents_config["business_strategy_advisor"]["role"],
        goal=agents_config["business_strategy_advisor"]["goal"],
        backstory=agents_config["business_strategy_advisor"]["backstory"],
        verbose=True
    )
    
    # Initialize tasks
    handle_user_query = Task(
        description=tasks_config["handle_user_query"]["description"],
        expected_output=tasks_config["handle_user_query"]["expected_output"],
        agent=conversation_orchestrator
    )
    
    # Define crew
    return Crew(
        agents=[
            conversation_orchestrator,
            data_analyst,
            chat_data_analyst,
            visualization_specialist,
            business_strategy_advisor
        ],
        tasks=[handle_user_query],
        process=Process.hierarchical,
        verbose=True
    )
```

### Additional Implementation Challenges

1. **Tools Implementation**:
   - The tools specified in the YAML like `GeneralVisualizationTool` need to be actual tool instances
   - These would need to be implemented based on the current tools in the project
   - The project may use custom tools that need to be properly integrated

2. **Template Handling**:
   - The task description contains templates like `{user_query}` that need special handling
   - The original CrewAI version may have had built-in template handling

3. **Python Version**:
   - CrewAI requires Python 3.10-3.12 (not 3.13)
   - A virtual environment with Python 3.11 is recommended

4. **CrewAI Version**:
   - Current version (0.108.0) contains significant API differences
   - The project was likely built with a much earlier version (possibly 0.30.0 or earlier)

### Project Structure Overview

The Plazza Analytics project is organized as follows:

1. **Configuration Files**:
   - `agents.yaml`: Defines agent roles, goals, backstories, and tools
   - `tasks.yaml`: Defines task descriptions, expected outputs, and templates

2. **Core Modules**:
   - `crew.py`: Creates the CrewAI system with agents and tasks
   - `main.py`: Entry point that accepts user input and runs the crew

3. **Agent Architecture**:
   - Conversation Orchestrator: Routes queries to appropriate specialists
   - Data Analyst: Deep business analysis and schema discovery
   - Chat Data Analyst: Quick answers using knowledge base or direct queries
   - Visualization Specialist: Creates charts from analysis data
   - Business Strategy Advisor: Proposes data-driven business strategies

### Environment Setup Requirements

1. **Virtual Environment**:
   ```bash
   python3.11 -m venv venv_py311
   source venv_py311/bin/activate
   pip install crewai
   pip install pyyaml
   ```

2. **Dependencies**:
   - CrewAI and its dependencies
   - PyYAML for configuration parsing
   - Potentially custom tools for database access and visualization

### Recommendations

1. **Short-Term**:
   - Update `crew.py` to work with current CrewAI version
   - Implement the necessary tool classes
   - Update main.py to create the crew using the updated approach

2. **Medium-Term**:
   - Consider migrating to CrewAI's official templates
   - Use `crewai install` for dependency management
   - Standardize the project structure according to CrewAI best practices

3. **Long-Term**:
   - Refactor to use CrewAI's latest features like agent memory
   - Consider Docker containerization for deployment
   - Implement proper testing framework

## Database Connections

The project connects to multiple CockroachDB databases:

```
DATABASE_URL="postgresql://aniruddha:qls3UibsCfTOXA9P7CbgnQ@plazza-catalogue-5312.jxf.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
DATABASE_URL_ERP="postgresql://aniruddha:qls3UibsCfTOXA9P7CbgnQ@plazza-catalogue-5312.jxf.gcp-us-central1.cockroachlabs.cloud:26257/plazza_erp?sslmode=verify-full"
DATABASE_URL_USER="postgresql://aniruddha:qls3UibsCfTOXA9P7CbgnQ@plazza-catalogue-5312.jxf.gcp-us-central1.cockroachlabs.cloud:26257/user_events?sslmode=verify-full"
DATABASE_URL_USER_TRANSACTIONS="postgresql://aniruddha:qls3UibsCfTOXA9P7CbgnQ@plazza-catalogue-5312.jxf.gcp-us-central1.cockroachlabs.cloud:26257/user_transactions?sslmode=verify-full"
```

Each database serves a different purpose:

1. **defaultdb**: Core product catalog
2. **plazza_erp**: Business operations
3. **user_events**: User activity tracking
4. **user_transactions**: Customer and order management

The CockroachDBTool implementation needs to be updated to work with the current CrewAI version while maintaining the ability to query these databases.

## Custom Tools Implementation

The project includes several custom tools that need to be implemented:

1. **CockroachDBTool**: 
   - Connects to multiple databases
   - Executes SQL queries against CockroachDB
   - Handles schema discovery and data retrieval

2. **GeneralVisualizationTool**:
   - Creates visualizations from analysis data
   - Parses markdown content to extract metrics
   - Generates charts and dashboards

3. **MethodologyTool**:
   - Standardizes and documents queries
   - Provides transparency in data analysis

4. **RetentionAnalysisTool**:
   - Specialized for customer retention metrics
   - May need to connect to user_transactions database

Proper implementation of these tools is critical for the system to function correctly. Each tool needs to be defined as a class extending `BaseTool` from CrewAI.

## CrewAI Compatibility Fixes (March 2025)

### Pydantic Type Annotation Issues

When working with CrewAI v0.108.0, we encountered Pydantic validation errors related to tool implementations:

```
pydantic.errors.PydanticUserError: Field 'name' defined on a base class was overridden by a non-annotated attribute. All field definitions, including overrides, require a type annotation.
```

This error occurs because:
1. The tool classes were originally extending `langchain.tools.BaseTool`
2. In newer versions of CrewAI and Pydantic v2, all field overrides require type annotations
3. The `name` and `description` attributes in tool classes needed explicit type annotations

#### Fix Implementation:

1. Changed imports from `langchain.tools` to `crewai.tools` in all tool files:
   ```python
   # Change this
   from langchain.tools import BaseTool
   
   # To this
   from crewai.tools import BaseTool
   ```

2. Added proper type annotations to name and description attributes:
   ```python
   # Change this
   name = "ToolName"
   description = "Tool description"
   
   # To this
   name: str = "ToolName"
   description: str = "Tool description"
   ```

3. Modified tools to be instantiated before being passed to agents:
   ```python
   # Create tool instances
   cockroach_db_tool = CockroachDBTool()
   methodology_tool = MethodologyTool()
   
   # Use instances in agent definitions
   agent_tools = {
       "data_analyst": [cockroach_db_tool, retention_analysis_tool],
   }
   ```

### Delegation Tool Issues

The agent delegation was failing with errors related to the input format:

```
Input should be a valid string [type=string_type, input_value={'description': '...', 'type': 'str'}, input_type=dict]
```

This error occurs because:
1. The delegation tool in CrewAI v0.108.0 expects string values for 'task', 'context', and 'coworker'
2. The delegation examples in the tasks.yaml file were using nested dictionaries
3. The template variables in the task description caused conflicts with JSON examples

#### Fix Implementation:

1. Updated tasks.yaml to use proper delegation format:
   ```yaml
   Delegation format with these exact fields:
   task - what to do (must be a string, not a dictionary)
   context - details and background (must be a string, not a dictionary)
   coworker - agent name (must be a string with an exact agent name)
   ```

2. Simplified JSON examples to avoid template variable conflicts:
   ```yaml
   Example of correct JSON format for delegation:
   task - "Calculate the total sales for the past month"
   context - "User wants to know sales figures"
   coworker - "Data Q&A Expert"
   ```

### Knowledge Configuration

For the RAG knowledge integration, we needed to fix:

1. The knowledge directory structure and file setup
2. Import paths for `Knowledge` class
3. File access paths and error handling

#### Fix Implementation:

1. Implemented fallback imports for the Knowledge class:
   ```python
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
   except ImportError as e:
       print(f"Warning: Could not set up knowledge: {e}")
       knowledge = None
   ```

2. Created empty knowledge files to be populated with real data:
   - sales_analysis.md
   - database_schemas.md
   - customer_insights.md

These changes successfully addressed the compatibility issues with CrewAI v0.108.0, allowing the application to run correctly with delegation between agents working as expected.

## Next Steps

1. Populate knowledge files with real business data
2. Configure actual database connections in .env
3. Test the system with real queries against the database
4. Document any additional issues that emerge during testing