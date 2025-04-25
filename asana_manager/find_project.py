#!/usr/bin/env python3
"""
Find Project By Name Tool

This script finds an Asana project by its name across all workspaces or in a specified workspace.

Usage:
  python find_project.py --project-name "Project Name" [--workspace-gid GID] [--output-format FORMAT]
  
Options:
  --project-name NAME     Name (or partial name) of the project to find
  --workspace-gid GID     Specific workspace to search in (optional)
  --output-format FORMAT  Output format (text or json, default: text)
  --help                  Show this help message
"""

import sys
import argparse
import json
from src.asana_manager.tools.asana_tools import FindProjectByNameTool

def main():
    parser = argparse.ArgumentParser(
        description="Find an Asana project by name across all workspaces or in a specified workspace."
    )
    
    # Required arguments
    parser.add_argument(
        "--project-name",
        required=True,
        help="Name (or partial name) of the project to find"
    )
    
    # Optional arguments
    parser.add_argument(
        "--workspace-gid",
        help="Specific workspace to search in (optional)"
    )
    parser.add_argument(
        "--output-format",
        choices=["text", "json"],
        default="text",
        help="Output format (text or json, default: text)"
    )
    
    args = parser.parse_args()
    
    print(f"🔍 Searching for projects with name: '{args.project_name}'...")
    
    # Use FindProjectByNameTool to find the project
    tool = FindProjectByNameTool()
    result = tool._run(
        project_name=args.project_name,
        workspace_gid=args.workspace_gid
    )
    
    # Handle the result based on the desired output format
    if args.output_format == "json":
        print(json.dumps(result, indent=2))
        return
    
    # Handle potential errors
    if isinstance(result, dict) and "error" in result:
        print(f"❌ Error: {result['error']}")
        sys.exit(1)
    
    # Format and display the matches in text format
    if isinstance(result, dict) and "matches" in result:
        matches = result["matches"]
        if not matches:
            print("🔍 No matching projects found.")
            sys.exit(0)
        
        print(f"\n✅ Found {len(matches)} matching project(s):\n")
        
        for i, project_data in enumerate(matches, 1):
            # Handle potential nested 'data' structure
            project = project_data.get('data', project_data)
            
            # Debug the first project structure
            if i == 1:
                print(f"   First project data structure: {json.dumps(project, indent=2)[:200]}...")
            
            # Access project attributes with error handling
            if 'name' in project:
                print(f"{i}. Project: {project['name']}")
            else:
                print(f"{i}. Project: Name not found")
                
            if 'gid' in project:
                project_gid = project['gid']
                print(f"   GID: {project_gid}")
                print(f"   URL: https://app.asana.com/0/{project_gid}")
            else:
                print(f"   GID: Not found")
            
            # Handle nested workspace data
            if 'workspace' in project and isinstance(project['workspace'], dict):
                ws_name = project['workspace'].get('name', 'Unknown')
                print(f"   Workspace: {ws_name}")
            
            # Handle nested team data
            if "team" in project and project["team"] and isinstance(project["team"], dict):
                team_name = project["team"].get('name', 'Unknown')
                print(f"   Team: {team_name}")
            
            print()
    else:
        print("❌ Unexpected result format")
        sys.exit(1)

if __name__ == "__main__":
    main()