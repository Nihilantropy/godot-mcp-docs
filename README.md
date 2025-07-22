# Godot MCP Server

A Model Context Protocol (MCP) server for serving Godot documentation to AI assistants.

## Features

- **Direct file serving**: Access Godot documentation through MCP resources
- **Search functionality**: Search across all documentation files
- **Navigation tools**: Discover and list available documentation sections
- **Security**: Path validation prevents directory traversal attacks
- **Stdio transport**: Easy local deployment with no network configuration

## Installation

```bash
# Install dependencies
uv add "mcp[cli]" pypandoc

# Or with pip
pip install "mcp[cli]" pypandoc>=1.15
```

## Setup

1. **Convert Godot docs**: First, use your RST→MD converter to populate the `docs/` directory:
   ```bash
   python main.py  # Your existing converter script
   ```

2. **Verify structure**: Ensure your `docs/` directory contains converted markdown files:
   ```
   docs/
   ├── classes/           # API reference
   ├── tutorials/         # Tutorial documentation  
   ├── getting_started/   # Setup guides
   ├── contributing/      # Contribution docs
   ├── community/         # Community resources
   └── about/            # Release notes, changelog
   ```

## Usage

### Local Development
```bash
# Run the server directly
python main.py

# Or with uv
uv run main.py

# Test with MCP Inspector
npx @modelcontextprotocol/inspector uv run main.py
```

### Claude Desktop Integration

Add to your Claude Desktop MCP configuration:

```json
{
  "mcpServers": {
    "godot-docs": {
      "command": "uv",
      "args": [
        "--directory", "/path/to/godot-mcp-server",
        "run", "main.py"
      ]
    }
  }
}
```

## Available Resources

- `godot://classes/{class_name}` - Get API documentation for a specific class
- `godot://tutorials/{category}/{tutorial_name}` - Get tutorial documentation
- `godot://getting_started/{guide_name}` - Get setup and basic guides
- `godot://contributing/{doc_name}` - Get contribution guidelines
- `godot://community/{doc_name}` - Get community resources
- `godot://about/{doc_name}` - Get release notes and changelog
- `godot://doc/{file_path}` - Get any documentation file by path

## Available Tools

### Navigation
- `list_sections()` - List all documentation sections
- `list_classes()` - List available Godot classes
- `list_tutorials()` - List tutorials by category
- `list_guides()` - List getting started guides
- `get_documentation_overview()` - Get complete overview

### Search
- `search_docs(query, section?, max_results?)` - Search documentation content
- `search_class_methods(class_name, method_query?)` - Search methods in a class

## Project Structure

```
godot-mcp-server/
├── main.py              # Entry point
├── server.py            # FastMCP server instance
├── tools/               # Search and navigation tools
│   ├── search_tools.py
│   └── navigation_tools.py
├── resources/           # Documentation resource handlers
│   └── doc_resources.py
├── utils/               # File utilities
│   └── file_utils.py
├── docs/                # Converted Godot documentation (created by converter)
└── pyproject.toml       # Dependencies
```

## Security

- **Path validation**: All file access is validated to prevent directory traversal
- **Read-only access**: Server only reads documentation files
- **Directory restrictions**: Access limited to the `docs/` directory
- **Process isolation**: Stdio transport provides natural sandboxing

## Development

```bash
# Install development dependencies
uv sync

# Run with logging
python main.py

# Test specific functionality
python -c "from tools.search_tools import search_docs; print(search_docs('Node'))"
```

## Troubleshooting

1. **"Documentation directory not found"**: Ensure the `docs/` directory exists and contains `.md` files
2. **"No results found"**: Use `list_sections()` to verify available documentation
3. **Server startup issues**: Check that all dependencies are installed and the `docs/` directory is accessible