#!/usr/bin/env python3
"""
Godot MCP Server - Main Entry Point
Serves Godot documentation through MCP with stdio transport
"""

import sys
import logging
from srcs.utils.docs_utils import ensure_docs_dir
from srcs.server import mcp
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "srcs"))

# Import modules to register decorators
import srcs.tools.navigation_tools
import srcs.resources.doc_resources

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
        
        # Check if documentation is available
        if not ensure_docs_dir():
            logger.warning("Documentation directory not found or empty. Some tools may not work properly.")
            logger.warning("Please run 'python docs_converter/godot_docs_converter.py' to download and convert documentation.")

        logger.info("Documentation directory is ready for you my love <3.")

        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        logger.info("Server interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()