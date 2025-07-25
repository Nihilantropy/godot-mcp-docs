"""
Godot MCP Server - Navigation Tools

Tools for navigating and discovering Godot documentation structure
"""

from srcs.server import mcp
from utils.docs_utils import get_docs_dir
from utils.file_utils import read_cached_file
from resources.doc_resources import get_documentation_resource

@mcp.tool()
def get_documentation_tree() -> str:
    """
    Get a tree-style overview of the documentation folder.

    Returns:
        String containing a directory tree representation of the documentation.
        
    Usage Examples:
        - get_documentation_overview() -> Full docs tree from root

    Note: 
        Files are exposed via get_documentation_resource(file_path: str) resource.
    """
    docs_root = get_docs_dir()

    tree_struct_file = docs_root / "docs_tree.txt"
    try:
        tree_structure_str = open(tree_struct_file, "r")
        return tree_structure_str.read()
    except FileNotFoundError:
        return "Documentation tree file not found. Please ensure the docs directory is set up correctly."
    except Exception as e:
        return f"Error generating overview: {str(e)}"
    
@mcp.tool()
def get_documentation_file(file_path: str) -> str:
    """
    Get the content of a specific documentation file.

    Args:
        file_path: Path to the documentation file relative to the docs directory (e.g., "classes/class_camera2d.md").

    Returns:
        The content of the requested documentation file, or an error message if not found.
        
    Usage Example:
        - get_documentation_file("classes/class_camera2d.md") -> Content of class_camera2d.md
    """
    docs_root = get_docs_dir()
    abs_file_path = docs_root / file_path

    if not abs_file_path.exists():
        return f"Documentation file not found: {file_path}. Use get_documentation_tree tool to see available paths and files."
    try:
        return read_cached_file(abs_file_path)
    except Exception as e:
        return f"Error accessing documentation file: {str(e)}"