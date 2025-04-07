# main.py
import os
import sys
from crew import create_api_scraper_crew

if len(sys.argv) != 3:
    print("Usage: python main.py <url> <output_filename>")
    sys.exit(1)

url = sys.argv[1]
filename = sys.argv[2]

# Set your Firecrawl API Key (or load from environment)
if not os.getenv("FIRECRAWLER_API_KEY"):
    print("Please set the FIRECRAWLER_API_KEY environment variable.")
    sys.exit(1)

crew = create_api_scraper_crew(url, filename)
result = crew.kickoff()
print("\n✅ Finished scraping!")