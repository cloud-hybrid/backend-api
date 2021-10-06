#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:    Jacob B. Sanders
# Source:   https://gitlab.cloud-technology.io
# License:  BSD 3-Clause License

"""
...
"""

from Database import (
    Client
)

Database = Client["{0}".format(__package__.split(".").pop())]

__all__ = [
    "Database"
]
