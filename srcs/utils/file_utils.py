"""
Godot MCP Server - File Utilities
Utility functions for file handling and documentation processing
"""

from pathlib import Path
from functools import lru_cache

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
