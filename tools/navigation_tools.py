"""
Godot MCP Server - Navigation Tools
Tools for discovering and listing Godot documentation structure
"""

from pathlib import Path
from server import mcp, get_docs_dir

@mcp.tool()
def list_sections() -> str:
    """List all available documentation sections"""
    docs_dir = get_docs_dir()
    
    if not docs_dir.exists():
        return "Documentation directory not found. Please ensure Godot documentation is available."
    
    sections = []
    for item in docs_dir.iterdir():
        if item.is_dir():
            md_files = list(item.rglob("*.md"))
            sections.append(f"**{item.name}** ({len(md_files)} files)")
    
    if not sections:
        return "No documentation sections found."
    
    return "Available documentation sections:\n\n" + "\n".join(sorted(sections))

@mcp.tool()
def list_about() -> str:
    """List available about documentation (introduction, FAQ, features, etc.)"""
    docs_dir = get_docs_dir()
    about_dir = docs_dir / "about"
    
    if not about_dir.exists():
        return "About directory not found. Use list_sections() to see available sections."
    
    docs = [f.stem for f in about_dir.glob("*.md")]
    
    if not docs:
        return "No about documentation found."
    
    return "Available about documentation:\n\n" + "\n".join(sorted(docs))

@mcp.tool()
def list_classes(limit: int = 50) -> str:
    """List available Godot API classes"""
    docs_dir = get_docs_dir()
    classes_dir = docs_dir / "classes"
    
    if not classes_dir.exists():
        return "Classes directory not found. Use list_sections() to see available sections."
    
    classes = []
    for class_file in classes_dir.glob("*.md"):
        classes.append(class_file.stem)
        if len(classes) >= limit:
            break
    
    if not classes:
        return "No class documentation found."
    
    result = f"Available Godot classes ({len(classes)} shown):\n\n"
    result += ", ".join(sorted(classes))
    
    if len(classes) == limit:
        result += f"\n\n*Showing first {limit} classes. Use search_docs() to find specific classes.*"
    
    return result

@mcp.tool()
def list_guides() -> str:
    """List available getting started guides by section"""
    docs_dir = get_docs_dir()
    guides_dir = docs_dir / "getting_started"
    
    if not guides_dir.exists():
        return "Getting started directory not found. Use list_sections() to see available sections."
    
    sections = {}
    for item in guides_dir.rglob("*.md"):
        relative_path = item.relative_to(guides_dir)
        if len(relative_path.parts) > 1:
            section = relative_path.parts[0]
            if section not in sections:
                sections[section] = []
            sections[section].append(relative_path.stem)
        else:
            # Guide directly in getting_started directory
            if "root" not in sections:
                sections["root"] = []
            sections["root"].append(item.stem)
    
    if not sections:
        return "No getting started guides found."
    
    result = "Available getting started guides by section:\n\n"
    for section, guides in sorted(sections.items()):
        result += f"**{section}** ({len(guides)} guides)\n"
        result += f"  {', '.join(sorted(guides))}\n\n"
    
    return result

@mcp.tool()
def list_tutorials(category: str = None) -> str:
    """List available tutorials, optionally filtered by category"""
    docs_dir = get_docs_dir()
    tutorials_dir = docs_dir / "tutorials"
    
    if not tutorials_dir.exists():
        return "Tutorials directory not found. Use list_sections() to see available sections."
    
    if category:
        category_dir = tutorials_dir / category
        if not category_dir.exists():
            return f"Tutorial category '{category}' not found. Use list_tutorials() without category to see all categories."
        
        tutorials = [f.stem for f in category_dir.glob("*.md")]
        if not tutorials:
            return f"No tutorials found in category '{category}'."
        
        return f"Tutorials in '{category}' category:\n\n" + "\n".join(sorted(tutorials))
    
    # List all categories
    categories = {}
    for item in tutorials_dir.rglob("*.md"):
        relative_path = item.relative_to(tutorials_dir)
        if len(relative_path.parts) > 1:
            cat = relative_path.parts[0]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(relative_path.stem)
    
    if not categories:
        return "No tutorials found."
    
    result = "Available tutorial categories:\n\n"
    for cat, tutorials in sorted(categories.items()):
        result += f"**{cat}** ({len(tutorials)} tutorials)\n"
        result += f"  {', '.join(sorted(tutorials))}\n\n"
    
    return result

@mcp.tool()
def list_contributing() -> str:
    """List available contributing documentation by section"""
    docs_dir = get_docs_dir()
    contrib_dir = docs_dir / "contributing"
    
    if not contrib_dir.exists():
        return "Contributing directory not found. Use list_sections() to see available sections."
    
    sections = {}
    for item in contrib_dir.rglob("*.md"):
        relative_path = item.relative_to(contrib_dir)
        if len(relative_path.parts) > 1:
            section = relative_path.parts[0]
            if section not in sections:
                sections[section] = []
            sections[section].append(relative_path.stem)
        else:
            # Doc directly in contributing directory
            if "root" not in sections:
                sections["root"] = []
            sections["root"].append(item.stem)
    
    if not sections:
        return "No contributing documentation found."
    
    result = "Available contributing documentation by section:\n\n"
    for section, docs in sorted(sections.items()):
        result += f"**{section}** ({len(docs)} docs)\n"
        result += f"  {', '.join(sorted(docs))}\n\n"
    
    return result

@mcp.tool()
def get_documentation_overview() -> str:
    """Get complete overview of Godot documentation structure"""
    docs_dir = get_docs_dir()
    
    if not docs_dir.exists():
        return "Documentation directory not found. Please ensure Godot documentation is available."
    
    overview = "# Godot Documentation Overview\n\n"
    
    sections = []
    total_files = 0
    
    for item in docs_dir.iterdir():
        if item.is_dir():
            md_files = list(item.rglob("*.md"))
            file_count = len(md_files)
            total_files += file_count
            sections.append(f"**{item.name}**: {file_count} files")
    
    overview += f"Total documentation files: {total_files}\n\n"
    overview += "Sections:\n" + "\n".join(sorted(sections))
    overview += "\n\nResource patterns:\n"
    overview += "- godot://about/{topic}\n"
    overview += "- godot://api/classes/{class_name}\n"
    overview += "- godot://getting-started/{section}/{topic}\n"
    overview += "- godot://tutorials/{category}/{topic}\n"
    overview += "- godot://contributing/{section}/{topic}\n"
    
    return overview