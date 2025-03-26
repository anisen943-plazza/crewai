# src/plazza_analytics/tools/previous_analysis_tool.py

import os
from langchain.tools import BaseTool

class PreviousAnalysisTool(BaseTool):
    name = "PreviousAnalysisTool"
    description = """Access the most recent saved sales analysis file from previous runs.
    Use this to refer to earlier findings or compare with new results."""
    
    def run(self):
        """Retrieve the most recent sales analysis from the Run_Results directory."""
        return self._run()
    
    def _run(self) -> str:
        try:
            # Define the known analysis path
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            result_path = os.path.join(base_dir, "Run_Results", "sales_ai_run_result.md")

            if not os.path.exists(result_path):
                return "ℹ️ No previous analysis file found at expected path."

            with open(result_path, 'r') as f:
                content = f.read()

            # Only show the actual analysis part if present
            if "## Final Answer:" in content:
                content = content.split("## Final Answer:")[1].strip()

            return f"## Previous Analysis Results\n\n{content[:2000]}..."  # Truncate for safety

        except Exception as e:
            return f"❌ Error loading previous analysis: {str(e)}"
