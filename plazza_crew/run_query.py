"""
Simple script to run a query using the CrewAI system.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY environment variable not set!")
    print("Please check your .env file contains a valid OpenAI API key.")
    sys.exit(1)

# Try to ensure yaml and psycopg2 are installed
try:
    import yaml
    import psycopg2
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "psycopg2-binary", "python-dotenv"])
    import yaml
    import psycopg2

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

# Import crew
from plazza_crew.crew import crew

def main():
    # Define user question (modify as needed)
    user_question = "Which distributors had the highest inventory transactions based on transaction count last month?"
    
    # Get schema path
    schema_path = os.path.join(current_dir, 'schema_summary.md')
    
    # Read schema
    with open(schema_path) as f:
        schema = f.read()
    
    # Run the crew
    print(f'\n\nProcessing question: "{user_question}"\n')
    try:
        result = crew.kickoff(inputs={
            'user_question': user_question,
            'schema': schema,
            'db_goal': user_question
        })
        
        print('\n\nResult:')
        print(result)
    except Exception as e:
        print(f"\n\nError: {e}")
        print("\nCommon issues:")
        print("1. OpenAI API key not set correctly")
        print("2. Database connection problems")
        print("3. Missing required packages")
        
        # Print environment variables (without leaking secrets)
        print("\nEnvironment check:")
        print(f"OPENAI_API_KEY set: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")
        print(f"POSTGRES_DB set: {'Yes' if os.getenv('POSTGRES_DB') else 'No'}")
        print(f"POSTGRES_USER set: {'Yes' if os.getenv('POSTGRES_USER') else 'No'}")

if __name__ == "__main__":
    main()