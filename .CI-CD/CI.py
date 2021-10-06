#!/usr/bin/env python3

import os, os.path

import ssl
import sys
import stat

import subprocess

CWD = os.path.abspath(os.path.dirname(__file__))

global UMASK

UMASK      = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
             | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
             | stat.S_IROTH |                stat.S_IXOTH )

def main():
    Target = CWD + os.sep + ".State"

    os.makedirs(Target, UMASK, True)

    print("[Nexus-API] ...")

if __name__ == "__main__":
    main()
