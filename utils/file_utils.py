"""
Godot MCP Server - File Utilities
Utility functions for file handling and documentation processing
"""

from pathlib import Path
from functools import lru_cache
from typing import List, Optional

@lru_cache(maxsize=128)
def read_cached_file(file_path: Path) -> str:
    """
    Read file content with caching for frequently accessed files
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        File content as string
    """
    return file_path.read_text(encoding='utf-8')

def find_markdown_files(directory: Path, pattern: str = "*.md") -> List[Path]:
    """
    Find all markdown files in a directory
    
    Args:
        directory: Directory to search in
        pattern: Glob pattern for files (default: "*.md")
        
    Returns:
        List of markdown file paths
    """
    if not directory.exists():
        return []
    
    return list(directory.glob(pattern))

def find_markdown_files_recursive(directory: Path, pattern: str = "**/*.md") -> List[Path]:
    """
    Recursively find all markdown files in a directory
    
    Args:
        directory: Directory to search in
        pattern: Glob pattern for files (default: "**/*.md")
        
    Returns:
        List of markdown file paths
    """
    if not directory.exists():
        return []
    
    return list(directory.rglob("*.md"))

def get_file_sections(content: str) -> List[str]:
    """
    Extract section headers from markdown content
    
    Args:
        content: Markdown content
        
    Returns:
        List of section headers
    """
    lines = content.split('\n')
    sections = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            # Remove markdown header symbols and clean up
            header = stripped.lstrip('#').strip()
            if header:
                sections.append(header)
    
    return sections

def extract_snippet(content: str, query: str, context_lines: int = 2) -> Optional[str]:
    """
    Extract a snippet around a search query match
    
    Args:
        content: Text content to search in
        query: Search query
        context_lines: Number of lines to include before/after match
        
    Returns:
        Snippet around the match, or None if no match
    """
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if query.lower() in line.lower():
            start = max(0, i - context_lines)
            end = min(len(lines), i + context_lines + 1)
            snippet_lines = lines[start:end]
            
            # Highlight the matching line with markers
            for j, snippet_line in enumerate(snippet_lines):
                if query.lower() in snippet_line.lower():
                    snippet_lines[j] = f">>> {snippet_line}"
            
            return '\n'.join(snippet_lines)
    
    return None

def is_valid_markdown_file(file_path: Path) -> bool:
    """
    Check if a file is a valid markdown file
    
    Args:
        file_path: Path to check
        
    Returns:
        True if file exists and is a markdown file
    """
    return (
        file_path.exists() and 
        file_path.is_file() and 
        file_path.suffix.lower() == '.md'
    )

def get_relative_path_string(file_path: Path, base_path: Path) -> str:
    """
    Get relative path as string, handling errors gracefully
    
    Args:
        file_path: File path
        base_path: Base path to calculate relative to
        
    Returns:
        Relative path as string
    """
    try:
        return str(file_path.relative_to(base_path))
    except ValueError:
        # If file_path is not relative to base_path
        return str(file_path)