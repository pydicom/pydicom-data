"""Tests for the interface with pydicom."""

import os
from pathlib import Path

import pytest

from pydicom.data import get_testdata_file


class TestPydicom:
    """Test the interface with pydicom works correctly."""
    def setup(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        self.data_path = Path(cur_dir).joinpath("..", "..", "data").resolve()

    def test_pydicom_local(self):
        """Test that pydicom gets its own test data."""
        fname = "CT_small.dcm"
        assert "pydicom/data/test_files" in get_testdata_file(fname)

    def test_pydicom_external(self):
        """Test that pydicom uses external data sources first."""
        fname = "693_UNCI.dcm"
        assert os.path.join(self.data_path, fname) == get_testdata_file(fname)
