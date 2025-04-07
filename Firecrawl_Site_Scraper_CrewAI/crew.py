# crew.py
from pathlib import Path
import json
from crewai import Agent, Task, Crew, Process
from crewai_tools import FirecrawlScrapeWebsiteTool, FirecrawlCrawlWebsiteTool
from assemble_md import assemble_markdown
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Set Firecrawl API key from environment variable
firecrawl_api_key = os.getenv("FIRECRAWLER_API_KEY")
if not firecrawl_api_key:
    raise ValueError("Please set your Firecrawl API key in the 'FIRECRAWLER_API_KEY' environment variable.")
    

def create_api_scraper_crew(url: str, filename: str):
    firecrawl_api_key = os.getenv("FIRECRAWLER_API_KEY")
    crawl_tool = FirecrawlCrawlWebsiteTool(api_key=firecrawl_api_key)
    scrape_tool = FirecrawlScrapeWebsiteTool(api_key=firecrawl_api_key)

    output_dir = Path("API_documents")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / filename

    agent = Agent(
        role="Web Crawler and Scraper",
        goal="Extract high-quality API documentation and produce clean markdown",
        backstory="You are an expert at navigating API documentation sites and gathering complete content.",
        tools=[crawl_tool, scrape_tool],
        allow_delegation=False,
        verbose=True
    )

    crawl_task = Task(
        agent=agent,
        description=f"""
        Use the FirecrawlCrawlWebsiteTool to discover all relevant pages on {url}.
        Limit the crawl to 50 pages and maxDepth of 3. Your final answer MUST be
        a valid JSON array of URLs (strings) with no explanations.
        """,
        expected_output="A JSON array of discovered documentation page URLs.",
        output_file="API_documents/discovered_urls.json"
    )

    scrape_task = Task(
        agent=agent,
        description=f"""
        Load the discovered URLs from the previous step and scrape them using FirecrawlScrapeWebsiteTool.
        Additionally scrape these manual pages if available:
          - {url}/methods
          - {url}/web
          - {url}/authentication
          - {url}/block-kit
          - {url}/tools
          - {url}/tutorials

        For each URL:
        - Scrape and convert content to markdown
        - Clean out navigation, ads, footers, and duplicates
        - Properly format code, headings, tables, and links

        After scraping, return a complete markdown document combining all pages.
        Your final output MUST be valid markdown text.
        """,
        expected_output="A single comprehensive Markdown file combining all scraped docs.",
        output_file=str(output_path)
    )

    return Crew(
        agents=[agent],
        tasks=[crawl_task, scrape_task],
        process=Process.sequential,
        verbose=True
    )