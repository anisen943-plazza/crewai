#!/usr/bin/env python3
"""
CrewAI Tools Verification Script

This script checks your CrewAI installation to diagnose BaseTool import issues.
Run it on both your Mac and MacBook to compare environments.
"""

import os
import sys
import inspect
import importlib.util
from pathlib import Path

def print_header(text):
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"  {text}")
    print(f"{'=' * 60}")

def check_imports():
    """Check if various imports are available."""
    print_header("IMPORT AVAILABILITY CHECK")
    
    # Check crewai
    try:
        import crewai
        print(f"✅ crewai is installed (version: {crewai.__version__})")
    except ImportError:
        print("❌ crewai is not installed")
        return
    except AttributeError:
        print("⚠️ crewai is installed but version number could not be determined")

    # Check crewai.tools
    try:
        import crewai.tools
        print(f"✅ crewai.tools is available")
        print(f"  📍 Located at: {inspect.getfile(crewai.tools)}")
    except ImportError:
        print("❌ crewai.tools is not available")
        return

    # Check BaseTool in crewai.tools
    try:
        from crewai.tools import BaseTool
        print(f"✅ crewai.tools.BaseTool is available")
        print(f"  📍 BaseTool defined in: {inspect.getfile(BaseTool)}")
    except ImportError:
        print("❌ BaseTool cannot be imported from crewai.tools")

    # Check langchain
    try:
        import langchain
        print(f"✅ langchain is installed")
    except ImportError:
        print("❌ langchain is not installed")
        return

    # Check langchain.tools
    try:
        import langchain.tools
        print(f"✅ langchain.tools is available")
    except ImportError:
        print("❌ langchain.tools is not available")
        return

    # Check BaseTool in langchain.tools
    try:
        from langchain.tools import BaseTool as LangchainBaseTool
        print(f"✅ langchain.tools.BaseTool is available")
        print(f"  📍 Located at: {inspect.getfile(LangchainBaseTool)}")
    except ImportError:
        print("❌ BaseTool cannot be imported from langchain.tools")

def check_crewai_tools_content():
    """Check the content of crewai/tools/__init__.py."""
    print_header("CREWAI TOOLS MODULE INSPECTION")
    
    try:
        import crewai.tools
        tools_dir = Path(inspect.getfile(crewai.tools)).parent
        init_file = tools_dir / "__init__.py"
        
        if not init_file.exists():
            print(f"❌ Cannot locate __init__.py file at {init_file}")
            return
            
        print(f"✅ Found __init__.py at {init_file}")
        
        # Read the file content
        with open(init_file, 'r') as f:
            content = f.read()
            
        print(f"\n📄 Content of {init_file.name}:")
        print(f"\n{content}")
        
        # Check for BaseTool import
        if "from langchain.tools import BaseTool" in content:
            print("\n✅ Found 'from langchain.tools import BaseTool' in __init__.py")
        else:
            print("\n❌ 'from langchain.tools import BaseTool' is MISSING from __init__.py")
            print("   This is likely why you can't import BaseTool from crewai.tools")
    
    except Exception as e:
        print(f"❌ Error examining crewai.tools: {str(e)}")

def check_dir_contents():
    """Print the contents of dir() for relevant modules."""
    print_header("MODULE CONTENTS CHECK")
    
    try:
        import crewai.tools
        print("📋 dir(crewai.tools):")
        for item in sorted(dir(crewai.tools)):
            if not item.startswith('__'):
                print(f"  - {item}")
                
        print("\n'BaseTool' in dir(crewai.tools):", 'BaseTool' in dir(crewai.tools))
    except ImportError:
        print("❌ Cannot import crewai.tools to check contents")
    
    try:
        import langchain.tools
        print("\n📋 dir(langchain.tools):")
        for item in sorted(dir(langchain.tools)):
            if not item.startswith('__') and not item.startswith('_'):
                print(f"  - {item}")
                
        print("\n'BaseTool' in dir(langchain.tools):", 'BaseTool' in dir(langchain.tools))
    except ImportError:
        print("❌ Cannot import langchain.tools to check contents")

def check_python_env():
    """Display information about the Python environment."""
    print_header("PYTHON ENVIRONMENT")
    
    print(f"Python version: {sys.version}")
    print(f"Executable path: {sys.executable}")
    
    try:
        import site
        print(f"Site packages: {site.getsitepackages()}")
    except:
        print("Could not determine site packages location")

def main():
    """Run all verification checks."""
    print("\n🔍 CREWAI TOOLS VERIFICATION SCRIPT 🔍")
    print(f"Running on: {os.uname().nodename}")
    print(f"Date: {os.popen('date').read().strip()}")
    
    check_python_env()
    check_imports()
    check_dir_contents()
    check_crewai_tools_content()
    
    print("\n✨ Verification complete! ✨")
    print("Compare these results between your Mac and MacBook to identify differences")
    print("If 'from langchain.tools import BaseTool' is missing in __init__.py,")
    print("you can manually add it to fix the import issue.")

if __name__ == "__main__":
    main()