#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:   Jacob B. Sanders
# Source:  gitlab.cloud-technology.io
# License: BSD 3-Clause License

"""
...
"""

import os
import sys
import threading

class Percentage(object):
    def __init__(self, filename):
        self.file = filename
        self.size = float(os.path.getsize(filename))
        self.status = 0
        self.lock = threading.Lock()
        self.value = 0

    def __call__(self, amount):
        with self.lock:
            self.status += amount

            percentage = (self.status / self.size) * 100

            self.value = percentage

            sys.stdout.write(
                "\r" + "%s  %s / %s  (%.2f%%)" % (
                    self.file, self.status, self.size, percentage
                )
            ); sys.stdout.write("\n") if int(percentage) == 100 else sys.stdout.flush()
