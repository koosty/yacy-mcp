# YaCy MCP Server

MCP (Model Context Protocol) Server implementation that provides AI tools to search using YaCy web search API.

## Installation

1. Make sure you have `uv` installed:

```bash
pip install uv
```

2. Install the package in development mode:

```bash
cd yacy-mcp
uv sync  # Sync all dependencies from pyproject.toml and uv.lock
```

Or alternatively:

```bash
cd yacy-mcp
uv pip install -e .
```

## Usage

1. Make sure you have a YaCy server running (typically on http://localhost:8090)
2. Set environment variables (optional):

```bash
export YACY_URL=http://localhost:8090
```

3. Run the MCP server:

```bash
python -m yacy_mcp
```

## Configuration

The server can be configured using environment variables:

- `YACY_URL`: URL of your YaCy instance (default: http://localhost:8090)

## Available Tools

- `yacy-search`: Search using YaCy web search engine
  - Parameters:
    - `query` (string, required): Search query string
    - `max_results` (integer, optional): Maximum number of results to return (default: 10)
    - `resource` (string, optional): Search resource (local or global, default: global)

## MCP Configuration for AI Applications

To use this server with AI applications that support the Model Context Protocol (MCP), configure your MCP client to connect to the server using stdio transport.

Example configuration for Claude Desktop (settings.json):
```json
{
  "mcpServers": {
    "yacy-mcp": {
      "command": "uvx",
      "args": ["yacy_mcp"],
      "env": {
        "YACY_URL": "http://localhost:8090"
      }
    }
  }
}
```

For other MCP-compatible applications, use the command `uvx yacy_mcp` as the server executable. The server will be automatically fetched and run from PyPI.

## Integration with AI Applications

This MCP server can be used with AI applications that support the Model Context Protocol to perform web searches using the YaCy search engine.