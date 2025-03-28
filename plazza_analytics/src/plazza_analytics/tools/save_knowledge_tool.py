# src/plazza_analytics/tools/save_knowledge_tool.py

import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Union, Dict, Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Version History
# 2025-03-28: Updated for CrewAI v0.108.0+ compatibility
#   - Added proper type annotations for name and description
#   - Added args_schema with Pydantic BaseModel validation
#   - Enhanced parameter validation with robust error handling
#   - Added **kwargs to run method for better compatibility
#   - Improved error messages with troubleshooting guidance
#   - Added rupee (₹) formatting detection and standardization

class SaveKnowledgeArgs(BaseModel):
    content: str = Field(
        description="The content to save to the knowledge base"
    )
    filename: Optional[str] = Field(
        default=None,
        description="Optional specific filename, otherwise a timestamped name is used"
    )
    append: bool = Field(
        default=False,
        description="Whether to append to an existing file or create a new one"
    )

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
    
    args_schema: type[SaveKnowledgeArgs] = SaveKnowledgeArgs
    
    def run(self, content: str, filename: Optional[str] = None, append: bool = False, **kwargs):
        """Save content to the knowledge directory.
        
        Args:
            content: The content to save
            filename: Optional specific filename, otherwise a timestamped name is used
            append: Whether to append to an existing file or create a new one
        """
        try:
            print(f"SaveKnowledgeTool saving content to filename: {filename if filename else 'auto-generated'} (append={append})")
            
            # Basic validation
            if not content or not isinstance(content, str):
                return "❌ Content must be a non-empty string"
                
            return self._run(content=content, filename=filename, append=append)
        except Exception as e:
            error_message = f"ERROR in SaveKnowledgeTool.run: {str(e)}"
            print(error_message)
            import traceback
            print(traceback.format_exc())
            return error_message
    
    def _run(self, content: str, filename: Optional[str] = None, append: bool = False) -> str:
        """Internal implementation of knowledge saving.
        
        Args:
            content: The content to save to the knowledge base
            filename: Optional specific filename
            append: Whether to append to an existing file
            
        Returns:
            str: Success message or error
        """
        try:
            # Find the project root and knowledge directory
            base_dir = Path(__file__).resolve().parents[3]  # Navigate up to project root
            knowledge_dir = base_dir / "knowledge"
            
            # Create knowledge directory if it doesn't exist
            os.makedirs(knowledge_dir, exist_ok=True)
            
            # Determine filename if not provided
            if not filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"insight_{timestamp}.md"
            elif not filename.endswith(".md") and not filename.endswith(".txt"):
                # Add markdown extension if no extension is provided
                filename += ".md"
            
            file_path = knowledge_dir / filename
            
            # Standardize currency format (ensure rupee symbol usage)
            standardized_content = self._standardize_currency_format(content)
            
            # Add timestamp to content
            timestamped_content = f"## Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{standardized_content}"
            
            # Write to file
            if append and file_path.exists():
                with open(file_path, 'a') as f:
                    f.write(f"\n\n---\n\n{timestamped_content}")
                return f"✅ Knowledge appended to {file_path}"
            else:
                with open(file_path, 'w') as f:
                    f.write(timestamped_content)
                return f"✅ Knowledge saved to {file_path}"
            
        except Exception as e:
            return f"""❌ Error saving knowledge: {str(e)}
            
## Troubleshooting Information
- Error type: {type(e).__name__}
- Error message: {str(e)}
- Target filename: {filename}

### Possible causes:
1. Permission denied when writing to the knowledge directory
2. Invalid filename or path
3. Disk space issue

Try using a different filename or check permissions on the knowledge directory."""
            
    def _standardize_currency_format(self, content: str) -> str:
        """Standardize currency format to use ₹ (rupee) symbol.
        
        Args:
            content: The content to process
            
        Returns:
            str: Content with standardized currency format
        """
        import re
        
        # Replace dollar signs with rupee symbol (unless in code blocks)
        lines = content.split('\n')
        in_code_block = False
        result_lines = []
        
        for line in lines:
            # Skip currency standardization in code blocks
            if line.strip().startswith('```') or line.strip() == '```':
                in_code_block = not in_code_block
                result_lines.append(line)
                continue
                
            if not in_code_block:
                # Replace dollar amounts with rupee format
                line = re.sub(r'\$(\d+(?:,\d+)*(?:\.\d+)?)', r'₹\1', line)
                
                # Format numbers with comma separators when followed by "rupees"
                line = re.sub(r'(\d+)(?:\.\d+)?\s*(?:rupees|Rupees)', r'₹\1', line)
            
            result_lines.append(line)
            
        return '\n'.join(result_lines)