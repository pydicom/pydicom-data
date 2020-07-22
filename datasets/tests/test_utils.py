"""Tests for utils.py"""

import os

import pytest

from datasets import get_interface


class TestInterface:
    """Test the interface for the data sources"""
    def setup(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        self.data_path = os.path.abspath(
            os.path.join(cur_dir, "../", "../", "data")
        )
        self.fname = "693_UNCI.dcm"

    def test_data_path(self):
        """Test the path to the data is correct."""
        i = get_interface()
        assert self.data_path == i.data_path

    def test_get_path(self):
        """Test retrieving a file path."""
        i = get_interface()
        assert (
            os.path.join(self.data_path, self.fname) == i.get_path(self.fname)
        )

    def test_get_path_raises_bad_fname(self):
        """Test get_path raises if no matching filename."""
        i = get_interface()
        msg = r"No file found named 'no matching name.txt'"
        with pytest.raises(ValueError, match=msg):
            i.get_path("no matching name.txt")

    def test_get_path_raises_bad_dtype(self):
        """Test get_path raises if unsupported dtype."""
        i = get_interface()
        msg = r"No files available for the data type"
        with pytest.raises(ValueError, match=msg):
            i.get_path(self.fname, dtype=1)

    def test_get_paths(self):
        """Test get_paths."""
        i = get_interface()
        files = i.get_paths('693*')
        assert len(files) == 3

    def test_get_paths_bad_dtype(self):
        """Test get_paths returns empty list if unsupported dtype."""
        i = get_interface()
        assert [] == i.get_paths("*", dtype=1)
