# Asana Manager

A CrewAI-powered assistant that helps you manage Asana projects and tasks. This project demonstrates how to build AI agents that interact with the Asana API to create projects, tasks, and manage them effectively.

## Features

- Create Asana projects programmatically
- Add tasks with due dates
- Browse projects and tasks
- List users in your workspace
- Auto-discovery of your Asana workspaces and teams
- Full Asana API integration with proper error handling

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. 

1. Clone the repository and navigate to the project directory:

```bash
cd asana_manager
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

If requirements.txt doesn't exist, install these core dependencies:

```bash
pip install "crewai[tools]>=0.102.0,<1.0.0" python-dotenv pyyaml requests
```

## Configuration

The project can use environment variables from:

1. The Master ENV file at `/Users/aniruddhasen/Projects/Master_ENV/.env`
2. A local `.env` file in the project root
3. System environment variables

Required environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for CrewAI agents
- `ASANA_API_TOKEN`: Your Asana Personal Access Token

### Getting an Asana API Token

1. Go to your Asana account settings: https://app.asana.com/0/my-apps
2. Create a new personal access token
3. Copy the token and add it to your environment variables

## Running the Project

To use the Asana Manager:

```bash
cd /Users/aniruddhasen/Projects/CrewAI/asana_manager
python -m src.asana_manager.main
```

The AI agent will:
1. List your available Asana workspaces
2. List teams in your workspace (required for creating projects in Asana)
3. Create a new "Q2 Launch Plan" project in your default workspace
4. Add three tasks: Planning, Execution, and Review
5. Set deadlines for each task (3, 7, and 10 days from today)
6. Return the project ID and task details

### Important Note About Teams

Asana requires a team_gid when creating a project. The system now automatically:
1. Discovers your available workspaces
2. Finds teams within that workspace
3. Uses the first team found for creating projects

If you want to specify a different team, you can modify the input parameters in main.py.

## Customizing

You can customize the project by modifying:

- `config/agents.yaml`: Define agent roles, goals, backstory, and available tools
- `config/tasks.yaml`: Define tasks for the agents to perform
- `main.py`: Change default project names or task structures

## Available Tools

The system includes the following Asana tools:

1. **ListWorkspacesTool**: Find all workspaces you have access to
2. **ListTeamsTool**: Find all teams in a workspace (required for project creation)
3. **CreateProjectTool**: Create new Asana projects (requires team_gid)
4. **CreateTaskTool**: Add tasks to projects
5. **SetDueDateTool**: Set due dates for tasks
6. **AssignTaskTool**: Assign tasks to users
7. **BrowseProjectTool**: View project details and tasks
8. **ListUsersTool**: View all users in a workspace
9. **FindProjectByNameTool**: Find projects by name across workspaces
10. **CompareTasksWithDocumentationTool**: Compare project tasks with markdown checklist items

All tools use real Asana API calls with comprehensive error handling.

## Project Tools

The project includes two powerful standalone tools for working with Asana projects and documentation:

### 1. Markdown to Asana Tool

Create complete Asana projects directly from structured markdown files:

```bash
python create_project_from_markdown.py --create-project --markdown-file checklist.md --project-name "New Project"
```

Generate template markdown files to use as starting points:

```bash
python create_project_from_markdown.py --create-template --template-output template.md --template-type software
```

### 2. Project Comparison Tool

Compare existing Asana projects with markdown documentation:

```bash
# Using project GID directly (recommended method):
python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md"

# Alternatively, using project name (slower, searches across workspaces):
python compare_project.py --project-name "Project Name" "/path/to/documentation.md"
```

### Key Features

- **Direct GID Access**: Use project GID for faster, more reliable project access
- **Smart Matching**: Uses intelligent similarity matching to identify tasks that correspond between systems
- **Comprehensive Reports**: Generates detailed reports showing missing tasks and completion status
- **Action-Oriented**: Provides recommendations for synchronizing Asana with documentation
- **Flexible Output**: Supports both detailed and summary reporting modes
- **JSON Export**: Can generate JSON files for missing tasks
- **Direct Updates**: Can automatically add missing checklist items to Asana

### Advanced Usage

```bash
# Show only a summary report
python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --summary-only

# Generate a JSON file with missing tasks
python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --generate-json

# Adjust the similarity threshold (0.0-1.0)
python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --similarity 0.7

# Show detailed logs
python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --verbose

# Automatically add missing tasks to Asana (with confirmation)
python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --update-asana
```

### Markdown Format Requirements

#### For Project Creation

The markdown-to-Asana tool uses a specific structure to create projects with the proper hierarchy:

```markdown
## Implementation Checklist

### Section Name
- [ ] Task 1
- [ ] Task 2

#### Subsection Name
- [ ] Subtask 1
- [x] Subtask 2 (already completed)
```

This creates:
- A section named "Section Name"
- Two tasks: "Task 1" and "Task 2" in that section
- A task named "Subsection Name" in that section
- Two subtasks: "Subtask 1" and "Subtask 2" (marked complete) under the "Subsection Name" task

#### For Project Comparison

The comparison tool now supports various markdown formats through template specification:

1. **Standard Format** (default):
   ```markdown
   - [ ] Uncompleted task description
   - [x] Completed task description
   ```

2. **Headings Format**:
   ```markdown
   ### Task Name
   #### Subtask Name
   ```

3. **Custom Format** (using a custom regex pattern):
   ```markdown
   Task: My Task | Status: Incomplete
   Task: Another Task | Status: Complete
   ```

Example usage with different formats:
```bash
# Standard format (default)
python compare_project.py --project-gid "1234567890123456" "documentation.md"

# Headings format (extract from ### level 3 headings)
python compare_project.py --project-gid "1234567890123456" "documentation.md" --template headings --heading-level 3

# Custom format (using a regex pattern)
python compare_project.py --project-gid "1234567890123456" "documentation.md" --template custom --pattern "Task: (.+?) \| Status: (.+?)$"

# Only compare a specific section of the document
python compare_project.py --project-gid "1234567890123456" "documentation.md" --section "Implementation Checklist"
```

## Troubleshooting

- **API Token Issues**: Make sure your Asana token is valid and has appropriate permissions
- **Workspace Discovery**: If the tool can't find your workspaces, set the WORKSPACE_GID manually
- **Team Requirements**: Asana requires a team_gid when creating projects. If you see errors about missing team_gid, make sure your account has at least one team in the workspace.
- **API Errors**: The tools include detailed error handling. Check the response for status codes and error messages from the Asana API.
- **Import Errors**: Make sure you're running from the correct directory

## About CrewAI

This project is built on [CrewAI](https://crewai.com), a framework for creating AI agent systems that collaborate to accomplish complex tasks. For more information:

- [CrewAI Documentation](https://docs.crewai.com)
- [GitHub Repository](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)
