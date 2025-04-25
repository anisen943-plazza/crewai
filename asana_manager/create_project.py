#!/usr/bin/env python3
"""
Create Project Tool

This script creates a new project in Asana.

Usage:
  python create_project.py --name "Project Name" [--notes "Project Notes"] [--workspace-gid GID] [--team-gid GID]
  
Options:
  --name NAME           Name of the project to create (required)
  --notes NOTES         Optional notes/description for the project
  --workspace-gid GID   Specific workspace to create the project in (optional)
  --team-gid GID        Specific team to associate with the project (optional)
  --output-format FORMAT  Output format (text or json, default: text)
  --help                Show this help message
"""

import sys
import argparse
import json
from src.asana_manager.tools.asana_tools import CreateProjectTool

def main():
    parser = argparse.ArgumentParser(
        description="Create a new project in Asana."
    )
    
    # Required arguments
    parser.add_argument(
        "--name",
        required=True,
        help="Name of the project to create"
    )
    
    # Optional arguments
    parser.add_argument(
        "--notes",
        default="",
        help="Optional notes/description for the project"
    )
    parser.add_argument(
        "--workspace-gid",
        help="Specific workspace to create the project in (optional)"
    )
    parser.add_argument(
        "--team-gid",
        help="Specific team to associate with the project (optional)"
    )
    parser.add_argument(
        "--output-format",
        choices=["text", "json"],
        default="text",
        help="Output format (text or json, default: text)"
    )
    
    args = parser.parse_args()
    
    print(f"🛠️ Creating new project: '{args.name}'...")
    
    # Use CreateProjectTool to create the project
    tool = CreateProjectTool()
    result = tool._run(
        name=args.name,
        notes=args.notes,
        workspace_gid=args.workspace_gid,
        team_gid=args.team_gid
    )
    
    # Handle the result based on the desired output format
    if args.output_format == "json":
        print(json.dumps(result, indent=2))
        return
    
    # Handle potential errors
    if isinstance(result, dict) and "error" in result:
        print(f"❌ Error: {result['error']}")
        sys.exit(1)
    
    # Format and display the project information in text format
    if isinstance(result, dict) and "data" in result:
        project_data = result["data"]
        
        # Debug output to see the structure
        print(f"   Project data structure: {json.dumps(project_data, indent=2)[:200]}...")
        
        # Handle Asana API response structure - data might be nested differently
        if isinstance(project_data, dict):
            project = project_data
        else:
            print("❌ Unexpected project data format")
            sys.exit(1)
        
        print(f"\n✅ Project created successfully!")
        
        # Access project attributes with error handling
        if 'name' in project:
            print(f"   Name: {project['name']}")
        else:
            print(f"   Name: Not found in response")
            
        if 'gid' in project:
            project_gid = project['gid']
            print(f"   GID: {project_gid}")
            print(f"   URL: https://app.asana.com/0/{project_gid}")
        else:
            print(f"   GID: Not found in response")
            
        if "notes" in project and project["notes"]:
            print(f"   Notes: {project['notes']}")
    else:
        print("❌ Unexpected result format")
        sys.exit(1)

if __name__ == "__main__":
    main()