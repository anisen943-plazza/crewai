#!/usr/bin/env python3
"""
Browse Project Tool

This script displays sections, tasks, and subtasks in an Asana project.

Usage:
  python browse_project.py --project-gid GID [--output-format FORMAT] [--show-subtasks]
  
Options:
  --project-gid GID       GID of the Asana project to browse
  --output-format FORMAT  Output format (text or json, default: text)
  --show-subtasks         Include subtasks in the output (makes additional API calls)
  --help                  Show this help message
"""

import sys
import argparse
import json
from src.asana_manager.tools.asana_tools import BrowseProjectTool

def main():
    parser = argparse.ArgumentParser(
        description="Browse sections and tasks in an Asana project."
    )
    
    # Required arguments
    parser.add_argument(
        "--project-gid",
        required=True,
        help="GID of the Asana project to browse"
    )
    
    # Optional arguments
    parser.add_argument(
        "--output-format",
        choices=["text", "json"],
        default="text",
        help="Output format (text or json, default: text)"
    )
    
    parser.add_argument(
        "--show-subtasks",
        action="store_true",
        help="Include subtasks in the output"
    )
    
    args = parser.parse_args()
    
    print(f"📋 Browsing project with GID: {args.project_gid}...")
    
    # Use BrowseProjectTool to browse the project
    tool = BrowseProjectTool()
    result = tool._run(
        project_gid=args.project_gid
    )
    
    # Handle the result based on the desired output format
    if args.output_format == "json":
        # Add subtasks to the JSON output if requested
        if args.show_subtasks and isinstance(result, dict) and "tasks" in result:
            import requests
            from src.asana_manager.tools.asana_tools import BASE_URL, HEADERS
            
            tasks = result.get("tasks", [])
            
            # Ensure tasks is a list of dicts, not a dict with 'data' key
            if isinstance(tasks, dict) and 'data' in tasks:
                task_items = tasks['data']
            else:
                task_items = tasks
            
            # Fetch subtasks for each task
            for task in task_items:
                task_data = task.get('data', task)
                if 'gid' in task_data:
                    task_gid = task_data['gid']
                    
                    # Get subtasks
                    try:
                        subtask_url = f"{BASE_URL}/tasks/{task_gid}/subtasks"
                        subtask_response = requests.get(subtask_url, headers=HEADERS)
                        subtask_response.raise_for_status()
                        subtasks = subtask_response.json().get('data', [])
                        
                        # Add subtasks to the task
                        task_data['subtasks'] = subtasks
                    except Exception as e:
                        task_data['subtasks_error'] = str(e)
            
        print(json.dumps(result, indent=2))
        return
    
    # Handle potential errors
    if isinstance(result, dict) and "error" in result:
        print(f"❌ Error: {result['error']}")
        sys.exit(1)
    
    # Format and display the project information in text format
    if isinstance(result, dict) and "project" in result:
        project_data = result["project"]
        sections = result.get("sections", [])
        tasks = result.get("tasks", [])
        
        # Handle Asana API response structure which may include a 'data' wrapper
        project = project_data.get('data', project_data)
        
        print(f"\n📋 Project Details:")
        
        # Debug output to see the actual structure
        print(f"   Project data structure: {json.dumps(project, indent=2)[:200]}...")
        
        # Access name with error handling
        if 'name' in project:
            print(f"   Name: {project['name']}")
        elif isinstance(project, dict) and 'data' in project and 'name' in project['data']:
            print(f"   Name: {project['data']['name']}")
        else:
            print(f"   Name: Unknown (Name key not found in project data)")
            
        # Access gid with error handling    
        if 'gid' in project:
            project_gid = project['gid']
        elif isinstance(project, dict) and 'data' in project and 'gid' in project['data']:
            project_gid = project['data']['gid']
        else:
            project_gid = args.project_gid
            print(f"   GID: {project_gid} (from command line)")
            
        print(f"   GID: {project_gid}")
        
        # Access notes with error handling
        if "notes" in project and project["notes"]:
            print(f"   Notes: {project['notes']}")
        elif isinstance(project, dict) and 'data' in project and 'notes' in project['data']:
            print(f"   Notes: {project['data']['notes']}")
            
        print(f"   URL: https://app.asana.com/0/{project_gid}")
        
        # Handle sections with 'data' wrapper
        section_items = []
        if isinstance(sections, dict) and 'data' in sections:
            section_items = sections['data']
        else:
            section_items = sections
            
        print(f"\n📑 Sections ({len(section_items)}):")
        for i, section_data in enumerate(section_items, 1):
            # Handle possible 'data' wrapper for each section
            section = section_data.get('data', section_data)
            if 'name' in section and 'gid' in section:
                print(f"{i}. {section['name']} (GID: {section['gid']})")
            else:
                print(f"{i}. Section data format not as expected: {section}")
        
        # Handle tasks with 'data' wrapper
        task_items = []
        if isinstance(tasks, dict) and 'data' in tasks:
            task_items = tasks['data']
        else:
            task_items = tasks
            
        print(f"\n✓ Tasks ({len(task_items)}):")
        for i, task_data in enumerate(task_items, 1):
            # Handle possible 'data' wrapper for each task
            task = task_data.get('data', task_data)
            
            # Debug the first task data structure if available
            if i == 1:
                print(f"   First task data structure: {json.dumps(task, indent=2)[:200]}...")
            
            # Try to get task attributes with error handling
            status = "✅" if task.get("completed", False) else "⬜"
            section_name = task.get("section_name", "No Section")
            
            # Handle assignee which might be nested
            assignee = task.get("assignee", {})
            assignee_name = "Unassigned"
            if isinstance(assignee, dict) and 'name' in assignee:
                assignee_name = assignee['name']
            
            due_date = task.get("due_on", "No due date")
            
            # Access task name and gid with error handling
            if 'name' in task and 'gid' in task:
                print(f"{i}. {status} {task['name']}")
                print(f"   GID: {task['gid']}")
            else:
                print(f"{i}. {status} Task name not found")
                if 'gid' in task:
                    print(f"   GID: {task['gid']}")
                    
            print(f"   Section: {section_name}")
            print(f"   Assignee: {assignee_name}")
            print(f"   Due Date: {due_date}")
            
            # Get subtasks if requested
            if args.show_subtasks:
                print(f"   Subtasks:")
                subtask_url = f"{BASE_URL}/tasks/{task['gid']}/subtasks"
                try:
                    import requests
                    from src.asana_manager.tools.asana_tools import BASE_URL, HEADERS
                    
                    subtask_response = requests.get(subtask_url, headers=HEADERS)
                    subtask_response.raise_for_status()
                    subtasks = subtask_response.json().get('data', [])
                    
                    if subtasks:
                        for i, subtask in enumerate(subtasks, 1):
                            subtask_status = "✅" if subtask.get("completed", False) else "⬜"
                            print(f"      {i}. {subtask_status} {subtask['name']} (GID: {subtask['gid']})")
                    else:
                        print("      No subtasks found")
                except Exception as e:
                    print(f"      Error retrieving subtasks: {e}")
            
            print()
    else:
        print("❌ Unexpected result format")
        sys.exit(1)

if __name__ == "__main__":
    main()