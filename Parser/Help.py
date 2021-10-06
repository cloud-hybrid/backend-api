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
import os
import sys
import typing
import textwrap

from . import Action, Color

Type = typing.Type

Color = Color.TTY

class Output:
    """
    ...
    """

    def __init__(self, *argv, **kwargs):
        map(setattr, kwargs.items())

    class Command(Action):
        """
        ...
        """

        def __call__(self, *argv, **kwargs):
            """
            ...
            """

            Width = os.get_terminal_size(sys.stdin.fileno()).columns

            String = str(
                " " + "┏━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓".center(0) + "\n" +
                " " + "┃ Nexus-API │ https://gitlab.cloud-technology.io/Nexus ┃".center(0).replace("Nexus-API", Color().bold("Nexus-API")) + "\n" +
                " " + "┠───────────┴──────────────────────────────────────────┨".center(0) + "\n" +
                " " + "┃    A Command-Line Interface to the Nexus CLI Tool    ┃".center(0) + "\n" +
                " " + "┃   ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄   ┃".center(0) + "\n" +
                " " + "┃         Copyright 2021, All Rights Reserved          ┃".center(0) + "\n" +
                " " + "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛".center(0)
            )

            Wrapper = textwrap.TextWrapper(width = 100, initial_indent = " " * 0, subsequent_indent = " " * 8, expand_tabs = False, break_on_hyphens = False, break_long_words = False)
            Usage = [
                str("\n" + " ").join(list(map(lambda _: _, (
                    "",
                    "  ↳ CLI Usage  ",
                    " - - - - - - - ",

                    Color().yellow(" python[3] -m API ")
                        + Color().green("")
                        + "\n" + "   " +
                    Color().blue(" - Start the API Service"),

                    Color().yellow(" python[3] -m API ")
                        + Color().green("[--[H]elp | -h]")
                        + "\n" + "   " +
                    Color().blue(" - Print Help Message"),

                    Color().yellow(" python[3] -m API ")
                        + Color().green("[--Unit-Test | --Test | --UAT | -U]")
                        + "\n" + "   " +
                    Color().blue(" - Initialize the API Service with Try-Caught, Logged Validation(s)"),

                    Color().yellow(" python[3] -m API ")
                        + Color().green("[--TLS | --HTTPS | --HTTPs | --https]")
                        + "\n" + "   " +
                    Color().blue(" - Enable Local Environment Encryption via HTTP + TLS"),

                    Color().yellow(" python[3] -m API ")
                        + Color().green("[--Assertion ? (--Unit-Test | --Test | --UAT | -U)]")
                        + "\n" + "   " +
                    Color().blue(" - Run the API Service, with Optional, Forced Validation(s)"),

                    Color().yellow(" python[3] -m API ")
                        + Color().green("[SQL] (--[C]reate | --[D]rop | --[R]ecycle)")
                        + "\n" + "   " +
                    Color().blue(" - Perform a Database Function(s) before Starting the API Service"),

                    Color().yellow(" python[3] -m API ")
                        + Color().green("[Package] (--[I]nvalidate | --Clear-Cache)")
                        + "\n" + "   " +
                    Color().blue(" - Clear the Package's Modularized Caches"),

                    Color().yellow(" python[3] -m API ")
                        + Color().green("[Server] (--[H]ost | --[H]ostname | -H)") + " " + Color().underline("Hostname")
                        + "\n" + "   " +
                    Color().blue(" - Set the API Service's Targetted Hostname"),

                    Color().yellow(" python[3] -m API ")
                        + Color().green("[Server] (--[P]ort | -[P])") + " " + Color().underline("Port-Number")
                        + "\n" + "   " +
                    Color().blue(" - Set the API Service's Targetted Port Number"),
                ))))
            ]

            print(Color().italic(String))

            for line in Usage: print(line)

            exit(0)

__all__ = [
    "Output"
]
