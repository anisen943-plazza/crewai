#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Website Scraper - API Documentation Extractor

This script uses the CrewAI framework with the Firecrawl tool to scrape API documentation
from websites and convert it to markdown format. The markdown files are saved in the
API_documents directory.

Usage:
    python website_scraper.py <url> <output_filename>
    
Example:
    python website_scraper.py https://api.slack.com Slack_API_Documentation.md
"""

import os
import sys
from pathlib import Path
import time
import json

from crewai import Agent, Task, Crew, Process
from crewai_tools import FirecrawlScrapeWebsiteTool
from crewai_tools import FirecrawlCrawlWebsiteTool

# Set Firecrawl API key from environment variable
firecrawl_api_key = os.getenv("FIRECRAWLER_API_KEY")
if not firecrawl_api_key:
    print("Error: FIRECRAWLER_API_KEY not found in environment variables.")
    sys.exit(1)

# Initialize the Firecrawl tools
# Note: param values are defined when the tool is used by the agent, not in the initialization
firecrawl_scrape_tool = FirecrawlScrapeWebsiteTool(api_key=firecrawl_api_key)
# Both limit and crawler_options are passed when the tool is used, not here
firecrawl_crawl_tool = FirecrawlCrawlWebsiteTool(api_key=firecrawl_api_key)

# Define output directory
output_dir = Path("API_documents")
output_dir.mkdir(exist_ok=True)

def main():
    # Get URL and output filename from command line arguments
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <url> <output_filename>")
        print(f"Example: {sys.argv[0]} https://api.slack.com Slack_API_Documentation.md")
        sys.exit(1)
        
    url = sys.argv[1]
    output_filename = sys.argv[2]
    output_path = output_dir / output_filename
    
    print(f"\n{'='*80}")
    print(f"Web Scraper - API Documentation Extractor")
    print(f"{'='*80}")
    print(f"URL: {url}")
    print(f"Output: {output_path}")
    print(f"{'='*80}\n")
    
    # Define the website scraper agent with the Firecrawl tools
    website_scraper = Agent(
        role="Website Content Scraper",
        goal="Extract comprehensive content from websites and convert it to well-structured markdown",
        backstory="""You are an expert at scraping websites and extracting valuable content. 
        You know how to navigate through different parts of a website, identify the important 
        sections, and compile them into a comprehensive, well-structured markdown document.
        You're skilled at removing navigation elements, ads, and other distractions to focus
        on the valuable content that users need.""",
        verbose=True,
        allow_delegation=False,
        tools=[firecrawl_scrape_tool, firecrawl_crawl_tool]
    )
    
    # Define the task to scrape the website and create documentation
    scraping_task = Task(
        description=f"""
        Extract all content from {url} and create a comprehensive markdown document.
        
        IMPORTANT INSTRUCTIONS:
        
        1. Use the FirecrawlCrawlWebsiteTool to discover pages on the website:
           - When using this tool, set limit to 50 pages and use maxDepth of 3
        
        2. Use the FirecrawlScrapeWebsiteTool to extract content from these key pages:
           - {url} 
           - {url}/methods
           - {url}/web
           - {url}/authentication
           - {url}/block-kit
           - {url}/tools
           - {url}/tutorials
           - Any additional important pages you discover
        
        3. Create a well-structured markdown document with:
           - Proper heading hierarchy (#, ##, ###)
           - Code examples in markdown code blocks
           - Tables and lists preserved
           - Images linked properly
           - URLs in markdown link format
           
        4. Clean, readable content:
           - Remove navigation, footers, ads, and cookie notices
           - Focus on documentation content only
           - Eliminate duplicates and irrelevant sections
           
        Be thorough and ensure you capture the complete API documentation.
        """,
        agent=website_scraper,
        expected_output="A comprehensive markdown document containing all the valuable content from the website."
    )
    
    # Create the crew with the website scraper agent
    crew = Crew(
        agents=[website_scraper],
        tasks=[scraping_task],
        verbose=True,
        process=Process.sequential
    )
    
    # Execute the crew to get the research results
    print(f"Starting API documentation extraction from {url}...")
    start_time = time.time()
    result = crew.kickoff()
    end_time = time.time()
    
    # Handle CrewOutput object to get the actual response text
    if hasattr(result, 'raw_output'):
        content = result.raw_output
    elif hasattr(result, '__str__'):
        content = str(result)
    else:
        print(f"Warning: Unexpected result type: {type(result)}")
        content = str(result)
    
    # Save the result to the output file
    output_path.write_text(content)
    
    print(f"\nAPI documentation extraction complete!")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Output saved to: {output_path}")

if __name__ == "__main__":
    main()