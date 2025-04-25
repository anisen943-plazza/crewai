#!/usr/bin/env python3
"""
List All Asana Projects Tool

This tool lists all projects across all accessible Asana workspaces.
Provides a clear, organized view of all projects with their GIDs.

Usage:
  python -m src.asana_manager.tools.list_all_projects
  
Options:
  --format [text|json]  Output format (default: text)
  --workspace GID       Only list projects in this workspace
"""

import os
import sys
import json
import argparse
import requests
from typing import Dict, List, Any

# Add the proper paths to sys.path to make imports work
from pathlib import Path
current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
src_dir = current_dir.parent.parent.parent  # Navigate up to src directory
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

# Import from asana_tools
from src.asana_manager.tools.asana_tools import (
    ListWorkspacesTool, HEADERS, BASE_URL
)

class ListAllProjectsTool:
    """Tool for listing all projects across all Asana workspaces."""
    
    def run(self, workspace_gid: str = None, output_format: str = "text") -> Dict[str, Any]:
        """
        List all projects across all workspaces or in a specific workspace.
        
        Args:
            workspace_gid: Optional workspace GID to filter projects
            output_format: Output format ("text" or "json")
            
        Returns:
            Dictionary with workspaces and their projects
        """
        # Initialize the workspaces tool
        workspaces_tool = ListWorkspacesTool()
        
        # Get all workspaces if no specific workspace provided
        if workspace_gid:
            workspaces = [{"gid": workspace_gid, "name": "Specified Workspace"}]
        else:
            workspaces_result = workspaces_tool._run()
            if "data" not in workspaces_result:
                return {"error": f"Failed to list workspaces: {workspaces_result.get('error', 'Unknown error')}"}
            workspaces = workspaces_result["data"]
        
        # Store all results
        result = {
            "workspaces": []
        }
        total_projects = 0
        
        # For each workspace, get all projects
        for workspace in workspaces:
            workspace_info = {
                "name": workspace["name"],
                "gid": workspace["gid"],
                "projects": []
            }
            
            # Get projects in this workspace
            url = f"{BASE_URL}/projects?workspace={workspace['gid']}&limit=100"
            response = requests.get(url, headers=HEADERS)
            
            if response.status_code == 200:
                projects_data = response.json()
                
                if "data" in projects_data:
                    workspace_info["projects"] = projects_data["data"]
                    total_projects += len(projects_data["data"])
            else:
                workspace_info["error"] = f"Status: {response.status_code} - {response.text}"
            
            result["workspaces"].append(workspace_info)
        
        result["total_projects"] = total_projects
        
        # Format and display the result based on output_format
        if output_format == "text":
            self._display_text_output(result)
        
        return result
    
    def _display_text_output(self, result: Dict[str, Any]) -> None:
        """Display the result in a human-readable text format."""
        if "error" in result:
            print(f"❌ Error: {result['error']}")
            return
        
        print(f"📊 Found {result['total_projects']} projects across {len(result['workspaces'])} workspaces\n")
        
        for workspace in result["workspaces"]:
            print(f"📁 Workspace: {workspace['name']} (GID: {workspace['gid']})")
            
            if "error" in workspace:
                print(f"  ❌ Error: {workspace['error']}")
                continue
            
            if workspace["projects"]:
                print(f"  Found {len(workspace['projects'])} projects:")
                for i, project in enumerate(workspace["projects"]):
                    print(f"  {i+1}. {project['name']} (GID: {project['gid']})")
            else:
                print("  No projects found in this workspace")
            
            print()  # Add a newline between workspaces

def main():
    """Main function to run the tool from command line."""
    parser = argparse.ArgumentParser(description="List all projects across Asana workspaces")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                        help="Output format (text or json)")
    parser.add_argument("--workspace", help="Only list projects in this workspace GID")
    
    args = parser.parse_args()
    
    # Create and run the tool
    tool = ListAllProjectsTool()
    result = tool.run(workspace_gid=args.workspace, output_format=args.format)
    
    # Output JSON if requested
    if args.format == "json":
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()