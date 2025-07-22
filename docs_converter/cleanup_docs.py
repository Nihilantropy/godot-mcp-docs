"""
Cleanup script to keep only .md files in proper structure
"""

import os
import shutil
from pathlib import Path

def cleanup_docs(docs_dir="docs"):
    """Remove all files except .md files, preserving directory structure"""
    docs_path = Path(docs_dir)
    
    if not docs_path.exists():
        print(f"Error: {docs_dir} directory not found")
        return
    
    print("Cleaning up documentation folder...")
    
    # Walk through all files and directories
    for root, dirs, files in os.walk(docs_path):
        root_path = Path(root)
        
        for file in files:
            file_path = root_path / file
            
            # Keep only .md files
            if not file.endswith('.md'):
                try:
                    file_path.unlink()
                    print(f"Removed: {file_path.relative_to(docs_path)}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")
    
    # Remove empty directories
    for root, dirs, files in os.walk(docs_path, topdown=False):
        for dir_name in dirs:
            dir_path = Path(root) / dir_name
            try:
                if not any(dir_path.iterdir()):  # Check if directory is empty
                    dir_path.rmdir()
                    print(f"Removed empty directory: {dir_path.relative_to(docs_path)}")
            except OSError:
                pass  # Directory not empty or other error
    
    print("Cleanup completed!")
    
    # Generate summary
    md_count = sum(1 for _ in docs_path.rglob("*.md"))
    print(f"Total .md files preserved: {md_count}")

if __name__ == "__main__":
    cleanup_docs()