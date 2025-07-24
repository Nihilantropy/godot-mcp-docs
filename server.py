"""
Godot MCP Server - Core Server Instance
FastMCP server for serving Godot documentation
"""

from pathlib import Path
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("godot-docs-server")

# Documentation directory (where converted .md files are stored)
DOCS_DIR = Path("docs").resolve()

def validate_doc_path(relative_path: str) -> Path:
    """
    Validate that requested path is within allowed docs directory
    Prevents directory traversal attacks
    """
    requested_path = (DOCS_DIR / relative_path).resolve()
    
    # Security check: ensure path is within docs directory
    if not str(requested_path).startswith(str(DOCS_DIR)):
        raise ValueError("Access denied: Path outside allowed directory")
    
    # Check if file exists
    if not requested_path.exists():
        raise FileNotFoundError(f"Documentation file not found: {relative_path}")
        
    return requested_path

def get_docs_dir() -> Path:
    """Get the documentation directory path"""
    return DOCS_DIR

def ensure_docs_dir() -> bool:
    """Ensure docs directory exists and contains documentation"""
    if not DOCS_DIR.exists():
        return False
    
    # Check if directory has any .md files
    md_files = list(DOCS_DIR.rglob("*.md"))
    return len(md_files) > 0