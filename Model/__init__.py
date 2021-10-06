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
import enum
import json
import typing
import inspect
import datetime
import dataclasses

import pydantic
import devtools
import fastapi

import Utility.Color

Any = typing.Any
Optional = typing.Optional
Union = typing.Union
Integer = int
Dictionary = typing.Dict
List = typing.List
Boolean = bool
Tuple = typing.Tuple
String = str
Set = typing.Set

Color = Utility.Color.TTY()

Field = pydantic.Field

@dataclasses.dataclass()
class Base:
    Integer: Integer = int

    Any: Any = typing.Any
    Optional: Optional = typing.Optional
    Dictionary: Dictionary = typing.Dict
    List: List = typing.List
    Union: Union = typing.Union
    Tuple: Tuple = typing.Tuple
    String: String = str
    Boolean: Boolean = bool
    Field: Field = pydantic.Field
    Set: Set = typing.Set

    Enumeration: enum.Enum = enum.Enum

Serialization = {
    "skipkeys":               True,
    "ensure_ascii":           False,
    "check_circular":         True,
    "allow_nan":              True,
    "indent":                 4,
    "separators":             (", ", ": "),
    "sort_keys":              True
}

Load = json.loads
Debug = devtools.debug
Dump = lambda _: json.dumps(_, **Serialization)

class Model(pydantic.BaseModel):
    """

    """

    __mapping__: Dictionary[String, String] = {}

    Types: Base = Base

    def __init_subclass__(cls, **kwargs):
        cls.Config = pydantic.BaseConfig

        cls.Config.title = "{0}".format(".".join([__package__, __name__]))

        cls.Config.alias_priority = -1

        cls.Config.allow_mutation = True
        cls.Config.anystr_strip_whitespace = False

        cls.Config.allow_population_by_field_name = True

        ### --> Settings Under Consideration

        cls.Config.schema_extra = {}

        cls.Config.underscore_attrs_are_private = True

        cls.Config.orm_mode = True

        cls.Config.json_loads = Load
        cls.Config.json_dumps = Dump

    @property
    def Configuration(self):
        return self.Config

    @classmethod
    def remux(cls, **kwargs):
        target = cls.construct(**kwargs).dict()
        target.update({
            k: target[v] for k, v in cls.__mapping__.items()
        }); return target
