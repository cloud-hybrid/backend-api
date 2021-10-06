#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

""" ...
-----------

"""

import functools

import flask

Wrapper = functools.wraps

Blueprint   = flask.Blueprint
Session     = flask.session
Redirection = flask.redirect

__all__ = [
    "Blueprint", "Session", "Redirection"
]