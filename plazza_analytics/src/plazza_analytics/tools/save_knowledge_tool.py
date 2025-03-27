# src/plazza_analytics/tools/save_knowledge_tool.py

import os
from datetime import datetime
from pathlib import Path
from crewai.tools import BaseTool

class SaveKnowledgeTool(BaseTool):
    name: str = "SaveKnowledgeTool"
    description: str = """Save newly discovered insights to the knowledge base for future reference.
    
    WHEN TO USE THIS TOOL:
    1. When explicitly directed to save insights (e.g., "save this to knowledge base")
    2. When handling multi-step tasks that include saving (e.g., "find X and save it")
    3. When discovering important information not already in the knowledge base
    4. When updating database schema documentation
    
    STANDARD FILENAMES:
    - database_schemas.md - For database structure information
    - sales_analysis.md - For sales metrics and trends
    - customer_insights.md - For customer behavior data
    - user_preference.txt - For user preference information
    
    Always use append=True to add to existing files rather than overwriting them."""
    
    def run(self, content: str, filename: str = None, append: bool = False):
        """Save content to the knowledge directory.
        
        Args:
            content: The content to save
            filename: Optional specific filename, otherwise a timestamped name is used
            append: Whether to append to an existing file or create a new one
        """
        return self._run(content=content, filename=filename, append=append)
    
    def _run(self, content: str, filename: str = None, append: bool = False) -> str:
        try:
            # Find the project root and knowledge directory
            base_dir = Path(__file__).resolve().parents[3]  # Navigate up to project root
            knowledge_dir = base_dir / "knowledge"
            
            # Determine filename if not provided
            if not filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"insight_{timestamp}.md"
            elif not filename.endswith(".md"):
                filename += ".md"
            
            file_path = knowledge_dir / filename
            
            # Add timestamp to content
            timestamped_content = f"## Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{content}"
            
            # Write to file
            if append and file_path.exists():
                with open(file_path, 'a') as f:
                    f.write(f"\n\n---\n\n{timestamped_content}")
            else:
                with open(file_path, 'w') as f:
                    f.write(timestamped_content)
            
            return f"Knowledge saved to {file_path}"
            
        except Exception as e:
            return f"Error saving knowledge: {str(e)}"