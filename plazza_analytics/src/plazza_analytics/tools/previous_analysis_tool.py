# src/plazza_analytics/tools/previous_analysis_tool.py

import os
from pathlib import Path
from typing import Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Version History
# 2025-03-28: Updated for CrewAI v0.108.0+ compatibility
#   - Added proper type annotations for name and description
#   - Added args_schema with Pydantic BaseModel validation
#   - Enhanced parameter validation with robust error handling
#   - Added **kwargs to run method for better compatibility
#   - Improved error messages with troubleshooting guidance

class PreviousAnalysisArgs(BaseModel):
    file: Optional[str] = Field(
        default=None,
        description="Specific knowledge file to retrieve (e.g., 'sales_analysis.md')"
    )

class PreviousAnalysisTool(BaseTool):
    name: str = "PreviousAnalysisTool"
    description: str = """Access knowledge files or previous analysis results.
    
    Use this tool to:
    1. Retrieve specific knowledge files by filename (e.g., "sales_analysis.md")
    2. Access the most recent saved sales analysis from previous runs
    
    Parameters:
    - file (optional): Name of a specific file to retrieve from the knowledge directory
      Example values: "sales_analysis", "database_schemas", "customer_insights"
      
    If no file is specified, returns the most recent analysis result."""
    
    args_schema: type[PreviousAnalysisArgs] = PreviousAnalysisArgs
    
    def run(self, file: Optional[str] = None, **kwargs):
        """Retrieve the most recent sales analysis or a specific file from the knowledge directory.
        
        Args:
            file (str, optional): Specific knowledge file to retrieve (e.g., 'sales_analysis.md'). 
                                 If None, looks for sales_ai_run_result.md
        """
        try:
            print(f"PreviousAnalysisTool retrieving file: {file if file else 'most recent analysis'}")
            return self._run(file=file)
        except Exception as e:
            error_message = f"ERROR in PreviousAnalysisTool.run: {str(e)}"
            print(error_message)
            import traceback
            print(traceback.format_exc())
            return error_message
    
    def _run(self, file: Optional[str] = None) -> str:
        """Internal implementation of file retrieval.
        
        Args:
            file: Optional specific knowledge file to retrieve
            
        Returns:
            str: Content of the requested file or error message
        """
        try:
            # Try multiple possible locations for files
            from pathlib import Path
            
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            project_root = Path(__file__).resolve().parents[3]  # Navigate up to project root
            parent_dir = Path(__file__).resolve().parents[4]  # One level above project root
            
            # Handle different file types
            if file is not None:
                # User requested a specific file (likely from knowledge directory)
                knowledge_dir = project_root / "knowledge"
                knowledge_file = file
                if not knowledge_file.endswith(".md"):
                    knowledge_file += ".md"
                
                # Use different path patterns for knowledge files
                possible_paths = [
                    # Knowledge directory - project root
                    knowledge_dir / knowledge_file,
                    # Knowledge directory - one level up
                    parent_dir / "knowledge" / knowledge_file,
                    # Relative path - base_dir
                    Path(base_dir) / "knowledge" / knowledge_file
                ]
                file_type = "knowledge file"
            else:
                # Default: look for previous analysis result
                possible_paths = [
                    # Original location
                    os.path.join(base_dir, "Run_Results", "sales_ai_run_result.md"),
                    # Project root
                    project_root / "Run_Results" / "sales_ai_run_result.md",
                    # Parent directory (e.g., /Users/aniruddhasen/Projects/CrewAI/Run_Results)
                    parent_dir / "Run_Results" / "sales_ai_run_result.md"
                ]
                file_type = "previous analysis file"
            
            # Try each path
            result_path = None
            for path in possible_paths:
                path_str = str(path)
                if os.path.exists(path_str):
                    result_path = path_str
                    break
            
            if not result_path:
                return f"""ℹ️ No {file_type} found at any expected path.
                
## Possible Locations Checked
{chr(10).join([f"- {p}" for p in possible_paths])}

## Recommendation
If you're looking for a specific knowledge file, try using one of the standard filenames:
- sales_analysis.md
- database_schemas.md 
- customer_insights.md

Or use the SaveKnowledgeTool to create a new knowledge file."""

            with open(result_path, 'r') as f:
                content = f.read()

            # Only show the actual analysis part if present
            if "## Final Answer:" in content:
                content = content.split("## Final Answer:")[1].strip()

            # Add source information and truncate if too long
            result = f"## Previous Analysis Results\n\nSource: {result_path}\n\n{content[:5000]}"
            
            if len(content) > 5000:
                result += "...\n\n(Content truncated for display - use a more specific file name for targeted information)"
                
            return result

        except Exception as e:
            return f"""❌ Error loading previous analysis: {str(e)}
            
## Troubleshooting Information
- Error type: {type(e).__name__}
- Error message: {str(e)}
- Requested file: {file if file else 'most recent analysis'}

### Possible causes:
1. File does not exist at expected locations
2. Permissions issue with file access
3. File contains invalid content or encoding

Try using a different file name or check if the file exists in the knowledge directory."""