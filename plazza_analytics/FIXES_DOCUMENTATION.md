# RetentionAnalysisTool Fixes Documentation

## Overview

This document provides a comprehensive overview of the fixes implemented for the `RetentionAnalysisTool` to address compatibility issues with CrewAI v0.108.0+ and improve overall functionality.

## Problem Summary

The `RetentionAnalysisTool` was experiencing several issues:

1. **CrewAI v0.108.0+ Compatibility**: The tool wasn't using Pydantic schemas correctly for parameter validation, causing errors with newer versions of CrewAI.
2. **Parameter Validation**: Parameters like `query_intent`, `limit`, and `include_contact_details` weren't being properly validated.
3. **Test Data Filtering**: Test data wasn't being consistently filtered out in all queries.
4. **Contact Detail Retrieval**: There were issues with retrieving customer contact details due to improper joins.
5. **Inconsistent Type Casting**: Type compatibility issues between UUID and string types in SQL queries.

## Implemented Fixes

### 1. CrewAI v0.108.0+ Compatibility

Added proper Pydantic schema for parameters:

```python
class RetentionAnalysisArgs(BaseModel):
    generate_visuals: bool = Field(
        default=True, 
        description="Whether to generate visualizations"
    )
    force_refresh: bool = Field(
        default=False, 
        description="Force a refresh of the analysis, ignoring the cache"
    )
    query_intent: Literal["general", "repeat_customers"] = Field(
        default="general", 
        description="Type of analysis to perform ('general' or 'repeat_customers')"
    )
    limit: int = Field(
        default=10, 
        description="Maximum number of results to return for detailed queries",
        ge=1,
        le=100
    )
    include_contact_details: bool = Field(
        default=False, 
        description="Whether to include customer names and contact information"
    )
```

And attached it to the tool:

```python
class RetentionAnalysisTool(BaseTool):
    # ...
    args_schema = RetentionAnalysisArgs
```

### 2. Enhanced Parameter Validation

Added robust parameter validation:

```python
# Validate query_intent
if query_intent not in ["general", "repeat_customers"]:
    print(f"WARNING: Invalid query_intent '{query_intent}'. Falling back to 'general'.")
    query_intent = "general"
    
# Validate limit
try:
    limit = int(limit)
    if limit < 1:
        print(f"WARNING: limit {limit} is too small. Setting to 1.")
        limit = 1
    elif limit > 100:
        print(f"WARNING: limit {limit} is too large. Setting to 100.")
        limit = 100
except (ValueError, TypeError):
    print(f"WARNING: Invalid limit '{limit}'. Falling back to default (10).")
    limit = 10
```

### 3. Improved Test Data Filtering

Added comprehensive test data detection:

```python
# Known test data patterns
TEST_PHONE_NUMBERS = {'8850959517', '9999999999', '9876543210', '0000000000'}
TEST_EMAIL_PATTERNS = ['test', 'example.com', 'noreply', 'nowhere']
TEST_ORDER_PATTERNS = ['TEST', 'POD-WEBHOOK', 'POD-TEST']

def _is_test_user(self, row):
    """Check if a user record is test data based on various indicators."""
    # Check known test phone numbers
    phone = str(row.get('phone_number', '')) if row.get('phone_number') else ""
    if phone in TEST_PHONE_NUMBERS:
        return True
        
    # Check email for test patterns
    email = str(row.get('email', '')) if row.get('email') else ""
    if any(pattern in email.lower() for pattern in TEST_EMAIL_PATTERNS):
        return True
        
    # Check order patterns
    order_id = str(row.get('order_id', '')) if row.get('order_id') else ""
    if any(pattern in order_id for pattern in TEST_ORDER_PATTERNS):
        return True
        
    # Additional test user detection - check for common test names
    first_name = str(row.get('first_name', '')).lower() if row.get('first_name') else ""
    last_name = str(row.get('last_name', '')).lower() if row.get('last_name') else ""
    if first_name in ['test', 'dummy', 'example'] or last_name in ['test', 'dummy', 'example']:
        return True
        
    return False
```

Enhanced SQL queries with consistent test data filtering:

```sql
-- Enhanced filtering in SQL queries
WHERE ao.status = 'paid'
  AND ao.order_id NOT LIKE '%TEST%'
  AND ao.order_id NOT LIKE 'POD-WEBHOOK%'
  AND (ac.email IS NULL OR ac.email NOT ILIKE '%test%')
  AND (c.phone IS NULL OR c.phone NOT IN ('8850959517', '9999999999', '9876543210'))
```

### 4. Fixed Contact Details Retrieval

Implemented proper joins with explicit aliases and type casting:

```python
# Explicit JOIN clauses with proper aliases
if has_contacts:
    contact_joins_regular.append("LEFT JOIN contacts c ON CAST(o.contact_id AS text) = CAST(c.id AS text)")
    
    # Add join for contact_phones if it exists
    if has_contact_phones:
        phone_joins_regular.append("LEFT JOIN contact_phones cp ON CAST(c.id AS text) = CAST(cp.contact_id AS text)")
```

Used `COALESCE` for combining data from multiple sources:

```python
# Add phone number if available with COALESCE
if phone_fields:
    phone_coalesce = f"COALESCE({', '.join(phone_fields)}) AS phone_number"
    contact_fields.append(phone_coalesce)
```

### 5. Consistent Type Casting

Added explicit type casting for all ID fields:

```sql
-- Common Table Expression (CTE) for regular orders with type casting
WITH regular_orders AS (
    SELECT CAST(o.contact_id AS text) AS contact_id, COUNT(*) as order_count
    FROM orders o
    LEFT JOIN contacts c ON o.contact_id = c.id
    -- more conditions...
)
```

## Usage Examples

### Basic Usage

```python
from plazza_analytics.tools.retention_analysis_tool_fix import RetentionAnalysisTool

# Create the tool
tool = RetentionAnalysisTool()

# Run general retention analysis
result = tool.run()

# Force refresh of the analysis
result_refresh = tool.run(force_refresh=True)
```

### Repeat Customers Query

```python
# Get repeat customers without contact details
result = tool.run(query_intent="repeat_customers")

# Get repeat customers with contact details
result = tool.run(query_intent="repeat_customers", include_contact_details=True)

# Limit the number of results
result = tool.run(query_intent="repeat_customers", limit=5)
```

### Using with CrewAI

```python
from crewai import Agent
from plazza_analytics.tools.retention_analysis_tool_fix import RetentionAnalysisTool

# Create the tool
retention_tool = RetentionAnalysisTool()

# Create an agent with the tool
analyst = Agent(
    role="Retention Analyst",
    goal="Analyze customer retention patterns",
    backstory="You are an expert in analyzing customer behavior and retention metrics.",
    tools=[retention_tool],
    verbose=True
)

# Define a task for the agent
task = Task(
    description="Analyze repeat customer patterns and provide insights",
    expected_output="A comprehensive analysis of customer retention with metrics and insights"
)

# Execute the task
result = analyst.execute_task(task)
```

## Testing

You can use the included `test_retention_tool.py` script to verify the functionality of the fixed tool:

```bash
python test_retention_tool.py
```

The script tests:
- General retention analysis
- Repeat customers query (with and without contact details)
- Parameter validation (invalid query_intent, invalid limit)

## Implementation Notes

1. **Module-Level Caching**: Implemented for performance optimization in repeated queries
2. **Enhanced Debugging**: Added detailed error messages with troubleshooting guidance
3. **Flexible Schema Discovery**: Dynamically adapts to differences in database structure
4. **Safe Query Generation**: Builds SQL based on available tables and columns
5. **Formatted Output**: Results are consistently formatted with markdown structure

## Conclusion

The `RetentionAnalysisTool` has been fixed to work correctly with CrewAI v0.108.0+ and provides enhanced functionality for customer retention analysis. The implementation is now more robust, with better parameter validation, improved test data filtering, and consistent SQL query generation.