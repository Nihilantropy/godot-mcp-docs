
"""
Download module for Godot documentation repository
"""

import os
import shutil
import urllib.request
import zipfile

def download_repo():
    """Download godot-docs ZIP file and extract to docs folder"""
    zip_url = "https://github.com/godotengine/godot-docs/archive/refs/heads/master.zip"
    zip_file = "godot-docs.zip"
    docs_dir = "docs"
    
    print("Downloading Godot docs ZIP...")
    
    # Remove existing directory if it exists
    if os.path.exists(docs_dir):
        print(f"Removing existing {docs_dir} directory...")
        shutil.rmtree(docs_dir)
    
    try:
        # Download ZIP file
        urllib.request.urlretrieve(zip_url, zip_file)
        print("ZIP file downloaded")
        
        # Extract ZIP file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall("temp")
        
        # Move extracted folder to docs directory
        extracted_dir = "temp/godot-docs-master"
        shutil.move(extracted_dir, docs_dir)
        
        # Cleanup
        os.remove(zip_file)
        shutil.rmtree("temp")
        
        print(f"Documentation extracted to {docs_dir}/")
        return docs_dir
        
    except Exception as e:
        # Cleanup on error
        if os.path.exists(zip_file):
            os.remove(zip_file)
        if os.path.exists("temp"):
            shutil.rmtree("temp")
        raise Exception(f"Download failed: {e}")