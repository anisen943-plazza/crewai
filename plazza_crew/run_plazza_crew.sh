#!/bin/bash

# Activate virtual environment
source /Users/aniruddhasen/Projects/crewai/plazza_crew/.venv/bin/activate

# Install required packages (just to be safe)
pip install pyyaml psycopg2-binary

# Set Python path to include the src directory
export PYTHONPATH=$PYTHONPATH:/Users/aniruddhasen/Projects/crewai/plazza_crew/src

# Set OpenAI API key from .env file (important!)
export OPENAI_API_KEY=$(grep OPENAI_API_KEY /Users/aniruddhasen/Projects/crewai/plazza_crew/.env | cut -d= -f2)

# Define user question (modify as needed)
USER_QUESTION="Which distributors had the highest inventory transactions based on transaction count last month?"

# Execute the script with the user question
cd /Users/aniruddhasen/Projects/crewai/plazza_crew
python -c "
import os
from plazza_crew.crew import crew

user_question = \"$USER_QUESTION\"

# Get schema path
current_dir = os.getcwd()
schema_path = os.path.join(current_dir, 'schema_summary.md')

# Read schema
with open(schema_path) as f:
    schema = f.read()

# Run the crew
print(f'\n\nProcessing question: \"{user_question}\"\n')
result = crew.kickoff(inputs={
    'user_question': user_question,
    'schema': schema,
    'db_goal': user_question
})

print('\n\nResult:')
print(result)
"