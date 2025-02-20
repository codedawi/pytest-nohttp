#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(name: str):
    file_path = os.path.join(os.path.dirname(__file__), name)
    return codecs.open(file_path, encoding="utf-8").read()

setup(
    name="pytest-nohttp",
    version="0.1.0",
    author="Brett Dawidowski",
    author_email="brett@codedawi.com",
    maintainer="Brett Dawidowski",
    maintainer_email="brett@codedawi.com",
    license="MIT",
    url="https://github.com/codedawi/pytest-nohttp",
    description="Protect against unit tests accidentally interacting with external services via http",
    long_description=read("README.md"),
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=["pytest>=3.5.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "pytest11": [
            "nohttp = pytest_nohttp",
        ],
    },
)
