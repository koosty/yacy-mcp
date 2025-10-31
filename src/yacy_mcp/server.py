"""
MCP Server for YaCy Web Search
"""
from typing import Any
import httpx
import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("yacy-search-mcp")

# Constants
YACY_DEFAULT_URL = "http://localhost:8090"
USER_AGENT = "yacy-mcp/0.1.0"


async def make_yacy_request(query: str, max_results: int = 10, resource: str = "global") -> dict[str, Any] | None:
    """Make a request to the YaCy API with proper error handling."""
    yacy_url = os.getenv("YACY_URL", YACY_DEFAULT_URL)
    
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    
    params = {
        "query": query,
        "maximumRecords": max_results,
        "resource": resource,
        "format": "json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{yacy_url}/yacysearch.json", headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


def format_results(data: dict) -> str:
    """Format search results into a readable string."""
    if not data or "channels" not in data or len(data["channels"]) == 0:
        return "No search results found."
    
    channel = data["channels"][0]
    if "items" not in channel or not channel["items"]:
        return "No search results found."
    
    results = []
    for item in channel["items"]:
        result = f"""
Title: {item.get('title', 'No title')}
Link: {item.get('link', 'No link')}
Description: {item.get('description', 'No description available')}
"""
        results.append(result)
    
    return "\n---\n".join(results)


@mcp.tool()
async def yacy_search(query: str, max_results: int = 10, resource: str = "global") -> str:
    """Search using YaCy web search engine.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return (default: 10)
        resource: Search resource (local or global, default: global)
    """
    data = await make_yacy_request(query, max_results, resource)
    
    if not data:
        return f"Unable to fetch search results for query: {query}"
    
    return format_results(data)


def main():
    # Initialize and run the server
    mcp.run(transport='stdio')    


if __name__ == "__main__":
    main()