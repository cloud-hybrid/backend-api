#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

import ipaddress
import datetime
import ctypes
import struct
import time
import json

from Cloud.Settings import Configuration as Settings

from flask import Blueprint, Response

from psutil import net_io_counters as getNetworkStatistics, \
    net_connections as getNetworkConnections, \
        boot_time

from Cloud.Authentication.Wrapper import Authenticate

from Cloud.API.Imports import *

class Base(object):
    Generator = Blueprint(None, __name__)

    Generator.add_url_rule(Generator, strict_slashes = False)

    Route = "/API/Network"
    Methods = [
        "GET", "POST", "HEAD", "CONNECT"
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

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @staticmethod
    @Generator.route(Route, methods = Methods)
    @Authenticate
    def Index(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        return 200

class Event(object):
    def __init__(self, ingress: Request, status: Integer, message: Tuple, **data):
        self.data = JTYPE({
            "Status" : status,
            "Label" : message[0],
            "Message": message[1],
            "Root"      : (
                {"Request"  : ingress.url_root,
                    "Data"      : data.get("Root-Data", None)}),
            "Method"    : (
                {"Request" : ingress.method,
                    "Data"      : data.get("Method-Data", None)}),
            "Endpoint"  : (
                {"Request" : ingress.endpoint,
                    "Data"      : data.get("Endpoint-Data", None)}),
            "URL": data.get("URL", ingress.url),
            "Occurrence" : (datetime.datetime.ctime(datetime.datetime.now()).split(" "), "ctime"),
            "Path": data.get("Path", ingress.path),
            "Full-Path": data.get("Full-Path", ingress.full_path),
            "Arguments": data.get("Arguments", Dictionary(ingress.values)),
            "Data": ({"Keys" : (Tuple(data.keys())), "Values" : (Tuple(data.values()))}),
        }), status

    @property
    def Response(self):
        return self.data

    @property
    def Status(self):
        return self.data["Status"]

    @property
    def Label(self):
        return self.data["Label"]

    @property
    def Message(self):
        return self.data["Message"]

    @property
    def Root(self):
        return self.data["Root"]

    @property
    def Method(self):
        return self.data["Method"]

    @property
    def Endpoint(self):
        return self.data["Endpoint"]

    @property
    def URL(self):
        return self.data["URL"]

    @property
    def Occurrence(self):
        return self.data["Occurence"]

    @property
    def Path(self):
        return (self.data["Path"], self.data["Full-Path"])

    @property
    def Arguments(self):
        return self.data["Arguments"]

    @property
    def Data(self):
        return self.data["Data"]
