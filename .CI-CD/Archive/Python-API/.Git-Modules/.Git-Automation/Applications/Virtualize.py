#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Usage: .py

import io
import os
import re
import sys
import ctypes
import datetime
import time
import errno
import subprocess
import ipaddress
import threading
import subprocess
import socket
import venv
import yaml

from dataclasses import dataclass, field
from subprocess import Popen, PIPE
from threading import Thread
from urllib.parse import urlparse
from urllib.request import urlretrieve

class STDOUT(object):
    """ Color (object)
    Abstract TTY color escape sequences to style STDOUT with compatable buffers.

    > There is no need to instantiate this class unless \
        extending the class's capabilities.

        :param CEND         (lambda `input` -> str)    = lambda x: '\33[0m' + str(x)
        :param CBOLD        (lambda `input` -> str)    = lambda x: '\33[1m' + str(x)
        :param CITALIC      (lambda `input` -> str)    = lambda x: '\33[3m' + str(x)
        :param CURL         (lambda `input` -> str)    = lambda x: '\33[4m' + str(x)
        :param CBLINK       (lambda `input` -> str)    = lambda x: '\33[5m' + str(x)
        :param CBLINK2      (lambda `input` -> str)    = lambda x: '\33[6m' + str(x)
        :param CSELECTED    (lambda `input` -> str)    = lambda x: '\33[7m' + str(x)

        :param CBLACK       (lambda `input` -> str)    = lambda x: '\33[30m' + str(x)
        :param CRED         (lambda `input` -> str)    = lambda x: '\33[31m' + str(x)
        :param CGREEN       (lambda `input` -> str)    = lambda x: '\33[32m' + str(x)
        :param CYELLOW      (lambda `input` -> str)    = lambda x: '\33[33m' + str(x)
        :param CBLUE        (lambda `input` -> str)    = lambda x: '\33[34m' + str(x)
        :param CVIOLET      (lambda `input` -> str)    = lambda x: '\33[35m' + str(x)
        :param CBEIGE       (lambda `input` -> str)    = lambda x: '\33[36m' + str(x)
        :param CWHITE       (lambda `input` -> str)    = lambda x: '\33[37m' + str(x)

        :param CBLACKBG     (lambda `input` -> str)    = lambda x: '\33[40m' + str(x)
        :param CREDBG       (lambda `input` -> str)    = lambda x: '\33[41m' + str(x)
        :param CGREENBG     (lambda `input` -> str)    = lambda x: '\33[42m' + str(x)
        :param CYELLOWBG    (lambda `input` -> str)    = lambda x: '\33[43m' + str(x)
        :param CBLUEBG      (lambda `input` -> str)    = lambda x: '\33[44m' + str(x)
        :param CVIOLETBG    (lambda `input` -> str)    = lambda x: '\33[45m' + str(x)
        :param CBEIGEBG     (lambda `input` -> str)    = lambda x: '\33[46m' + str(x)
        :param CWHITEBG     (lambda `input` -> str)    = lambda x: '\33[47m' + str(x)

        :param CGREY        (lambda `input` -> str)    = lambda x: '\33[90m' + str(x)
        :param CRED2        (lambda `input` -> str)    = lambda x: '\33[91m' + str(x)
        :param CGREEN2      (lambda `input` -> str)    = lambda x: '\33[92m' + str(x)
        :param CYELLOW2     (lambda `input` -> str)    = lambda x: '\33[93m' + str(x)
        :param CBLUE2       (lambda `input` -> str)    = lambda x: '\33[94m' + str(x)
        :param CVIOLET2     (lambda `input` -> str)    = lambda x: '\33[95m' + str(x)
        :param CBEIGE2      (lambda `input` -> str)    = lambda x: '\33[96m' + str(x)
        :param CWHITE2      (lambda `input` -> str)    = lambda x: '\33[97m' + str(x)

        :param CGREYBG      (lambda `input` -> str)    = lambda x: '\33[100m' + str(x)
        :param CREDBG2      (lambda `input` -> str)    = lambda x: '\33[101m' + str(x)
        :param CGREENBG2    (lambda `input` -> str)    = lambda x: '\33[102m' + str(x)
        :param CYELLOWBG2   (lambda `input` -> str)    = lambda x: '\33[103m' + str(x)
        :param CBLUEBG2     (lambda `input` -> str)    = lambda x: '\33[104m' + str(x)
        :param CVIOLETBG2   (lambda `input` -> str)    = lambda x: '\33[105m' + str(x)
        :param CBEIGEBG2    (lambda `input` -> str)    = lambda x: '\33[106m' + str(x)
        :param CWHITEBG2    (lambda `input` -> str)    = lambda x: '\33[107m' + str(x)
    """

    _               = '\033[0m'
    CNORMAL         = lambda x: '\33[0m'   + str(x)     + '\033[0m'
    CBOLD           = lambda x: '\33[1m'   + str(x)     + '\033[0m'
    CITALIC         = lambda x: '\33[3m'   + str(x)     + '\033[0m'
    CURL            = lambda x: '\33[4m'   + str(x)     + '\033[0m'
    CBLINK          = lambda x: '\33[5m'   + str(x)     + '\033[0m'
    CUNDERLINE      = lambda x: '\033[4m'  + str(x)     + '\033[0m'
    CBLINK2         = lambda x: '\33[6m'   + str(x)     + '\033[0m'
    CSELECTED       = lambda x: '\33[7m'   + str(x)     + '\033[0m'

    CBLACK          = lambda x: '\33[30m'  + str(x)     + '\033[0m'
    CRED            = lambda x: '\33[31m'  + str(x)     + '\033[0m'
    CGREEN          = lambda x: '\33[32m'  + str(x)     + '\033[0m'
    CYELLOW         = lambda x: '\33[33m'  + str(x)     + '\033[0m'
    CBLUE           = lambda x: '\33[34m'  + str(x)     + '\033[0m'
    CVIOLET         = lambda x: '\33[35m'  + str(x)     + '\033[0m'
    CBEIGE          = lambda x: '\33[36m'  + str(x)     + '\033[0m'
    CWHITE          = lambda x: '\33[37m'  + str(x)     + '\033[0m'

    CBLACKBG        = lambda x: '\33[40m'  + str(x)     + '\033[0m'
    CREDBG          = lambda x: '\33[41m'  + str(x)     + '\033[0m'
    CGREENBG        = lambda x: '\33[42m'  + str(x)     + '\033[0m'
    CYELLOWBG       = lambda x: '\33[43m'  + str(x)     + '\033[0m'
    CBLUEBG         = lambda x: '\33[44m'  + str(x)     + '\033[0m'
    CVIOLETBG       = lambda x: '\33[45m'  + str(x)     + '\033[0m'
    CBEIGEBG        = lambda x: '\33[46m'  + str(x)     + '\033[0m'
    CWHITEBG        = lambda x: '\33[47m'  + str(x)     + '\033[0m'

    CGREY           = lambda x: '\33[90m'  + str(x)     + '\033[0m'
    CRED2           = lambda x: '\33[91m'  + str(x)     + '\033[0m'
    CGREEN2         = lambda x: '\33[92m'  + str(x)     + '\033[0m'
    CYELLOW2        = lambda x: '\33[93m'  + str(x)     + '\033[0m'
    CBLUE2          = lambda x: '\33[94m'  + str(x)     + '\033[0m'
    CVIOLET2        = lambda x: '\33[95m'  + str(x)     + '\033[0m'
    CBEIGE2         = lambda x: '\33[96m'  + str(x)     + '\033[0m'
    CWHITE2         = lambda x: '\33[97m'  + str(x)     + '\033[0m'

    CGREYBG         = lambda x: '\33[100m' + str(x)     + '\033[0m'
    CREDBG2         = lambda x: '\33[101m' + str(x)     + '\033[0m'
    CGREENBG2       = lambda x: '\33[102m' + str(x)     + '\033[0m'
    CYELLOWBG2      = lambda x: '\33[103m' + str(x)     + '\033[0m'
    CBLUEBG2        = lambda x: '\33[104m' + str(x)     + '\033[0m'
    CVIOLETBG2      = lambda x: '\33[105m' + str(x)     + '\033[0m'
    CBEIGEBG2       = lambda x: '\33[106m' + str(x)     + '\033[0m'
    CWHITEBG2       = lambda x: '\33[107m' + str(x)     + '\033[0m'

    RESET           = '\033[0m'

    @staticmethod
    def Write(message: str, data: str = "N/A", status: bool = None, colors: tuple = (CGREEN, CBLUE, CRED)) -> sys.stdout.write:
        if status == 0 or status == False:
            data = colors[2](data)
        elif status == 1 or status == True:
            data = colors[0](data)
        else:
            data = colors[1](data)

        data = STDOUT.CBOLD(data)

        sys.stdout.write(
            " " * os.get_terminal_size()[0]
            + "\r"
            + " " * len(Loader.String)
            + " "
            + "{}".format(
                message
            ) + ": "
            + "{}".format(
                data
            ) + "\r"
        )

    @staticmethod
    def Clear():
        sys.stdout.write(
            "\r"
            + " " * os.get_terminal_size()[0]
            + "\r"
        )

    def __getattribute__(self, name):
        if sys.platform.casefold() == "win32":
            raise NotImplementedError("Cannot Use POSIX Color Escape Sequences")

        return super().__getattribute__(name)

    def __getattr__(self, name):
        if sys.platform.casefold() == "win32":
            raise NotImplementedError("Cannot Use POSIX Color Escape Sequences")

        return getattr(self, name, default = r"'")

class Loader(threading.Thread):
    Status = True
    String = r"▐           ▌"
    Spinner = (
        STDOUT.CWHITE(r"▐●          ▌"),
        STDOUT.CWHITE(r"▐ ●         ▌"),
        STDOUT.CWHITE(r"▐  ●        ▌"),
        STDOUT.CWHITE(r"▐   ●       ▌"),
        STDOUT.CWHITE(r"▐    ●      ▌"),
        STDOUT.CWHITE(r"▐     ●     ▌"),
        STDOUT.CWHITE(r"▐      ●    ▌"),
        STDOUT.CWHITE(r"▐       ●   ▌"),
        STDOUT.CWHITE(r"▐        ●  ▌"),
        STDOUT.CWHITE(r"▐         ● ▌"),
        STDOUT.CWHITE(r"▐          ●▌"),
        STDOUT.CWHITE(r"▐         ● ▌"),
        STDOUT.CWHITE(r"▐        ●  ▌"),
        STDOUT.CWHITE(r"▐       ●   ▌"),
        STDOUT.CWHITE(r"▐      ●    ▌"),
        STDOUT.CWHITE(r"▐     ●     ▌"),
        STDOUT.CWHITE(r"▐    ●      ▌"),
        STDOUT.CWHITE(r"▐   ●       ▌"),
        STDOUT.CWHITE(r"▐  ●        ▌"),
        STDOUT.CWHITE(r"▐ ●         ▌"),
    )
    def __init__(self, name):
        super(Loader, self).__init__()
        self.name = name

    @staticmethod
    def Generate():
        """ Generator Method """
        while True:
            for cursor in Loader.Spinner: yield cursor

    def run(self):
        Generator = Loader.Generate()
        while Loader.Status == True:
            sys.stdout.write(next(Generator) + "\r")
            time.sleep(0.09875)

class __Cursor__(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),("visible", ctypes.c_byte)]

    @staticmethod
    def hide_cursor():
        if os.name == 'nt':
            instantiation = __Cursor__()
            stdout_handler = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(
                stdout_handler, ctypes.byref(instantiation))
            instantiation.visible = False
            ctypes.windll.kernel32.SetConsoleCursorInfo(stdout_handler, ctypes.byref(instantiation))
        elif os.name == 'posix':
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()

    @staticmethod
    def show_cursor():
        if os.name == 'nt':
            instantiation = __Cursor__()
            stdout_handler = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(stdout_handler, ctypes.byref(instantiation))
            instantiation.visible = True
            ctypes.windll.kernel32.SetConsoleCursorInfo(stdout_handler, ctypes.byref(instantiation))
        elif os.name == 'posix':
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()

class Environment(object):
    Shell = os.environ["SHELL"] if os.name != "nt" else None

    def __init__(self): ()

    @staticmethod
    def count(object: object):
        return len(object)

    @staticmethod
    def clear(): os.system("clear||cls")

    @staticmethod
    def start():
        os.system("python -m Cloud")

    @staticmethod
    def validate():
        Compatible = True
        if sys.version_info < (3, 7):
            Compatible = False
        elif not hasattr(sys, 'base_prefix'):
            Compatible = False
        if not Compatible:
            raise ValueError("Python Version not Compatable (VERSION == 3.7 | VERSION > 3.7)")

    @staticmethod
    def parse():
        count = Environment.count(sys.argv)

        if count == 1:
            Environment.updateDirectory()
            Environment.determineOS()
            Environment.evaluate()
            Environment.activate()
        elif count == 2:
            argument = sys.argv[1].casefold()
            if argument == "Start".casefold() or argument == "Activate".casefold():
                Environment.updateDirectory()
                Environment.determineOS()
                Environment.evaluate()
                Environment.activate()
            elif argument == "Exit".casefold() or argument == "Deactivate".casefold():
                Environment.exit()
            elif argument == "Update".casefold():
                Environment.update()
            elif argument == "Start".casefold():
                Environment.start()

    @staticmethod
    def exit(route: str = None):
        route = "N/A" if route == None else route

        if route.casefold() == "Activate".casefold(): Environment.activate()
        elif route.casefold() == "Deactivate".casefold(): Environment.deactivate()
        else: Environment.flush()

    @staticmethod
    def flush():
        time.sleep(1.0)
        Loader.Status = False
        STDOUT.Clear()
        sys.stdout.flush()
        sys.stdout.write("\r")
        __Cursor__.show_cursor()

    @staticmethod
    def updateDirectory():
        FILE = os.path.dirname(__file__)

        STDOUT.Write("Updating Directory", "{}".format(FILE))
        time.sleep(2.5)
        os.chdir(FILE)
        STDOUT.Write("Path", "{}".format(
            os.path.abspath(FILE)
        ))
        time.sleep(2.5)

    @staticmethod
    def determineOS():
        STDOUT.Write("Determining Operating System", "...", False)

        OS = os.name

        time.sleep(2.5)

        if OS == "NT".casefold():
            STDOUT.Write("System", "Windows", True)
        else:
            STDOUT.Write("System", "POSIX", True)
        time.sleep(2.5)

    @staticmethod
    def evaluate():
        output = None

        if os.path.isdir("venv") == False or os.path.isfile("./venv/bin/activate") == False:
            STDOUT.Write("Creating Directory", "venv")
            os.makedirs("venv", exist_ok = True)
            time.sleep(2.5)

            if os.name == "NT".casefold():
                command = []
                output = subprocess.Popen(["python", "-m", "venv", "{}".format("venv")],
                                    stdin = subprocess.DEVNULL,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE,
                                    shell = False,
                                    text = True
                        ).communicate(timeout = 15.0)[0]

            else:
                command = []
                output = subprocess.Popen(["python3", "-m", "venv", "{}".format("./venv")],
                                    stdin = subprocess.DEVNULL,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE,
                                    shell = False,
                                    text = True
                        ).communicate(timeout = 15.0)[0]

            time.sleep(5)

            STDOUT.Write("Virtual Environment", "Created", True)

        if output != None:
            STDOUT.Write("System Output", "{}".format(
                output
            ))

    @staticmethod
    def activate():
        STDOUT.Write("Activating", "Virtual Environment - Discord")

        Environment.flush()

        if os.name == "NT".casefold():
            os.system("> venv/Scripts/Activate.ps1")
        else:
            os.system("bash --rcfile ./venv/bin/activate")

    @staticmethod
    def deactivate():
        STDOUT.Write("Deactivating", "Virtual Environment - Discord")

        Environment.flush()

        if os.name == "NT".casefold():
            os.system("> venv/Scripts/Deactivate.ps1")
        else:
            os.system("bash --rcfile ./venv/bin/deactivate")

def main():
    Loader("Display").start()

    Environment.clear()
    Environment.validate()
    Environment.parse()

if __name__ == "__main__":
    try:
        __Cursor__.hide_cursor()
        main()

    except KeyboardInterrupt:
        __Cursor__.show_cursor()

        Loader.Status = False

        sys.stdout.flush()
        sys.stdout.write("\r")

    except Exception as Error:
        time.sleep(0.5)

        __Cursor__.show_cursor()

        Loader.Status = False

        sys.stdout.flush()
        sys.stdout.write(" " * os.get_terminal_size()[0])
        sys.stdout.write("\r")

        sys.stdout.write(""""""
            + STDOUT.CRED(STDOUT.CBOLD("Error"))
            + ": "
            + str(Error)
            + "\n"
            + "  ↳ Exception: "
            + STDOUT.CYELLOW(
                STDOUT.CBOLD("{}".format(Error.args[0])))
            + "\n"
        )

    finally:
        Environment.exit()