from setuptools import setup, find_packages
import os
import sys

# Version
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
VERSION_FILE = os.path.join(BASE_DIR, 'datasets', '_version.py')
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
    author = "",
    author_email = "FIXME",
    url = "https://github.com/pydicom/pydicom-data",
    license = "MIT",
    keywords = (
        "dicom python medicalimaging radiotherapy oncology pydicom imaging"
    ),
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[],
    entry_points={
        "pydicom.data.external_sources": "datasets = datasets:get_interface",
    },
)
