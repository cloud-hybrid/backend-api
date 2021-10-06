#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Usage: .py

""" Statistics
==============

Various server hardware statistics, accessible via REST-based endpoints.

"""

import Cloud
import Cloud.API
import Cloud.API.Imports

from Cloud.API.Imports import *

from psutil import cpu_count as getCPUCount, \
    cpu_freq as getCPUFrequencies, \
        cpu_percent as getCPUPercentage, \
            cpu_stats as getCPUStatistics, \
                cpu_times as getCPUTimings, \
                    cpu_times_percent as getCPUTimingPercentages, \
                        net_io_counters as getNetworkStatistics, \
                            net_connections as getNetworkConnections, \
                                virtual_memory as getRAMInformation, \
                                    version_info as Versioning, \
                                        boot_time

def getSystemUptime() -> str:
    return datetime.datetime.fromtimestamp(boot_time())

def getTotalSystemUptime():
    try:
        library = ctypes.CDLL("libc.so.6")
        buffer = ctypes.create_string_buffer(4096)

        if library.sysinfo(buffer) != 0: return -1

        return struct.unpack_from("@l", buffer.raw)[0]
    except OSError:
        return time.time() - boot_time()

def getTotalSystemUptimeDelta():
    return time.time() - boot_time()

class Base(object):
    Generator = Blueprint("Base", __name__)
    Route = "/API/Server/"
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

    def __init__(self, *argv, **kwargs): ()

    @staticmethod
    @Generator.route(Route, methods = Methods)
    def generate(): raise NotImplementedError

    @staticmethod
    @Generator.route(Route, methods = Methods)
    def Index(internal: bool = False, mime: str = "application/json") -> Response(type({})): raise NotImplementedError()

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
