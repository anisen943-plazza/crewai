# CrewAI RAG Implementation Guide

This document describes how the Retrieval-Augmented Generation (RAG) system is implemented in the CrewAI sales analysis project.

## Overview

The RAG system consists of two main components:

1. **PreviousAnalysisTool**: A custom BaseTool that provides direct access to previous analysis content
2. **Knowledge Integration**: CrewAI's built-in Knowledge system that provides semantic search capabilities

Together, these components allow the agent to:
- Directly access previous analysis results when needed (using PreviousAnalysisTool)
- Automatically integrate relevant information from previous analyses into reasoning (using Knowledge)

## Implementation Details

### File Storage

Analysis results are stored in a markdown file:
- Location: `sales_ai_run_result.md`
- Format: Structured markdown with headers, sections, and timestamps
- Persistence: Automatically updated after each run

### Knowledge Creation

The system creates a knowledge source from previous analysis results:

```python
# Create knowledge source from markdown file
markdown_source = TextFileKnowledgeSource(
    file_paths=[ANALYSIS_RESULTS_PATH],
    chunk_size=800,       # Optimized for analysis content
    chunk_overlap=200,    # Ensures context is maintained between chunks
    metadata={"source": "sales_analysis", "date": file_timestamp}
)

# Create knowledge object with the source
sales_knowledge = Knowledge(
    collection_name="sales_analysis",
    sources=[markdown_source]
)
```

### Agent Configuration

The agent is configured to use both the tool and knowledge system:

```python
data_analyst = Agent(
    # Other parameters...
    tools=[CockroachDBTool(), PreviousAnalysisTool()],
    knowledge=[sales_knowledge],
    # Other parameters...
)
```

### How It Works

1. **During Initialization**:
   - The system reads the sales_ai_run_result.md file
   - Creates chunks of content (800 chars with 200 char overlap)
   - Generates embeddings for each chunk
   - Stores the embeddings in memory

2. **During Agent Processing**:
   - The agent can explicitly call the PreviousAnalysisTool to get the full previous analysis
   - LLM queries are automatically augmented with relevant chunks from previous analyses
   - The agent can build upon previous findings without redundant work

3. **After Analysis**:
   - New results are saved to the markdown file with timestamps
   - Future runs will automatically include the latest analysis
   - Historical analysis is preserved up to 30 days

## Optimization Notes

- **Chunk Size**: Set to 800 characters for optimal embedding performance
- **Overlap**: Set to 200 characters to maintain context across chunks
- **Formatting**: Structured with headers to improve chunking quality
- **Timestamp**: Added to track the age of analyses
- **Content Extraction**: Only the meaningful parts of the analysis are used

## Usage

No special commands are needed to use the RAG system. It's automatically integrated into:

```bash
# Full analysis with RAG integration
python sales_ai.py

# Debug version with RAG integration
python sales_ai_debug.py
```

The agent will automatically use both the explicit tool and the implicit knowledge retrieval system to access previous analyses.