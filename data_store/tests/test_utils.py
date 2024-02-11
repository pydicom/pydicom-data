"""Tests for utils.py"""

import os
from pathlib import Path

import pytest

from data_store import DataStore


class TestDataStore:
    """Test the interface for the data sources"""
    def setup_method(self):
        self.data_path = Path(__file__).resolve().parent.parent / "data"
        self.fname = "693_UNCI.dcm"

    def test_data_path(self):
        """Test the path to the data is correct."""
        s = DataStore()
        assert self.data_path == s.data_path

    def test_get_path(self):
        """Test retrieving a file path."""
        s = DataStore()
        result = s.get_path(self.fname)
        assert isinstance(result, str)
        assert os.fspath(self.data_path / self.fname) == result

        with pytest.raises(ValueError, match=r"No file found named"):
            s.get_path("693_UNCI")

    def test_get_path_raises_bad_fname(self):
        """Test get_path raises if no matching filename."""
        s = DataStore()
        msg = r"No file found named 'no matching name.txt'"
        with pytest.raises(ValueError, match=msg):
            s.get_path("no matching name.txt")

    def test_get_path_raises_bad_dtype(self):
        """Test get_path raises if unsupported dtype."""
        s = DataStore()
        msg = r"No files available for the data type"
        with pytest.raises(ValueError, match=msg):
            s.get_path(self.fname, dtype=1)

    def test_get_paths(self):
        """Test get_paths."""
        s = DataStore()
        files = s.get_paths('693*')
        assert len(files) == 3
        assert isinstance(files[0], str)

    def test_get_paths_bad_dtype(self):
        """Test get_paths returns empty list if unsupported dtype."""
        s = DataStore()
        assert [] == s.get_paths("*", dtype=1)
