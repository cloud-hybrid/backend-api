#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:    Jacob B. Sanders
# Source:   code.cloud-technology.io
# License:  BSD 2-Clause License

""" Nexus API - CLI Parser Package
----------------------------------

**Note** - `Action` is Required to be defined prior to the `Context` import; without
this specific namespace order, the packaged runtime will simply fail:

    >>> import os
    >>> import sys
    >>> import pprint
    >>> import logging
    >>> import argparse
    >>> import dataclasses

    >>> Action = argparse.Action

    >>> import Parser.Base as Context

    ...

"""

import os
import sys
import pprint
import typing
import logging
import argparse
import dataclasses

Action = argparse.Action

import Parser.Base as Context

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

Schema = dataclasses.dataclass(
    init = False,
    frozen = False,
    unsafe_hash = True,
    order = True
)

@Schema
class Environment:
    """
    ...
    """

    SQL:        ... = lambda: ...
    Host:       ... = lambda: ...
    Port:       ... = lambda: ...
    Debug:      ... = lambda: ...
    Token:      ... = lambda: ...
    Discord:    ... = lambda: ...
    Unit:       ... = lambda: ...
    HTTPs:      ... = lambda: ...
    Silent:     ... = lambda: ...
    Assert:     ... = lambda: ...

    Arguments:  ...

    Update = lambda K, V: os.environ.update({K: V})

__all__ = [
    "os",
    "sys",
    "pprint",
    "logging",
    "argparse",

    "Integer",
    "String",
    "Float",
    "Bytes",
    "Array",
    "List",
    "Dictionary",
    "Tuple",
    "Address",

    "Optional",
    "Union",

    "Context",

    "Environment"
]
