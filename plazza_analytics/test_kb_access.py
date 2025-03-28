#!/usr/bin/env python
# Test script to verify knowledge base access in CrewAI

import os
from pathlib import Path
import time

# Try to import CrewAI components
try:
    from crewai import Knowledge
    # The TextFileKnowledgeSource is still in a similar location
    try:
        # Try the new import path first
        from crewai.knowledge_source.text_file_knowledge_source import TextFileKnowledgeSource
    except ImportError:
        # Fall back to old import path
        from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
    
    print("✅ Successfully imported Knowledge and TextFileKnowledgeSource from CrewAI")
except ImportError as e:
    print(f"❌ Failed to import CrewAI Knowledge components: {e}")
    exit(1)

def main():
    # Calculate different potential knowledge directory paths
    print("\n🔍 Checking potential knowledge directories...")
    
    # Absolute path to knowledge directory
    kb_absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'knowledge'))
    print(f"Testing absolute knowledge path: {kb_absolute_path}")
    
    # Check if directory exists
    if os.path.isdir(kb_absolute_path):
        print(f"✅ Directory exists at: {kb_absolute_path}")
        
        # List files in the directory
        kb_files = os.listdir(kb_absolute_path)
        print(f"📚 Files in knowledge directory: {', '.join(kb_files)}")
        
        # Check specifically for the key knowledge files
        required_files = ["sales_analysis.md", "database_schemas.md", "customer_insights.md"]
        missing_files = [f for f in required_files if f not in kb_files]
        
        if missing_files:
            print(f"⚠️ Warning: Some required knowledge files are missing: {', '.join(missing_files)}")
        else:
            print("✅ All required knowledge files are present")
    else:
        print(f"❌ Directory does not exist at: {kb_absolute_path}")
    
    # Try to create knowledge sources with the absolute path
    print("\n📝 Attempting to create knowledge sources...")
    
    knowledge_files = [
        {"file": "sales_analysis.md", "domain": "sales", "type": "business_intelligence"},
        {"file": "database_schemas.md", "domain": "technical", "type": "database_schema"},
        {"file": "customer_insights.md", "domain": "customer", "type": "retention_analysis"}
    ]
    
    knowledge_sources = []
    for kf in knowledge_files:
        file_path = os.path.join(kb_absolute_path, kf["file"])
        try:
            source = TextFileKnowledgeSource(
                file_paths=[file_path],
                chunk_size=800,
                chunk_overlap=200,
                metadata={"domain": kf["domain"], "type": kf["type"]}
            )
            knowledge_sources.append(source)
            print(f"✅ Successfully created knowledge source for {kf['file']}")
        except Exception as e:
            print(f"❌ Failed to create knowledge source for {kf['file']}: {e}")
    
    # Try to create a Knowledge object with the sources
    if knowledge_sources:
        try:
            knowledge = Knowledge(
                collection_name="test_plazza_knowledge",
                sources=knowledge_sources
            )
            print("✅ Successfully created Knowledge object with sources")
            
            # Try to actually retrieve content from the knowledge
            print("\n🔎 Testing knowledge retrieval...")
            query_result = knowledge.retrieve("What are our top selling products?")
            print(f"📊 Knowledge retrieval result contains {len(query_result)} items")
            
            if query_result:
                print("✅ Successfully retrieved content from knowledge base")
                print("\n📝 Sample of retrieved content:")
                for i, item in enumerate(query_result[:2]):  # Show first 2 items
                    print(f"\nItem {i+1}:")
                    print(f"Content: {item.content[:200]}...")  # Truncate long content
                    print(f"Metadata: {item.metadata}")
            else:
                print("⚠️ Knowledge retrieval returned empty result")
            
        except Exception as e:
            print(f"❌ Failed to create Knowledge object: {e}")
    else:
        print("❌ No knowledge sources were created successfully")

if __name__ == "__main__":
    print("🧪 Testing CrewAI Knowledge Base Access")
    start_time = time.time()
    main()
    print(f"\n✨ Test completed in {time.time() - start_time:.2f} seconds")