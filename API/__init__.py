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
# Python, Standard Library
# =============================================================================

import os
import sys
import time
import atexit
import typing
import asyncio
import logging
import warnings

# ... import ssl as SSL

# =============================================================================
# Contextual & Synchronization
# =============================================================================

# import uvloop as UV

# Context = UV.new_event_loop()

Lock    = lambda: asyncio.Lock()
Wait    = lambda: asyncio.sleep(2.5)

# UV.install()

# asyncio.set_event_loop(Context)

# ----------------------
# Environment Constants
# ----------------------

ENVIRONMENT = "NEXUS_API_ENVIRONMENT_LOCK"

# =============================================================================
# Type Hinting
# =============================================================================

Integer = int
Boolean = bool
String = str
Float = float

Optional = typing.Optional

List = typing.List
Tuple = typing.Tuple
Dictionary = typing.Dict
Collection = typing.OrderedDict
Callable = typing.Callable
Type = typing.Final

# ------------------------------
# Logging & Debug Configuration
# ------------------------------

os.environ["PYTHONWARNINGS"] = "0"

logging.captureWarnings(False)

# -----------------------------
# API Modules, Web Application
# -----------------------------

import API.AWS.S3.Interface

# -----------------------------
# Command-Line Argument Parser
# -----------------------------

import Parser.Parse as CLI

# -----------------------------
# Non-Relational Database APIs
# -----------------------------

import Database.Taskboard
import Database.Taskboard.Interfaces.Task
import Database.Taskboard.Interfaces.LinkedResource

# -------------------------------
# ASGI Application(s)
# -------------------------------

import Server

Application = Server.Application

Mongo = Database.Server

# =============================================================================
#  --> Exports
# =============================================================================

ASGI        = asyncio.get_event_loop()
ASGI.wait   = asyncio.sleep
ASGI.run    = asyncio.run
ASGI.queue  = ASGI.run_until_complete
