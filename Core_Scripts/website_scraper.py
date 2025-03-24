from firecrawl import FirecrawlApp
import os
import pypandoc
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FirecrawlApp with your API key
api_key = os.getenv("FIRECRAWLER_API_KEY")  # Ensure your API key is set in the environment variable
if not api_key:
    raise ValueError("Please set your Firecrawl API key in the 'FIRECRAWLER_API_KEY' environment variable.")

app = FirecrawlApp(api_key=api_key)

# URL to crawl
url_to_crawl = "https://metabase.plazza.in/api/docs"

# Start the crawl
print(f"Starting crawl for {url_to_crawl}...")
try:
    crawl_result = app.crawl_url(
        url_to_crawl,
        params={
            'scrapeOptions': {'formats': ['markdown']},  # Fetch content in markdown format
            'limit': 50,  # Limit the number of pages to crawl
            'allowBackwardLinks': False  # Don't crawl backward links
        },
        poll_interval=30  # Check the status every 30 seconds
    )
except Exception as e:
    print(f"Error during crawl: {str(e)}")
    raise
print("Crawl completed!")

# Extract and combine the markdown content
combined_markdown = ""
if 'data' in crawl_result and crawl_result['data']:
    for page in crawl_result['data']:
        if 'metadata' in page and 'title' in page['metadata']:
            combined_markdown += f"# {page['metadata']['title']}\n\n"
        else:
            combined_markdown += f"# Untitled Page\n\n"
            
        if 'markdown' in page:
            combined_markdown += page['markdown'] + "\n\n"
        else:
            combined_markdown += "No content available\n\n"
else:
    combined_markdown = "# No data retrieved\n\nThe crawl did not return any data. Please check the URL and try again."

# Custom filename
markdown_file = "Metabase API docs - Plazza.md"
with open(markdown_file, "w", encoding="utf-8") as md_file:
    md_file.write(combined_markdown)
print(f"Combined markdown saved to {markdown_file}")