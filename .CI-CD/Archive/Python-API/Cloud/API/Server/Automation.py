#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

"""\
Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

# --- Internal Imports --- #
import json
import textwrap

# --- External Imports --- #
from flask import Blueprint, \
    Response, \
        Request, request

# --- Package Imports --- #
from . import *

#   ---> CPU Statistics
from . import getCPUCount, \
    getCPUFrequencies, \
        getCPUPercentage, \
            getCPUStatistics, \
                getCPUTimingPercentages, \
                    getCPUTimings

#   ---> RAM Statistics
from . import getRAMInformation

#   ---> Disk Statistics
from . import Disk

#   ---> Network Statistics
from . import getNetworkStatistics, \
    getNetworkConnections

#   ---> General Statistics
from . import getSystemUptime, \
    getTotalSystemUptime, \
        getTotalSystemUptimeDelta

class Automata(Base):
    Generator = Blueprint("Automation", __name__)
    Route = Base.Route + "Automation"
    Methods = Base.Methods

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @staticmethod
    @Generator.route(Route, methods = Methods)
    def Index(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        if internal == False: return Response(json.dumps({
            "SSH-Banner" : Automata.Banner(internal = True)
        }, ensure_ascii = False) , status = 200, mimetype = mime)
        elif internal == True: return {
            "SSH-Banner" : Automata.Banner(internal = True),
        }

    @staticmethod
    @Generator.route(Route + "/" + "SSH-Banner", methods = Methods)
    def Banner(internal: bool = False, mime: str = "text/plain") -> Response(type({})):
        """ Cloud-Hybrid Default SSH Banner

        An SSH banner that displays a security notice.

        - mime: (String)                - The `Return` variable-response's Mimetype.
        - internal: (Boolean)           - Boolean that indicates if a response or the
                                          response's attributed value should be returned.
                                          `internal` is primarily set to True when a GET
                                          request is made to the root of the Blueprint.

        """

        if internal == False: return Response(textwrap.dedent("""\

            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┃              Cloud Hybrid - Security Notice             ┃
            ┃              ------------------------------             ┃
            ┃   The following source file(s) contains confidential,   ┃
            ┃  proprietary information. Unauthorized use is strictly  ┃
            ┃    prohibited. No portions may be copied, reproduced,   ┃
            ┃      or incorporated outside of this domain without     ┃
            ┃         Cloud Hybrid LLC's prior written consent.       ┃
            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

        """), status = 200, mimetype = mime)

        elif internal == True: return textwrap.dedent("""\

            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┃              Cloud Hybrid - Security Notice             ┃
            ┃              ------------------------------             ┃
            ┃   The following source file(s) contains confidential,   ┃
            ┃  proprietary information. Unauthorized use is strictly  ┃
            ┃    prohibited. No portions may be copied, reproduced,   ┃
            ┃      or incorporated outside of this domain without     ┃
            ┃         Cloud Hybrid LLC's prior written consent.       ┃
            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

        """)
