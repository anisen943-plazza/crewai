#!/usr/bin/env python3
"""
Asana Project Lister

This script lists all projects across all your Asana workspaces.
Provides a clear, organized list with project names and GIDs.

Usage:
  python list_projects.py
  
Options:
  --format [text|json]  Output format (default: text)
  --workspace GID       Only list projects in this workspace
"""

import sys
from src.asana_manager.tools.list_all_projects import main

if __name__ == "__main__":
    # Forward all command line arguments to the main function
    sys.exit(main())