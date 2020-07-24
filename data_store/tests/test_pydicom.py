"""Tests for the interface with pydicom."""

import os
from pathlib import Path

import pytest

from pydicom.data import get_testdata_file


class TestPydicom:
    """Test the interface with pydicom works correctly."""
    def setup(self):
        self.data_path = Path(__file__).resolve().parent.parent.parent / "data"

    def test_pydicom_local(self):
        """Test that pydicom gets its own test data."""
        fname = "CT_small.dcm"
        assert "pydicom/data/test_files" in get_testdata_file(fname)

    def test_pydicom_external(self):
        """Test that pydicom uses external data sources first."""
        fname = "693_UNCI.dcm"
        assert os.fspath(self.data_path / fname) == get_testdata_file(fname)
