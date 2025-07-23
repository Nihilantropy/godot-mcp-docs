"""
Godot MCP Server - Documentation Resources
Simplified resource handler for serving only Godot class documentation files
"""

from server import mcp, validate_doc_path

@mcp.resource("godot://classes/{class_name}")
def get_class_documentation(class_name: str) -> str:
    """
    Get Godot API documentation for a specific class
    
    Args:
        class_name: The full class name as it appears in the filename (e.g., "class_camera2d")
        
    Returns:
        The markdown content of the class documentation file
        
    Example:
        godot://classes/class_camera2d -> returns content of class_camera2d.md
    """
    try:
        doc_path = validate_doc_path(f"classes/{class_name}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Class documentation not found: {class_name}. Use list_all_classes() tool to see available classes."
    except Exception as e:
        return f"Error accessing class documentation: {str(e)}"