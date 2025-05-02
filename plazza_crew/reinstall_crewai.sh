#!/bin/bash

# This script completely reinstalls CrewAI and its dependencies

echo "Reinstalling CrewAI and dependencies..."

# Activate virtual environment
source .venv/bin/activate

# Remove previous installations
pip uninstall -y crewai openai pyyaml psycopg2-binary python-dotenv

# Reinstall all required packages
pip install --no-cache-dir crewai==0.118.0
pip install --no-cache-dir pyyaml psycopg2-binary python-dotenv openai

# Check installation
echo "Installed packages:"
pip list | grep -E "crewai|pyyaml|psycopg2|dotenv|openai"

# Test the basic CrewAI functionality
echo -e "\nTesting CrewAI installation..."
python test_crewai.py

echo -e "\nIf the test runs without errors, you can now run your actual project."
echo "Run: ./run.sh"