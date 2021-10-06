#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

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

import flask
import Cloud.Settings

import Cloud.Authentication.Wrapper as Wrapper

Flask = flask.Flask
Request = flask.Request
Blueprint = flask.Blueprint

request = flask.request
Response = flask.Response
send_file = flask.send_file
session = flask.session
sessions = flask.sessions
jsonify = flask.jsonify
redirect = flask.redirect
url_for = flask.url_for
render_template = flask.render_template
make_response = flask.render_template

Settings = Cloud.Settings.Configuration

Authenticate = Wrapper.Authenticate