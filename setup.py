#!/usr/bin/env python

import sys
if sys.version_info < (3, 3):
    sys.stderr.write("ERROR: defringe requires Python 3.3 or later\n")
    sys.exit(1)

import os
import glob
import builtins

from setuptools import setup

PACKAGE_NAME = 'defringe'
DESCRIPTION = 'Python tools for defringing data'
AUTHOR = 'STScI'
AUTHOR_EMAIL = 'stis@stsci.edu'

# VERSION should be PEP386 compatible (http://www.python.org/dev/peps/pep-0386)
VERSION = '0.1.0.dev0'

#Define entry points for command-line scripts
entry_points = {}
entry_points['console_scripts'] = [
    'defringe = defringe.scripts.defringe:main',
]


setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      python_requires='>=3.3',
      install_requires=[
          'numpy',
          'astropy>=3.0'
      ],
      tests_require=['pytest'],
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      zip_safe=False,
      entry_points=entry_points,
)
