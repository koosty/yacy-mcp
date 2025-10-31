#!/usr/bin/env python3
"""
Simple client to test the YaCy MCP server
"""
import asyncio
import json
from mcp.client import ClientSession
from mcp.types import Request, Method


async def test_yacy_mcp():
    """Test the YaCy MCP server."""
    # This would connect to the running MCP server
    # For testing purposes, we'll simulate the interaction
    print("Testing YaCy MCP Server...")
    print("Available tools:")
    print("- yacy-search: Search using YaCy web search engine")
    
    print("\nExample usage:")
    print("Tool: yacy-search")
    print('Arguments: {"query": "open source search engine", "max_results": 5}')
    
    # If you have a running YaCy instance, you can test directly
    try:
        from yacy_mcp.server import perform_yacy_search
        print("\nTesting direct search function (requires YaCy server running):")
        results = await perform_yacy_search("open source", 3)
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"Direct test failed (YaCy likely not running): {e}")
        print("Start YaCy server and try again.")


if __name__ == "__main__":
    asyncio.run(test_yacy_mcp())