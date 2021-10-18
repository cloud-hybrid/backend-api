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

# =============================================================================
# Standard Library
# =============================================================================

import os
import sys
import bson
import enum
import uuid
import typing
import pkgutil
import secrets
import datetime
import dataclasses

Type = dataclasses.dataclass
Optional = typing.Optional
String = typing.AnyStr
List = typing.List
Union = typing.Union
Integer = typing.SupportsInt

# =============================================================================
# External
# =============================================================================

import pydantic

import motor
import motor.core
import motor.motor_asyncio as Motor

# =============================================================================
# Local Imports
# =============================================================================

import Database

# =============================================================================
# Type Declarations & Importable(s)
# =============================================================================

Stamp = datetime.datetime.utcnow

Secret = pydantic.SecretStr

Agnostic: motor.core.AgnosticCollection = motor.core.AgnosticCollection

BSON = bson

# =============================================================================
# Packaged Exports
# =============================================================================

UID = lambda: "{0}".format(uuid.uuid4()).upper()

Day = lambda: datetime.datetime.today().isoweekday()
ISO8601 = lambda: datetime.datetime.today().strftime("%U")
Year = lambda: datetime.datetime.today().year

Boolean = bool
Array = bytearray
Dictionary = dict
Enumeration = enum.Enum
String = str

Date = lambda: datetime.datetime.now(tz = None)
UUID = lambda: "{0}".format(uuid.uuid4()).upper()

__all__ = [
    "motor",
    "Motor",
    "BSON",
    "Dictionary",
    "Type",
    "String",
    "Database",
    "Agnostic",
    "Boolean",
    "Integer",
    "String",
    "List",
    "Array",
    "Secret",
    "Date",
    "Enumeration",
    "String",
    "Optional",
    "secrets",
    "Union",
    "UUID",
    "UID",
    "ISO8601",
    "Year",
    "Day"
]
