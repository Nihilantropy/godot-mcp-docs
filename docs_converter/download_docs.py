
"""
Download module for Godot documentation repository
"""

import os
import shutil
import urllib.request
import zipfile
import requests

def download_repo():
    """Download godot-docs ZIP file and extract to docs folder"""

    
    versions = None

    try:
        print("Fetching available versions from GitHub API...\n")
        response = requests.get(
            "https://api.github.com/repos/godotengine/godot-docs/branches",
            timeout=10
        )

        if response.status_code == 200:
            branches = response.json()
            versions = [b["name"] for b in branches]

            print("Available versions:")
            for v in versions:
                print(f"- {v}")

    except Exception as e:
        print(f"Could not fetch versions from GitHub API: {e}")

    # unified input handling (ONLY ONCE)
    version = input("Enter version (press Enter for latest): ").strip()

    if not version:
        version = "master"

    elif versions and version not in versions:
        print(f"Invalid version '{version}', falling back to master")
        version = "master"

    zip_url = f"https://github.com/godotengine/godot-docs/archive/refs/heads/{version}.zip"
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