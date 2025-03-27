# Testing the RetentionAnalysisTool Fixes

This document provides instructions for testing the fixes implemented in the `RetentionAnalysisTool` to ensure it works correctly with CrewAI v0.108.0+.

## Prerequisites

1. Python 3.10 or higher
2. CrewAI v0.108.0 or later
3. Access to the Plazza CockroachDB databases

## Running the Tests

The project includes a test script that automatically validates the key functionality of the RetentionAnalysisTool:

```bash
python test_retention_tool.py
```

This script tests:
- General retention analysis
- Repeat customers query
- Parameter validation
- Error handling

## Manual Testing Steps

For a more comprehensive validation, follow these manual testing steps:

### 1. Basic Functionality

```python
from plazza_analytics.tools.retention_analysis_tool_fix import RetentionAnalysisTool

# Create the tool
tool = RetentionAnalysisTool()

# Run general retention analysis (should return comprehensive results)
result = tool.run()
print(result)

# Check that caching works (should be faster and return identical results)
import time
start = time.time()
cached_result = tool.run()
end = time.time()
print(f"Cached execution took {end-start:.2f} seconds")
```

**Expected Result**: A markdown-formatted retention analysis with sections for data volume, sales summary, retention summary, time between purchases, discount impact, and cohort performance.

### 2. Force Refresh

```python
# Force refresh of the analysis (bypass cache)
result_refresh = tool.run(force_refresh=True)
```

**Expected Result**: Should generate a fresh analysis, bypassing the cache.

### 3. Repeat Customers Query

```python
# Get repeat customers without contact details
result_no_details = tool.run(query_intent="repeat_customers", include_contact_details=False)
print(result_no_details)

# Get repeat customers with contact details
result_with_details = tool.run(query_intent="repeat_customers", include_contact_details=True)
print(result_with_details)
```

**Expected Result**: 
- Without contact details: List of repeat customers with their purchase history, but no names, emails, or phone numbers
- With contact details: List of repeat customers with full contact information and purchase history

### 4. Limit Parameter

```python
# Test with a custom limit (should return exactly 5 customers)
result_limit = tool.run(query_intent="repeat_customers", limit=5, include_contact_details=True)
print(result_limit)
```

**Expected Result**: List of repeat customers, but limited to 5 entries.

### 5. Parameter Validation

```python
# Test invalid query_intent (should fall back to general)
result_invalid_intent = tool.run(query_intent="invalid_intent")

# Test invalid limit (too high - should clamp to 100)
result_high_limit = tool.run(query_intent="repeat_customers", limit=1000)

# Test invalid limit (non-integer - should fallback to 10)
result_bad_limit = tool.run(query_intent="repeat_customers", limit="abc")
```

**Expected Results**:
- Invalid intent: Should fall back to general analysis
- Too high limit: Should clamp to 100 and execute normally
- Non-integer limit: Should use default limit of 10

### 6. CrewAI Agent Integration

```python
from crewai import Agent, Task
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
print(result)
```

**Expected Result**: The agent should successfully use the tool and provide a formatted analysis with insights.

## Troubleshooting Common Issues

### Database Connection Errors

If you encounter database connection errors:
1. Verify your database environment variables are set correctly
2. Check VPN connectivity if accessing remote databases
3. Test a simple query using the CockroachDBTool to verify connectivity

### Parameter Validation Errors

If you encounter parameter validation errors:
1. Verify you're using the correct parameter names
2. Check that parameter values are within valid ranges (e.g., limit between 1 and 100)
3. Ensure query_intent is one of the valid options ("general" or "repeat_customers")

### Empty Results

If you get empty results:
1. Check that test data filtering isn't removing all results
2. Verify there are actual repeat customers in the database
3. Try running with force_refresh=True to bypass caching

## Verifying Specific Fixes

### 1. CrewAI v0.108.0+ Compatibility

Test that the tool works with the newer CrewAI version:

```python
import crewai
print(f"CrewAI version: {crewai.__version__}")

from plazza_analytics.tools.retention_analysis_tool_fix import RetentionAnalysisTool
tool = RetentionAnalysisTool()
result = tool.run()
```

**Expected Result**: No errors related to Pydantic validation or schema.

### 2. Contact Details Retrieval

Test that contact details are correctly retrieved:

```python
result = tool.run(query_intent="repeat_customers", include_contact_details=True)
```

**Expected Results**: Output should include customer names, email addresses, and phone numbers where available.

### 3. Test Data Filtering

Check that test data is properly filtered out:

```python
result = tool.run(query_intent="repeat_customers", include_contact_details=True)
```

**Expected Results**: No test users (with phone numbers like 8850959517 or emails containing "test") should appear in the results.

## Regression Testing

To ensure the fixes don't break existing functionality:

1. Run the original RetentionAnalysisTool and the fixed version with identical parameters
2. Compare the results for general retention analysis
3. Check that metrics like retention rate and average days between purchases are similar
4. Ensure test data filtering is at least as effective in the new version

## Integration Testing Plan

After verifying the tool works correctly on its own, test it in these integration scenarios:

1. **Agent Usage**: Test the tool as part of an agent workflow
2. **Multi-tool Workflow**: Test it alongside other tools like CockroachDBTool
3. **Long Running Session**: Test caching and performance over multiple invocations
4. **Cache Management**: Test that force_refresh properly invalidates cached results
5. **Parameter Handling**: Test that all parameter combinations work correctly

## Final Verification

To complete validation, verify these key fixes are working:

- [x] Pydantic schema validation for parameters is correct
- [x] Contact details are properly retrieved with JOINs
- [x] Test data is filtered out consistently
- [x] Type casting is applied to all ID fields
- [x] Error messages are detailed and helpful
- [x] Parameter validation handles invalid inputs gracefully
- [x] The tool runs successfully with CrewAI v0.108.0+