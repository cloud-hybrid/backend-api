#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

#
# ========================================================================
# ...
# ========================================================================
#

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

import Cloud
import Cloud.API
import Cloud.API.Imports

from Cloud.API.Imports import *

class Base(object):
    Generator = Blueprint("Base", __name__)
    Route = "/"
    Methods = [
        "GET", "HEAD"
    ]

    DisableHostChecking = "-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"

    Metadata = {
        "JWN"           : "{}".format(Settings.JWN),
        "Author"        : Settings.Author,
        "Company"       : Settings.Company,
        "Shortname"     : Settings.Shortname,
        "Directories"   : Settings.Directories,
        "Favicons"      : Settings.Favicons,
        "Domain"        : Settings.Domain,
        "Application"   : Settings.Application,

        "X-Access-Token"    : None
    }

    Template = {
        "Background-Color": "Light"
    }

    Grays = [("rgb({INDEX}, {INDEX}, {INDEX})".format(
        INDEX = index
    )) for index in range(0, 255, 15)]

    def __init__(self, *argv, **kwargs): ()

    @classmethod
    @Generator.route(Route, methods = Methods)
    def generate(cls, *argv, **kwargs):
        return 200
