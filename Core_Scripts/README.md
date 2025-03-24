# Plazza Analytics System

This directory contains the core analytics system for Plazza, including both interactive chat interface and batch analysis capabilities.

## Components

### 1. Interactive Chat Interface (`plazza_chat.py`)

The chat interface allows users to interact with the Plazza Analytics multi-agent system in real-time, asking questions about business data and requesting visualizations on demand.

**Features:**
- Interactive CLI interface
- Question routing to specialized agents
- On-demand visualization generation
- Conversation history tracking
- Knowledge persistence
- Error handling and recovery

**Usage:**
```bash
python plazza_chat.py
```

**Commands:**
- Type any business question to get analysis
- Type 'viz' to generate visualizations from the last response
- Type 'exit' or 'quit' to end the session

### 2. Batch Analysis System (`batch_analysis.py`)

The batch analysis script runs a comprehensive data analysis and visualization pipeline, designed for scheduled execution (e.g., via CRON). It includes intelligence to avoid redundant analysis when the Knowledge Base is fresh.

**Features:**
- Full database schema discovery
- Multi-database analysis
- Automatic visualization generation
- Results persistence to knowledge base
- Knowledge Base freshness checking
- Visualization ZIP bundle creation
- Multiple operational modes
- Smart file discovery logic

**Usage:**
```bash
# Basic usage - full analysis with visualizations
python batch_analysis.py

# Force analysis even if KB is fresh
python batch_analysis.py --force

# Skip visualization generation
python batch_analysis.py --no-viz

# Specify a custom output directory
python batch_analysis.py --output-dir /path/to/output

# Refresh visualizations only (no analysis)
python batch_analysis.py --viz-only
```

For comprehensive documentation, see `batch_analysis_README.md`.

### 3. Core Analytics Engine (`plazza_analytics.py`)

The core module that powers both the chat interface and batch analysis, containing agent definitions, tool implementations, and task configurations.

### 4. Visualization System (`crewai_visualization.py`)

The visualization module that generates charts, dashboards, and visual representations of analytical insights.

## Architecture

The system uses a multi-agent architecture powered by CrewAI:

1. **Enterprise Data Analyst Agent** - Specializes in database querying and analysis
2. **Data Visualization Specialist Agent** - Creates visual representations of data

These agents use specialized tools:
- `CockroachDBTool` - Executes SQL queries against multiple databases
- `RetentionAnalysisTool` - Calculates customer retention metrics
- `VisualizationTool` - Generates charts and dashboards

## Knowledge Persistence

The system uses CrewAI's knowledge persistence mechanisms to maintain context between sessions:
- Analysis results are saved to the `knowledge/` directory
- Conversation history is maintained within sessions
- Chat results are saved to `Run_Results/` for reference

## Visualization Outputs

Visualizations are saved to the `visuals/` directory and include:
- Product sales charts
- Customer retention pie charts
- Business metrics dashboards
- Time series charts
- Geographic distribution charts

## Requirements

- Python 3.10+
- Environment variables for database connections
- OpenAI API key for GPT-4o
- Required Python packages (see `requirements.txt`)

### Package Version Notes

- CrewAI: The system now uses version-agnostic path handling for the knowledge directory
- The code has been tested with CrewAI v0.102.0 and should work with newer versions
- If upgrading CrewAI, pay special attention to changes in knowledge system implementation
- Consider using a virtual environment with pinned dependencies for production deployments

## Testing

The system includes unit tests to ensure correct behavior and catch regressions:

### Running Tests

```bash
# Run all tests
python -m unittest discover Core_Scripts/tests

# Run specific test file
python -m unittest Core_Scripts/tests/test_batch_analysis.py
python -m unittest Core_Scripts/tests/test_visualization_cli.py
```

### Test Coverage

The test suite includes:

1. **Batch Analysis Tests**:
   - Command-line argument validation
   - Knowledge Base freshness checking
   - File discovery logic
   - Handling of conflicting flags
   - Multiple operational modes

2. **Visualization CLI Tests**:
   - File argument handling
   - Direct content processing
   - ZIP bundle creation
   - Output directory specification

## Troubleshooting

If visualizations are not generating:
1. Check that the `visuals/` directory exists and is writable
2. Ensure the analysis contains structured data points
3. Try using the 'viz' command explicitly
4. Check the console for error messages

If batch_analysis.py throws errors:
1. Check for conflicting command-line flags (e.g., --no-viz and --viz-only)
2. Ensure the output directory is writable
3. Check that required functions exist in plazza_analytics.py
4. Review the error message for specific causes

If you encounter a "No module named 'crewai.utils'" error:
1. This has been fixed in the latest version with a path handling update
2. The system now uses direct path construction instead of relying on crewai.utils
3. If you're using a different branch or older version, modify the create_knowledge_source() function in plazza_analytics.py to use direct paths
4. See the "CrewAI Compatibility Fix" section in CLAUDE.md for details