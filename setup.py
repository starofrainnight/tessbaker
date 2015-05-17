#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

import os
import os.path
import sys
import shutil
import logging
import fnmatch
import rabird.core.distutils
from setuptools import setup, find_packages

package_name = 'tesseract_baker'

# Convert source to v2.x if we are using python 2.x.
source_dir = rabird.core.distutils.preprocess_source()

# Exclude the original source package, only accept the preprocessed package!
our_packages = find_packages(where=source_dir)

our_requires = [
	]

long_description=(
     open('README.rst', 'r').read()
     + '\n' +
     open('CHANGES.rst', 'r').read()
     )
	
setup(
	name=package_name,
	version='.'.join(map(str, (0, 0, 1))),
	author='Hong-She Liang',
	author_email='starofrainnight@gmail.com',
	url='https://github.com/starofrainnight/%s' % package_name,
	description='An Tesseract-OCR trainer program',
	long_description=long_description,
	classifiers=[
		"Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",        
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
	install_requires=our_requires,
	package_dir = {'': source_dir},
    packages=our_packages,
    # If we don't set the zip_safe to False, pip can't find us.
    zip_safe=False,
	)

