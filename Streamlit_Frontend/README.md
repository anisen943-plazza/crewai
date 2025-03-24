# Plazza AI Streamlit Frontend

A web-based user interface for the Plazza AI system built with Streamlit.

## Features

- **Dual Chat Interface**: 
  - Standard Chat: Direct interaction with PlazzaChat
  - Advanced Router: Intent-based routing with AI Orchestrator
- **System Status Dashboard**:
  - Knowledge Base freshness monitoring
  - Metadata display from recent queries
  - Router logs with self-evaluation
- **Visualization Display**:
  - Automatic display of generated charts and dashboards
  - Support for both PNG and interactive HTML visualizations
- **Chat History**:
  - Display of recent chat responses
  - Advanced router conversation logs

## Installation

1. Ensure you have Python 3.8+ installed
2. Install the required packages:

```bash
cd Streamlit_Frontend
pip install -r requirements.txt
```

## Usage

Run the Streamlit app from the project root directory:

```bash
streamlit run Streamlit_Frontend/streamlit_app.py
```

The app will be available at http://localhost:8501 by default.

## Directory Structure

- `streamlit_app.py`: Main Streamlit application
- `utils.py`: Helper functions for file handling and metrics
- `requirements.txt`: Required Python packages

## Environment Configuration

The frontend expects the following directories in the parent folder:

- `/Run_Results`: For chat outputs and router logs
- `/visuals`: For visualization outputs (PNG/HTML)
- `/knowledge`: For the knowledge base

## Integration with Core System

This frontend integrates with the existing CrewAI system:

- `Core_Scripts/plazza_chat.py`: For the standard chat interface
- `Core_Scripts/advanced_router.py`: For the AI Orchestrator interface

## Troubleshooting

If you encounter errors:

1. Check that all required files and directories exist
2. Ensure the core system is properly installed and configured
3. Verify that all dependencies are installed
4. Check permissions on the result directories