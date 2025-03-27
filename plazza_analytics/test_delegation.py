#!/usr/bin/env python3
# test_delegation.py - Test for DelegateWorkTool formatting fix

import os
import sys
import yaml
from pprint import pprint

# Add src to Python path to find modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

def test_yaml_templates():
    """Test that YAML task descriptions have properly escaped curly braces."""
    print("\n=== Testing YAML template formatting ===")
    
    # Check tasks.yaml
    tasks_file = os.path.join("src", "plazza_analytics", "config", "tasks.yaml")
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r') as f:
            try:
                tasks_yaml = yaml.safe_load(f)
                print(f"Tasks YAML loaded successfully: ✅")
                
                # Check for delegation examples
                for task_name, task_data in tasks_yaml.items():
                    if "description" in task_data:
                        desc = task_data["description"]
                        if "delegate" in desc.lower() and "json" in desc.lower():
                            print(f"\nFound delegation example in task '{task_name}':")
                            
                            # Check for properly escaped curly braces
                            if "{{" in desc and "}}" in desc:
                                print(f"  Properly escaped curly braces found: ✅")
                            else:
                                print(f"  WARNING: No escaped curly braces found in JSON example: ❌")
                                print(f"  This may cause template interpolation errors.")
                            
                            # Check for field requirements
                            if '"task":' in desc and '"context":' in desc and '"coworker":' in desc:
                                print(f"  All required fields (task, context, coworker) mentioned: ✅")
                            else:
                                missing = []
                                if '"task":' not in desc: missing.append("task")
                                if '"context":' not in desc: missing.append("context")
                                if '"coworker":' not in desc: missing.append("coworker")
                                print(f"  WARNING: Missing required fields in example: {', '.join(missing)} ❌")
            except Exception as e:
                print(f"Error parsing tasks.yaml: ❌")
                print(f"Exception: {str(e)}")
    else:
        print(f"tasks.yaml not found at {tasks_file} ❌")

    # Check agents.yaml
    agents_file = os.path.join("src", "plazza_analytics", "config", "agents.yaml")
    if os.path.exists(agents_file):
        with open(agents_file, 'r') as f:
            try:
                agents_yaml = yaml.safe_load(f)
                print(f"\nAgents YAML loaded successfully: ✅")
                
                # Check for delegation examples in agent backstories
                for agent_name, agent_data in agents_yaml.items():
                    if "backstory" in agent_data:
                        backstory = agent_data["backstory"]
                        if "delegate" in backstory.lower() and "json" in backstory.lower():
                            print(f"\nFound delegation example in agent '{agent_name}' backstory:")
                            
                            # Check for properly escaped curly braces
                            if "{{" in backstory and "}}" in backstory:
                                print(f"  Properly escaped curly braces found: ✅")
                            else:
                                print(f"  WARNING: No escaped curly braces found in JSON example: ❌")
                                print(f"  This may cause template interpolation errors.")
                            
                            # Check for field requirements
                            if '"task":' in backstory and '"context":' in backstory and '"coworker":' in backstory:
                                print(f"  All required fields (task, context, coworker) mentioned: ✅")
                            else:
                                missing = []
                                if '"task":' not in backstory: missing.append("task")
                                if '"context":' not in backstory: missing.append("context")
                                if '"coworker":' not in backstory: missing.append("coworker")
                                print(f"  WARNING: Missing required fields in example: {', '.join(missing)} ❌")
            except Exception as e:
                print(f"Error parsing agents.yaml: ❌")
                print(f"Exception: {str(e)}")
    else:
        print(f"agents.yaml not found at {agents_file} ❌")

def main():
    """Run all delegation format tests"""
    print("Testing delegation format fixes for CrewAI v0.108.0+ compatibility")
    test_yaml_templates()
    print("\nAll delegation format tests completed.")

if __name__ == "__main__":
    main()