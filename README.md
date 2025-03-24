# CrewAI Business Intelligence System

## Project Overview

This project combines CrewAI with CockroachDB to create an AI-powered data analysis system for the Plazza ecosystem (a retail/pharmaceutical platform). The system includes database schema documentation generation, AI-driven data analysis, and API documentation tools.

## Enhanced Features

### 1. RAG Integration
The system has been enhanced with RAG (Retrieval-Augmented Generation) capabilities to provide knowledge persistence across analysis runs. This allows agents to reference past analyses and build upon prior findings.

### 2. Data Visualization
The system now includes comprehensive visualization capabilities:
- Bar charts for product sales analysis
- Pie charts for customer retention metrics
- Interactive dashboards for business metrics
- Automated visualization generation integrated with analysis results

### 3. Human-Readable Insights
- Product names instead of IDs in all analyses
- Test data filtering to ensure accurate business insights
- Structured output format optimized for visualization
- Enhanced metadata and context in analysis results

### 4. Advanced Retention Analysis
- Enhanced customer segmentation
- Time-between-purchase metrics
- Product categories driving repeat purchases
- Correlation between discounts and customer retention

## Components

### Core Files
- `sales_ai.py`: Main analysis system with RAG integration and visualization
- `crewai_visualization.py`: Visualization module for creating charts and dashboards
- `knowledge/sales_analysis_results.md`: Persistent knowledge store for RAG

### Tools
- `CockroachDBTool`: Enhanced with product name extraction and test data filtering
- `PreviousAnalysisTool`: Access to historical analysis results
- `CrewAIVisualization`: Class for creating visualizations from analysis results

### Visualization Types
- Product sales bar charts
- Customer retention pie charts
- Business metrics dashboards
- Interactive HTML visualizations

## Usage

```bash
# Install dependencies
pip install -r requirements_db_doc.txt

# Run the analysis system
python sales_ai.py

# View generated visualizations in the visuals/ directory
```

## Visualization Examples

After running `sales_ai.py`, the system will:
1. Generate comprehensive business analysis
2. Create visualizations in the `visuals/` directory
3. Embed visualizations in the enhanced markdown report
4. Generate both static images and interactive HTML visualizations

## Environment Variables

Requires the following environment variables:
- `OPENAI_API_KEY`: For CrewAI agent (GPT-4o)
- `DATABASE_URL`: CockroachDB connection string for defaultdb
- `DATABASE_URL_USER_TRANSACTIONS`: Connection string for user_transactions
- `DATABASE_URL_ERP`: Connection string for plazza_erp database
- `DATABASE_URL_USER`: Connection string for user_events database