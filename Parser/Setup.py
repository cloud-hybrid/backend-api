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
import shlex
import signal
import typing
import argparse

Action = argparse.Action

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
    def Setup(Hostname: String):
        """
        Project Setup Prompts & User Guide
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

if __name__ == "__main__":
    """
    Run the following section if ...
        >>> python[3] Parser/Setup.py
    or
        >>> python[3] Setup.py
    """

    Symbols = {
        True: "✓",
        False: "X"
    }

    Requirements = {
        "Version": {
            "Major": 3,
            "Minor": 8,
            "Patch": 1
        }
    }

    print("Running Nexus Setup + Validations")

    try:
        print("Validating Python Version ... ")

        Major = sys.version_info.major
        Minor = sys.version_info.minor
        Patch = sys.version_info.micro

        assert Major >= Requirements.get("Version").get("Major", 0)
        print(" " * 2 + " - " + "[%s]" % Symbols.get(True) + ": Major (Successful)")
        assert Minor >= Requirements.get("Version").get("Minor", 0)
        print(" " * 2 + " - " + "[%s]" % Symbols.get(True) + ": Minor (Successful)")
        assert Patch >= Requirements.get("Version").get("Patch", 0)
        print(" " * 2 + " - " + "[%s]" % Symbols.get(True) + ": Patch (Successful)")

        print()

        print("Validating Host Operating System ... ")

        OS = {
            "darwin": "OSX",
            "nt":     "Windows-10",
            "linux":  "Linux",
            "aix":    "BSD",
            "cygwin": "N/A"
        }.get(sys.platform)

        assert OS != "Windows-10"
        print(" " * 2 + " - " + "[%s]" % Symbols.get(True) + ": ! Windows   (Successful)")
        assert OS != "BSD"
        print(" " * 2 + " - " + "[%s]" % Symbols.get(True) + ": ! BSD       (Successful)")
        assert OS != "N/A"
        print(" " * 2 + " - " + "[%s]" % Symbols.get(True) + ": ! Other     (Successful)")

        print()

        # @Task Implement (.GIT)/Database/.env Setup
        #   - @Task (Use getpass)
        # @Task Implement (.GIT)/API/Discord/Token Setup
        #   - @Task (Use getpass)
        # @Task Implement (.GIT)/development.pem Setup

    except AssertionError as Error: ...
        # @Task Implement Error Message(s) upon Unique Assertions
        # ... @Task - Likely will require custom Errors

    finally: ...
        # @Task Perform Clean-Up if Neccessary
