#!/usr/bin/env python
# Test script to directly use the SaveKnowledgeTool

import os
from pathlib import Path
from src.plazza_analytics.tools.save_knowledge_tool import SaveKnowledgeTool

def main():
    # Create the tool instance
    save_tool = SaveKnowledgeTool()
    
    # Define some content to save
    content = """# Order Statistics (2025-03-26)

## Order Count
The system currently has 57 orders stored in the database.

## Data Source
This information was retrieved by querying the user_transactions database:
```sql
SELECT COUNT(*) FROM orders;
```

## Timestamp
This information was last updated on 2025-03-26."""
    
    # Save to a specific file
    result = save_tool.run(content=content, filename="order_statistics.md", append=False)
    print(result)
    
    # Check if the file was created
    knowledge_dir = Path(__file__).resolve().parent / "knowledge"
    file_path = knowledge_dir / "order_statistics.md"
    if file_path.exists():
        print(f"File created successfully at: {file_path}")
        print("\nFile contents:")
        print("-" * 50)
        print(file_path.read_text())
        print("-" * 50)
    else:
        print(f"File not found at: {file_path}")

if __name__ == "__main__":
    main()