"""
Godot MCP Server - Navigation Tools
Tools for navigating and discovering Godot documentation structure
"""

from server import mcp, get_docs_dir
from utils.file_utils import find_markdown_files_recursive

@mcp.tool()
def get_documentation_overview() -> str:
    """
    Get an overview of all available documentation sections
    
    Returns:
        String describing the documentation structure and available sections
    """
    docs_dir = get_docs_dir()
    
    if not docs_dir.exists():
        return "Documentation directory not found. Please run the docs converter first."
    # Find all markdown files
    md_files = find_markdown_files_recursive(docs_dir)
    
    if not md_files:
        return "No documentation files found. Please run the docs converter first."
    # Group files by directory
    sections = {}
    for file_path in md_files:
        try:
            relative_path = file_path.relative_to(docs_dir)
            section = relative_path.parts[0] if relative_path.parts else "root"
            
            if section not in sections:
                sections[section] = []
            sections[section].append(str(relative_path))
        except ValueError:
            continue
    # Build overview
    result = f"Godot Documentation Overview ({len(md_files)} total files):\n\n"
    
    for section, files in sorted(sections.items()):
        result += f"📁 {section}/ ({len(files)} files)\n"
        # Show first few files as examples
        for file_path in sorted(files)[:3]:
            result += f"   • {file_path}\n"
        
        if len(files) > 3:
            result += f"   ... and {len(files) - 3} more files\n"
        result += "\n"
    
    return result