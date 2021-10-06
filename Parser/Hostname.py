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
    def System(Hostname: String):
        """
        Hostname Environment Configuration
        """

        Key: String = "NEXUS_API_HOSTNAME"

        Value: String = Hostname

        print("Configuring Environment Hostname")

        Update(Key, Value)

        print("  ↳ ", "Configured Variable ... ")
        print("  - ", "Key:     {0}".format(
            Key), "\n", " -  Value:   {0}".format(
                Environment(Key)
            ), "\n"
        )

    class Command(Action):
        """
        ...
        """

        def __call__(self, Parser, Namespace, Values: List, Options = None):
            """
            ...
            """

            setattr(Namespace, self.dest, lambda: Configuration.System(Values.pop(0)))

__all__ = [
    "Configuration"
]
