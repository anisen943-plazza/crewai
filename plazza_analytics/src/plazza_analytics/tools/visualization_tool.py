# File: visualization_tool.py

import os
from datetime import datetime
from dotenv import load_dotenv
from langchain.tools import BaseTool
from plazza_analytics.visualization_engine import CrewAIVisualization

class VisualizationTool(BaseTool):
    def run(self, *args, **kwargs):
        return self._run(**kwargs)
    name = "VisualizationTool"
    description = (
        "Generate visualizations from markdown-based business analysis. "
        "Pass in the markdown result and this will return a markdown response "
        "with links to generated visuals (charts, dashboards)."
    )

    def _run(self, **kwargs) -> str:
        input_data = kwargs.get("input_data", "")
        """
        Generate visualizations from analysis markdown and return markdown response with links.
        """

        load_dotenv()
        output_dir = os.getenv("VISUALIZATION_OUTPUT_DIR", "visuals")
        os.makedirs(output_dir, exist_ok=True)

        try:
            viz = CrewAIVisualization(output_dir=output_dir)
            parsed = viz.parse_markdown_content(input_data)
            results = viz.generate_all_visualizations(input_data)

            markdown = "## 📊 Visualizations Generated\n\n"
            if "metrics_dashboard" in results:
                markdown += f"### Business Dashboard\n[Open Dashboard]({results['metrics_dashboard']})\n\n"
            if "top_products_chart" in results:
                markdown += f"### Top Products\n[View Chart]({results['top_products_chart']})\n\n"
            if "customer_retention_chart" in results:
                markdown += f"### Customer Retention\n[View Chart]({results['customer_retention_chart']})\n\n"
            if "time_series_chart" in results:
                markdown += f"### Sales Trend\n[View Chart]({results['time_series_chart']})\n\n"
            if "geographic_chart" in results:
                markdown += f"### Regional Insights\n[View Chart]({results['geographic_chart']})\n\n"
            if "comparative_chart" in results:
                markdown += f"### Period Comparison\n[View Chart]({results['comparative_chart']})\n\n"

            markdown += f"\nVisualizations saved in `{output_dir}`.\n"

            return markdown

        except Exception as e:
            return f"⚠️ Error generating visualizations: {str(e)}"