#!/usr/bin/env python3
"""
Markdown to Asana Project Creator

This script creates an Asana project from a markdown document containing
implementation checklists.

Usage:
  python create_project_from_markdown.py <markdown_file> <project_name>
  
Options:
  --workspace-gid GID   Specify Asana workspace GID (optional)
  --team-gid GID        Specify Asana team GID (optional)
  --create-template     Create a template markdown file (specify output path)
  --template-type TYPE  Type of template to create (generic, software, marketing)
  --help                Show this help message
"""

import os
import sys
import argparse
from src.asana_manager.tools.markdown_to_asana import MarkdownToAsanaTool, CreateTemplateMdFileTool

def main():
    parser = argparse.ArgumentParser(
        description="Create an Asana project from a markdown document containing implementation checklists."
    )
    
    # Create two mutually exclusive argument groups
    action_group = parser.add_mutually_exclusive_group(required=True)
    
    # Group 1: Create project from markdown
    action_group.add_argument(
        "--create-project",
        action="store_true",
        help="Create a project from a markdown file"
    )
    
    # Group 2: Create a template markdown file
    action_group.add_argument(
        "--create-template",
        action="store_true",
        help="Create a template markdown file"
    )
    
    # Arguments for creating a project
    parser.add_argument(
        "--markdown-file",
        help="Path to the markdown file containing implementation checklist"
    )
    parser.add_argument(
        "--project-name",
        help="Name of the Asana project to create"
    )
    parser.add_argument(
        "--workspace-gid",
        help="Asana workspace GID (optional)"
    )
    parser.add_argument(
        "--team-gid",
        help="Asana team GID (optional)"
    )
    
    # Arguments for creating a template
    parser.add_argument(
        "--template-output",
        help="Path to save the template markdown file"
    )
    parser.add_argument(
        "--template-type",
        choices=["generic", "software", "marketing"],
        default="generic",
        help="Type of template to create (generic, software, marketing)"
    )
    
    args = parser.parse_args()
    
    if args.create_project:
        # Validate required arguments
        if not args.markdown_file:
            parser.error("--markdown-file is required with --create-project")
        if not args.project_name:
            parser.error("--project-name is required with --create-project")
        
        # Check if the markdown file exists
        if not os.path.exists(args.markdown_file):
            print(f"❌ Markdown file not found: {args.markdown_file}")
            sys.exit(1)
        
        print(f"📝 Creating Asana project from markdown file: {args.markdown_file}")
        
        # Use the MarkdownToAsanaTool to create the project
        tool = MarkdownToAsanaTool()
        result = tool._run(
            markdown_file_path=args.markdown_file,
            project_name=args.project_name,
            workspace_gid=args.workspace_gid,
            team_gid=args.team_gid
        )
        
        # Handle the result
        if isinstance(result, dict) and "error" in result:
            print(f"❌ Error: {result['error']}")
            sys.exit(1)
        
        # Print the success message
        print("\n✅ Asana project created successfully!")
        print(f"   Project Name: {result['project_name']}")
        print(f"   Project URL: {result['project_url']}")
        print("\n📊 Statistics:")
        for key, value in result['statistics'].items():
            print(f"   - {key.replace('_', ' ').title()}: {value}")
    
    elif args.create_template:
        # Validate required arguments
        if not args.template_output:
            parser.error("--template-output is required with --create-template")
        
        print(f"📝 Creating {args.template_type} template markdown file: {args.template_output}")
        
        # Use the CreateTemplateMdFileTool to create the template
        tool = CreateTemplateMdFileTool()
        result = tool._run(
            output_path=args.template_output,
            project_type=args.template_type
        )
        
        # Handle the result
        if isinstance(result, dict) and "error" in result:
            print(f"❌ Error: {result['error']}")
            sys.exit(1)
        
        # Print the success message
        print(f"\n✅ Template created successfully at: {result['file_path']}")
        print(f"   Project Type: {result['project_type']}")

if __name__ == "__main__":
    main()