"""
Godot MCP Server - Search Tools
Simple search tools for finding Godot documentation
"""

import re
from pathlib import Path
from server import mcp, get_docs_dir
from utils.file_utils import find_markdown_files_recursive, read_cached_file, extract_snippet

@mcp.tool()
def search_docs(query: str, section: str = None, max_results: int = 10) -> str:
    """
    Search documentation content for a query
    
    Args:
        query: Search term or phrase
        section: Optional section to limit search (about, classes, tutorials, etc.)
        max_results: Maximum number of results to return
    """
    docs_dir = get_docs_dir()
    
    if not docs_dir.exists():
        return "Documentation directory not found. Please ensure Godot documentation is available."
    
    # Determine search directory
    search_dir = docs_dir
    if section:
        search_dir = docs_dir / section
        if not search_dir.exists():
            return f"Section '{section}' not found. Use list_sections() to see available sections."
    
    # Find all markdown files
    md_files = find_markdown_files_recursive(search_dir)
    
    if not md_files:
        return "No documentation files found."
    
    results = []
    query_lower = query.lower()
    
    for file_path in md_files:
        try:
            content = read_cached_file(file_path)
            
            # Check if query matches in content
            if query_lower in content.lower():
                # Get relative path for resource identification
                relative_path = file_path.relative_to(docs_dir)
                
                # Extract snippet around match
                snippet = extract_snippet(content, query, context_lines=2)
                
                results.append({
                    'file': str(relative_path),
                    'snippet': snippet or content[:200] + "..."
                })
                
                if len(results) >= max_results:
                    break
                    
        except Exception:
            continue  # Skip files that can't be read
    
    if not results:
        return f"No matches found for '{query}'"
    
    response = f"Found {len(results)} matches for '{query}':\n\n"
    
    for i, result in enumerate(results, 1):
        response += f"**{i}. {result['file']}**\n"
        response += f"{result['snippet']}\n\n"
    
    return response

@mcp.tool()
def search_class_methods(class_name: str, method_query: str = None) -> str:
    """
    Search for methods in a specific Godot class
    
    Args:
        class_name: Name of the Godot class
        method_query: Optional method name to search for
    """
    docs_dir = get_docs_dir()
    classes_dir = docs_dir / "classes"
    
    if not classes_dir.exists():
        return "Classes directory not found. Use list_sections() to see available sections."
    
    class_file = classes_dir / f"{class_name}.md"
    if not class_file.exists():
        return f"Class '{class_name}' not found. Use list_classes() to see available classes."
    
    try:
        content = read_cached_file(class_file)
        
        # Extract method sections (look for method patterns in markdown)
        method_pattern = r'^#+\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        methods = []
        
        for line in content.split('\n'):
            match = re.match(method_pattern, line)
            if match:
                method_name = match.group(1)
                if not method_query or method_query.lower() in method_name.lower():
                    methods.append(method_name)
        
        if not methods:
            if method_query:
                return f"No methods matching '{method_query}' found in class '{class_name}'"
            else:
                return f"No methods found in class '{class_name}'"
        
        if method_query:
            result = f"Methods matching '{method_query}' in class '{class_name}':\n\n"
        else:
            result = f"Methods in class '{class_name}':\n\n"
        
        result += "\n".join(f"- {method}" for method in sorted(methods))
        
        return result
        
    except Exception as e:
        return f"Error searching class methods: {str(e)}"