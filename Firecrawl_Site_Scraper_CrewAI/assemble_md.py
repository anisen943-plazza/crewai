# assemble_md.py

def assemble_markdown(scraped_pages: list) -> str:
    """Combine multiple pages of markdown content into one document."""
    combined = ["# Complete API Documentation\n"]
    for page in scraped_pages:
        if isinstance(page, str) and len(page.strip()) > 0:
            combined.append(page.strip())
            combined.append("\n\n---\n")
    return "\n".join(combined)