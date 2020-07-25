from setuptools import setup, find_packages
from pathlib import Path
import sys

# Version
BASE_DIR = Path(__file__).resolve().parent
VERSION_FILE = BASE_DIR.joinpath('data_store', '_version.py')
with open(VERSION_FILE) as fp:
    exec(fp.read())

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "pydicom-data",
    packages = find_packages(),
    include_package_data = True,
    version = __version__,
    zip_safe = False,
    description = "",
    long_description = long_description,
    long_description_content_type="text/x-rst",
    author = "Darcy Mason and contributors",
    author_email = "darcymason@gmail.com",
    url = "https://github.com/pydicom/pydicom-data",
    license = "MIT",
    keywords = "dicom python pydicom",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[],
    tests_require=["pytest"],
    entry_points={
        "pydicom.data.external_sources": "pydicom-data = data_store:DataStore",
    },
)
