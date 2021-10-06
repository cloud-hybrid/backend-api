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

from . import *

global Environment

def arguments():
    """
    ...
    """

    CMD = Context.CMD()
    Parser = CMD.Parser

    Parser.add_argument("--Debug", "--debug", dest = "Debug", action = "store_true", default = False)

    Parser.add_argument("--Help", "--help", "-H", "-h",
        action = Context.Help.Output.Command,
        default = argparse.SUPPRESS,
        nargs = 0
    )

    Auxiliary = Parser.add_subparsers(metavar = "Service", required = False)

    Server = Auxiliary.add_parser(name = "Server").add_argument_group()
    Server.add_argument("--Port", "--port", "-P", "-p",
        action = Context.Port.Configuration.Command,
        default = argparse.SUPPRESS,
        dest = "Port",
        type = Integer,
        nargs = 1
    )
    Server.add_argument("--Host", "--Hostname", "--host", "--hostname", "-H",
        action = Context.Hostname.Configuration.Command,
        default = argparse.SUPPRESS,
        dest = "Host",
        type = String,
        nargs = 1
    )

    Server.add_argument("--TLS", "--HTTPS", "--HTTPs", "--https",
        action = Context.HTTPs.Configuration.Command,
        default = argparse.SUPPRESS,
        dest = "HTTPs",
        nargs = 0
    )

    Server.add_argument("--Silent", "--silent",
        action = Context.Silent.Configuration.Command,
        default = argparse.SUPPRESS,
        dest = "Silent",
        nargs = 0,
        const = True
    )

    Package = Auxiliary.add_parser(name = "Package").add_argument_group()
    Package.add_argument("--Invalidate", "--Clear-Cache", "-I", "-i",
        action = Context.Package.Importer.Command,
        default = argparse.SUPPRESS,
        dest = "Invalidate",
        nargs = 0
    )

    Arguments = Parser.parse_args(namespace = Environment)

    Environment.SQL()

    Environment.Port()
    Environment.Host()
    Environment.HTTPs()
    Environment.Silent()

    # Environment.Arguments = Arguments

    Environment.Update("NEXUS_API_ENVIRONMENT_LOCK", "STATEFUL")

    return Environment

__all__ = ["Environment", "arguments"]
