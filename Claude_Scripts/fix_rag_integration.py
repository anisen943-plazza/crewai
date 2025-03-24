#!/usr/bin/env python3
"""
Script to fix the RAG integration in the CrewAI sales analysis system.
This implements the solution outlined in CLAUDE.md.
"""

import os
import sys
import shutil
from pathlib import Path

# Project constants
PROJECT_ROOT = Path(__file__).parent
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
SOURCE_FILE = PROJECT_ROOT / "sales_ai_run_result.md"
TARGET_FILE = KNOWLEDGE_DIR / "sales_analysis_results.md"

def create_knowledge_directory():
    """Create the knowledge directory if it doesn't exist."""
    if not KNOWLEDGE_DIR.exists():
        print(f"Creating knowledge directory at {KNOWLEDGE_DIR}")
        KNOWLEDGE_DIR.mkdir(exist_ok=True)
        return True
    else:
        print(f"Knowledge directory already exists at {KNOWLEDGE_DIR}")
        return True

def copy_analysis_results():
    """Copy the analysis results to the knowledge directory."""
    if not SOURCE_FILE.exists():
        print(f"Error: Source file {SOURCE_FILE} not found!")
        return False
    
    print(f"Copying {SOURCE_FILE} to {TARGET_FILE}")
    shutil.copy2(SOURCE_FILE, TARGET_FILE)
    return True

def update_sales_ai_code():
    """Generate code to fix the RAG integration in sales_ai.py."""
    knowledge_import_fix = """
# Modified Knowledge integration - fixed path handling
def create_knowledge_source():
    \"\"\"Create a knowledge source from the analysis results file.\"\"\"
    knowledge_file = 'sales_analysis_results.md'  # Relative path - will be prefixed with 'knowledge/'
    knowledge_path = os.path.join('knowledge', knowledge_file)
    
    # Check if the file exists
    if os.path.exists(knowledge_path):
        # First copy the latest content to knowledge directory
        shutil.copy2(ANALYSIS_RESULTS_PATH, knowledge_path)
        
        print(f"Creating knowledge source from {knowledge_file}")
        from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
        from crewai.knowledge.knowledge import Knowledge
        
        # Use relative path that will work with CrewAI's knowledge directory structure
        markdown_source = TextFileKnowledgeSource(
            file_paths=[knowledge_file],  # Just the filename, CrewAI will prepend "knowledge/"
            chunk_size=800,
            chunk_overlap=200,
            metadata={"source": "sales_analysis", "date": os.path.getmtime(knowledge_path)}
        )
        
        # Create the knowledge object
        return Knowledge(
            collection_name="sales_analysis",
            sources=[markdown_source]
        )
    else:
        print(f"Warning: Knowledge file {knowledge_path} not found")
        return None

# Create knowledge source
sales_knowledge = create_knowledge_source()
"""
    
    save_results_fix = """
def save_analysis_results(content, filepath=ANALYSIS_RESULTS_PATH):
    \"\"\"
    Save the analysis results to a file for future reference.
    Also saves a copy to the knowledge directory for RAG.
    
    Args:
        content (str): The analysis results to save
        filepath (str): The path to save the results to
    \"\"\"
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Add timestamp and metadata to help with retrieval
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format the content with clear section headers
        if not content.startswith("# "):
            content = f"# Sales Analysis Results - {timestamp}\\n\\n{content}"
        
        # Save to main filepath
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"Analysis results saved to {filepath}")
        
        # Also save to knowledge directory
        knowledge_file = os.path.join('knowledge', 'sales_analysis_results.md')
        os.makedirs('knowledge', exist_ok=True)
        with open(knowledge_file, 'w') as file:
            file.write(content)
        print(f"Analysis results also saved to {knowledge_file} for RAG integration")
        
    except Exception as e:
        print(f"Error saving analysis results: {str(e)}")
"""
    
    print("\n\n=== CODE UPDATES FOR sales_ai.py ===")
    print("Replace the existing knowledge creation code with:")
    print(knowledge_import_fix)
    print("\nReplace the existing save_analysis_results function with:")
    print(save_results_fix)

def main():
    """Main function to fix the RAG integration."""
    print("Starting RAG integration fix...")
    
    # Step 1: Create knowledge directory
    if not create_knowledge_directory():
        sys.exit(1)
    
    # Step 2: Copy analysis results to knowledge directory
    if not copy_analysis_results():
        print("Warning: Could not copy analysis results file")
    
    # Step 3: Show code updates
    update_sales_ai_code()
    
    print("\nRAG integration fix preparation complete!")
    print("To complete the fix, update the code in sales_ai.py and sales_ai_debug.py as shown above.")

if __name__ == "__main__":
    main()