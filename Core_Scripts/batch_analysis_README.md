# Plazza Analytics Batch Analysis

A comprehensive, automated data analysis and visualization tool for the Plazza ecosystem.

## Overview

This script runs a full batch analysis of Plazza business data and generates visualizations of the findings. It's designed to be both interactive for one-off analyses and schedulable via CRON for automated regular updates.

## Features

- 📊 **Full Business Analysis**: Aggregates data from multiple databases, analyzes patterns, and generates business insights.
- 🎨 **Automatic Visualization**: Creates interactive charts and dashboards from the analysis results.
- 🔄 **Knowledge Base Integration**: Checks existing knowledge freshness, avoids redundant analyses.
- 📦 **Visualization Bundles**: Creates ZIP archives of visualizations for easy sharing.
- 🌐 **Environment Variable Support**: Configurable paths through environment variables.
- 🕒 **Smart Scheduling**: Ideal for CRON jobs with freshness checking to avoid redundant runs.

## Installation

1. Ensure you're in the CrewAI project directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run a full analysis and generate visualizations:

```bash
python Core_Scripts/batch_analysis.py
```

### Command Line Options

The script supports several command line options for flexible execution:

```
Usage: python batch_analysis.py [--force] [--no-viz] [--output-dir DIR] [--viz-only]
    
Options:
    --force: Force batch analysis even if Knowledge Base is fresh
    --no-viz: Skip visualization generation
    --output-dir: Custom directory for visualizations (default: visuals)
    --viz-only: Skip analysis and only refresh visualizations using existing data
```

### Example Commands

1. **Force a fresh analysis** even if the KB is recent:
   ```bash
   python Core_Scripts/batch_analysis.py --force
   ```

2. **Run analysis without visualizations**:
   ```bash
   python Core_Scripts/batch_analysis.py --no-viz
   ```

3. **Specify a custom output directory** for visualizations:
   ```bash
   python Core_Scripts/batch_analysis.py --output-dir /path/to/custom/visuals
   ```

4. **Refresh only visualizations** using existing analysis data:
   ```bash
   python Core_Scripts/batch_analysis.py --viz-only
   ```

5. **Force analysis with custom output directory**:
   ```bash
   python Core_Scripts/batch_analysis.py --force --output-dir /path/to/output
   ```

## Operational Modes

### Full Analysis Mode (Default)
- Runs a complete business analysis
- Generates comprehensive visualizations
- Updates the knowledge base
- Creates visualization ZIP bundle

### Visualization-Only Mode
- Skips the analysis process
- Uses existing analysis data
- Regenerates all visualizations
- Good for trying different visualization styles

### No-Visualization Mode
- Performs only the data analysis
- Updates the knowledge base
- Skips visualization generation
- Useful for headless environments

## Environment Variables

The script supports configuration through environment variables:

- `VISUALIZATION_OUTPUT_DIR`: Custom directory for visualizations
- `DEFAULT_ANALYSIS_FILE`: Path to default analysis file when running viz-only

## Knowledge Base Freshness

The script intelligently checks the freshness of the knowledge base:

- Extracts timestamps from knowledge base content
- Falls back to file modification time if needed
- Default threshold is 7 days
- Can be overridden with `--force` flag

## Output Files

The script generates several output files:

1. **Analysis Results**: Saved to `Run_Results/batch_analysis_TIMESTAMP.md`
2. **Knowledge Base**: Updated at `knowledge/sales_analysis_results.md`
3. **Visualizations**: Saved to the specified output directory:
   - HTML dashboards
   - PNG chart images
   - Enhanced markdown with embedded charts
4. **ZIP Bundle**: Creates a timestamped ZIP file with all visualizations

## Scheduling

For automated analysis, add the script to your crontab:

```bash
# Run batch analysis every Monday at 5:00 AM
0 5 * * 1 cd /path/to/CrewAI && python Core_Scripts/batch_analysis.py
```

The built-in knowledge freshness check prevents unnecessary analysis runs, making it efficient for scheduled execution.

## Testing

Run the unit tests to ensure proper functionality:

```bash
cd /path/to/CrewAI
python -m unittest Core_Scripts/tests/test_batch_analysis.py
```

## Troubleshooting

### Common Issues

1. **Missing Knowledge Base**
   - Error: "Knowledge file not found"
   - Solution: Run with `--force` to generate initial knowledge base

2. **Visualization Failures**
   - Error: "Could not generate visualizations"
   - Solution: Ensure plotly and kaleido packages are installed

3. **Path Issues**
   - Error: "No module named 'Core_Scripts'"
   - Solution: Run from the project root directory

### Getting Help

For additional help, run:

```bash
python Core_Scripts/batch_analysis.py --help
```

## Next Steps

After running the batch analysis:

1. View visualizations in the output directory
2. Use the ZIP bundle for easy sharing
3. Run `plazza_chat.py` for interactive queries against the analysis
4. Schedule the script using cron for regular updates