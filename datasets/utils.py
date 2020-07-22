
from enum import IntEnum
import fnmatch
import os
from typing import List


class DataTypes(IntEnum):
    """Constants for data types."""
    DATASET = 0
    CHARSET = 1
    PALETTE = 2
    DICOMDIR = 3
    JPEG = 4

    @classmethod
    def add(cls, name: str, code: int):
        """Add a new constant to `DataTypes`.

        Parameters
        ----------
        name : str
            The name of the constant to add.
        code : int
            The status code corresponding to the name.
        """
        setattr(cls, name, code)


def get_interface() -> "Interface":
    return Interface()


# TODO: possibly not needed
class Interface:
    """"""
    def __init__(self) -> None:
        """"""
        lib_dir = os.path.dirname(os.path.realpath(__file__))
        self.data_path = os.path.abspath(os.path.join(lib_dir, '../', 'data'))

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

        for root, _, fnames in os.walk(self.data_path):
            fnames = [fname for fname in fnames if fname == name]
            if fnames:
                return os.path.join(root, fnames[0])

        raise ValueError(f"No file found named '{name}'")

    def get_paths(
        self, pattern: str = "*", dtype: int = DataTypes.DATASET
    ) -> List[str]:
        """Return a list of absolute paths for files matching `pattern`.

        Parameters
        ----------
        pattern : str, optional
            A string pattern to filter the files (default ``*``).
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

        # if the user forgot to add them
        pattern = "*" + pattern + "*"

        out = []
        for root, _, fnames in os.walk(self.data_path):
            for fname in fnames:
                matches = fnmatch.filter([os.path.join(root, fname)], pattern)
                if matches:
                    out.append(matches[0])

        return out
