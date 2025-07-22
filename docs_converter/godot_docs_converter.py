#!/usr/bin/env python3
"""
Godot Documentation Converter - Main Entry Point
Downloads godot-docs repo and converts all .rst files to .md
"""

from download_docs import download_repo
from converter import find_rst_files, convert_files_parallel
from cleanup_docs import cleanup_docs

def main():
    """Main conversion process"""
    print("Godot Documentation RST -> Markdown Converter")
    print("=" * 50)
    
    try:
        # Download repository
        docs_dir = download_repo()
        
        # Find all RST files
        rst_files = find_rst_files(docs_dir)
        
        if not rst_files:
            print("No RST files found!")
            return
        
        # Convert files
        convert_files_parallel(rst_files)

        cleanup_docs(docs_dir)
        
        print(f"\nAll files processed! Check the {docs_dir}/ directory for .md files")
        
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()