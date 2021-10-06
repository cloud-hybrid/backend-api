#!/usr/bin/env python3

#  Copyright (c) 2021. Jacob B. Sanders, Cloud Hybrid LLC. & Affiliates.
#
#  Redistribution and use in source and binary forms, with or without modification, are permitted
#  provided that the following conditions are met:
#
#  1.  Redistributions of source code must retain the above copyright notice, this list of
#      conditions and the following disclaimer.
#  2.  Redistributions in binary form must reproduce the above copyright notice, this list of
#      conditions and the following disclaimer in the documentation and/or other materials
#      provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
#  OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
#  AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER
#  OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#  OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
#  OF SUCH DAMAGE.

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
    def System():
        """
        Hostname Environment Configuration
        """

        Key: String = "NEXUS_API_ASSERTION"

        Value: String = "%s" % 1

        print("Configuring Environment Assertion")

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

            setattr(Namespace, self.dest, lambda: Configuration.System())

__all__ = [
    "Configuration"
]
