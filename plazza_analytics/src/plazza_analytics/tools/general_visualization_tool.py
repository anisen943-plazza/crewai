# src/plazza_analytics/tools/general_visualization_tool.py

import os
from typing import Optional, Dict, Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Version History
# 2025-03-28: Updated for CrewAI v0.108.0+ compatibility
#   - Added proper type annotations for name and description
#   - Added args_schema with Pydantic BaseModel validation
#   - Enhanced parameter validation with robust error handling
#   - Added **kwargs to run method for better compatibility
#   - Improved error messages with troubleshooting guidance

class GeneralVisualizationArgs(BaseModel):
    input_text: str = Field(
        default="",
        description="The markdown analysis text containing metrics and data to visualize"
    )

class GeneralVisualizationTool(BaseTool):
    name: str = "GeneralVisualizationTool"
    description: str = """Generate business charts from markdown analysis.
This tool parses an existing analysis (from Knowledge Base or analyst output)
and generates multiple visualizations automatically.

Types of visualizations:
- Bar charts (e.g. top-selling products)
- Pie charts (e.g. retention breakdown)
- KPI dashboards
- Trend charts (if time data is present)

Usage:
Provide the markdown-formatted analysis text as input. It should contain
clearly structured sections, bullet points, or tables with metrics.

This tool will:
1. Parse the analysis
2. Generate appropriate charts
3. Save them to the 'visuals' directory
4. Return a summary of chart types and saved file names

This tool does NOT query live data or the database.
"""
    
    args_schema: type[GeneralVisualizationArgs] = GeneralVisualizationArgs
    
    def run(self, input_text: str = "", **kwargs):
        """Generate visualizations from the provided markdown analysis text.
        
        Args:
            input_text: The markdown analysis text containing metrics and data to visualize
        """
        try:
            print(f"GeneralVisualizationTool processing input of length: {len(input_text) if input_text else 0} characters")
            
            # Basic validation
            if not input_text or not isinstance(input_text, str):
                return "❌ Please provide valid analysis content as a string."
                
            return self._run(input_text=input_text)
        except Exception as e:
            error_message = f"ERROR in GeneralVisualizationTool.run: {str(e)}"
            print(error_message)
            import traceback
            print(traceback.format_exc())
            return error_message
    
    def _run(self, input_text: str = "") -> str:
        """Generate visualizations from markdown analysis text.
        
        Args:
            input_text: The markdown text containing metrics to visualize
            
        Returns:
            str: Summary of generated visualizations with file paths
        """
        try:
            # Import visualization module
            try:
                from crewai_visualization import visualize_analysis_results
            except ImportError:
                return """❌ Could not import crewai_visualization module.
                
## Troubleshooting Information
The visualization module is missing or not in the Python path.

### Recommendation
Check that the crewai_visualization module is installed and available.
You may need to install it with:
```
pip install crewai_visualization
```
or add the Core_Scripts directory to your Python path."""

            # Basic validation
            if not input_text or not isinstance(input_text, str):
                return "❌ Please provide valid analysis content as a string."

            # Generate visualizations
            results = visualize_analysis_results(
                content=input_text,
                enable_json_output=True
            )

            if not results:
                return """⚠️ No visualizations were generated.
                
## Possible causes:
1. The input text doesn't contain numeric data suitable for visualization
2. The text structure couldn't be parsed correctly
3. The text doesn't contain supported visualization patterns

Try providing content with clear sections, bullet point metrics, or tables containing:
- Product sales figures
- Customer retention metrics 
- Time-based trends
- Proportion/percentage data suitable for pie charts"""

            # Format results
            output = "✅ Visualizations generated:\n\n"
            
            # Report on each visualization type
            for key, path in results.items():
                if key != "enhanced_markdown":
                    # Format the title nicely (e.g., "top_products_chart" -> "Top Products Chart")
                    title = key.replace('_', ' ').title()
                    
                    # Add the filename (without the full path)
                    filename = os.path.basename(path)
                    
                    # Format the line with emoji based on chart type
                    emoji = "📊"  # Default chart emoji
                    if "bar" in key or "product" in key:
                        emoji = "📊"  # Bar chart
                    elif "pie" in key or "retention" in key:
                        emoji = "🥧"  # Pie chart
                    elif "dashboard" in key:
                        emoji = "📈"  # Dashboard
                    elif "time" in key or "trend" in key:
                        emoji = "📉"  # Trend chart
                    
                    output += f"{emoji} **{title}**: `{filename}`\n"
            
            # Add note about where files are stored
            env_var = os.getenv("VISUALIZATION_OUTPUT_DIR", "visuals")
            output += f"\nVisualizations saved in `{env_var}` directory."
            
            return output

        except Exception as e:
            return f"""❌ Error generating visualizations: {str(e)}
            
## Troubleshooting Information
- Error type: {type(e).__name__}
- Error message: {str(e)}
- Input length: {len(input_text) if input_text else 0} characters

### Possible causes:
1. Input text format is not suitable for visualization
2. Missing dependencies for visualization generation
3. Permission issues writing to the visualization directory
4. Memory constraints with very large input

Try with a simpler, more structured input text or check directory permissions."""