"""
Compatibility module for CrewAI tools.

This module provides compatibility layers for different versions of CrewAI and LangChain.
"""

import importlib
import inspect
from typing import Optional, Type, Dict, Any, List, Union

# Try to get BaseTool from crewai.tools first
try:
    from crewai.tools import BaseTool
    CREWAI_TOOLS_BASETOOL_AVAILABLE = True
except ImportError:
    # If that fails, get it from langchain.tools
    try:
        from langchain.tools import BaseTool
        CREWAI_TOOLS_BASETOOL_AVAILABLE = False
    except ImportError:
        # If both fail, try langchain_core.tools (newer LangChain versions)
        try:
            from langchain_core.tools import BaseTool
            CREWAI_TOOLS_BASETOOL_AVAILABLE = False
        except ImportError:
            # If all imports fail, raise an error
            raise ImportError(
                "Could not import BaseTool from crewai.tools, langchain.tools, "
                "or langchain_core.tools. Please ensure you have either crewai with tools "
                "support or langchain installed."
            )

def ensure_crewai_tools_basetool():
    """
    Ensure that crewai.tools.__init__.py has the BaseTool import.
    
    This function will attempt to add the import to crewai.tools.__init__.py
    if it's missing. This is a workaround for some CrewAI installations
    where the re-export is missing.
    """
    if CREWAI_TOOLS_BASETOOL_AVAILABLE:
        # BaseTool is already available from crewai.tools
        return
    
    try:
        import crewai.tools
        tools_init_path = inspect.getfile(crewai.tools)
        
        # Read the current content
        with open(tools_init_path, 'r') as f:
            content = f.read()
        
        # Check if the import is already there
        if 'from langchain.tools import BaseTool' in content:
            return
        
        # Add the import
        with open(tools_init_path, 'a') as f:
            f.write('\n# Added by plazza_analytics compatibility layer\n')
            f.write('from langchain.tools import BaseTool\n')
        
        # Reload the module to apply the changes
        importlib.reload(crewai.tools)
        
        print("✅ Added BaseTool import to crewai.tools.__init__.py")
    except Exception as e:
        print(f"⚠️ Could not add BaseTool import to crewai.tools: {str(e)}")
        print("Using langchain.tools.BaseTool directly instead.")