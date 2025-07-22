"""
Godot MCP Server - Documentation Resources
Resource handlers for serving Godot documentation files
"""

from pathlib import Path
from server import mcp, validate_doc_path, get_docs_dir

@mcp.resource("godot://about/{topic}")
def get_about_documentation(topic: str) -> str:
    """Get Godot about documentation (introduction, FAQ, features, etc.)"""
    try:
        doc_path = validate_doc_path(f"about/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"About documentation not found: {topic}. Use list_about() tool to see available docs."
    except Exception as e:
        return f"Error accessing about documentation: {str(e)}"

@mcp.resource("godot://api/classes/{class_name}")
def get_class_documentation(class_name: str) -> str:
    """Get Godot API documentation for a specific class"""
    try:
        doc_path = validate_doc_path(f"classes/{class_name}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Class documentation not found: {class_name}. Use list_classes() tool to see available classes."
    except Exception as e:
        return f"Error accessing class documentation: {str(e)}"

@mcp.resource("godot://getting-started/{section}/{topic}")
def get_getting_started_documentation(section: str, topic: str) -> str:
    """Get Godot getting started guides"""
    try:
        doc_path = validate_doc_path(f"getting_started/{section}/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Getting started guide not found: {section}/{topic}. Use list_guides() tool to see available guides."
    except Exception as e:
        return f"Error accessing getting started guide: {str(e)}"

@mcp.resource("godot://tutorials/{category}/{topic}")
def get_tutorial_documentation(category: str, topic: str) -> str:
    """Get Godot tutorial documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/{category}/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Tutorial not found: {category}/{topic}. Use list_tutorials() tool to see available tutorials."
    except Exception as e:
        return f"Error accessing tutorial: {str(e)}"

@mcp.resource("godot://contributing/{section}/{topic}")
def get_contributing_documentation(section: str, topic: str) -> str:
    """Get Godot contributing documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/{section}/{topic}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing documentation not found: {section}/{topic}. Use list_contributing() tool to see available docs."
    except Exception as e:
        return f"Error accessing contributing documentation: {str(e)}"