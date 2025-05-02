import os
import sys
from dotenv import load_dotenv

# Add the project directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# Import with the corrected path
from src.plazza_crew.crew import crew

# Get the directory structure
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))

# Load environment variables from .env file at project root
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

# Verify environment variables are loaded
print("Environment variables loaded:")
print(f"DATABASE_URL set: {'Yes' if os.getenv('DATABASE_URL') else 'No'}")
print(f"DATABASE_URL_ERP set: {'Yes' if os.getenv('DATABASE_URL_ERP') else 'No'}")
print(f"DATABASE_URL_USER_TRANSACTIONS set: {'Yes' if os.getenv('DATABASE_URL_USER_TRANSACTIONS') else 'No'}")
print(f"OPENAI_API_KEY set: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")

# Get schema path
schema_path = os.path.join(project_root, "schema_summary.md")

with open(schema_path) as f:
    schema = f.read()

# Simple interactive mode
print("\n📊 PlazzaCrew Chat")
print("Type 'exit' to end the session")

while True:
    # Get user input
    user_query = input("\nEnter your query: ").strip()
    
    # Exit if requested
    if user_query.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Skip empty inputs
    if not user_query:
        continue
    
    # Run the query
    print(f"Querying database for: {user_query}")
    result = crew.kickoff(inputs={
        "user_question": user_query,
        "schema": schema,
        "db_goal": user_query
    })
    
    print("\nResult:")
    print(result)