#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

""" \
...
===

...
"""

from flask import Response, session, render_template, request, redirect, make_response, url_for, sessions
from functools import wraps

import flask

from Cloud.API.Imports import *

from Cloud.Constants import SECRET_KEY

import datetime

from pprint import pprint

def Authenticate(Generator):
    @wraps(Generator)
    def validate(*args, **kwargs):
        if request.is_secure == False:
            print("Response: (401, SSL, HTTP)" + "\n")
            session.clear()
            return Response(redirect(Settings.Domain), status = 401, mimetype = "Text/HTML", headers = { "WWW-Authenticate": "Bearer JWT", "Referer" : "{}".format(Generator.route)}).response
        elif session.get("Authenticated", False) == True:
            print("X-Authentication-Token: -< ")
            for key, value in Dictionary(JWT.decode(session["API-Token"], key = SECRET_KEY, algorithms = ["HS256"])).items():
                print("  - {}: {}".format(key, value))
            if session.get("API-Token", None) != None:
                Token = JWT.decode(
                        session["API-Token"],
                        key = SECRET_KEY,
                        algorithms = ["HS256"]
                    )
                if Token["Time"] >= Token["Expiration"]:
                    print("Response: (401, Time)" + "\n")
                    session.clear()
                    return Response(redirect(Settings.Domain + "/" + "login"), status = 401, mimetype = "Text/HTML", headers = { "WWW-Authenticate": "Bearer JWT", "Referer" : "{}".format(Generator.route)}).response
                elif Token["JTI"] != Settings.JTI:
                    print("Response: (401, JTI)" + "\n")
                    session.clear()
                    return Response(redirect(Settings.Domain + "/" + "login"), status = 401, mimetype = "Text/HTML", headers = {"Referer": "{}".format(Settings.Domain + request.path), "WWW-Authenticate": "Bearer JWT"}).response
                else:
                    print("Response: (200, Success)" + "\n")
                    return Generator(*args, **kwargs)
        else:
            session.clear()
            return Response(redirect(Settings.Domain + "/" + "login"), status = 405, mimetype = "Text/HTML").response

    return validate
