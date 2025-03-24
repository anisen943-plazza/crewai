from crewai import Agent, Task, LLM
from crewai.knowledge.knowledge import Knowledge
from pathlib import Path
import os
import datetime

# Strategy templates for reusability
STRATEGY_TASK_TEMPLATE = """
Develop actionable business strategies based on existing insights in the Knowledge Base.

## Knowledge Base First Approach - CRITICAL FIRST STEP

Your strategy development MUST begin with a thorough review of the Knowledge Base:

1. Extract business metrics, trends, and insights from the KB
2. Identify strengths, weaknesses, and opportunities based on KB data
3. Note knowledge gaps that may require additional information
4. NEVER conduct new database analysis yourself

## Strategy Development Framework

Develop a comprehensive business strategy with these components:

1. **Current State Assessment**:
   - Summarize key metrics and trends from the KB
   - Identify operational strengths and weaknesses
   - Highlight critical business challenges
   - Document current performance baselines

2. **Strategic Opportunities**:
   - Identify 3-5 key business opportunities based on KB insights
   - Prioritize opportunities by impact and feasibility
   - Assess competitive landscape implications
   - Note potential quick wins vs. long-term initiatives

3. **Implementation Roadmap**:
   - Suggest concrete next steps for each opportunity
   - Outline implementation phasing and dependencies
   - Provide decision frameworks for evaluation
   - Recommend timeframes and resource considerations

Your response should be business-focused, action-oriented, and grounded in KB data.
Provide clear, specific recommendations rather than general advice.
"""

EXPECTED_OUTPUT_TEMPLATE = """
A comprehensive business strategy document including:
1. Current state assessment based on KB metrics
2. 3-5 prioritized strategic opportunities with rationale
3. Concrete implementation steps for each opportunity
4. Decision frameworks and evaluation criteria
5. Clear recommendations tied directly to KB insights
"""

# Setup directories and paths
BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"
STRATEGY_DIR = BASE_DIR / "Run_Results" / "strategies"
knowledge_file = KNOWLEDGE_DIR / "sales_analysis_results.md"

# Ensure directories exist
STRATEGY_DIR.mkdir(parents=True, exist_ok=True)

# Create knowledge source
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
kb_source = TextFileKnowledgeSource(
    file_paths=[knowledge_file],
    chunk_size=800,
    chunk_overlap=200
)
shared_knowledge = Knowledge(collection_name="sales_analysis", sources=[kb_source])

# Utility function for strategy logging
def save_strategy_output(output, filename_prefix="strategy"):
    """
    Save generated strategy to a timestamped file for audit and reference.
    
    Args:
        output (str): The strategy content to save
        filename_prefix (str): Prefix for the output filename
        
    Returns:
        str: Path to the saved file
    """
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{ts}.md"
    filepath = STRATEGY_DIR / filename
    
    # Ensure content has proper formatting
    if not output.startswith("# "):
        output = f"# Business Strategy - {ts}\n\n{output}"
        
    # Add metadata for better organization
    if "## Metadata" not in output:
        metadata = f"""
## Metadata
- **Generated**: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **Type**: Business Strategy
- **Model**: gpt-4o
- **File**: {filename}
"""
        # Insert after title
        parts = output.split("\n\n", 1)
        if len(parts) > 1:
            output = f"{parts[0]}{metadata}\n\n{parts[1]}"
        else:
            output = f"{parts[0]}{metadata}"
    
    with open(filepath, "w") as f:
        f.write(output)
    
    print(f"Strategy saved to {filepath}")
    return str(filepath)

# Strategy Agent
business_strategy_advisor = Agent(
    role="Strategic Business Consultant",
    goal="Recommend actionable business strategies based on sales, customer, and product performance insights.",
    backstory="""You are a senior advisor helping the Plazza business scale effectively.

    🎯 Your strategy work is always grounded in **existing insights from the Knowledge Base** (`sales_analysis_results.md`), which contains schema discoveries, sales analytics, product performance, and customer behaviors.

    ✅ Your process:
    1. Always begin by reading and interpreting findings from the Knowledge Base.
    2. Identify business levers and opportunities based on current metrics.
    3. Suggest concrete, actionable recommendations across areas like pricing, promotions, retention, and operational optimization.
    4. If the KB is incomplete, you may **ask the Data Q&A Expert** to investigate specific metrics — but you never query databases yourself.

    ❌ You do not perform technical data analysis or visualizations directly.
    ❌ You do not overwrite or refresh the Knowledge Base.

    ✅ Your outputs are strategic summaries, decision frameworks, and implementation suggestions.""",
    tools=[],  # No direct tools - relies on Knowledge Base
    llm=LLM(model="gpt-4o", temperature=0.4, max_tokens=4000),  # Slightly higher temperature for creative strategies
    knowledge=shared_knowledge,  # Shared knowledge with other agents
    verbose=False  # Disable verbose mode to hide thought process and just show final answer
)

# Strategy Task Factory
def create_strategy_task(user_query=None, analysis_content=None, data_analyst_agent=None):
    """
    Creates a strategy recommendation task based on analysis results.
    
    Args:
        user_query (str): Optional user query to focus the strategy recommendations
        analysis_content (str): Optional analysis content to reference
        data_analyst_agent (Agent): Optional data analyst agent for delegation
        
    Returns:
        Task: A task object configured with appropriate description
    """
    # Start with the base template
    base_description = STRATEGY_TASK_TEMPLATE
    
    # Add specific focus if provided in user query
    if user_query:
        query_focus = f"""
        ## Strategic Focus
        
        Address the following strategic question in your recommendations:
        "{user_query}"
        
        Ensure your strategic recommendations directly address this focus area
        while still providing a comprehensive business strategy framework.
        """
        base_description += query_focus
    
    # Add specific analysis content reference if provided
    if analysis_content:
        content_reference = f"""
        ## Analysis Reference
        
        Base your strategy recommendations on the following analysis:
        
        {analysis_content}
        
        Focus on creating actionable recommendations that directly address
        the insights from this analysis, while ensuring all recommendations
        are concrete and implementable.
        """
        base_description += content_reference
    
    # Add delegation instructions if data analyst is provided
    if data_analyst_agent:
        delegation_instructions = f"""
        ## Knowledge Gap Handling
        
        If you identify critical knowledge gaps that prevent effective strategy development:
        
        1. Clearly document what specific data or metrics you need
        2. Formulate precise questions that would fill these knowledge gaps
        3. You can delegate these questions to the Data Q&A Expert
        
        However, always try to work with available knowledge first before concluding
        that delegation is necessary. Your primary responsibility is to develop
        strategies based on existing insights.
        """
        base_description += delegation_instructions
        
        # Create a task with delegation enabled
        return Task(
            description=base_description,
            expected_output=EXPECTED_OUTPUT_TEMPLATE,
            agent=business_strategy_advisor,
            async_execution=False,
            callback=lambda output: save_strategy_output(output),
            allow_delegation=True
        )
    
    # Default task without delegation
    return Task(
        description=base_description,
        expected_output=EXPECTED_OUTPUT_TEMPLATE,
        agent=business_strategy_advisor,
        callback=lambda output: save_strategy_output(output)
    )