#!/usr/bin/env python3
# test_template_interpolation.py - Test template interpolation with curly braces

import os
import sys
import re
from string import Formatter

# Add src to Python path to find modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

def test_template_interpolation():
    """Test interpolation of curly braces in string templates"""
    print("\n=== Testing template interpolation with escaped curly braces ===")
    
    # Test case 1: Simple template with user_input variable
    print("\nTest case 1: Simple template with user_input variable")
    template1 = """
    You are given the following user request:
    
    "{user_input}"
    
    Analyze it and provide a response.
    """
    
    variables1 = {"user_input": "What are the top-selling products?"}
    
    try:
        result1 = template1.format(**variables1)
        print(f"Template interpolation successful: ✅")
        print(f"Preview: {result1[:50]}...")
    except KeyError as e:
        print(f"Template interpolation failed with KeyError: ❌")
        print(f"Missing key: {str(e)}")
    except Exception as e:
        print(f"Template interpolation failed with unexpected error: ❌")
        print(f"Error: {str(e)}")
    
    # Test case 2: Template with JSON example (no escaping)
    print("\nTest case 2: Template with JSON example (no escaping)")
    template2 = """
    When you use the delegation tool, the input must be a valid JSON object like this:
    {
      "task": "Do something specific",
      "context": "Everything they need to know in detail",
      "coworker": "Data Q&A Expert" 
    }
    
    Your query is: "{user_input}"
    """
    
    variables2 = {"user_input": "What are the top-selling products?"}
    
    try:
        result2 = template2.format(**variables2)
        print(f"Template interpolation successful: ✅")
        print(f"Preview: {result2[:50]}...")
    except KeyError as e:
        print(f"Template interpolation failed with KeyError: ❌")
        print(f"Missing key: {str(e)}")
    except Exception as e:
        print(f"Template interpolation failed with unexpected error: ❌")
        print(f"Error: {str(e)}")
    
    # Test case.3: Template with JSON example (properly escaped)
    print("\nTest case 3: Template with JSON example (properly escaped)")
    template3 = """
    When you use the delegation tool, the input must be a valid JSON object like this:
    {{
      "task": "Do something specific",
      "context": "Everything they need to know in detail",
      "coworker": "Data Q&A Expert" 
    }}
    
    Your query is: "{user_input}"
    """
    
    variables3 = {"user_input": "What are the top-selling products?"}
    
    try:
        result3 = template3.format(**variables3)
        print(f"Template interpolation successful: ✅")
        print(f"Preview: {result3[:50]}...")
    except KeyError as e:
        print(f"Template interpolation failed with KeyError: ❌")
        print(f"Missing key: {str(e)}")
    except Exception as e:
        print(f"Template interpolation failed with unexpected error: ❌")
        print(f"Error: {str(e)}")

def scan_yaml_for_template_vars():
    """Scan YAML files for template variables and check interpolation"""
    print("\n=== Scanning YAML files for template variables ===")
    
    # Pattern to find template variables: {variable_name}
    var_pattern = re.compile(r'{([^{}]+)}')
    
    # Check tasks.yaml
    tasks_file = os.path.join("src", "plazza_analytics", "config", "tasks.yaml")
    if os.path.exists(tasks_file):
        print(f"\nScanning tasks.yaml for template variables:")
        with open(tasks_file, 'r') as f:
            content = f.read()
            # Find all template variables
            matches = var_pattern.findall(content)
            if matches:
                print(f"Found {len(matches)} potential template variables:")
                for var in sorted(set(matches)):
                    print(f"  - {var}")
            else:
                print("No template variables found.")

    # Check agents.yaml
    agents_file = os.path.join("src", "plazza_analytics", "config", "agents.yaml")
    if os.path.exists(agents_file):
        print(f"\nScanning agents.yaml for template variables:")
        with open(agents_file, 'r') as f:
            content = f.read()
            # Find all template variables
            matches = var_pattern.findall(content)
            if matches:
                print(f"Found {len(matches)} potential template variables:")
                for var in sorted(set(matches)):
                    print(f"  - {var}")
            else:
                print("No template variables found.")

def main():
    """Run all template interpolation tests"""
    print("Testing template interpolation for CrewAI v0.108.0+ compatibility")
    test_template_interpolation()
    scan_yaml_for_template_vars()
    print("\nAll template interpolation tests completed.")

if __name__ == "__main__":
    main()