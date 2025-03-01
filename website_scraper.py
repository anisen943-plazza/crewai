from firecrawl import FirecrawlApp
import os
import pypandoc
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Initialize FirecrawlApp with your API key
api_key = os.getenv("FC_API_KEY")  # Ensure your API key is set in the environment variable
if not api_key:
    raise ValueError("Please set your Firecrawl API key in the 'FC_API_KEY' environment variable.")

app = FirecrawlApp(api_key=api_key)

# Define the URL to crawl
url_to_crawl = "https://www.zoho.com/books/api/v3/invoices/#list-invoice-templates"

# Start the crawl
print(f"Starting crawl for {url_to_crawl}...")
crawl_result = app.crawl_url(
    url_to_crawl,
    params={
        'scrapeOptions': {'formats': ['markdown']},  # Fetch content in markdown format
        'limit': 35,  # Limit the number of pages to crawl
        'allowBackwardLinks': False  # Allow crawling of backward links
    },
    poll_interval=30  # Check the status every 30 seconds
)
print("Crawl completed!")

# Extract and combine the markdown content
combined_markdown = ""
for page in crawl_result['data']:
    combined_markdown += f"# {page['metadata']['title']}\n\n"
    combined_markdown += page['markdown'] + "\n\n"

# Save the combined markdown to a file
markdown_file = "LiteLLM_Documentation_Zoho_invoice.md"
with open(markdown_file, "w", encoding="utf-8") as md_file:
    md_file.write(combined_markdown)
print(f"Combined markdown saved to {markdown_file}")