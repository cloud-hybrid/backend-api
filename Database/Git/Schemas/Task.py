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

# =============================================================================
# Local Imports
# =============================================================================

import dataclasses
import ipaddress
import datetime
import secrets
import enum

from . import *

import Database.Git.Schemas
import Model

Enum = enum.Enum
Type = Model.Model

# =============================================================================
# Reference Type(s)
# =============================================================================

import Database.Git.Schemas

# =============================================================================
# Class (Schema) Initialization
# =============================================================================

class Task(String, Enum):
    Issue = "Issue"
    Story = "Story"
    Epic = "Epic"
    Reference = "Reference"
    Spike = "Spike"

    Null = ""

    Default = Null

class Target(Type):
    Time: Date = Field(
        default = None,
        alias = "Scheduled-Date",
        description = "Task Scheduled Date"
    )

    Completion: Date = Field(
        default = None,
        alias = "Completion-Date",
        description = "Task Completion Date"
    )

    Due: Date = Field(
        default = None,
        alias = "Due-Date",
        description = "Task Due Date"
    )

class Priority(String, Enum):
    Severe = "Severe"
    High = "High"
    Standard = "Standard"
    Low = "Low"
    Queue = "Queue"

    Null = None

    Default = Null

class Status(String, Enum):
    Completed = "Completed"
    Progress = "WIP"
    Delayed = "Delayed"
    Waiting = "Waiting"
    Cancelled = "Cancelled"

    Null = None

    Default = Null

class Periodicity(String, Enum):
    Daily = "Daily"
    Weekly = "Weekly"
    Monthly = "Monthly"

    Never = "Never"

    Default = Never

class Parent(Type):
    "..."

    ID: String = Field(
        default_factory = lambda: Secret(32),
        alias = "ID",
        description = "Parent-Task ID"
    )

    Title: String = Field(
        default = None,
        alias="Title",
        description="Parent-Task Title"
    )

    Canonical: String = Field(
        default = None,
        alias="Canonical",
        description="Canonical Human-Readable Title of Attributed Parent-Task"
    )

class Board(Type):
    "..."

    ID: String = Field(
        default = None,
        alias="ID",
        description="Collection-Board ID"
    )

    Title: String = Field(
        default = None,
        alias="Title",
        description="Collection-board Title"
    )

    Canonical: String = Field(
        default = None,
        alias="Canonical",
        description="Canonical Human-Readable Title of Attributed Collection-Board"
    )

class Schedule(Type):
    Frequency: Periodicity = Field(
        default = Periodicity.Never,
        alias = "Frequency",
    )

    Time: List[Date] = []

class Base(Type):
    Abstraction: List[Optional[Parent]] = Field(
        default = [],
        alias = "Associations",
        description = "Parent-Task Metadata"
    )

    Collection: Board = Field(
        default = Board(),
        alias = "Collection-Board",
        description = "Collection-Board Metadata"
    )

    Title: String = Field(
        default = None,
        alias = "Title",
        description = "Task Title"
    )

    Canonical: String = Field(
        default = None,
        alias = "Canonical",
        description = "Canonical Human-Readable Title of Attributed Task"
    )

    Subscription: Optional[Union[URL, String, None]] = Field(
        default = None,
        alias = "Subscription",
        description = "HTTP(s) Subscription Endpoint"
    )

    Assignee: String = Field(
        default = None,
        alias = "Assignee"
    )

    Confidential: Boolean = Field(
        default = False,
        alias = "Confidential",
        description = "Confidential State of the Assigned Task"
    )

    Type: Task = Field(
        default = None,
        alias = "Type",
        description = "The Type of Assigned Task"
    )

    Body: String = Field(
        default = None,
        alias = "Body",
        description = "Body Metadata of Assigned Task; [Character] <= 1000",
        max_length = 1000
    )

    Scheduled: Optional[Target] = Field(
        default = Target(),
        alias = "Target",
        description = "Target Schedules of Task"
    )

    Importance: Optional[Priority] = Field(
        default = Priority.Standard,
        alias = "Priority",
        description = "Task Priority"
    )

    Recurrence: Optional[List[Optional[Schedule]]] = [Schedule()]

    Reminder: Optional[List[Optional[Schedule]]] = [Schedule()]

    State: Status = Field(
        default = None,
        alias = "Status",
        description = "The Current Status of the Task"
    )

    Active: Boolean = Field(
        default = False,
        alias = "Active",
        description = "Determines if Task is WIP"
    )

class Create(Base):
    """
    ...
    """

    Data: dict

class Update(Base):
    """
    ...
    """

    Modification: Date = Field(
        default_factory = Date.utcnow,
        alias = "Modification",
        description = "Document Last Modified Date"
    )

    class Config(Base.Config): title = Base.Config.title + "-" + "Update"

class Delete(Type):
    """
    ...
    """

    class Config(Base.Config): title = Base.Config.title + "-" + "Delete"

class Schema(Base):
    """
    ...
    """

    ID: Union[Object, String, None] = Field(None, alias = "ID")

    class Config(Base.Config): title = Base.Config.title + "-" + "Schema"

class Association(Schema):
    """
    ...
    """

    class Config(Base.Config): title = Base.Config.title + "-" + "Association"

class Generator(Schema):
    """
    ...
    """

    class Config(Base.Config): title = Base.Config.title + "-" + "Generator"

class JSON(Generator):
    """
    ...
    """

    class Config(Base.Config): title = Base.Config.title + "-" + "JSON"

class Response(Type):
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
