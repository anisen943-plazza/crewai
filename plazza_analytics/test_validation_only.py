#!/usr/bin/env python3
# test_validation_only.py - Test RetentionAnalysisTool's validation without database

import os
import sys
from pprint import pprint
from typing import Literal, Dict, Any
from unittest.mock import patch, MagicMock

# Add src to Python path to find modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# Import the RetentionAnalysisArgs schema for testing
from plazza_analytics.tools.retention_analysis_tool_fix import RetentionAnalysisArgs

def test_schema_validation():
    """Test Pydantic schema validation"""
    print("\n=== Testing RetentionAnalysisArgs schema validation ===")
    
    # Test valid parameters
    print("\nTesting valid parameters:")
    try:
        args = RetentionAnalysisArgs(
            generate_visuals=True,
            force_refresh=False,
            query_intent="general",
            limit=10,
            include_contact_details=False
        )
        print(f"Valid parameters accepted: ✅")
        print(f"Model dump: {args.model_dump()}")
    except Exception as e:
        print(f"Error with valid parameters: ❌")
        print(f"Exception: {str(e)}")
    
    # Test query_intent validation
    print("\nTesting query_intent validation:")
    try:
        args = RetentionAnalysisArgs(query_intent="invalid_intent")
        print(f"Invalid query_intent accepted (shouldn't happen): ❌")
    except Exception as e:
        print(f"Invalid query_intent properly rejected: ✅")
        print(f"Exception: {str(e)}")
    
    # Test limit validation (too low)
    print("\nTesting limit validation (too low):")
    try:
        args = RetentionAnalysisArgs(limit=0)
        print(f"Invalid limit (too low) accepted (shouldn't happen): ❌")
    except Exception as e:
        print(f"Invalid limit (too low) properly rejected: ✅")
        print(f"Exception: {str(e)}")
    
    # Test limit validation (too high)
    print("\nTesting limit validation (too high):")
    try:
        args = RetentionAnalysisArgs(limit=101)
        print(f"Invalid limit (too high) accepted (shouldn't happen): ❌")
    except Exception as e:
        print(f"Invalid limit (too high) properly rejected: ✅")
        print(f"Exception: {str(e)}")

def main():
    """Run all validation tests"""
    print("Testing RetentionAnalysisTool validation with CrewAI v0.108.0+ compatibility fixes")
    test_schema_validation()
    print("\nAll validation tests completed.")

if __name__ == "__main__":
    main()