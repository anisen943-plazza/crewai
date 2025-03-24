"""
Visualization Agent Demo Script with Plazza Styling

This script demonstrates the Plazza-styled visualization capabilities
by creating visualizations from existing analysis results.
"""

import os
import sys
import shutil
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.knowledge import Knowledge

# Add parent directory to PATH for imports
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Import visualization module with correct path
from Core_Scripts.crewai_visualization import visualize_analysis_results, VisualizationTool

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")
os.environ["OPENAI_API_KEY"] = openai_key

# Paths for analysis results and output
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
knowledge_dir = os.path.join(project_dir, "knowledge")
visuals_dir = os.path.join(project_dir, "visuals")

# Ensure visuals directory exists
os.makedirs(visuals_dir, exist_ok=True)

# Find analysis results file
knowledge_file = os.path.join(knowledge_dir, "sales_analysis_results.md")
run_results_file = os.path.join(project_dir, "Run_Results", "sales_ai_run_result.md")

# Use the appropriate file that exists
if os.path.exists(knowledge_file):
    ANALYSIS_RESULTS_PATH = knowledge_file
    print(f"Using knowledge file: {knowledge_file}")
elif os.path.exists(run_results_file):
    ANALYSIS_RESULTS_PATH = run_results_file
    print(f"Using run results file: {run_results_file}")
else:
    ANALYSIS_RESULTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sales_ai_run_result.md")
    print(f"Using local file: {ANALYSIS_RESULTS_PATH}")

def direct_visualization_test():
    """Test the updated visualization module directly"""
    print("\n===== Testing Direct Visualization =====")
    try:
        print(f"Generating visualizations from: {ANALYSIS_RESULTS_PATH}")
        viz_results = visualize_analysis_results(ANALYSIS_RESULTS_PATH, output_dir=visuals_dir)
        print(f"Visualizations generated: {viz_results}")
        print("✅ Direct visualization test succeeded!")
        return True
    except Exception as e:
        print(f"❌ Direct visualization test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def agent_visualization_test():
    """Test the visualization agent with Plazza styling"""
    print("\n===== Testing Visualization Agent =====")
    
    # Create a specialized visualization agent with Plazza styling knowledge
    visualization_specialist = Agent(
        role="Data Visualization Specialist",
        goal="Create compelling visualizations with Plazza styling",
        backstory="""You are an expert in data visualization with years of experience creating
        interactive dashboards for business intelligence. You specialize in Plazza brand-compliant
        visualizations that transform complex data into clear, actionable visuals highlighting
        key insights and trends.""",
        tools=[VisualizationTool()],
        llm=LLM(model="gpt-4o", temperature=0.3, max_tokens=2000),
        verbose=True
    )

    # Create a visualization task with Plazza styling requirements
    visualization_task = Task(
        description="""
        Create visualizations based on the latest sales analysis results using Plazza brand styling.
        
        ## Plazza Brand Guidelines
        
        1. **Color Palette**:
           - Primary: #FF0084 (bright pink) - Use for titles, important values, and highlights
           - Background: #fafafa (light gray) - Use for page backgrounds
           - Card Background: white - Use for cards and widget backgrounds
           - Text: Dark gray (#333) for body text, #666 for secondary text
        
        2. **UI Components**:
           - Card-based layout with rounded corners (12px radius)
           - Clean grid system for organizing content
           - Large, bold numbers for KPI values (using Plazza pink)
           - Insight cards with highlighted titles
        
        Your task is to:
        1. Use the VisualizationTool to generate Plazza-styled visualizations from the latest analysis
        2. The tool will automatically extract data and create appropriately styled charts
        
        Just call the tool with no parameters and it will handle everything.
        The visualization module has been updated with Plazza styling.
        """,
        expected_output="""
        A set of Plazza-styled visualizations including:
        1. Product sales charts with Plazza styling
        2. Customer retention visualizations with Plazza styling
        3. Business metrics dashboard with Plazza styling and KPI cards
        """,
        agent=visualization_specialist
    )

    # Create the crew
    crew = Crew(
        agents=[visualization_specialist],
        tasks=[visualization_task],
        verbose=True
    )

    # Run the crew and display results
    print("Running visualization agent with Plazza styling...")
    result = crew.kickoff()
    print("\n✅ Visualization Complete!")
    print(result)
    return True

if __name__ == "__main__":
    print("===== Plazza-Styled Visualization Demo =====")
    direct_result = direct_visualization_test()
    agent_result = agent_visualization_test()
    
    if direct_result and agent_result:
        print("\n===== All tests passed! =====")
        print(f"Visualizations saved to: {visuals_dir}")
    else:
        print("\n⚠️ Some tests failed!")
        sys.exit(1)