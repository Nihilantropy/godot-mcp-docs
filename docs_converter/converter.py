"""
Converter module for RST to Markdown conversion
"""

import os
import glob
from multiprocessing import Pool, cpu_count
import pypandoc

def find_rst_files(docs_dir):
    """Find all .rst files in the documentation directory"""
    rst_pattern = os.path.join(docs_dir, "**", "*.rst")
    rst_files = glob.glob(rst_pattern, recursive=True)
    return rst_files

def convert_rst_file(rst_path):
    """Convert single RST file to Markdown"""
    try:
        md_path = rst_path.replace('.rst', '.md')
        pypandoc.convert_file(rst_path, 'md', outputfile=md_path)
        return f"✓ {rst_path} -> {md_path}"
    except Exception as e:
        return f"✗ Failed {rst_path}: {str(e)}"

def convert_files_parallel(rst_files):
    """Convert files using parallel processing"""
    print(f"Converting {len(rst_files)} RST files to Markdown...")
    
    # Use all CPU cores but limit to reasonable number
    num_workers = min(cpu_count(), 8)
    print(f"Using {num_workers} parallel workers")
    
    with Pool(num_workers) as pool:
        results = pool.map(convert_rst_file, rst_files)
    
    # Print results
    successful = sum(1 for r in results if r.startswith("✓"))
    failed = len(results) - successful
    
    print(f"\nConversion complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    # Print failed conversions
    if failed > 0:
        print("\nFailed conversions:")
        for result in results:
            if result.startswith("✗"):
                print(result)