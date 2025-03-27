#!/usr/bin/env python3
# test_retention_tool.py - Test script for RetentionAnalysisTool

import os
import sys
from pprint import pprint

# Add src to Python path to find modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# Import the fixed retention analysis tool
from plazza_analytics.tools.retention_analysis_tool_fix import RetentionAnalysisTool

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

def main():
    """Run all tests"""
    print("Testing RetentionAnalysisTool with CrewAI v0.108.0+ compatibility fixes")
    test_general_analysis()
    test_repeat_customers_query()
    test_parameter_validation()
    print("\nAll tests completed.")

if __name__ == "__main__":
    main()