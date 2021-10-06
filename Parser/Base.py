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
import argparse
import dataclasses

import Parser.Help as Help

import Parser.Port as Port
import Parser.HTTPs as HTTPs
import Parser.Silent as Silent
import Parser.Hostname as Hostname

import Parser.Assertion as Assertion

import Parser.Package as Package

Action: argparse.Action = argparse.Action

Schema = dataclasses.dataclass(init = False, frozen = False)

@Schema
class CMD:
    """
    ...
    """

    OS: ... = os

    Module: ... = argparse

    Type: Action = Action
    Help: Action = Help.Output.Command
    Parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog = "Nexus ... ",
        description = "Description ... ", add_help = False
    )

    Port: Action = Port.Configuration.Command
    HTTPs: Action = HTTPs.Configuration.Command
    Silent: Action = Silent.Configuration.Command
    Hostname: Action = Hostname.Configuration.Command

    Assertion: Action = Assertion.Configuration.Command

    Package: Action = Package.Importer.Command

__all__ = [
    "CMD"
]
