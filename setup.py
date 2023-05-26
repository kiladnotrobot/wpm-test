from distutils.core import setup
from setuptools import find_packages
import py2exe


setup(windows=['main.py'], packages=find_packages())