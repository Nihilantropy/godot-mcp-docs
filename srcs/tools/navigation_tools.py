"""
Godot MCP Server - Navigation Tools

Tools for navigating and discovering Godot documentation structure
"""

import os
from pathlib import Path

from srcs.server import mcp
from utils.docs_utils import get_docs_dir
from utils.navigation_utils import tree_structure

@mcp.tool()
def get_documentation_overview(directory: str = "") -> str:
    """
    Get a tree-style overview of the documentation folder
    
    Args:
        directory: Directory path within docs to start from. If empty, uses docs root.
    
    Returns:
        String containing a directory tree representation of the documentation.
        
    Usage Examples:
        - get_documentation_overview() -> Full docs tree from root
        - get_documentation_overview("tutorials/3d") -> Tree starting from 3d tutorials
        - get_documentation_overview("classes") -> Tree starting from classes directory
        
    Note: 
        Files are exposed via get_documentation_file(path: str, file_name: str) resource.
    """
    docs_root = get_docs_dir()
    
    if not directory:
        base_dir = docs_root
    else:
        target_dir = docs_root / directory
        if not target_dir.exists():
            return f"Directory '{directory}' not found in documentation root."
        base_dir = target_dir
    
    try:
        return tree_structure(base_dir)
    except Exception as e:
        return f"Error generating overview: {str(e)}"