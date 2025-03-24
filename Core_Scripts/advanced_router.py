# Core_Scripts/advanced_router.py
from crewai import Crew, Process, Task
import os
from datetime import datetime
from pathlib import Path

# Import agents from the registry
from Core_Scripts.agent_registry import (
    get_routing_agent,
    get_chat_data_analyst,
    get_data_analyst,
    get_visualization_specialist,
    get_strategy_advisor
)

# Load .env if needed
from dotenv import load_dotenv
load_dotenv()

# Directory for logs
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "Run_Results" / "router_logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

def save_conversation(query, response):
    """Save the conversation to a log file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversation_{timestamp}.md"
    filepath = LOG_DIR / filename
    
    content = f"""# Conversation Log - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## User Query
```
{query}
```

## AI Response
```
{response}
```

## Metadata
- Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- Model: {os.getenv('OPENAI_API_MODEL', 'Not specified')}
- System: Advanced Router
"""
    
    with open(filepath, "w") as f:
        f.write(content)
    
    print(f"Conversation saved to {filepath}")
    return str(filepath)

def run_advanced_router(user_query):
    """Run the advanced router with the given user query."""
    # Create all agents
    router = get_routing_agent()
    chat_qa = get_chat_data_analyst()
    analyst = get_data_analyst()
    visualizer = get_visualization_specialist()
    strategist = get_strategy_advisor()
    
    # The router agent will dynamically create a task and delegate it
    router_task = Task(
        description=f"""
You are given the following user request:

"{user_query}"

1. Classify what kind of task this is:
   - Quick Q&A from KB or DB
   - Full business analysis
   - Visualization/chart generation
   - Strategic business recommendation

2. Choose the best specialist agent to handle this.

3. Construct a task for that agent with clear instructions.

4. Delegate it using CrewAI delegation.

Your final output should be the result of the delegated task only.
""",
        expected_output="A delegated response based on the user's intent.",
        agent=router,
        async_execution=False
    )
    
    # Assemble the crew
    crew = Crew(
        agents=[router, chat_qa, analyst, visualizer, strategist],
        tasks=[router_task],
        process=Process.sequential,
        verbose=2
    )
    
    # Execute the crew
    print(f"\n🧠 Processing: \"{user_query}\"")
    print(f"🔄 Routing request to the appropriate specialist...\n")
    
    try:
        result = crew.kickoff(inputs={"user_input": user_query})
        save_conversation(user_query, result)
        return result
    except Exception as e:
        error_message = f"Error during routing: {str(e)}"
        print(f"\n❌ {error_message}")
        return error_message

if __name__ == "__main__":
    print("\n🔍 Advanced Plazza AI Router")
    print("==============================")
    print("This interface intelligently routes your queries to the most appropriate AI specialist.")
    print("Options:")
    print("  - Quick DB questions (Q&A Expert)")
    print("  - Deep analysis requests (Enterprise Analyst)")
    print("  - Visualization tasks (Visualization Specialist)")
    print("  - Strategy recommendations (Business Strategy Advisor)")
    print("==============================\n")
    
    while True:
        user_query = input("🧠 Ask Plazza AI something (or type 'exit' to quit): ")
        
        if user_query.lower() in ['exit', 'quit', 'q']:
            print("\nThank you for using Plazza AI Router. Goodbye!")
            break
        
        result = run_advanced_router(user_query)
        print("\n🧠 Final Answer:\n")
        print(result)
        print("\n" + "-"*50 + "\n")