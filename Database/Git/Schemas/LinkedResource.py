# !/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:    Cloud-Technology LLC.
# Source:   gitlab.cloud-technology.io
# License:  BSD 3-Clause License

"""
...
"""

from . import *

# =============================================================================
# Local Imports
# =============================================================================

Enum = enum.Enum

# =============================================================================
# Reference Type(s)
# =============================================================================

Setup = Model.Model

# =============================================================================
# Class (Schema) Initialization
# =============================================================================

class Application(Scheme):
    Web: URL = Field(
        default = "https://google.com",
        alias = "Web-URL"
    )

    External: String = Field(
        default = "",
        alias = "External-ID"
    )

    Schematic: Json = Field(
        default = "{}",
        alias = "Schematic"
    )

class WebHook(Scheme):
    Web: URL = Field(
        default = "https://google.com",
        alias = "Web-URL"
    )

    Schematic: Json = Field(
        default = "{}",
        alias = "Schematic"
    )


class Type(Scheme):
    App: Application = Field(default = Application(), alias = "Application")
    Web: WebHook = Field(default = WebHook(), alias = "WebHook")
    Reference: URL = Field(
        default = "https://google.com",
        alias = "Web-URL"
    )

class Base(Scheme):
    Title: String = Field(
        default = "",
        alias = "Title"
    )

    Canonical: String = Field(
        default = "",
        alias = "Canonical"
    )

    Synopsis: Type = Field(default = Type(), alias = "Type")

    class Config(Setup):
        title = "{0}".format(__module__.split(".").pop())

class Create(Base):
    """
    ...
    """

class Shard(Base):
    """
    ...
    """

class Update(Base):
    """
    ...
    """

class Delete(Scheme):
    """
    ...
    """

class Schema(Base):
    """
    ...
    """

    ID: Union[Object, String, None] = Field("", alias = "ID")

class Association(Schema):
    """
    ...
    """

class Generator(Schema):
    """
    ...
    """

class JSON(Generator):
    """
    ...
    """

class Response(Scheme):
    Mutation: String = Field(...)
    Status: Integer = Field(...)
    Message: String = Field(...)

class Success(Response):
    Mutation: String = Field("[Mutation]")
    Status: Integer = Field(200, alias="Status-Code")
    Message: String = Field("Success", description="...")

class Error(Response):
    Mutation: String = Field("[Error]")
    Status: Integer = Field(400, alias="Status-Code")
    Message: String = Field("Error", description="...")
