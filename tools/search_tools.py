"""
Godot MCP Server - Class Tools
Simple tools for listing and retrieving Godot class documentation
"""

from pathlib import Path
from server import mcp, get_docs_dir, validate_doc_path
from utils.file_utils import find_markdown_files, read_cached_file

@mcp.tool()
def list_all_classes() -> str:
    """
    List all available Godot class names from the classes directory
    
    Returns:
        String containing all available class names, one per line
        
    Example:
        Returns: "class_camera2d\nclass_node\nclass_rigidbody2d\n..."
    """
    docs_dir = get_docs_dir()
    classes_dir = docs_dir / "classes"
    
    if not classes_dir.exists():
        return "Classes directory not found. Please ensure Godot documentation is available."
    
    # Find all markdown files in classes directory
    md_files = find_markdown_files(classes_dir)
    
    if not md_files:
        return "No class documentation files found."
    
    # Extract class names (filename without .md extension)
    class_names = [f.stem for f in md_files]
    class_names.sort()
    
    result = f"Available Godot classes ({len(class_names)} total):\n\n"
    result += "\n".join(class_names)
    
    return result

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