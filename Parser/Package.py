#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:    Jacob B. Sanders
# Source:   code.cloud-technology.io
# License:  BSD 2-Clause License

"""
...
"""

import sys
import time
import importlib

from . import Action

class Importer:
    """
    ...
    """

    def __init__(self, *argv, **kwargs):
        map(setattr, kwargs.items())

    class Command(Action):
        """
        ...
        """

        def __call__(self, Parser, Namespace, Values, Options = None):
            """
            Module & Package Cache Cleaning
            """

            print("Clearing Caches")

            time.sleep(1.0)

            importlib.invalidate_caches()

            print("  ↳ ", "Invalidated & Cleared")

            time.sleep(1.0)

            print("  - ", "Exiting (Successful, 0)")

            time.sleep(1.0)

            sys.exit(0)

__all__ = [
    "Tables"
]
