"""
Godot MCP Server - Documentation Resources
Simplified resource handler for serving Godot documentation files
"""

from srcs.server import mcp
from utils.docs_utils import validate_doc_path
from utils.file_utils import read_cached_file

@mcp.resource("file://{file_path}")
def get_documentation_resource(file_path: str) -> str:
    """
    Get Godot documentation file from a specific path

    Args:
        file_path: The file path to the documentation file (e.g., "classes/class_camera2d.md")

    Returns:
        The content of the requested documentation file
    """
    try:
        doc_path = validate_doc_path(file_path)
        return read_cached_file(doc_path)
    except FileNotFoundError:
        return f"Documentation not found: {file_path}. Use get_documentation_tree tool to see available paths and files."
    except Exception as e:
        return f"Error accessing documentation: {str(e)}"
