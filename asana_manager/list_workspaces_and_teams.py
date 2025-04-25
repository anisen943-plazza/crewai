#!/usr/bin/env python3
"""
List Workspaces and Teams Tool

This script lists Asana workspaces and teams that the authenticated user has access to.

Usage:
  python list_workspaces_and_teams.py [--workspace-gid GID] [--output-format FORMAT]
  
Options:
  --workspace-gid GID     Specific workspace to list teams from (optional)
  --output-format FORMAT  Output format (text or json, default: text)
  --list-type TYPE        What to list (workspaces, teams, or both, default: both)
  --help                  Show this help message
"""

import sys
import argparse
import json
from src.asana_manager.tools.asana_tools import ListWorkspacesTool, ListTeamsTool

def main():
    parser = argparse.ArgumentParser(
        description="List Asana workspaces and teams that the authenticated user has access to."
    )
    
    # Optional arguments
    parser.add_argument(
        "--workspace-gid",
        help="Specific workspace to list teams from (optional)"
    )
    parser.add_argument(
        "--output-format",
        choices=["text", "json"],
        default="text",
        help="Output format (text or json, default: text)"
    )
    parser.add_argument(
        "--list-type",
        choices=["workspaces", "teams", "both"],
        default="both",
        help="What to list (workspaces, teams, or both, default: both)"
    )
    
    args = parser.parse_args()
    
    # Initialize results dictionary
    results = {}
    
    # List workspaces if requested
    if args.list_type in ["workspaces", "both"]:
        print("🔍 Listing Asana workspaces...")
        workspaces_tool = ListWorkspacesTool()
        workspaces_result = workspaces_tool._run()
        
        # Handle potential errors
        if isinstance(workspaces_result, dict) and "error" in workspaces_result:
            print(f"❌ Error listing workspaces: {workspaces_result['error']}")
            sys.exit(1)
        
        results["workspaces"] = workspaces_result
    
    # List teams if requested
    if args.list_type in ["teams", "both"]:
        if args.list_type == "both" and "workspaces" in results and "data" in results["workspaces"]:
            # If we're listing both and found workspaces, list teams for each workspace
            teams_by_workspace = {}
            
            for workspace in results["workspaces"]["data"]:
                workspace_gid = workspace["gid"]
                workspace_name = workspace["name"]
                print(f"🔍 Listing teams in workspace: {workspace_name} ({workspace_gid})...")
                
                teams_tool = ListTeamsTool()
                teams_result = teams_tool._run(workspace_gid=workspace_gid)
                
                # Skip if there was an error but continue with other workspaces
                if isinstance(teams_result, dict) and "error" in teams_result:
                    print(f"⚠️ Error listing teams in workspace {workspace_name}: {teams_result['error']}")
                    teams_by_workspace[workspace_gid] = {"error": teams_result["error"], "workspace_name": workspace_name}
                else:
                    teams_by_workspace[workspace_gid] = {
                        "workspace_name": workspace_name,
                        "teams": teams_result
                    }
            
            results["teams_by_workspace"] = teams_by_workspace
        else:
            # If just listing teams or no workspaces found, use the specified workspace
            print(f"🔍 Listing teams in specified workspace...")
            teams_tool = ListTeamsTool()
            teams_result = teams_tool._run(workspace_gid=args.workspace_gid)
            
            # Handle potential errors
            if isinstance(teams_result, dict) and "error" in teams_result:
                print(f"❌ Error listing teams: {teams_result['error']}")
                sys.exit(1)
            
            results["teams"] = teams_result
    
    # Handle the result based on the desired output format
    if args.output_format == "json":
        print(json.dumps(results, indent=2))
        return
    
    # Format and display the information in text format
    if args.list_type in ["workspaces", "both"] and "workspaces" in results:
        workspaces = results["workspaces"].get("data", [])
        print(f"\n🏢 Workspaces ({len(workspaces)}):")
        for i, workspace in enumerate(workspaces, 1):
            print(f"{i}. {workspace['name']}")
            print(f"   GID: {workspace['gid']}")
            print()
    
    if args.list_type in ["teams", "both"]:
        if "teams_by_workspace" in results:
            # Display teams organized by workspace
            for workspace_gid, workspace_data in results["teams_by_workspace"].items():
                workspace_name = workspace_data["workspace_name"]
                
                if "error" in workspace_data:
                    print(f"\n👥 Teams in workspace '{workspace_name}':")
                    print(f"   ⚠️ Error: {workspace_data['error']}")
                    continue
                
                teams = workspace_data["teams"].get("data", [])
                print(f"\n👥 Teams in workspace '{workspace_name}' ({len(teams)}):")
                
                if not teams:
                    print("   No teams found in this workspace")
                    continue
                
                for i, team in enumerate(teams, 1):
                    print(f"   {i}. {team['name']}")
                    print(f"      GID: {team['gid']}")
        elif "teams" in results:
            # Display teams for a single workspace
            teams = results["teams"].get("data", [])
            print(f"\n👥 Teams ({len(teams)}):")
            
            if not teams:
                print("   No teams found")
            else:
                for i, team in enumerate(teams, 1):
                    print(f"{i}. {team['name']}")
                    print(f"   GID: {team['gid']}")
                    print()

if __name__ == "__main__":
    main()