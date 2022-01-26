"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
"""

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
from os import path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup


VERSION = "0.0.10"
NAME = "pygination"
AUTHOR = "Celsia innovacion"
AUTHOR_EMAIL = "jdmoralesar@gmail.com"
DESCRIPTION = "Pagination helper"
PROJECT_URL = "https://github.com/jdmoralesar/pygination"
DOWNLOAD_URL = "https://github.com/jdmoralesar/pygination/archive/refs/tags/0.0.1.tar.gz"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
try:
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,  # Required
    version=VERSION,  # Required
    description=DESCRIPTION,  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url=PROJECT_URL,  # Optional
    download_url=DOWNLOAD_URL,
    author=AUTHOR,  # Optional
    author_email=AUTHOR_EMAIL,  # Optional
    classifiers=[  # Optional
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="python pagination",  # Optional
    packages=find_packages(include=[NAME, f"{NAME}.*"]),  # Required
    python_requires=">=3.6, <3.10",
    install_requires=["SQLAlchemy", "pydantic"],  # Optional
)