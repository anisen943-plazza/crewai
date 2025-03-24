"""
Plazza Analytics Batch Analysis

This script runs a full batch analysis of Plazza business data and generates 
comprehensive visualizations. It's designed to be scheduled via CRON for 
automated analysis and dashboard generation.

Usage:
    python batch_analysis.py [--force] [--no-viz] [--output-dir DIR] [--viz-only]
    
Options:
    --force: Force batch analysis even if Knowledge Base is fresh
    --no-viz: Skip visualization generation
    --output-dir: Custom directory for visualizations (default: visuals)
    --viz-only: Skip analysis and only refresh visualizations using existing data
"""

import os
import sys
import argparse
import re
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up parent directory path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Import centralized analysis functionality
sys.path.append(parent_dir)
from Core_Scripts.plazza_analytics import run_analysis
from crewai_visualization import visualize_analysis_results, export_visualizations_as_zip

def check_kb_freshness(max_age_days=7):
    """
    Check when the knowledge base was last updated.
    
    Args:
        max_age_days (int): Maximum age in days to consider the KB fresh
        
    Returns:
        bool: True if KB is fresh (updated within max_age_days), False otherwise
        datetime: The timestamp of the last update
    """
    knowledge_file = os.path.join(parent_dir, 'knowledge', 'sales_analysis_results.md')
    
    if not os.path.exists(knowledge_file):
        print(f"Knowledge file not found at {knowledge_file}")
        return False, None
        
    try:
        # Get modification time of the knowledge file
        mod_time = os.path.getmtime(knowledge_file)
        mod_date = datetime.fromtimestamp(mod_time)
        
        # Check the content for timestamps
        with open(knowledge_file, 'r') as file:
            content = file.read()
            
        # Look for analysis timestamps in the content
        timestamp_matches = re.findall(r'## Full Analysis on (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', content)
        
        if timestamp_matches:
            # Use the most recent timestamp from the content
            latest_timestamp = max(timestamp_matches)
            last_updated = datetime.strptime(latest_timestamp, '%Y-%m-%d %H:%M:%S')
            print(f"Found timestamp in content: {latest_timestamp}")
        else:
            # Fall back to file modification time if no timestamps found
            last_updated = mod_date
            print(f"No timestamp found in content, using file modification time: {mod_date}")
            
        # Check if KB is fresh (updated within max_age_days)
        days_old = (datetime.now() - last_updated).days
        hours_old = (datetime.now() - last_updated).total_seconds() / 3600
        
        if days_old > 0:
            freshness_msg = f"Knowledge Base is {days_old} days old"
        else:
            freshness_msg = f"Knowledge Base is {hours_old:.1f} hours old"
            
        print(f"📊 {freshness_msg} (threshold: {max_age_days} days)")
        return days_old <= max_age_days, last_updated
            
    except Exception as e:
        print(f"Error checking KB freshness: {str(e)}")
        return False, None

def get_latest_analysis_file():
    """
    Find the most recent analysis file from standard locations.
    
    Returns:
        str: Path to the most recent analysis file
        None: If no analysis file is found
    """
    # Look in standard locations
    potential_paths = [
        os.path.join(parent_dir, "Run_Results", "sales_ai_run_result.md"),
        os.path.join(parent_dir, "Run_Results", "batch_analysis_*.md"),
        os.path.join(parent_dir, "knowledge", "sales_analysis_results.md"),
    ]
    
    # Expand glob patterns and find all matching files
    all_matched_files = []
    for path in potential_paths:
        if '*' in path:
            # Handle glob pattern
            from glob import glob
            matches = glob(path)
            all_matched_files.extend(matches)
        elif os.path.exists(path):
            all_matched_files.append(path)
    
    if not all_matched_files:
        return None
    
    # Sort by modification time (most recent first)
    all_matched_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return all_matched_files[0]

def run_batch_analysis(force=False, skip_visualization=False, output_dir=None, viz_only=False):
    """
    Run full batch analysis and generate visualizations.
    
    Args:
        force (bool): Force analysis even if KB is fresh
        skip_visualization (bool): Skip visualization generation
        output_dir (str): Custom directory for visualizations
        viz_only (bool): Skip analysis and only refresh visualizations
        
    Returns:
        str: Analysis result or status message
        str: Path to output directory for visualizations
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set up visualization output directory
    if output_dir is None:
        output_dir = os.getenv("VISUALIZATION_OUTPUT_DIR", os.path.join(parent_dir, "visuals"))
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Check if we're only refreshing visualizations
    if viz_only:
        analysis_file = get_latest_analysis_file()
        if not analysis_file:
            print("❌ No existing analysis file found for visualization.")
            return "Error: No analysis file found", output_dir
            
        print(f"🔄 Refreshing visualizations from {os.path.basename(analysis_file)}")
        try:
            viz_results = visualize_analysis_results(input_file=analysis_file, output_dir=output_dir)
            
            # Create a ZIP bundle for convenience
            try:
                zip_path = export_visualizations_as_zip(output_dir)
                print(f"📦 Visualizations bundled in {os.path.basename(zip_path)}")
            except Exception as e:
                print(f"Warning: Could not create visualization bundle: {str(e)}")
                
            print(f"✅ Visualizations refreshed successfully in {output_dir}")
            return f"Visualizations refreshed from {os.path.basename(analysis_file)}", output_dir
        except Exception as e:
            print(f"❌ Error refreshing visualizations: {str(e)}")
            return f"Error refreshing visualizations: {str(e)}", output_dir
    
    # Check KB freshness if not forced
    if not force:
        is_fresh, last_updated = check_kb_freshness(max_age_days=7)
        if is_fresh:
            print("✅ Knowledge Base is fresh. Skipping batch analysis.")
            
            # If visualization is still requested, use the existing KB file
            if not skip_visualization:
                kb_file = os.path.join(parent_dir, 'knowledge', 'sales_analysis_results.md')
                try:
                    print(f"🎨 Generating visualizations from existing knowledge...")
                    viz_results = visualize_analysis_results(input_file=kb_file, output_dir=output_dir)
                    
                    # Create a ZIP bundle
                    zip_path = export_visualizations_as_zip(output_dir)
                    print(f"📦 Visualizations bundled in {os.path.basename(zip_path)}")
                    
                    print(f"✅ Visualizations generated in {output_dir}")
                except Exception as e:
                    print(f"⚠️ Warning: Could not generate visualizations: {str(e)}")
                
            return "Skipped analysis. Knowledge Base is up to date.", output_dir
    
    # Run the analysis if we've reached here
    print(f"🔍 Starting batch analysis at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        result = run_analysis()  # from plazza_analytics
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")
        return f"Error: {str(e)}", output_dir

    # Save to timestamped result file in Run_Results directory
    filename = f"batch_analysis_{timestamp}.md"
    result_dir = os.path.join(parent_dir, "Run_Results")
    filepath = os.path.join(result_dir, filename)
    os.makedirs(result_dir, exist_ok=True)
    
    with open(filepath, "w") as f:
        f.write(str(result))

    print(f"✅ Batch analysis completed. Results saved to {filepath}")
    
    # Generate visualizations unless explicitly skipped
    if not skip_visualization:
        try:
            print(f"🎨 Generating visualizations from analysis...")
            viz_results = visualize_analysis_results(content=result, output_dir=output_dir)
            
            # Create a ZIP bundle
            zip_path = export_visualizations_as_zip(output_dir)
            print(f"📦 Visualizations bundled in {os.path.basename(zip_path)}")
            
            print(f"✅ Visualizations generated in {output_dir}")
            
        except Exception as e:
            print(f"⚠️ Warning: Could not generate visualizations: {str(e)}")
    
    return result, output_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run batch analysis and visualization generation")
    parser.add_argument("--force", action="store_true", help="Force batch analysis even if KB is fresh")
    parser.add_argument("--no-viz", action="store_true", help="Skip visualization generation")
    parser.add_argument("--output-dir", help="Custom directory for visualizations")
    parser.add_argument("--viz-only", action="store_true", help="Skip analysis and only refresh visualizations")
    args = parser.parse_args()
    
    # Validate arguments for conflicting flags
    if args.no_viz and args.viz_only:
        print("❌ Error: --no-viz and --viz-only flags are conflicting and cannot be used together")
        print("   --no-viz: Skip visualization generation")
        print("   --viz-only: Skip analysis and only refresh visualizations")
        sys.exit(1)
    
    # If viz-only is specified, forcing analysis doesn't make sense
    if args.viz_only and args.force:
        print("⚠️ Warning: --force flag is ignored when using --viz-only")
        args.force = False

    result, output_dir = run_batch_analysis(
        force=args.force, 
        skip_visualization=args.no_viz,
        output_dir=args.output_dir,
        viz_only=args.viz_only
    )

    # Only show the analysis preview if we actually ran the analysis
    if not args.viz_only and isinstance(result, str) and not result.startswith("Skipped") and not result.startswith("Error"):
        print("\nAnalysis Summary:")
        print("="*50)
        preview = str(result)[:500] + "..." if len(str(result)) > 500 else str(result)
        print(preview)
    
    # Show next steps
    print("\nNext Steps:")
    if args.no_viz:
        print("- Run without --no-viz to generate visualizations")
    else:
        print(f"- View visualizations in: {output_dir}")
        print(f"- Use the ZIP bundle for easy sharing")
    
    print("- Run plazza_chat.py for interactive queries against the analysis")
    print("- Schedule this script using cron for regular updates")