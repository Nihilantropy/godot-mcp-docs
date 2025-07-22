"""
Godot MCP Server - Documentation Resources
Resource handlers for serving Godot documentation files
"""

from pathlib import Path
from server import mcp, validate_doc_path, get_docs_dir

@mcp.resource("godot://classes/{class_name}")
def get_class_documentation(class_name: str) -> str:
    """Get Godot API documentation for a specific class"""
    try:
        doc_path = validate_doc_path(f"classes/{class_name}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Class documentation not found: {class_name}. Use list_classes() tool to see available classes."
    except Exception as e:
        return f"Error accessing class documentation: {str(e)}"

@mcp.resource("godot://tutorials/{category}/{tutorial_name}")
def get_tutorial_documentation(category: str, tutorial_name: str) -> str:
    """Get Godot tutorial documentation"""
    try:
        doc_path = validate_doc_path(f"tutorials/{category}/{tutorial_name}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Tutorial not found: {category}/{tutorial_name}. Use list_tutorials() tool to see available tutorials."
    except Exception as e:
        return f"Error accessing tutorial: {str(e)}"

@mcp.resource("godot://getting_started/{guide_name}")
def get_getting_started_guide(guide_name: str) -> str:
    """Get Godot getting started guides"""
    try:
        doc_path = validate_doc_path(f"getting_started/{guide_name}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Getting started guide not found: {guide_name}. Use list_guides() tool to see available guides."
    except Exception as e:
        return f"Error accessing guide: {str(e)}"

@mcp.resource("godot://contributing/{doc_name}")
def get_contributing_documentation(doc_name: str) -> str:
    """Get Godot contributing documentation"""
    try:
        doc_path = validate_doc_path(f"contributing/{doc_name}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Contributing documentation not found: {doc_name}. Use list_contributing() tool to see available docs."
    except Exception as e:
        return f"Error accessing contributing docs: {str(e)}"

@mcp.resource("godot://community/{doc_name}")
def get_community_documentation(doc_name: str) -> str:
    """Get Godot community documentation"""
    try:
        doc_path = validate_doc_path(f"community/{doc_name}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Community documentation not found: {doc_name}. Use list_community() tool to see available docs."
    except Exception as e:
        return f"Error accessing community docs: {str(e)}"

@mcp.resource("godot://about/{doc_name}")
def get_about_documentation(doc_name: str) -> str:
    """Get Godot about documentation (release policy, changelog, etc.)"""
    try:
        doc_path = validate_doc_path(f"about/{doc_name}.md")
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"About documentation not found: {doc_name}. Use list_about() tool to see available docs."
    except Exception as e:
        return f"Error accessing about docs: {str(e)}"

@mcp.resource("godot://doc/{file_path}")
def get_generic_documentation(file_path: str) -> str:
    """Get any Godot documentation file by relative path"""
    try:
        # Ensure .md extension
        if not file_path.endswith('.md'):
            file_path += '.md'
        
        doc_path = validate_doc_path(file_path)
        return doc_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f"Documentation file not found: {file_path}. Use search_docs() tool to find available documentation."
    except Exception as e:
        return f"Error accessing documentation: {str(e)}"