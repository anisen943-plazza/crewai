#!/usr/bin/env python3
"""
Test script for RetentionAnalysisTool to verify the Pydantic model-based args_schema fix.
"""

import os
import sys
from tools.retention_analysis_tool import RetentionAnalysisTool

def test_retention_tool():
    """Test the RetentionAnalysisTool with various parameter combinations."""
    print("Creating RetentionAnalysisTool instance...")
    tool = RetentionAnalysisTool()
    
    print("\n======== Test 1: Default Parameters ========")
    try:
        print("Calling tool.run() with no parameters")
        result = tool.run()
        print(f"Success! Result length: {len(str(result)) if result else 0} characters")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        print(traceback.format_exc())
    
    print("\n======== Test 2: General Intent with Force Refresh ========")
    try:
        print("Calling tool.run(force_refresh=True)")
        result = tool.run(force_refresh=True)
        print(f"Success! Result length: {len(str(result)) if result else 0} characters")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        print(traceback.format_exc())
    
    print("\n======== Test 3: Repeat Customers ========")
    try:
        print("Calling tool.run(query_intent='repeat_customers')")
        result = tool.run(query_intent="repeat_customers")
        print(f"Success! Result length: {len(str(result)) if result else 0} characters")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        print(traceback.format_exc())
    
    print("\n======== Test 4: Repeat Customers with Details ========")
    try:
        print("Calling tool.run(query_intent='repeat_customers', include_contact_details=True, limit=5)")
        result = tool.run(query_intent="repeat_customers", include_contact_details=True, limit=5)
        print(f"Success! Result length: {len(str(result)) if result else 0} characters")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        print(traceback.format_exc())
    
    print("\n======== Test 5: Invalid Query Intent ========")
    try:
        print("Calling tool.run(query_intent='invalid_intent')")
        result = tool.run(query_intent="invalid_intent")
        print(f"Success! Result length: {len(str(result)) if result else 0} characters")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        print(traceback.format_exc())
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    print("Starting RetentionAnalysisTool test script")
    test_retention_tool()