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
import enum
import uuid
import typing
import secrets
import datetime
import dataclasses

# =============================================================================
# External
# =============================================================================

import json as JSON

import pydantic
import pydantic.typing
import pydantic.networks
import pydantic.typing
import pydantic.types

from bson.objectid import (
    ObjectId as ID
)

# =============================================================================
# Package
# =============================================================================

import Model

# -----------------------------------------------------------------------------
# Object Reference Mapping(s)
# -----------------------------------------------------------------------------

String = str
Boolean = bool

Unique = enum.unique

General = typing.Any
Integer = pydantic.PositiveInt
List = typing.List

Enumeration = enum.Enum

Field = pydantic.Field

Date = datetime.datetime
UUID = pydantic.UUID4

Union = typing.Union

Email = String
Corporate = pydantic.NameEmail

Requirement = pydantic.Required
Optional = pydantic.typing.Optional
Scheme = pydantic.BaseModel

URL = pydantic.AnyUrl
Json = pydantic.Json

Secret = secrets
Password = pydantic.types.SecretStr
Token = pydantic.types.SecretStr

# =============================================================================
# Packaged Exports
# =============================================================================

@dataclasses.dataclass(frozen = True)
class IPv4:
    """
    ...
    """

    IP: pydantic.networks.IPv4Address = pydantic.networks.IPv4Address
    Interface: pydantic.networks.IPv4Interface = pydantic.networks.IPv4Interface
    Network: pydantic.networks.IPv4Network = pydantic.networks.IPv4Network

@dataclasses.dataclass(frozen = True)
class IPv6:
    """
    ...
    """

    IP: pydantic.networks.IPv6Address = pydantic.networks.IPv6Address
    Interface: pydantic.networks.IPv6Interface = pydantic.networks.IPv6Interface
    Network: pydantic.networks.IPv6Network = pydantic.networks.IPv6Network

@dataclasses.dataclass(init = False, frozen = True)
class Network:
    """
    ...
    """

    Module: pydantic.networks = pydantic.networks

    IPv4: IPv4 = IPv4()
    IPv6: IPv6 = IPv6()

@Unique
class Industry(str, enum.Enum):
    """
    Industry Types
    """

    IT = "IT"
    Medical = "Medical"
    Construction = "Construction"
    Entertainment = "Entertainment"
    Transportation = "Transportation"
    Security = "Security"
    Consulting = "Consulting"
    Hospitality = "Hospitality"
    Automobile = "Automobile"
    Estate = "Real-Estate"
    Finance = "Finance"
    Insurance = "Insurance"
    Oil = "Oil"
    Mining = "Mining"
    Energy = "Energy"
    Engineering = "Engineering"
    Electronics = "Electronics"
    Legal = "Legal"
    Telecommunications = "Telecommunications"
    Retail = "Retail"
    Education = "Education"
    Storage = "Storage"
    Textiles = "Textiles"
    Agriculture = "Agriculture"
    Manufacturing = "Manufacturing"
    Gaming = "Gaming"

class ISO5218(int, enum.Enum):
    """
    ISO/IEC 5218 - Gender Codes
    """

    NULL = 0x0
    MALE = 0x1
    FEMALE = 0x2
    OTHER = 0x9

# =============================================================================
# Custom Pydantic Types
# =============================================================================

class Object(String):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, ID):
            raise TypeError("Mongo.Document.ID Required")
        return String(value)

# =============================================================================
# Packaged Exports
# =============================================================================

UID = lambda: "{0}".format(uuid.uuid4()).upper()

UTC = lambda: "{0}".format(datetime.datetime.utcnow())
