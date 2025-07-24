"""
Godot MCP Server - Class Tools
Simple tools for listing and retrieving Godot class documentation
"""

from server import mcp, validate_doc_path
from utils.file_utils import read_cached_file

@mcp.tool()
def list_all_classes() -> str:
    """
    List all available Godot class names from the classes index file
    
    Returns:
        String containing the content of classes/index.md with all class information
        
    Example:
        Returns the full content of the index.md file which contains class names and scope
    """
    try:
        index_path = validate_doc_path("classes/index.md")
        content = read_cached_file(index_path)
        return content
    except FileNotFoundError:
        return "Class index not found. Please run the docs converter first."
    except Exception as e:
        return f"Error accessing class index: {str(e)}"

@mcp.tool()
def retrieve_specific_class(class_name: str) -> str:
    """
    Retrieve the full documentation content for a specific Godot class
    
    Args:
        class_name: The full class name as it appears in the filename (e.g., "class_camera2d")
        
    Returns:
        The complete markdown content of the class documentation file
        
    Example:
        retrieve_specific_class("class_camera2d") -> returns full content of class_camera2d.md
    """
    try:
        doc_path = validate_doc_path(f"classes/{class_name}.md")
        content = read_cached_file(doc_path)
        return content
    except FileNotFoundError:
        return f"Class documentation not found: {class_name}. Use list_all_classes() tool to see available classes."
    except Exception as e:
        return f"Error accessing class documentation: {str(e)}"