# Inspired by: https://gist.github.com/Joffreybvn/80653405085fda7e29a73782e67331e5
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name = "konect2networkx",
    version = "0.1.0",
    description = "Python package bridging the gap between the KONECT project and networkx",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jkudla/konect2networkx",
    author = "Jannik Kudla",
    author_email = "jannik.kudla@maths.ox.ac.uk",
    license = "GPLv3",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
        "Operating System :: OS Independent"
    ],
    packages = ["konect2networkx"],
    include_package_data = True,
    install_requires = ["networkx"]
)
