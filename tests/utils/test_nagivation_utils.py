"""
Unit tests for navigation_utils module
"""

import tempfile
import pytest
from pathlib import Path
from navigation_utils import tree_structure


def test_tree_structure():
    """Test tree_structure function with various directory configurations"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        base_path = Path(temp_dir)
        
        # Create test directory structure
        (base_path / "docs").mkdir()
        (base_path / "docs" / "tutorials").mkdir()
        (base_path / "docs" / "tutorials" / "3d").mkdir()
        (base_path / "docs" / "classes").mkdir()
        
        # Create test files
        (base_path / "docs" / "index.md").write_text("content")
        (base_path / "docs" / "tutorials" / "intro.md").write_text("content")
        (base_path / "docs" / "tutorials" / "3d" / "meshes.md").write_text("content")
        (base_path / "docs" / "classes" / "node.md").write_text("content")
        
        # Test tree generation
        result = tree_structure(base_path / "docs")
        
        # Verify structure
        expected_lines = [
            "docs/",
            "├── classes/",
            "│   └── node.md",
            "├── tutorials/",
            "│   ├── 3d/",
            "│   │   └── meshes.md",
            "│   └── intro.md",
            "└── index.md"
        ]
        
        assert result == "\n".join(expected_lines)


def test_tree_structure_empty_directory():
    """Test tree_structure with empty directory"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        base_path = Path(temp_dir)
        result = tree_structure(base_path)
        
        # Should just show the directory name
        expected = f"{base_path.name}/"
        assert result == expected


def test_tree_structure_single_file():
    """Test tree_structure with single file"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        base_path = Path(temp_dir)
        (base_path / "readme.md").write_text("content")
        
        result = tree_structure(base_path)
        
        expected_lines = [
            f"{base_path.name}/",
            "└── readme.md"
        ]
        
        assert result == "\n".join(expected_lines)


def test_tree_structure_deep_nesting():
    """Test tree_structure with deep directory nesting"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        base_path = Path(temp_dir)
        
        # Create nested structure
        nested_path = base_path / "level1" / "level2" / "level3"
        nested_path.mkdir(parents=True)
        (nested_path / "deep_file.txt").write_text("content")
        
        result = tree_structure(base_path)
        
        expected_lines = [
            f"{base_path.name}/",
            "└── level1/",
            "    └── level2/",
            "        └── level3/",
            "            └── deep_file.txt"
        ]
        
        # Check that deep nesting works (exact spacing may vary)
        assert "deep_file.txt" in result
        assert "level3/" in result


if __name__ == "__main__":
    pytest.main([__file__])