#!/usr/bin/env python3
"""
Godot MCP Server - Main Entry Point
Serves Godot documentation through MCP with stdio transport
"""

from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    name="godot-docs-server",
    instructions="""
        This server provides tools for interacting with Godot documentation.
    """
)