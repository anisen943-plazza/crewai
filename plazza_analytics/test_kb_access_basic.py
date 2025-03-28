#!/usr/bin/env python
# Basic test script to verify knowledge file access (without using CrewAI Knowledge class)

import os
from pathlib import Path
import time

def main():
    # Calculate absolute knowledge directory path (same as in crew.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    kb_absolute_path = os.path.abspath(os.path.join(script_dir, 'knowledge'))
    
    print(f"\n🔍 Testing knowledge file access")
    print(f"Using knowledge directory: {kb_absolute_path}")
    
    # Check if directory exists
    if not os.path.isdir(kb_absolute_path):
        print(f"❌ Knowledge directory does not exist at: {kb_absolute_path}")
        return
    
    print(f"✅ Knowledge directory exists")
    
    # List files in the directory
    kb_files = os.listdir(kb_absolute_path)
    print(f"📚 Files in knowledge directory: {', '.join(kb_files)}")
    
    # Required knowledge files
    required_files = ["sales_analysis.md", "database_schemas.md", "customer_insights.md"]
    
    # Try to read and display content preview from each file
    for filename in required_files:
        file_path = os.path.join(kb_absolute_path, filename)
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                content_preview = content[:200] + '...' if len(content) > 200 else content
                print(f"\n✅ Successfully read file: {filename}")
                print(f"File size: {os.path.getsize(file_path)} bytes")
                print(f"Content preview: {content_preview}")
                
                # Look for specific keywords to demonstrate content relevance
                keywords = ["sales", "product", "customer", "database", "schema", "insights"]
                found_keywords = [kw for kw in keywords if kw.lower() in content.lower()]
                
                if found_keywords:
                    print(f"Found relevant keywords: {', '.join(found_keywords)}")
                else:
                    print("⚠️ No relevant keywords found in content")
                
            except Exception as e:
                print(f"❌ Error reading file {filename}: {e}")
        else:
            print(f"❌ Required file not found: {filename}")

if __name__ == "__main__":
    print("🧪 Testing Basic Knowledge File Access (without CrewAI Knowledge class)")
    start_time = time.time()
    main()
    print(f"\n✨ Test completed in {time.time() - start_time:.2f} seconds")