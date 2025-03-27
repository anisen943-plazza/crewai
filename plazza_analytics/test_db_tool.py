#!/usr/bin/env python
# Test script to directly use the CockroachDBTool

import os
from dotenv import load_dotenv
from src.plazza_analytics.tools.cockroach_db_tool import CockroachDBTool

# Load environment variables
load_dotenv()

def main():
    # Create the tool instance
    db_tool = CockroachDBTool()
    
    # Test database list
    print("\n=== Testing SHOW DATABASES ===")
    result = db_tool.run(query="SHOW DATABASES;")
    print(result)
    
    # Test simple query on defaultdb
    print("\n=== Testing simple query on defaultdb ===")
    try:
        result = db_tool.run(query="SELECT current_database();", database="defaultdb")
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test user_transactions database
    print("\n=== Testing user_transactions database ===")
    try:
        result = db_tool.run(query="SELECT COUNT(*) FROM orders;", database="user_transactions")
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test table listing in user_transactions
    print("\n=== Testing table listing in user_transactions ===")
    try:
        result = db_tool.run(
            query="SELECT table_name FROM information_schema.tables WHERE table_schema='public';", 
            database="user_transactions"
        )
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()