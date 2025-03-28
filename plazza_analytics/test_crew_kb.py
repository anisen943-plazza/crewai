#!/usr/bin/env python
# Test script specifically for the crew.py knowledge integration

import os
import sys
from pathlib import Path
import importlib.util

def main():
    print("\n🔧 Testing crew.py knowledge integration")
    
    # Load the crew module dynamically
    try:
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
        from plazza_analytics.crew import crew
        print("✅ Successfully imported crew module")
    except Exception as e:
        print(f"❌ Failed to import crew module: {e}")
        print("This could be due to the Knowledge class missing in CrewAI v0.30.0")
        return
    
    # Check if crew was initialized successfully
    if crew:
        print("✅ Crew instance created successfully")
        
        # Inspect the crew agents to see if they have knowledge
        if hasattr(crew, 'agents'):
            print(f"✅ Crew has {len(crew.agents)} agents")
            
            # Check if any agents have knowledge attached
            for i, agent in enumerate(crew.agents):
                if hasattr(agent, 'knowledge') and agent.knowledge:
                    print(f"✅ Agent {i+1} has knowledge attached: {agent.knowledge}")
                else:
                    print(f"⚠️ Agent {i+1} ({agent.role}) does not have knowledge attached")
        else:
            print("❌ Crew instance does not have agents attribute")
    else:
        print("❌ Crew instance was not created successfully")
    
    # Suggest path forward
    print("\n🔍 Analysis and Recommendations:")
    print("1. CrewAI v0.30.0 does not have the Knowledge class imported in crew.py")
    print("2. The knowledge base access is handled through custom tools instead:")
    print("   - SaveKnowledgeTool for writing to knowledge files")
    print("   - PreviousAnalysisTool for reading from knowledge files")
    print("3. Recommended approach:")
    print("   - Continue using the custom tools approach for now")
    print("   - Update the crew.py file to remove the Knowledge class import attempt")
    print("   - Consider updating CrewAI to a newer version that supports the Knowledge class")

if __name__ == "__main__":
    print("🧪 Testing Crew Knowledge Integration")
    main()