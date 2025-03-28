# src/plazza_analytics/tools/visualization_tool.py

import os
from datetime import datetime
from typing import Optional, Dict, Any
from dotenv import load_dotenv
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Version History
# 2025-03-28: Updated for CrewAI v0.108.0+ compatibility
#   - Added proper type annotations for name and description
#   - Added args_schema with Pydantic BaseModel validation
#   - Enhanced parameter validation with robust error handling
#   - Added **kwargs to run method for better compatibility
#   - Improved error messages with troubleshooting guidance

class VisualizationArgs(BaseModel):
    input_data: str = Field(
        default="",
        description="The markdown analysis text containing metrics and data to visualize"
    )

class VisualizationTool(BaseTool):
    name: str = "VisualizationTool"
    description: str = """Generate visualizations from markdown-based business analysis.
Pass in the markdown result and this will return a markdown response
with links to generated visuals (charts, dashboards).

This tool creates:
- Business metric dashboards
- Top products charts
- Customer retention visualizations
- Time series trend analysis
- Regional insights maps
- Period-over-period comparisons

All monetary values will be properly formatted with the ₹ symbol."""
    
    args_schema: type[VisualizationArgs] = VisualizationArgs
    
    def run(self, input_data: str = "", **kwargs):
        """Generate visualizations from analysis markdown.
        
        Args:
            input_data: The markdown analysis text containing metrics and data to visualize
        """
        try:
            print(f"VisualizationTool processing input of length: {len(input_data) if input_data else 0} characters")
            
            # Basic validation
            if not input_data or not isinstance(input_data, str):
                return "❌ Please provide valid analysis content as a string."
                
            return self._run(input_data=input_data)
        except Exception as e:
            error_message = f"ERROR in VisualizationTool.run: {str(e)}"
            print(error_message)
            import traceback
            print(traceback.format_exc())
            return error_message
    
    def _run(self, input_data: str = "") -> str:
        """Generate visualizations from analysis markdown and return markdown response with links.
        
        Args:
            input_data: The markdown analysis text containing metrics to visualize
            
        Returns:
            str: Markdown formatted response with links to generated visualizations
        """
        load_dotenv()
        output_dir = os.getenv("VISUALIZATION_OUTPUT_DIR", "visuals")
        os.makedirs(output_dir, exist_ok=True)

        try:
            # Import visualization engine
            try:
                from plazza_analytics.visualization_engine import CrewAIVisualization
            except ImportError:
                return """❌ Could not import visualization_engine module.
                
## Troubleshooting Information
The visualization_engine module is missing or not in the Python path.

### Recommendation
Check that the visualization_engine module is properly installed and available.
You may need to check the Python path configuration.
"""

            # Validate input
            if not input_data or not isinstance(input_data, str):
                return "❌ Please provide valid analysis content as a string."
            
            # Generate visualizations
            viz = CrewAIVisualization(output_dir=output_dir)
            parsed = viz.parse_markdown_content(input_data)
            results = viz.generate_all_visualizations(input_data)

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

            # Build markdown response
            markdown = "## 📊 Visualizations Generated\n\n"
            
            # Add each visualization section with proper emoji
            visualization_sections = [
                ("metrics_dashboard", "📈 Business Dashboard", "Dashboard with key business metrics"),
                ("top_products_chart", "📊 Top Products", "Chart showing top-selling products"),
                ("customer_retention_chart", "🥧 Customer Retention", "Chart showing customer retention metrics"),
                ("time_series_chart", "📉 Sales Trend", "Chart showing sales trends over time"),
                ("geographic_chart", "🗺️ Regional Insights", "Map showing regional sales or customer distribution"),
                ("comparative_chart", "📊 Period Comparison", "Chart comparing metrics across different time periods")
            ]
            
            for key, title, description in visualization_sections:
                if key in results:
                    markdown += f"### {title}\n"
                    markdown += f"{description}\n\n"
                    
                    # Add link with clear button-like formatting
                    filename = os.path.basename(results[key])
                    markdown += f"[View {title}]({results[key]}) - `{filename}`\n\n"
            
            # Add note about where files are stored with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            markdown += f"\nVisualizations generated on {timestamp} and saved in `{output_dir}` directory.\n"

            return markdown

        except Exception as e:
            return f"""❌ Error generating visualizations: {str(e)}
            
## Troubleshooting Information
- Error type: {type(e).__name__}
- Error message: {str(e)}
- Input length: {len(input_data) if input_data else 0} characters

### Possible causes:
1. Input text format is not suitable for visualization
2. Missing dependencies for visualization generation
3. Permission issues writing to the visualization directory
4. Memory constraints with very large input

Try with a simpler, more structured input text or check directory permissions."""