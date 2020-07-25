
from enum import IntEnum
import fnmatch
import os
from pathlib import Path
from typing import List


class DataTypes(IntEnum):
    """Constants for data types."""
    DATASET = 0
    CHARSET = 1
    PALETTE = 2
    DICOMDIR = 3


class DataStore:
    """Interface to pydicom-data data storage.

    Attributes
    ----------
    data_path : pathlib.Path
        The absolute path to the data directory.
    """
    def __init__(self) -> None:
        """Initialise a new Interface."""
        self.data_path = Path(__file__).resolve().parent / "data"

    def get_path(self, name: str, dtype: int = DataTypes.DATASET) -> str:
        """Return the absolute path to the first file with filename `name`

        Parameters
        ----------
        name : str
            The filename of the file
        dtype : int, optional
            The type of data to search for, default ``0`` (DICOM dataset).

        Returns
        -------
        str
            The absolute path to the first file found with filename `name`.

        Raises
        ------
        ValueError
            If no file found with a matching filename.
        """
        if dtype != DataTypes.DATASET:
            raise ValueError("No files available for the data type")

        matches = [m for m in self.data_path.glob(name)]
        if matches:
            return os.fspath(matches[0])

        raise ValueError(f"No file found named '{name}'")

    def get_paths(self, pattern: str, dtype: int = DataTypes.DATASET) -> List[str]:
        """Return a list of absolute paths for files matching `pattern`.

        Parameters
        ----------
        pattern : str
            A string pattern to filter the files.
        dtype : int, optional
            The type of data to search for, default ``0`` (DICOM dataset).

        Returns
        -------
        list of str
            A list of absolute paths to files with filenames matching
            `pattern`.
        """
        if dtype != DataTypes.DATASET:
            return []

        return [os.fspath(p) for p in self.data_path.glob(pattern)]
