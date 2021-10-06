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
import dataclasses

Environment = lambda Variable, _ = None: os.getenv(Variable, _)

HOSTNAME = "NEXUS_API_HOSTNAME"
PORT = "NEXUS_API_PORT"
HTTPS = "NEXUS_API_HTTPS"
SILENT = "NEXUS_API_SILENT_LOGGING"

Schema = dataclasses.dataclass()

@Schema
class Default:
    """
    ...
    """

    Host = "0.0.0.0"
    HTTPs = False
    Port = 3000

    Silent = False

@Schema
class Uploader:
    """
    ...
    """

    Host = "localhost"
    Port = 1250
