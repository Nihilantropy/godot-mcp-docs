"""
Navigation utilities for directory tree operations
"""

import os
from pathlib import Path

def tree_structure(base_dir: Path) -> str:
    """
    Generate a tree-style string representation of directory structure
    
    Args:
        base_dir: Base directory to generate tree from
        
    Returns:
        String representation of directory tree with proper indentation
    """
    tree_lines = []
    # Add the root directory name
    tree_lines.append(f"{base_dir.name}/")
    # Walk through directory structure
    for root, dirs, files in os.walk(base_dir):
        level = root.replace(str(base_dir), '').count(os.sep)
        indent = '│   ' * level + '├── ' if level > 0 else ''
        # Add directories
        for i, dir_name in enumerate(sorted(dirs)):
            is_last_dir = (i == len(dirs) - 1) and not files
            branch = '└── ' if is_last_dir else '├── '
            tree_lines.append(f"{'│   ' * level}{branch}{dir_name}/")
        # Add files
        for i, file_name in enumerate(sorted(files)):
            is_last_file = i == len(files) - 1
            branch = '└── ' if is_last_file else '├── '
            tree_lines.append(f"{'│   ' * level}{branch}{file_name}")
    return '\n'.join(tree_lines)