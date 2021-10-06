#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:   Jacob B. Sanders
# Source:  gitlab.cloud-technology.io
# License: BSD 3-Clause License

"""
...
"""

# =============================================================================
# Standard Library
# =============================================================================

import os
import ssl
import sys
import copy
import enum
import json
import uuid
import time
import typing
import pprint
import asyncio
import datetime
import tempfile
import functools
import dataclasses

from devtools import debug

# =============================================================================
# External Package(s)
# =============================================================================

import fastapi
from fastapi import (
    Query,
    Form,
    File,
    Header,
    UploadFile,
    Path,
    Body,
    Request,
    Response,
    Security,
    Depends,
    HTTPException,
    websockets,
    WebSocket,
    WebSocketDisconnect
)

# =============================================================================
# Local Imports
# =============================================================================

import API
import Server

# from Server.Authentication.Context import (
#     Interface as Authentication
# )

# =============================================================================
# Type Declarations & Importable(s)
# =============================================================================

Boolean = bool
Integer = int
String = str
Dictionary = dict
Tuple = tuple
Bytes = bytes
Array = bytearray

JSON = json

Error = HTTPException
List = typing.List
Union = typing.Union
Optional = typing.Optional

Date: type(datetime.datetime) = datetime.datetime

Today = lambda: Date.strptime(Date.today().strftime("%d-%B-%Y"), "%d-%B-%Y")

class Type(str, enum.Enum):
    """
    Type-Hinted, Type-Forced Casting Types
    """

    String = "String"
    Integer = "Integer"
    Bytes = "Bytes"
    Default = "Integer"
    Pointer = "Pointer"
    Array = "Array"
    Hexadecimal = "Hexadecimal"

    @classmethod
    def MRO(cls) -> List[str]:
        """
        ...
        """

        return [Index for Index in
            cls.__members__.keys()
        ]

    def cast(self, value):
        if self.value == "String":
            return "{0}".format(value)
        elif self.value == "Integer":
            return Integer("%s" % value)
        elif self.value == "Bytes":
            return Bytes(value)
        elif self.value == "Array":
            return String(Array(value), encoding = "UTF-8")
        elif self.value == "Pointer":
            return "%s" % memoryview(Bytes(value))
        elif self.value == "Hexadecimal":
            return memoryview(Bytes(value)).hex()
        else: return value

# =============================================================================
# Packaged Exports
# =============================================================================

# Secure = Depends(Authentication.Session)

class Request:
    """
    Implicit Instance Idiom
    """

    Form = fastapi.Form
    File = fastapi.File
    Upload = fastapi.UploadFile

    Prefix = "".join(["/", "/".join(__module__.split(".")[:-1]), "/"])

    Tags = []

    Generator: Server.Base.Generator = Server.Base.Generator

    # Generator.dependencies = { Secure }

    __slots__ = ()

    __dict__ = None

    __new__ = lambda *_: ...
