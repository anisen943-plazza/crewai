# src/plazza_analytics/tools/previous_analysis_tool.py

import os
from crewai.tools import BaseTool

class PreviousAnalysisTool(BaseTool):
    name: str = "PreviousAnalysisTool"
    description: str = """Access the most recent saved sales analysis file from previous runs.
    Use this to refer to earlier findings or compare with new results."""
    
    def run(self):
        """Retrieve the most recent sales analysis from the Run_Results directory."""
        return self._run()
    
    def _run(self) -> str:
        try:
            # Try multiple possible locations for the Run_Results directory
            from pathlib import Path
            
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            project_root = Path(__file__).resolve().parents[3]  # Navigate up to project root
            parent_dir = Path(__file__).resolve().parents[4]  # One level above project root
            
            possible_paths = [
                # Original location
                os.path.join(base_dir, "Run_Results", "sales_ai_run_result.md"),
                # Project root
                project_root / "Run_Results" / "sales_ai_run_result.md",
                # Parent directory (e.g., /Users/aniruddhasen/Projects/CrewAI/Run_Results)
                parent_dir / "Run_Results" / "sales_ai_run_result.md"
            ]
            
            # Try each path
            result_path = None
            for path in possible_paths:
                path_str = str(path)
                if os.path.exists(path_str):
                    result_path = path_str
                    break
            
            if not result_path:
                return "ℹ️ No previous analysis file found at any expected path."

            with open(result_path, 'r') as f:
                content = f.read()

            # Only show the actual analysis part if present
            if "## Final Answer:" in content:
                content = content.split("## Final Answer:")[1].strip()

            return f"## Previous Analysis Results\n\nSource: {result_path}\n\n{content[:2000]}..."  # Truncate for safety

        except Exception as e:
            return f"❌ Error loading previous analysis: {str(e)}"
