#!/bin/bash

# Change to the project's root directory
cd "$(dirname "$0")/.."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Check if required packages are installed
if ! pip show streamlit > /dev/null 2>&1; then
    echo "Streamlit is not installed. Installing requirements..."
    pip install -r Streamlit_Frontend/requirements.txt
fi

# Run the Streamlit app
echo "Starting Streamlit server..."
streamlit run Streamlit_Frontend/streamlit_app.py "$@"