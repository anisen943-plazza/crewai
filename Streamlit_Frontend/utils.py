"""
Utility functions for the Streamlit frontend.
"""
from datetime import datetime
import os
import json
import re
from pathlib import Path

# Get the parent directory
parent_dir = Path(__file__).resolve().parent.parent
RESULTS_DIR = parent_dir / "Run_Results"
VISUALS_DIR = parent_dir / "visuals"
KB_FILE = parent_dir / "knowledge" / "sales_analysis_results.md"
ROUTER_LOGS_DIR = parent_dir / "Run_Results" / "router_logs"

def get_files_by_pattern(directory, pattern, limit=None, sort_by_mtime=True, reverse=True):
    """
    Get files matching a pattern, optionally sorted by modification time.
    
    Args:
        directory (Path): Directory to search
        pattern (str): Glob pattern to match
        limit (int, optional): Limit number of results
        sort_by_mtime (bool): Whether to sort by modification time
        reverse (bool): Whether to sort in reverse order (newest first)
        
    Returns:
        list: List of Path objects
    """
    if not directory.exists():
        return []
        
    files = list(directory.glob(pattern))
    
    if sort_by_mtime:
        files = sorted(files, key=os.path.getmtime, reverse=reverse)
    
    if limit:
        files = files[:limit]
        
    return files

def check_kb_freshness(kb_file=KB_FILE, max_age_days=7):
    """
    Check freshness of the knowledge base and return status and timestamp.
    
    Args:
        kb_file (Path): Path to knowledge base file
        max_age_days (int): Maximum age in days to consider fresh
        
    Returns:
        tuple: (status, timestamp_str) where status is a string with emoji
    """
    if not kb_file.exists():
        return "❌ Not found", None
    
    timestamp = None
    
    # First try to find timestamp in content
    try:
        with open(kb_file, "r") as f:
            content = f.read()
            
        # Look for timestamps in content
        timestamp_matches = re.findall(r'## Full Analysis on (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', content)
        
        if timestamp_matches:
            # Get the most recent timestamp
            latest_ts_str = max(timestamp_matches)
            timestamp = datetime.strptime(latest_ts_str, '%Y-%m-%d %H:%M:%S')
    except Exception:
        pass
    
    # Fallback to file modification time
    if not timestamp:
        try:
            timestamp = datetime.fromtimestamp(kb_file.stat().st_mtime)
        except Exception:
            return "❌ Error reading file", None
    
    # Determine freshness
    delta_days = (datetime.now() - timestamp).days
    
    if delta_days <= 1:
        freshness = "🟢 Very fresh (today)"
    elif delta_days <= max_age_days:
        freshness = "🟢 Fresh"
    elif delta_days <= max_age_days * 2:
        freshness = "🟠 Stale"
    else:
        freshness = "🔴 Very stale"
    
    return freshness, timestamp.strftime("%Y-%m-%d %H:%M:%S")

def extract_self_evaluation(content):
    """
    Extract self-evaluation section from router logs.
    
    Args:
        content (str): Log content
        
    Returns:
        str: Extracted self-evaluation or None
    """
    match = re.search(r'## Router Self-Evaluation\n```\n(.*?)\n```', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_metadata_from_log(log_path):
    """
    Extract and structure metadata from a router log file.
    
    Args:
        log_path (Path): Path to log file
        
    Returns:
        dict: Structured metadata
    """
    try:
        content = log_path.read_text()
        
        metadata = {
            "timestamp": None,
            "query": None,
            "evaluation": None,
            "model": None
        }
        
        # Extract timestamp from filename or content
        timestamp_match = re.search(r'conversation_(\d{8}_\d{6})\.md', log_path.name)
        if timestamp_match:
            ts_str = timestamp_match.group(1)
            metadata["timestamp"] = datetime.strptime(ts_str, "%Y%m%d_%H%M%S")
        
        # Extract query
        query_match = re.search(r'## User Query\n```\n(.*?)\n```', content, re.DOTALL)
        if query_match:
            metadata["query"] = query_match.group(1).strip()
            
        # Extract self-evaluation
        metadata["evaluation"] = extract_self_evaluation(content)
        
        # Extract model
        model_match = re.search(r'- Model: (.*?)$', content, re.MULTILINE)
        if model_match:
            metadata["model"] = model_match.group(1).strip()
            
        return metadata
    except Exception:
        return {"error": "Failed to parse log"}

def get_router_performance_stats():
    """
    Calculate performance stats from router logs.
    
    Returns:
        dict: Statistics about router performance
    """
    if not ROUTER_LOGS_DIR.exists():
        return {}
        
    logs = get_files_by_pattern(ROUTER_LOGS_DIR, "conversation_*.md")
    
    stats = {
        "total_queries": len(logs),
        "agents_used": {},
        "routing_errors": 0,
        "average_character_length": 0
    }
    
    if not logs:
        return stats
    
    total_length = 0
    
    for log in logs:
        try:
            content = log.read_text()
            
            # Extract self-evaluation
            eval_text = extract_self_evaluation(content)
            if eval_text:
                # Count routing errors
                if "error" in eval_text.lower():
                    stats["routing_errors"] += 1
                
                # Extract agent used
                agent_match = re.search(r'Routed to ([^.]+)', eval_text)
                if agent_match:
                    agent = agent_match.group(1).strip()
                    stats["agents_used"][agent] = stats["agents_used"].get(agent, 0) + 1
            
            # Calculate response length
            response_match = re.search(r'## AI Response\n```\n(.*?)\n```', content, re.DOTALL)
            if response_match:
                response = response_match.group(1)
                total_length += len(response)
        except Exception:
            continue
    
    # Calculate average response length
    if stats["total_queries"] > 0:
        stats["average_character_length"] = total_length / stats["total_queries"]
    
    return stats