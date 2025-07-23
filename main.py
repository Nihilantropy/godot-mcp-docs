#!/usr/bin/env python3
"""
Godot MCP Server - Main Entry Point
Serves Godot documentation through MCP with stdio transport
"""

import sys
import logging
from server import mcp

# Import modules to register decorators
import tools.search_tools
import resources.doc_resources

def setup_logging():
    """Configure logging to stderr (required for stdio transport)"""
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stderr,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    """Main entry point for the Godot MCP server"""
    setup_logging()
    logger = logging.getLogger("godot-mcp-server")
    
    try:
        logger.info("Starting Godot MCP Server...")
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        logger.info("Server interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()