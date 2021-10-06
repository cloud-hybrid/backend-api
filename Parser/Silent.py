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

import os
import sys
import time
import signal
import typing

from . import Action

Integer = int
String = str
Float = float
Bytes = bytes
Array = bytearray
List = list
Dictionary = dict
Tuple = tuple
Address = memoryview

Optional = typing.Optional

Union = typing.Union

Update = lambda Key, Value: os.environ.update({Key: Value})

Environment = lambda Variable, Default = None: os.getenv(Variable, Default)

class Configuration:
    """
    ...
    """

    def __init__(self, *argv, **kwargs):
        map(setattr, kwargs.items())

    @staticmethod
    def System() -> bool:
        """
        Server HTTPs Environment Configuration
        """

        Key: String = "NEXUS_API_SILENT_LOGGING"

        Value: String = "%s" % True

        sys.stdout.write("[Nexus-API]: Setting Silent Flag ➜ ")
        sys.stdout.flush()

        Update(Key, Value)

        sys.stdout.write("Environment[{0}]".format(Key) + " := " + "{0}".format(Value) + "\n")
        sys.stdout.flush()

        return True

    class Command(Action):
        """
        ...
        """

        def __call__(self, Parser, Namespace, Values: List, Options = None):
            """
            ...
            """

            setattr(Namespace, self.dest, lambda: Configuration.System())

__all__ = [
    "Configuration"
]
