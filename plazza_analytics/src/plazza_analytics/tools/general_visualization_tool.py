# src/plazza_analytics/tools/general_visualization_tool.py

import os
from langchain.tools import BaseTool

class GeneralVisualizationTool(BaseTool):
    name = "GeneralVisualizationTool"
    description = """Generate business charts from markdown analysis.
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
    
    def run(self, input_text: str = ""):
        """Generate visualizations from the provided markdown analysis text.
        
        Args:
            input_text: The markdown analysis text containing metrics and data to visualize
        """
        return self._run(input_text=input_text)
    
    def _run(self, input_text: str = "") -> str:
        try:
            from crewai_visualization import visualize_analysis_results

            if not input_text or not isinstance(input_text, str):
                return "❌ Please provide valid analysis content as a string."

            results = visualize_analysis_results(
                content=input_text,
                enable_json_output=True
            )

            if not results:
                return "⚠️ No visualizations were generated."

            output = "✅ Visualizations generated:\n"
            for key, path in results.items():
                if key != "enhanced_markdown":
                    output += f"- {key.replace('_', ' ').title()}: `{os.path.basename(path)}`\n"

            return output

        except Exception as e:
            return f"❌ Error generating visualizations: {str(e)}"