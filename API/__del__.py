#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:   Jacob B. Sanders
# Source:  gitlab.cloud-technology.io
# License: BSD 3-Clause License

import os
import sys
import shlex
import atexit
import shutil
import warnings
import subprocess

warnings.filterwarnings("ignore")

def Uninstall():
    subprocess.Popen(
        args = shlex.split("{0} -m pip uninstall Nexus-API --yes".format(
            sys.executable
        )), shell = False,
        stderr = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stdin = subprocess.PIPE
    )

    exit(0)

@atexit.register
def __clean__():
    Binary = [
        shutil.which("Nexus-API"),
        shutil.which("Uninstall-Nexus-API")
    ]

    os.remove(Binary[0])
    os.remove(Binary[1])

    sys.exit(0)
