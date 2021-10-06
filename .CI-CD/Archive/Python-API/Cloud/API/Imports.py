#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

""" Imports
-----------

API Packaged Imports

"""

class Memoization:
    def __init__(self, function):
        self.function = function
        self.attribution = {}

    def __call__(self, *args):
        if args not in self.attribution:
            self.attribution[args] = self.function(*args)
        return self.attribution[args]

import os
import json
import time
import flask
import shlex
import ctypes
import struct
import shutil
import datetime
import platform
import subprocess

import urllib.request

import Cloud.Constants  as Constants
import Cloud.Settings   as Settings

System          = Constants.System

Disk            = shutil

Configuration   = Constants.Configuration
Jinja           = Constants.Jinja

Response    = flask.Response
JTYPE       = flask.jsonify
Template    = flask.render_template
Request     = flask.request

Integer     = Constants.Integer
Dictionary  = Constants.Dictionary
Unicode     = Constants.Unicode
Codes       = Constants.HTTP_STATUS_CODES
Bytes       = Constants.Bytes
Array       = Constants.Array
List        = Constants.List
Data        = Constants.Data
Field       = Constants.Field
Item        = Constants.Item
SQL         = Constants.SQL
String      = Constants.String
Tuple       = Constants.Tuple
Object      = Constants.Object
Pointer     = Constants.Pointer
Singleton   = Constants.Singleton
Dedentation = Constants.Dedentation
Mapping     = Constants.Mapping
JSON        = Constants.JSON
Truth       = Constants.Truth
NTruth      = Constants.NTruth
CLIMIT      = Constants.CLIMIT
FQDN        = Constants.FQDN

JWT = Constants.JWT

Blueprint   = flask.Blueprint
Settings    = Settings.Configuration
CSession    = flask.session

Cryptic = Constants.Cryptic
Vault = Constants.Vault

import Cloud.JWT                        as JWT

import Cloud.API.Server.IO              as IO
import Cloud.API.Server.Controls        as Controls
import Cloud.API.Server.Statistics      as Statistics
import Cloud.API.Server.Automation      as Automation

import Cloud.Authentication.Wrapper     as Authentication

import Cloud.API.Security.PEM           as PEM
import Cloud.API.Security.RSA           as RSA
import Cloud.API.Security.ECDSA         as ECDSA

import Cloud.Steam.API                  as Steam

Authenticate = Authentication.Authenticate
