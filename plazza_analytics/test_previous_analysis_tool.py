#!/usr/bin/env python
# Test script for PreviousAnalysisTool to verify knowledge file access

import os
import sys
from pathlib import Path

def main():
    # Import the PreviousAnalysisTool
    try:
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
        from plazza_analytics.tools.previous_analysis_tool import PreviousAnalysisTool
        print("✅ Successfully imported PreviousAnalysisTool")
    except Exception as e:
        print(f"❌ Failed to import PreviousAnalysisTool: {e}")
        return
    
    # Create an instance of the tool
    tool = PreviousAnalysisTool()
    print("✅ Created PreviousAnalysisTool instance")
    
    # Test accessing the default file (should be sales_ai_run_result.md)
    print("\n🔍 Testing default file access (sales_ai_run_result.md):")
    default_result = tool.run()
    print(f"Result: {default_result[:100]}..." if len(default_result) > 100 else default_result)
    
    # Test accessing the sales_analysis.md file in the knowledge directory
    print("\n🔍 Testing sales_analysis.md file access:")
    sales_result = tool.run(file="sales_analysis")
    print(f"Result: {sales_result[:100]}..." if len(sales_result) > 100 else sales_result)
    
    # Test accessing the database_schemas.md file in the knowledge directory
    print("\n🔍 Testing database_schemas.md file access:")
    schema_result = tool.run(file="database_schemas")
    print(f"Result: {schema_result[:100]}..." if len(schema_result) > 100 else schema_result)
    
    # Test accessing the customer_insights.md file in the knowledge directory
    print("\n🔍 Testing customer_insights.md file access:")
    customer_result = tool.run(file="customer_insights")
    print(f"Result: {customer_result[:100]}..." if len(customer_result) > 100 else customer_result)
    
    # Test accessing a non-existent file
    print("\n🔍 Testing non-existent file access:")
    non_existent_result = tool.run(file="non_existent_file")
    print(f"Result: {non_existent_result}")
    
    # Print summary
    print("\n📊 Summary:")
    print(f"- Default file access: {'✅ SUCCESS' if not default_result.startswith('ℹ️ No') else '❌ FAILED'}")
    print(f"- sales_analysis.md access: {'✅ SUCCESS' if not sales_result.startswith('ℹ️ No') else '❌ FAILED'}")
    print(f"- database_schemas.md access: {'✅ SUCCESS' if not schema_result.startswith('ℹ️ No') else '❌ FAILED'}")
    print(f"- customer_insights.md access: {'✅ SUCCESS' if not customer_result.startswith('ℹ️ No') else '❌ FAILED'}")
    print(f"- Non-existent file access: {'✅ SUCCESS' if non_existent_result.startswith('ℹ️ No') else '❌ FAILED'}")

if __name__ == "__main__":
    print("🧪 Testing PreviousAnalysisTool Knowledge File Access")
    main()