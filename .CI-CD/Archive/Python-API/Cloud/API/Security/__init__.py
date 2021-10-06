""" ...
-----------

import flask
import Cloud.Settings

Flask = flask.Flask
Request = flask.Request
Blueprint = flask.Blueprint

request = flask.request
Response = flask.Response
render_template = flask.render_template
make_response = flask.render_template

Settings = Cloud.Settings.Configuration

"""

import os
import sys
import uuid
import shlex
import tempfile
import textwrap
import subprocess

import flask

import Cloud.API
import Cloud.Settings

import Cloud.Authentication.Wrapper as Wrapper

import Cloud.API.Imports as Imports

Terminal = os.get_terminal_size()

Spliter     = shlex.split
Condensor   = shlex.join

Format      = textwrap.dedent

TFile = tempfile.TemporaryFile
TDirectory = tempfile.TemporaryDirectory

Flask       = flask.Flask
Request     = flask.request
Blueprint   = flask.Blueprint
Handler     = flask.send_file

Method = staticmethod
String = str

Settings        = Cloud.Settings.Configuration
Memoization     = Imports.Memoization
Authenticate    = Wrapper.Authenticate

class Secure(object):
    Generator = Blueprint("Secure", __name__)
    Route = "/API/Security/"
    Methods = [
        "GET"
    ]

    Metadata = {
        "JWN"           : "{}".format(Settings.JWN),
        "Author"        : Settings.Author,
        "Company"       : Settings.Company,
        "Shortname"     : Settings.Shortname,
        "Directories"   : Settings.Directories,
        "Favicons"      : Settings.Favicons,
        "Domain"        : Settings.Domain,

        "X-Access-Token"    : None
    }


    def __init__(self, *argv, **kwargs): ()

    @staticmethod
    @Generator.route(Route, methods = Methods)
    def generate(): raise NotImplementedError
