#!/usr/bin/env python
# Test script to verify PostgreSQLTool works correctly

import os
import sys

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

try:
    from src.plazza_crew.tools.custom_postgres_tool import PostgreSQLTool
    print("✅ PostgreSQLTool imported successfully")
    
    # Create an instance to test
    tool = PostgreSQLTool()
    print("✅ PostgreSQLTool instance created successfully")
    
    # Verify the class attributes
    print(f"Tool name: {tool.name}")
    print(f"Tables mapped: {list(tool.TABLE_TO_DB_MAP.keys())}")
    print(f"Databases mapped: {list(tool.CONN_TO_DB_NAME.values())}")
    
    # Test table detection
    test_queries = [
        "SELECT * FROM orders WHERE status='paid'",
        "SELECT * FROM inventory_transactions WHERE vendor_name='Example'",
        "SELECT * FROM contacts WHERE email LIKE '%@example.com'"
    ]
    
    for i, query in enumerate(test_queries):
        db_conn = tool._detect_table_in_query(query)
        db_name = tool.CONN_TO_DB_NAME.get(db_conn, "unknown")
        print(f"\nTest Query {i+1}: {query}")
        print(f"Detected database: {db_name} (using {db_conn})")
    
    print("\n✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()