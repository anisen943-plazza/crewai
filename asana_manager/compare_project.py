#!/usr/bin/env python3
"""
Asana Project Comparison Tool

This script compares tasks in an Asana project with implementation checklist 
items in a markdown document to identify mismatches.

Usage:
  python compare_project.py --project-name <name> <markdown_file_path> [options]
  python compare_project.py --project-gid <gid> <markdown_file_path> [options]
  
Examples:
  # Using project name:
  python compare_project.py --project-name "Pharmacist Operations Module" "/path/to/documentation.md"
  
  # Using project GID directly (faster and more reliable):
  python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md"
  
  # Additional options:
  python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --generate-json
  python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --summary-only
  python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --similarity 0.7
  python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --template headings --heading-level 3
  python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --template custom --pattern "Task: (.+?) \| Status: (.+?)$"
  python compare_project.py --project-gid "1234567890123456" "/path/to/documentation.md" --section "Implementation Checklist"
  
Options:
  --project-name        Name of the Asana project to check (searches across workspaces)
  --project-gid         GID of the Asana project to check directly (faster, more reliable)
  --generate-json, -j   Generate a JSON file with missing tasks
  --output, -o          Output path for JSON file
  --verbose, -v         Show detailed logs
  --similarity, -s      Set similarity threshold (0.0-1.0) for matching tasks
  --summary-only        Show only summary statistics
  --update-asana        Add missing checklist items to Asana (requires confirmation)
  --template, -t        Template format to use for parsing markdown (standard, headings, custom)
  --heading-level       For headings template, the heading level to use (e.g., 3 for ###)
  --pattern             For custom template, the regex pattern to extract tasks
  --section             Only look at tasks under a specific section (e.g., "Implementation Checklist")
"""

import os
import sys
import re
import json
import argparse
import requests
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# Try to load environment variables from Master_ENV directory
master_env_path = "/Users/aniruddhasen/Projects/Master_ENV/.env"
if os.path.exists(master_env_path):
    load_dotenv(master_env_path)
else:
    # Fall back to local .env file if it exists
    load_dotenv()

# Get Asana API token from environment variables
ASANA_API_TOKEN = os.getenv("ASANA_API_TOKEN")
if not ASANA_API_TOKEN:
    print("❌ ASANA_API_TOKEN not found in environment variables")
    print("   Please set this variable in your .env file or environment")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {ASANA_API_TOKEN}",
    "Content-Type": "application/json"
}
BASE_URL = "https://app.asana.com/api/1.0"

def list_workspaces() -> List[Dict[str, Any]]:
    """List all workspaces accessible to the user in Asana"""
    try:
        url = f"{BASE_URL}/workspaces"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        result = response.json()
        
        if 'data' in result:
            return result['data']
        else:
            print("❌ No workspaces found")
            return []
    except requests.exceptions.RequestException as e:
        print(f"❌ Error listing workspaces: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Status code: {e.response.status_code}")
            print(f"   Response: {e.response.text}")
        return []

def find_project_by_name(project_name: str, workspace_gid: str) -> Optional[Dict[str, Any]]:
    """Find an Asana project by name in the workspace"""
    try:
        url = f"{BASE_URL}/projects?workspace={workspace_gid}&limit=100"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        result = response.json()
        
        matching_projects = []
        
        if 'data' in result:
            for project_data in result['data']:
                # Handle possible nested data structure
                project = project_data.get('data', project_data)
                
                # Check if name exists and matches
                if 'name' in project and project_name.lower() in project['name'].lower():
                    matching_projects.append(project)
        
        if matching_projects:
            if len(matching_projects) > 1:
                print(f"ℹ️ Found {len(matching_projects)} matching projects. Using the first match.")
                for i, project in enumerate(matching_projects):
                    # Access attributes safely
                    name = project.get('name', 'Unknown')
                    gid = project.get('gid', 'Unknown')
                    print(f"   {i+1}. {name} (GID: {gid})")
            return matching_projects[0]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error finding project: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Status code: {e.response.status_code}")
            print(f"   Response: {e.response.text}")
        return None

def get_project_tasks(project_gid: str) -> List[Dict[str, Any]]:
    """Get all tasks from an Asana project"""
    try:
        tasks_url = f"{BASE_URL}/projects/{project_gid}/tasks"
        tasks_response = requests.get(tasks_url, headers=HEADERS)
        tasks_response.raise_for_status()
        tasks_data = tasks_response.json()
        
        asana_tasks = []
        if 'data' in tasks_data:
            # For each task, get its details to access the name
            for task_ref in tasks_data['data']:
                task_id = task_ref['gid']
                task_url = f"{BASE_URL}/tasks/{task_id}"
                task_response = requests.get(task_url, headers=HEADERS)
                task_response.raise_for_status()
                task_detail = task_response.json()
                
                if 'data' in task_detail:
                    asana_tasks.append({
                        'gid': task_id,
                        'name': task_detail['data'].get('name', ''),
                        'completed': task_detail['data'].get('completed', False)
                    })
        
        return asana_tasks
    except requests.exceptions.RequestException as e:
        print(f"❌ Error getting project tasks: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Status code: {e.response.status_code}")
            print(f"   Response: {e.response.text}")
        return []

def extract_checklist_items(
    markdown_file_path: str,
    template: str = "standard",
    heading_level: Optional[int] = None,
    pattern: Optional[str] = None,
    section_filter: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Extract checklist items from a markdown file based on the selected template.
    
    Args:
        markdown_file_path: Path to the markdown file
        template: Format template to use for extraction (standard, headings, custom)
        heading_level: For headings template, which heading level to use (e.g., 3 for ###)
        pattern: For custom template, the regex pattern to extract tasks
        section_filter: Only look at tasks under a specific section
        
    Returns:
        List of checklist items with text and completion status
    """
    try:
        with open(markdown_file_path, 'r') as f:
            markdown_content = f.read()
        
        # If section_filter is provided, extract only that section
        if section_filter:
            section_pattern = re.compile(f'## {re.escape(section_filter)}.*?(?=^##|\Z)', re.MULTILINE | re.DOTALL)
            section_match = section_pattern.search(markdown_content)
            if section_match:
                markdown_content = section_match.group(0)
                print(f"✅ Found section '{section_filter}' and extracted {len(markdown_content.splitlines())} lines")
            else:
                print(f"⚠️ Section '{section_filter}' not found in markdown document - using entire document")
        
        checklist_items = []
        
        if template == "standard":
            # Standard format: "- [ ] Task description" or "- [x] Task description"
            checklist_pattern = re.compile(r'- \[([ x])\] (.+?)$', re.MULTILINE)
            
            for match in checklist_pattern.finditer(markdown_content):
                is_checked = match.group(1) == 'x'
                task_text = match.group(2).strip()
                checklist_items.append({
                    'text': task_text,
                    'completed': is_checked
                })
                
        elif template == "headings":
            # Extract tasks from headings (e.g., ### Task Name)
            if not heading_level:
                heading_level = 3  # Default to H3 (###)
                
            heading_prefix = '#' * heading_level
            heading_pattern = re.compile(f'{heading_prefix} (.+?)$', re.MULTILINE)
            
            for match in heading_pattern.finditer(markdown_content):
                task_text = match.group(1).strip()
                # For headings, check if there's an explicit completion marker
                is_checked = any(marker in task_text.upper() for marker in ["DONE", "COMPLETED", "FINISHED", "✓", "✅"])
                # Remove any status markers from the task text
                for marker in ["DONE", "COMPLETED", "FINISHED", "✓", "✅"]:
                    task_text = task_text.replace(marker, "").replace(marker.lower(), "").strip()
                
                checklist_items.append({
                    'text': task_text,
                    'completed': is_checked
                })
                
        elif template == "custom" and pattern:
            # Use a custom regex pattern with groups for task text and completion status
            try:
                custom_pattern = re.compile(pattern, re.MULTILINE)
                
                for match in custom_pattern.finditer(markdown_content):
                    if len(match.groups()) >= 2:
                        # Assume first group is task text, second is completion status
                        task_text = match.group(1).strip()
                        status_text = match.group(2).strip().upper()
                        is_checked = any(marker in status_text for marker in 
                                         ["DONE", "COMPLETED", "FINISHED", "YES", "Y", "TRUE", "✓", "✅"])
                        checklist_items.append({
                            'text': task_text,
                            'completed': is_checked
                        })
                    elif len(match.groups()) == 1:
                        # If only one group, assume it's the task text and status is unknown
                        task_text = match.group(1).strip()
                        checklist_items.append({
                            'text': task_text,
                            'completed': False  # Default to not completed
                        })
            except re.error as e:
                print(f"❌ Invalid regex pattern: {e}")
                print("⚠️ Falling back to standard template")
                return extract_checklist_items(markdown_file_path, "standard")
        else:
            # Fallback to standard format if template isn't recognized
            print(f"⚠️ Unknown template '{template}' or missing pattern for custom template - using standard template")
            return extract_checklist_items(markdown_file_path, "standard")
            
        print(f"✅ Extracted {len(checklist_items)} checklist items using template '{template}'")
        return checklist_items
    except Exception as e:
        print(f"❌ Error extracting checklist items: {e}")
        return []

def calculate_string_similarity(str1: str, str2: str) -> float:
    """Calculate similarity between two strings using a simple algorithm"""
    # Convert to lowercase for comparison
    s1 = str1.lower()
    s2 = str2.lower()
    
    # Check for containment (one string being a subset of the other)
    if s1 in s2:
        # If str1 is smaller and is contained within str2, it's highly similar
        return len(s1) / len(s2) if len(s2) > 0 else 0.0
    elif s2 in s1:
        # If str2 is smaller and is contained within str1, it's highly similar
        return len(s2) / len(s1) if len(s1) > 0 else 0.0
    
    # For more complex cases, we could implement more sophisticated similarity
    # algorithms here like Levenshtein distance or Jaccard similarity
    # For now, we'll use a simpler approach based on common words:
    words1 = set(s1.split())
    words2 = set(s2.split())
    
    # Count common words
    common_words = words1.intersection(words2)
    
    # Calculate similarity based on common words
    total_words = len(words1.union(words2))
    return len(common_words) / total_words if total_words > 0 else 0.0

def compare_tasks_with_checklist(asana_tasks: List[Dict[str, Any]], 
                                 checklist_items: List[Dict[str, Any]],
                                 similarity_threshold: float = 0.5,
                                 template_used: str = "standard") -> Dict[str, Any]:
    """Compare Asana tasks with markdown checklist items"""
    # Missing in Asana: checklist items that don't have a matching task in Asana
    missing_in_asana = []
    
    # Missing in documentation: Asana tasks that don't have a matching checklist item
    missing_in_doc = []
    
    # Matches between Asana tasks and checklist items with similarity scores
    matches = []
    
    # Check which checklist items are missing in Asana
    for doc_item in checklist_items:
        found = False
        best_match = None
        best_score = 0.0
        
        for asana_task in asana_tasks:
            # Calculate similarity between the two task names
            similarity = calculate_string_similarity(doc_item['text'], asana_task['name'])
            
            # If similarity is above threshold, consider it a match
            if similarity >= similarity_threshold:
                found = True
                # Keep track of the best match
                if similarity > best_score:
                    best_score = similarity
                    best_match = asana_task
        
        if found and best_match:
            matches.append({
                'doc_item': doc_item,
                'asana_task': best_match,
                'similarity': best_score
            })
        else:
            missing_in_asana.append(doc_item)
    
    # Check which Asana tasks are missing in the checklist
    # Use a set to track asana tasks that already matched
    matched_tasks = set(match['asana_task']['gid'] for match in matches)
    
    for asana_task in asana_tasks:
        if asana_task['gid'] in matched_tasks:
            continue  # Skip tasks that already matched
            
        found = False
        for doc_item in checklist_items:
            # Calculate similarity between the two task names
            similarity = calculate_string_similarity(doc_item['text'], asana_task['name'])
            
            # If similarity is above threshold, consider it a match
            if similarity >= similarity_threshold:
                found = True
                break
        
        if not found:
            missing_in_doc.append(asana_task)
    
    # Prepare the comparison summary
    return {
        "template_used": template_used,
        "asana_tasks_count": len(asana_tasks),
        "checklist_items_count": len(checklist_items),
        "missing_in_asana": missing_in_asana,
        "missing_in_doc": missing_in_doc,
        "matches": matches,
        "complete_in_asana": [task for task in asana_tasks if task['completed']],
        "incomplete_in_asana": [task for task in asana_tasks if not task['completed']],
        "checked_in_doc": [item for item in checklist_items if item['completed']],
        "unchecked_in_doc": [item for item in checklist_items if not item['completed']]
    }

def print_summary_report(project: Dict[str, Any],
                         comparison_result: Dict[str, Any]) -> None:
    """Print a simplified summary report"""
    print("\n" + "=" * 60)
    print(f"📊 ASANA PROJECT COMPARISON SUMMARY: {project['name']}")
    print("=" * 60)
    
    # Calculate completion percentages
    completion_asana = len(comparison_result['complete_in_asana']) / comparison_result['asana_tasks_count'] * 100 if comparison_result['asana_tasks_count'] > 0 else 0
    completion_doc = len(comparison_result['checked_in_doc']) / comparison_result['checklist_items_count'] * 100 if comparison_result['checklist_items_count'] > 0 else 0
    
    # Calculate match rate
    match_rate = (comparison_result['asana_tasks_count'] - len(comparison_result['missing_in_doc'])) / comparison_result['asana_tasks_count'] * 100 if comparison_result['asana_tasks_count'] > 0 else 0
    
    print(f"\n📊 KEY METRICS:")
    print(f"   - Tasks in Asana:        {comparison_result['asana_tasks_count']}")
    print(f"   - Items in Documentation: {comparison_result['checklist_items_count']}")
    print(f"   - Tasks missing in Asana: {len(comparison_result['missing_in_asana'])}")
    print(f"   - Tasks missing in Doc:   {len(comparison_result['missing_in_doc'])}")
    print(f"   - Matching tasks:         {len(comparison_result.get('matches', []))}")
    print(f"   - Match rate:             {match_rate:.1f}%")
    print(f"   - Asana completion:       {completion_asana:.1f}%")
    print(f"   - Documentation checked:  {completion_doc:.1f}%")
    
    # Overall status assessment
    if match_rate > 90 and abs(comparison_result['asana_tasks_count'] - comparison_result['checklist_items_count']) < 5:
        print(f"\n✅ ASSESSMENT: Excellent alignment between Asana and documentation")
    elif match_rate > 75:
        print(f"\n✓ ASSESSMENT: Good alignment with some minor inconsistencies")
    elif match_rate > 50:
        print(f"\n⚠️ ASSESSMENT: Moderate alignment with significant inconsistencies")
    else:
        print(f"\n❌ ASSESSMENT: Poor alignment, major synchronization needed")
    
    print("\n" + "=" * 60)

def print_comparison_report(project: Dict[str, Any], 
                            comparison_result: Dict[str, Any]) -> None:
    """Print a formatted comparison report"""
    print("\n" + "=" * 80)
    print(f"📊 ASANA PROJECT COMPARISON REPORT: {project['name']}")
    print("=" * 80)
    
    print(f"\n📌 PROJECT DETAILS:")
    print(f"   - Project Name: {project['name']}")
    print(f"   - Project ID:   {project['gid']}")
    print(f"   - Workspace:    {project['workspace']['name']}")
    
    # Add template information if available
    if 'template_used' in comparison_result:
        print(f"   - Template:     {comparison_result['template_used']}")
    
    print(f"\n📊 STATISTICS:")
    print(f"   - Asana Tasks:          {comparison_result['asana_tasks_count']}")
    print(f"   - Checklist Items:      {comparison_result['checklist_items_count']}")
    print(f"   - Completed Tasks:      {len(comparison_result['complete_in_asana'])}")
    print(f"   - Incomplete Tasks:     {len(comparison_result['incomplete_in_asana'])}")
    print(f"   - Checked in Doc:       {len(comparison_result['checked_in_doc'])}")
    print(f"   - Unchecked in Doc:     {len(comparison_result['unchecked_in_doc'])}")
    print(f"   - Missing from Asana:   {len(comparison_result['missing_in_asana'])}")
    print(f"   - Missing from Doc:     {len(comparison_result['missing_in_doc'])}")
    print(f"   - Matching Tasks:       {len(comparison_result.get('matches', []))}")
    
    # Show some of the matches with their similarity scores
    if comparison_result.get('matches') and len(comparison_result['matches']) > 0:
        print(f"\n✅ SAMPLE MATCHES (with similarity scores):")
        for i, match in enumerate(sorted(comparison_result['matches'], key=lambda x: x['similarity'], reverse=True)[:5]):
            print(f"   {i+1}. {match['asana_task']['name']} ↔ {match['doc_item']['text']}")
            print(f"      Similarity: {match['similarity']:.2f}")
    
    if comparison_result['missing_in_asana']:
        print(f"\n❌ CHECKLIST ITEMS MISSING FROM ASANA ({len(comparison_result['missing_in_asana'])}):")
        for i, item in enumerate(comparison_result['missing_in_asana']):
            status = "✓" if item['completed'] else " "
            print(f"   {i+1}. [{status}] {item['text']}")
    
    if comparison_result['missing_in_doc']:
        print(f"\n⚠️ ASANA TASKS NOT IN DOCUMENTATION ({len(comparison_result['missing_in_doc'])}):")
        for i, task in enumerate(comparison_result['missing_in_doc']):
            status = "✓" if task['completed'] else " "
            print(f"   {i+1}. [{status}] {task['name']} (ID: {task['gid']})")
    
    print("\n🔍 RECOMMENDATIONS:")
    
    if comparison_result['missing_in_asana']:
        print("   1. Add the following checklist items to your Asana project:")
        for i, item in enumerate(comparison_result['missing_in_asana'][:5]):  # Show first 5
            print(f"      - {item['text']}")
        if len(comparison_result['missing_in_asana']) > 5:
            print(f"      - ... and {len(comparison_result['missing_in_asana']) - 5} more items")
    
    if comparison_result['missing_in_doc']:
        print("   2. Update your documentation to include these Asana tasks:")
        for i, task in enumerate(comparison_result['missing_in_doc'][:5]):  # Show first 5
            print(f"      - {task['name']}")
        if len(comparison_result['missing_in_doc']) > 5:
            print(f"      - ... and {len(comparison_result['missing_in_doc']) - 5} more tasks")
    
    completion_asana = len(comparison_result['complete_in_asana']) / comparison_result['asana_tasks_count'] * 100 if comparison_result['asana_tasks_count'] > 0 else 0
    completion_doc = len(comparison_result['checked_in_doc']) / comparison_result['checklist_items_count'] * 100 if comparison_result['checklist_items_count'] > 0 else 0
    
    print(f"\n   3. Current completion status:")
    print(f"      - Asana: {completion_asana:.1f}% complete")
    print(f"      - Documentation: {completion_doc:.1f}% checked")
    
    print("\n" + "=" * 80)

def generate_tasks_json(comparison_result: Dict[str, Any], output_path: str) -> None:
    """Generate a JSON file with tasks that can be created in Asana"""
    tasks_to_create = []
    
    for item in comparison_result['missing_in_asana']:
        tasks_to_create.append({
            "name": item['text'],
            "completed": item['completed'],
            "notes": "Added from documentation checklist"
        })
    
    with open(output_path, 'w') as f:
        json.dump(tasks_to_create, f, indent=2)
    
    print(f"\n✅ Generated tasks JSON file: {output_path}")
    print(f"   Contains {len(tasks_to_create)} tasks that can be imported to Asana")

def add_tasks_to_asana(project_gid: str, items_to_add: List[Dict[str, Any]]) -> int:
    """Add missing checklist items to Asana project
    
    Args:
        project_gid: The GID of the Asana project
        items_to_add: List of checklist items to add
        
    Returns:
        int: Number of tasks successfully added
    """
    success_count = 0
    print(f"\n🔄 Adding {len(items_to_add)} tasks to Asana project...")
    
    for i, item in enumerate(items_to_add):
        try:
            print(f"   Adding task {i+1}/{len(items_to_add)}: {item['text'][:50]}..." + ("" if len(item['text']) <= 50 else "..."))
            
            # Create the task in Asana
            url = f"{BASE_URL}/tasks"
            data = {
                "data": {
                    "name": item['text'],
                    "projects": [project_gid],
                    "completed": item['completed'],
                    "notes": "Added automatically from documentation checklist"
                }
            }
            
            response = requests.post(url, headers=HEADERS, json=data)
            response.raise_for_status()
            result = response.json()
            
            if 'data' in result and 'gid' in result['data']:
                success_count += 1
                print(f"   ✅ Task created with ID: {result['data']['gid']}")
            else:
                print(f"   ❌ Task creation failed: Unexpected response format")
        
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Error creating task: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"      Status code: {e.response.status_code}")
                print(f"      Response: {e.response.text}")
    
    print(f"\n✅ Successfully added {success_count} out of {len(items_to_add)} tasks to Asana")
    return success_count

def get_project_by_gid(project_gid: str) -> Optional[Dict[str, Any]]:
    """Get an Asana project by its GID directly"""
    try:
        url = f"{BASE_URL}/projects/{project_gid}"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        result = response.json()
        
        if 'data' in result:
            print(f"✅ Found project: {result['data']['name']} (GID: {result['data']['gid']})")
            return result['data']
        else:
            print(f"❌ No project found with GID: {project_gid}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error retrieving project: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Status code: {e.response.status_code}")
            print(f"   Response: {e.response.text}")
        return None

def main():
    """Main function to run the comparison tool"""
    parser = argparse.ArgumentParser(description='Compare Asana project tasks with markdown checklist items')
    project_group = parser.add_mutually_exclusive_group(required=True)
    project_group.add_argument('--project-name', help='Name of the Asana project to check')
    project_group.add_argument('--project-gid', help='GID of the Asana project to check directly')
    parser.add_argument('markdown_file', help='Path to the markdown file with implementation checklist')
    parser.add_argument('--generate-json', '-j', help='Generate a JSON file with tasks to create in Asana', action='store_true')
    parser.add_argument('--output', '-o', help='Output path for JSON file (default: tasks_to_create.json)', default='tasks_to_create.json')
    parser.add_argument('--verbose', '-v', help='Show detailed logs', action='store_true')
    parser.add_argument('--similarity', '-s', help='Set similarity threshold (0.0-1.0) for matching tasks', type=float, default=0.5)
    parser.add_argument('--summary-only', help='Show only summary statistics', action='store_true')
    parser.add_argument('--update-asana', help='Add missing checklist items to Asana (requires confirmation)', action='store_true')
    parser.add_argument('--template', '-t', help='Template format to use for parsing markdown (standard, headings, custom)', choices=['standard', 'headings', 'custom'], default='standard')
    parser.add_argument('--heading-level', help='For headings template, the heading level to use (e.g., 3 for ###)', type=int)
    parser.add_argument('--pattern', help='For custom template, the regex pattern to extract tasks and completion status')
    parser.add_argument('--section', help='Only look at tasks under a specific section (e.g., "Implementation Checklist")')
    
    args = parser.parse_args()
    
    # Validate similarity threshold
    if args.similarity < 0.0 or args.similarity > 1.0:
        print("❌ Similarity threshold must be between 0.0 and 1.0")
        sys.exit(1)
    
    if args.verbose:
        print(f"🔧 Settings:")
        if args.project_name:
            print(f"   - Project name:     {args.project_name}")
        else:
            print(f"   - Project GID:      {args.project_gid}")
        print(f"   - Markdown file:    {args.markdown_file}")
        print(f"   - Generate JSON:    {args.generate_json}")
        print(f"   - JSON output path: {args.output}")
        print(f"   - Similarity:       {args.similarity}")
        print(f"   - Summary only:     {args.summary_only}")
        print(f"   - Update Asana:     {args.update_asana}")
    
    # Get project either by name or by GID
    project = None
    
    if args.project_gid:
        # Direct GID lookup
        print(f"🔍 Retrieving project with GID: {args.project_gid}")
        project = get_project_by_gid(args.project_gid)
    else:
        # Name-based search through workspaces
        print(f"🔍 Searching for project: {args.project_name}")
        # List workspaces
        workspaces = list_workspaces()
        if not workspaces:
            print("❌ No workspaces found. Please check your Asana API token.")
            sys.exit(1)
        
        if not args.summary_only:
            print(f"✅ Found {len(workspaces)} workspaces")
        
        # Find the project in all workspaces
        for workspace in workspaces:
            if args.verbose:
                print(f"   Searching in workspace: {workspace['name']}")
            found_project = find_project_by_name(args.project_name, workspace['gid'])
            if found_project:
                project = found_project
                print(f"✅ Found project: {project['name']} (GID: {project['gid']})")
                break
    
    if not project:
        if args.project_gid:
            print(f"❌ Project with GID '{args.project_gid}' not found")
        else:
            print(f"❌ Project '{args.project_name}' not found in any workspace")
        sys.exit(1)
    
    # Get project tasks
    print(f"📥 Getting tasks from project: {project['name']}")
    asana_tasks = get_project_tasks(project['gid'])
    print(f"✅ Found {len(asana_tasks)} tasks in Asana project")
    
    # Extract checklist items from markdown
    print(f"📂 Reading markdown file: {args.markdown_file} using template '{args.template}'")
    checklist_items = extract_checklist_items(
        args.markdown_file,
        template=args.template,
        heading_level=args.heading_level,
        pattern=args.pattern,
        section_filter=args.section
    )
    print(f"✅ Found {len(checklist_items)} checklist items in markdown")
    
    # Compare tasks with checklist items
    print("🔄 Comparing Asana tasks with checklist items...")
    comparison_result = compare_tasks_with_checklist(
        asana_tasks, 
        checklist_items, 
        similarity_threshold=args.similarity,
        template_used=args.template
    )
    
    # Print the comparison report
    if args.summary_only:
        print_summary_report(project, comparison_result)
    else:
        print_comparison_report(project, comparison_result)
    
    # Generate JSON file if requested
    if args.generate_json:
        generate_tasks_json(comparison_result, args.output)
    
    # Update Asana if requested
    if args.update_asana and comparison_result['missing_in_asana']:
        confirm = input(f"\n⚠️ Are you sure you want to add {len(comparison_result['missing_in_asana'])} missing tasks to Asana? (y/N): ")
        if confirm.lower() == 'y':
            tasks_added = add_tasks_to_asana(project['gid'], comparison_result['missing_in_asana'])
            print(f"✅ Added {tasks_added} tasks to Asana project: {project['name']}")

if __name__ == "__main__":
    main()