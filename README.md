# CrewAI Business Intelligence System

## Project Overview

This project combines CrewAI with CockroachDB to create an AI-powered data analysis system for the Plazza ecosystem (a retail/pharmaceutical platform). The system implements a fully modular, tool-based architecture with clearly separated responsibilities for database schema discovery, data analysis, visualization, and strategic recommendations.

## System Architecture

### Core Modules
- **agent_registry.py**: Centralized factory for all agents and tools
- **plazza_analytics.py**: Data analysis and visualization functionality
- **plazza_strategy.py**: Business strategy recommendations
- **plazza_chat.py**: User interface and query routing
- **crewai_visualization.py**: Enhanced visualization capabilities

### Agent Hierarchy
- **AI Orchestrator**: Central router that delegates tasks based on intent
- **Data Q&A Expert** (Primary chat agent): KB-first approach with specialized tools
- **Enterprise Data Analyst**: Deep analysis with database discovery
- **Visualization Specialist**: Creates charts and dashboards from KB data
- **Business Strategy Advisor**: Strategic recommendations based on KB insights

### Tool Composition
- **CockroachDBTool**: SQL query execution across databases
- **RetentionAnalysisTool**: Customer retention metrics calculation
- **MethodologyTool**: Structured query execution with documentation
- **VisualizationTool**: Visual representation of analysis results
- **Specialized Chart Tools**: TopProductsChartTool, CustomerRetentionChartTool, etc.

## Key Features

### Knowledge-First Architecture
- RAG-powered knowledge retrieval to minimize database queries
- Append-only knowledge storage with timestamp tracking
- Intelligent routing between KB access and fresh analysis
- Transparent methodology documentation with query tracking

### Enhanced Visualization System
- Interactive dashboards with Plazza branding
- Flexible input handling (file paths or direct content)
- Multiple chart types (product sales, customer retention, metrics)
- Specialized visualization tools for different data types
- Both HTML and PNG output formats

### Agent Delegation Framework
- Allows agents to request information from other agents
- Automatic logging of generated strategies with timestamps
- Cross-agent communication using CrewAI's delegation framework
- Structured metadata for better traceability

### Batch Analysis System
- Knowledge Base freshness checking to avoid redundant analysis
- Batch mode for scheduled execution via cron
- Command-line interface with flexible options
- Output persistence with timestamped file naming

## Project Structure

- **/Core_Scripts/**: Main application scripts (core system)
  - `agent_registry.py` - Centralized repository of agent definitions and tools
  - `crewai_visualization.py` - Core visualization module with chart generation
  - `plazza_analytics.py` - Main analysis script with database tools and tasks
  - `plazza_chat.py` - Interactive chat interface for database queries
  - `plazza_strategy.py` - Business strategy generation module
  - `tests/` - Test suite for Core_Scripts functionality

- **/Claude_Scripts/**: Contains helper scripts, debugging tools, and experimental implementations
  - Various database schema exploration scripts
  - Debugging tools and visualization demos
  - Experimental implementations

- **/Ref_documents/**: Reference materials and API documentation
  - API documentation for various services
  - Database schema JSON files
  - Sample files and templates

- **/Run_Results/**: Storage for analysis outputs
  - Analysis results with timestamped filenames
  - Strategy documents and reports
  - Chat logs and conversation history

- **/knowledge/**: RAG knowledge store
  - `sales_analysis_results.md` - Persistent storage of analysis for RAG
  - Used by CrewAI's knowledge retrieval system

- **/visuals/**: Visualization outputs
  - HTML dashboards with interactive elements
  - PNG exports for embedding in documentation
  - Each visualization named with timestamp for tracking

## Usage Examples

### Interactive Chat Interfaces

#### Standard Chat Interface
```bash
# Run the standard chat interface
python Core_Scripts/plazza_chat.py

# Common commands in the chat interface:
# "analyze sales data" - Trigger full analysis mode
# "what were our top products last month?" - Simple query mode
# "visualize the last analysis" - Generate visualizations
# "create a strategy for improving sales" - Generate business strategy
```

#### Advanced Router Interface (NEW)
```bash
# Run the advanced router with intelligent query delegation
python Core_Scripts/advanced_router.py

# Just ask any question naturally:
# "What are our top-selling products this quarter?"
# "Give me a dashboard showing repeat customers"
# "What strategy should we use to reduce customer churn?"
# "Analyze our sales performance compared to last year"

# The system will automatically route your query to the appropriate specialist
# and perform self-evaluation of response quality (logged for analysis)
```

The Advanced Router features:
- Intelligent intent classification and routing
- Self-evaluation of response quality
- Detailed logging of routing decisions
- Potential re-routing for inadequate responses
- Response quality metrics tracking

### Data Analysis
```bash
# Run full data analysis
python Core_Scripts/plazza_analytics.py

# Run analysis with specific focus
python Core_Scripts/plazza_analytics.py "Analyze customer retention trends"
```

### Batch Analysis with Freshness Check
```bash
# Normal run (skips if KB is fresh)
python Core_Scripts/batch_analysis.py

# Force run (ignores KB freshness)
python Core_Scripts/batch_analysis.py --force
```

### Visualization Generation
```bash
# Visualize from a file
python Core_Scripts/crewai_visualization.py --file analysis.md

# Visualize from direct content
python Core_Scripts/crewai_visualization.py --content "## Analysis..."

# Create a zip bundle of visualizations
python Core_Scripts/crewai_visualization.py --file analysis.md --zip
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/anisen943-plazza/crewai.git
cd crewai
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your database credentials and API keys
```

## Environment Variables

Required environment variables:
- `OPENAI_API_KEY`: For CrewAI agent (GPT-4o)
- `DATABASE_URL`: CockroachDB connection string for defaultdb
- `DATABASE_URL_USER_TRANSACTIONS`: Connection string for user_transactions
- `DATABASE_URL_ERP`: Connection string for plazza_erp database
- `DATABASE_URL_USER`: Connection string for user_events database
- `VISUALIZATION_OUTPUT_DIR`: Directory for visualization outputs
- `DEFAULT_ANALYSIS_FILE`: Default input file for visualizations

## Web Interface

A Streamlit-based web interface is available in the `/Streamlit_Frontend` directory.

### Features
- Dual chat interface (Standard Chat and Advanced Router)
- System status dashboard with knowledge base freshness monitoring
- Visualization display for generated charts
- Router logs and performance metrics

### Running the Web Interface
```bash
# Install requirements
pip install -r Streamlit_Frontend/requirements.txt

# Launch the web app
streamlit run Streamlit_Frontend/streamlit_app.py
```

The Dashboard view is also available:
```bash
streamlit run Streamlit_Frontend/dashboard.py
```

## Documentation

For comprehensive documentation about the system architecture, implementation details, and development history, see [CLAUDE.md](CLAUDE.md).

## License

This project is proprietary and confidential. All rights reserved.

## Contributors

- Aniruddha Sen (Project Lead)
- Claude (Technical Documentation and Development)