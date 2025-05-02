#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Set Python path to include the src directory
export PYTHONPATH=$PYTHONPATH:/Users/aniruddhasen/Projects/crewai/plazza_crew/src

# Run the program using main.py (proper entry point)
echo "Running main.py with PYTHONPATH=$PYTHONPATH"
python src/plazza_crew/main.py