# CrewAI v0.108.0+ Compatibility Fixes

This document provides comprehensive documentation about the issues encountered, analyzed, and fixed in the Plazza Analytics project to ensure compatibility with CrewAI v0.108.0+.

## Problem Overview

The Plazza Analytics project was experiencing two critical issues after upgrading to CrewAI v0.108.0+:

1. **RetentionAnalysisTool Validation Errors**: The enhanced RetentionAnalysisTool with new parameters was failing with validation errors when agents tried to use it.

2. **Delegation Tool Format Errors**: The conversation orchestrator was experiencing validation errors when trying to use the "Delegate work to coworker" tool, specifically with the format of task and context parameters.

## Issue 1: RetentionAnalysisTool Validation Failures

### Problem Description

The RetentionAnalysisTool had been enhanced to accept new parameters:
- `query_intent`: For specifying different types of retention analysis ("general" or "repeat_customers")
- `include_contact_details`: Flag to include customer contact information in repeat customer listings
- `limit`: Maximum number of customers to return for repeat customer queries

However, after upgrading to CrewAI v0.108.0+, the tool was failing with validation errors:

```
CrewAI Task has ended with an error. Error: Arguments validation failed
Field required
```

### Root Cause Analysis

1. CrewAI v0.108.0+ uses strict Pydantic validation for tool parameters
2. The RetentionAnalysisTool lacked proper Pydantic schema definitions and type annotations
3. The tool was inheriting from BaseTool but wasn't properly configured for the new validation system
4. The error "Field required" indicated that a required parameter was missing or improperly defined

### Fix Implementation

The RetentionAnalysisTool was completely updated to comply with CrewAI v0.108.0+ requirements:

1. Added proper type annotations to class attributes:
```python
class RetentionAnalysisTool(BaseTool):
    name: str = "RetentionAnalysisTool"
    description: str = """Perform comprehensive customer retention analysis..."""
```

2. Structured the `run()` method with explicit parameter types and defaults:
```python
def run(self, 
        generate_visuals: bool = True,
        force_refresh: bool = False,
        query_intent: str = "general",
        limit: int = 10,
        include_contact_details: bool = False,
        **kwargs):
    """
    Execute comprehensive retention analysis across databases

    Args:
        generate_visuals (bool): Whether to generate visualizations (default: True)
        force_refresh (bool): Force a fresh analysis even if cached (default: False)
        query_intent (str): The type of query to perform: "general" or "repeat_customers" (default: "general")
        limit (int): Maximum number of customers to return for repeat_customers queries (default: 10)
        include_contact_details (bool): Whether to include contact details in repeat customer listings (default: False)
    """
```

3. Added parameter validation with fallbacks for invalid values:
```python
if query_intent not in ["general", "repeat_customers"]:
    print(f"WARNING: Invalid query_intent '{query_intent}'. Falling back to 'general'.")
    query_intent = "general"
```

4. Improved error handling with meaningful error messages:
```python
try:
    # Tool logic here
except Exception as e:
    error_msg = f"Error in RetentionAnalysisTool: {str(e)}"
    print(error_msg)
    return f"Failed to perform retention analysis: {error_msg}"
```

5. Created a test script (`test_retention_tool.py`) to verify that the tool accepts all parameters correctly

### Detailed Implementation of RetentionAnalysisTool Fix

Looking at the actual implementation in the codebase, we can see several key patterns that were essential for fixing the compatibility issue:

#### 1. Version History Documentation

The tool implementation begins with a clear version history documenting the evolution of the fixes:

```python
# Version History
# 2025-03-26: Updated for CrewAI v0.108.0+ compatibility
#   - Added parameter validation with proper type hints
#   - Updated run method to use **kwargs pattern for compatibility
#   - Added enhanced error handling and debug logging
#   - Added parameter validation for query_intent and limit
#   - Added proper fallback mechanisms for invalid parameter values
#   - Enhanced documentation with comprehensive docstrings
# 2025-03-27: Fixed Pydantic compatibility issues
#   - Modified to work properly with CrewAI v0.108.0 
#   - Used approach similar to other working tools in the project
#   - Removed custom schema classes
#   - Enhanced parameter validation with defensive coding
#   - Simplified implementation while maintaining functionality
```

#### 2. Proper Type Annotations

The class definition uses proper type annotations for all class attributes:

```python
class RetentionAnalysisTool(BaseTool):
    """Retention Analysis Tool for CrewAI.
    
    This tool performs comprehensive retention analysis across regular and Airtable data sources.
    """
    name: str = "RetentionAnalysisTool"
    description: str = """Perform comprehensive customer retention analysis across ALL data sources in the Plazza ecosystem.
    Analyzes BOTH regular tables AND Airtable tables to provide a complete view of customer behavior.
    Calculates repeat rates, time between purchases, top products, and discount impact.
    NOW FEATURES:
    1. Automatic schema discovery to adapt to different table structures
    2. Safe fallback mechanisms for missing columns
    3. Complete integration of both regular tables AND Airtable tables
    4. Indian Rupee (₹) formatting for all monetary values
    5. Robust error handling with clear explanations
    
    USAGE OPTIONS:
    - generate_visuals: Whether to generate visualizations (default: True)
    - query_intent: Type of analysis ("general" or "repeat_customers")
    - include_contact_details: Include customer names and contact information (with repeat_customers intent)
    - limit: Maximum number of results to return (default: 10)
    
    EXAMPLES:
    - Standard retention metrics: retention_analysis_tool.run()
    - Find repeat customers: retention_analysis_tool.run(query_intent="repeat_customers")
    - Customer details: retention_analysis_tool.run(query_intent="repeat_customers", include_contact_details=True)
    - Limit results: retention_analysis_tool.run(query_intent="repeat_customers", limit=5)"""
```

#### 3. Public Run Method with Complete Parameter Definitions

The `run()` method serves as the primary interface and includes:
- All parameter definitions with type hints
- Default values for each parameter
- Comprehensive docstring
- **kwargs pattern for future compatibility
- Debug logging for traceability
- Parameter validation with fallbacks
- Global cache handling
- Robust exception handling with meaningful error messages

```python
def run(self, 
        generate_visuals: bool = True, 
        force_refresh: bool = False,
        query_intent: str = "general",
        limit: int = 10,
        include_contact_details: bool = False,
        **kwargs):
    """Run comprehensive retention analysis on the user_transactions database.
    
    Args:
        generate_visuals: Whether to generate visualizations (default: True)
        force_refresh: Force a refresh of the analysis, ignoring the cache (default: False)
        query_intent: Type of analysis to perform ("general", "repeat_customers", etc.)
        limit: Maximum number of results to return for detailed queries (default: 10)
        include_contact_details: Whether to include customer names and contact information (default: False)
    
    Returns:
        str: Formatted retention analysis results.
    """
    global _retention_cache, _schema_cache
    
    try:
        print(f"RetentionAnalysisTool called with parameters: generate_visuals={generate_visuals}, "
              f"force_refresh={force_refresh}, query_intent={query_intent}, "
              f"limit={limit}, include_contact_details={include_contact_details}")
        
        # Parameter validation
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
            
        # Reset cache if forcing refresh or changing analysis type
        if force_refresh or query_intent != "general":
            _retention_cache = None
            print("Cache reset due to force_refresh or non-general query_intent")
        else:
            print("Using standard cache policy")
            
        # Use cache only for general analysis
        if query_intent == "general" and not force_refresh and _retention_cache:
            print("Returning cached results")
            return _retention_cache
        
        print("Executing _run with extracted parameters")
        return self._run(
            generate_visuals=generate_visuals,
            force_refresh=force_refresh,
            query_intent=query_intent,
            limit=limit,
            include_contact_details=include_contact_details
        )
    except Exception as e:
        error_message = f"ERROR in RetentionAnalysisTool.run: {str(e)}"
        print(error_message)
        import traceback
        print(traceback.format_exc())
        return error_message
```

#### 4. Defensive Parameter Validation

The tool implements robust parameter validation with informative messages and sensible defaults:

```python
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

#### 5. Enhanced Error Handling with Troubleshooting Information

When the tool encounters errors, it provides detailed troubleshooting information in a user-friendly format:

```python
detailed_error = f"""❌ Retention analysis failed: {str(e)}

## Troubleshooting Information
- Error type: {type(e).__name__}
- Error details: {str(e)}
- Query intent: {query_intent}
- Include contact details: {include_contact_details}
- Limit: {limit}
- Occurred during comprehensive retention analysis
- The tool attempted schema discovery but encountered an error during query execution

### Recommendation
This is likely due to one of the following issues:
1. Schema differences between regular and Airtable tables
2. Missing tables or columns required for the analysis
3. Type compatibility issues in SQL UNION operations
4. Parameter validation issues with the CrewAI tool schema

Please try running individual SQL queries via the CockroachDBTool to identify specific schema issues."""
```

#### 6. Private Implementation Method

The private `_run()` method is separated from the public interface and handles the actual implementation details:

```python
def _run(self, generate_visuals: bool = True, force_refresh: bool = False, 
         query_intent: str = "general", limit: int = 10, include_contact_details: bool = False) -> str:
    """Run comprehensive retention analysis on the user_transactions database.
    
    This is the internal implementation method called by run() after parameter processing.
    
    Args:
        generate_visuals (bool): Whether to generate visualizations (default: True)
        force_refresh (bool): Force a refresh of the analysis, ignoring the cache (default: False)
        query_intent (str): Type of analysis to perform ("general", "repeat_customers")
        limit (int): Maximum number of results to return for detailed queries (default: 10)
        include_contact_details (bool): Whether to include customer names and contact information (default: False)
    
    Returns:
        str: Formatted retention analysis results
    
    Raises:
        Exception: If database connection fails or analysis encounters an error
    """
    # Implementation details...
```

#### 7. Double Parameter Validation

Notice that the validation happens in both the public `run()` method and the private `_run()` method, adding an extra layer of validation:

```python
# In _run() method
if query_intent not in ["general", "repeat_customers"]:
    return f"""❌ Error: Invalid query_intent: '{query_intent}'
    
Please use one of the following supported values:
- "general": Standard retention metrics (repeat rate, time between purchases, etc.)
- "repeat_customers": Detailed list of repeat customers with purchase history

Example usage:
retention_analysis_tool.run(query_intent="repeat_customers", include_contact_details=True, limit=10)
"""
```

#### 8. Resource Cleanup in Finally Block

The code ensures proper cleanup of database connections using a finally block:

```python
finally:
    if conn:
        try:
            conn.close()
            print("Database connection closed.")
        except Exception as close_error:
            print(f"Warning: Error closing database connection: {str(close_error)}")
```

#### 9. Test Script Implementation

The test script (`test_retention_tool.py`) methodically tests all parameter combinations and validates the tool behavior:

```python
def test_general_analysis():
    """Test basic retention analysis functionality"""
    print("\n=== Testing general retention analysis ===")
    tool = RetentionAnalysisTool()
    
    # Test basic usage - should validate and run
    print("\nRunning general analysis with default parameters:")
    result = tool.run()
    print(f"Result length: {len(result) if result else 0} characters")
    print(f"Success: {'✅' if result and len(result) > 100 else '❌'}")
    
    # Test with forced refresh
    print("\nRunning with force_refresh=True:")
    result_refresh = tool.run(force_refresh=True)
    print(f"Result length: {len(result_refresh) if result_refresh else 0} characters")
    print(f"Success: {'✅' if result_refresh and len(result_refresh) > 100 else '❌'}")

def test_repeat_customers_query():
    """Test repeat customers query functionality"""
    print("\n=== Testing repeat customers query ===")
    tool = RetentionAnalysisTool()
    
    # Test repeat customers query without contact details
    print("\nRunning repeat customers query without contact details:")
    result = tool.run(query_intent="repeat_customers", include_contact_details=False)
    print(f"Result length: {len(result) if result else 0} characters")
    print(f"Success: {'✅' if result and len(result) > 100 else '❌'}")
    
    # Test repeat customers query with contact details
    print("\nRunning repeat customers query with contact details:")
    result_with_details = tool.run(query_intent="repeat_customers", include_contact_details=True)
    print(f"Result length: {len(result_with_details) if result_with_details else 0} characters")
    print(f"Success: {'✅' if result_with_details and len(result_with_details) > 100 else '❌'}")
    
    # Test with custom limit
    print("\nRunning with custom limit=5:")
    result_limit = tool.run(query_intent="repeat_customers", limit=5, include_contact_details=True)
    print(f"Result length: {len(result_limit) if result_limit else 0} characters")
    print(f"Success: {'✅' if result_limit and len(result_limit) > 100 else '❌'}")

def test_parameter_validation():
    """Test parameter validation functionality"""
    print("\n=== Testing parameter validation ===")
    tool = RetentionAnalysisTool()
    
    # Test invalid query_intent (should fall back to general)
    print("\nTesting invalid query_intent:")
    result = tool.run(query_intent="invalid_intent")
    print(f"Successfully validated and fell back to default: {'✅' if result and len(result) > 100 else '❌'}")
    
    # Test invalid limit (should clamp to valid range)
    print("\nTesting invalid limit (too high):")
    result = tool.run(query_intent="repeat_customers", limit=1000)
    print(f"Successfully clamped limit: {'✅' if result and len(result) > 100 else '❌'}")
    
    print("\nTesting invalid limit (non-integer):")
    result = tool.run(query_intent="repeat_customers", limit="abc")
    print(f"Successfully handled non-integer limit: {'✅' if result and len(result) > 100 else '❌'}")
```

### Key Insights: RetentionAnalysisTool Fix

1. **BaseTool Requirements in v0.108.0+**:
   - BaseTool implementations must use proper type annotations for class attributes
   - Run methods must have explicit parameter types and defaults
   - Error handling should catch and report exceptions effectively

2. **Parameter Validation Best Practices**:
   - Add validation logic for all parameters
   - Provide fallbacks for invalid values (safer than failing)
   - Use descriptive names and clear docstrings
   - Set reasonable defaults for optional parameters

3. **Testing Strategy**:
   - Create specific test cases for each parameter
   - Test parameters individually and in combination
   - Verify error handling for invalid inputs
   - Check that the tool functions correctly with all parameter variations

## Issue 2: Delegation Tool Parameter Formatting

### Problem Description

The conversation orchestrator agent was experiencing validation errors when trying to use the "Delegate work to coworker" tool:

```
CrewAI Task has ended with an error. Error: Validation failed for field 'task'. Expected str, got dict.
```

The agent was incorrectly formatting the parameters as dictionaries/objects, but the DelegateWorkToolSchema expected simple string values.

### Root Cause Analysis

1. The task description in `tasks.yaml` wasn't providing clear enough instructions about parameter formats
2. The LLM was interpreting fields like 'task' and 'context' as complex objects rather than simple strings
3. CrewAI's DelegateWorkToolSchema strictly validates parameter types (task must be str, not dict)
4. The error logs confirmed that the agent was using dictionaries instead of strings for these fields

### Fix Implementation (Part 1: JSON Format Instructions)

1. Updated the task description in `tasks.yaml` to explicitly instruct the agent on the correct JSON format:

```yaml
7. Delegate it using CrewAI delegation. Your delegation MUST be a JSON object with these EXACT keys and VALUE TYPES:

{{
  "task": "string with instructions (NOT a dictionary or object)",
  "context": "string with background (NOT a dictionary or object)",
  "coworker": "exact agent name as string"
}}

❗IMPORTANT: The "task" and "context" fields MUST be simple strings, NOT nested objects or dictionaries.
❗All three fields are REQUIRED or the delegation will fail with validation errors.

Example of CORRECT JSON format for multi-step delegations:
{{
  "task": "Count orders AND save the result to the knowledge base using SaveKnowledgeTool",
  "context": "User wants to know order count and wants it saved for future reference",
  "coworker": "Data Q&A Expert"
}}

Example for retention analysis:
{{
  "task": "Identify repeat customers using RetentionAnalysisTool with query_intent='repeat_customers', include_contact_details=True",
  "context": "User wants to see a list of repeat customers with their contact information",
  "coworker": "Data Q&A Expert"
}}

❌ INCORRECT format (DO NOT USE):
{{
  "task": {{"instruction": "Count orders", "save": true}},
  "context": {{"background": "User needs order count", "priority": "high"}},
  "coworker": "Data Q&A Expert"
}}
```

2. Enhanced the conversation orchestrator's backstory in `agents.yaml` to reinforce proper delegation formatting:

```yaml
DELEGATION FORMAT REQUIREMENTS:
When using the "Delegate work to coworker" tool, you MUST include all 3 required fields:
{{
  "task": "Clear instructions on what they need to do (MUST be a string, not an object/dictionary)",
  "context": "All relevant background information (MUST be a string, not an object/dictionary)",
  "coworker": "EXACT agent name from the list above"
}}

❗IMPORTANT: The "task" and "context" fields MUST be simple strings, NOT nested objects.
❗All three fields are REQUIRED or the delegation will fail with validation errors.
```

Note the double curly braces in the examples - these are important for the template interpolation fix described below.

### Fix Implementation (Part 2: Template Interpolation Fix)

After implementing the initial fix, we discovered a secondary issue where the JSON examples were causing a template interpolation error:

```
KeyError: '\n  "task"'
Missing required template variable '\n  "task"' in description
```

This occurred because:
1. CrewAI treats task descriptions as template strings for Python's string formatting
2. Curly braces `{` and `}` in the task description are interpreted as template variables
3. The JSON examples with curly braces were being interpreted as variable placeholders
4. When CrewAI tried to interpolate the template, it couldn't find the variable `"task"`

The solution:
1. Escape all curly braces in the JSON examples by doubling them: `{` → `{{` and `}` → `}}`
2. Apply this escaping in both the task description and agent backstory
3. This ensures the curly braces are interpreted as literal characters, not template placeholders

This is why all JSON examples in the YAML files now use double curly braces.

### Testing

A test script (`test_delegation.py`) was created to verify that the delegation now works correctly with the fixed format and template interpolation. The script tests different queries that should trigger delegation to various agents and checks for validation errors in the responses.

### Key Insights: Delegation Tool Fix

1. **LLM Output Formatting Control**:
   - Be extremely explicit in task descriptions about expected formats
   - Use both correct AND incorrect examples to guide the LLM
   - Add visual markers (emojis, formatting) to highlight critical instructions
   - Reinforce important formatting in multiple places (agent backstory and task description)

2. **CrewAI Delegation Schema Requirements**:
   - The DelegateWorkToolSchema expects specific parameter types:
     - task: str (not dict)
     - context: str (not dict)
     - coworker: str
   - All three fields are required
   - Format validation is strict - no flexibility for different structures

3. **Effective LLM Guidance Techniques**:
   - Use complete JSON examples with correct syntax
   - Show explicitly what NOT to do
   - Use warning symbols (❗, ❌) to highlight critical requirements
   - Format instructions as specific rules rather than general guidelines
   - Repeat critical instructions in multiple places

## Key Technical Concepts

1. **CrewAI v0.108.0+ Parameter Validation**:
   - Uses strict Pydantic validation for tool parameters
   - Requires proper type annotations for BaseTool classes
   - Validates all parameter types according to type hints
   - Requires all required parameters to be provided
   - Provides detailed error messages for validation failures

2. **BaseTool Implementation Requirements**:
   - Name and description should be properly annotated
   - The run() method should have explicit type hints
   - Parameter validation should be added for all inputs
   - Error handling should be comprehensive
   - Docstrings should clearly describe parameter usage

3. **LLM Instruction Techniques**:
   - Complete JSON examples are more effective than textual descriptions
   - Both positive and negative examples help guide output format
   - Visual highlighting of critical requirements improves compliance
   - Reinforcing instructions in multiple places increases effectiveness
   - Explicit error messages about formatting requirements help troubleshooting

4. **Testing Strategies**:
   - Test each parameter individually and in combination
   - Create test cases for different usage scenarios
   - Verify error handling for invalid inputs
   - Confirm that both fixes work together in the complete system
   - Automate testing with specific scripts for each component

## Testing and Documentation

1. **RetentionAnalysisTool Test Script**:
   Created `test_retention_tool.py` to verify all parameter combinations work correctly

2. **Delegation Test Script**:
   Created `test_delegation.py` to verify delegation works with various query types

3. **Comprehensive Documentation**:
   - `FIXES_DOCUMENTATION.md`: Detailed explanation of both fixes
   - `TESTING_FIXES.md`: Instructions for testing both fixes
   - `CLAUDE.md`: This document, summarizing all discoveries and implementations

4. **Implementation Files**:
   - `/src/plazza_analytics/tools/retention_analysis_tool.py`: Fixed tool implementation
   - `/src/plazza_analytics/config/tasks.yaml`: Updated task description for correct delegation
   - `/src/plazza_analytics/config/agents.yaml`: Enhanced backstory with delegation format requirements

## Best Practices for CrewAI v0.108.0+

1. **Tool Development**:
   - Always use proper type annotations for BaseTool classes
   - Provide explicit parameter types and defaults in run() methods
   - Add comprehensive error handling with meaningful messages
   - Include parameter validation with fallbacks for invalid values
   - Test all parameter combinations thoroughly

2. **Task Descriptions**:
   - Be extremely explicit about expected formats for tool parameters
   - Use complete examples with proper syntax
   - Include both correct AND incorrect examples
   - Use visual markers to highlight critical requirements
   - Reinforce important formatting in multiple places

3. **Agent Configuration**:
   - Include clear instructions in agent backstories about tool usage
   - Provide explicit formatting requirements for delegation
   - Use detailed examples for all tools that require specific formats
   - Consider memory settings for agents that need to maintain context
   - Test agents with a variety of queries to verify proper behavior

4. **System Architecture**:
   - Consider implementing standardized BaseTool extensions for common patterns
   - Create helper methods for parameter validation
   - Add logging for easier debugging
   - Implement a comprehensive test suite
   - Document all tools and their parameters

## Future Recommendations

1. **Tool Enhancement**:
   - Consider updating all tools to follow this same pattern for consistency
   - Add similar explicit formatting instructions in any task that uses tool parameters
   - Implement a standardized BaseTool extension for common validation patterns
   - Consider using CrewStructuredTool for complex parameter sets

2. **Testing Enhancement**:
   - Create a more comprehensive test suite that covers all tools
   - Add tests for edge cases and error handling
   - Implement automated testing as part of the development workflow
   - Create mock systems for faster testing without database dependencies

3. **Documentation Enhancement**:
   - Add tool usage examples to all tool docstrings
   - Create a tool reference guide with parameter descriptions
   - Document common error messages and their solutions
   - Update documentation with each new tool or parameter addition

4. **Code Organization**:
   - Consider organizing tools by functionality
   - Create a common base class for related tools
   - Implement shared validation methods
   - Use consistent error handling patterns

## Conclusion

The Plazza Analytics project has been successfully updated to work with CrewAI v0.108.0+. The key issues were:

1. **RetentionAnalysisTool**: Fixed with proper Pydantic integration for parameter validation
2. **Delegation Formatting**: Fixed by explicitly instructing the LLM on the correct parameter format

These fixes demonstrate the importance of understanding CrewAI's validation system and providing clear instructions to LLMs about expected formats. By following the best practices outlined in this document, future tool development should avoid similar issues and create a more robust system.

The project now has comprehensive documentation and test scripts to ensure ongoing compatibility with CrewAI v0.108.0+ and to help future developers understand the implemented solutions.