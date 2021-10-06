#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:   Jacob B. Sanders
# Source:  gitlab.cloud-technology.io
# License: BSD 3-Clause License

"""
Usage: $ Nexus-API --Help
"""

from __future__ import annotations

import os
import ssl
import signal
import pprint
import textwrap

import Utility.Color

global UMASK

from . import *

ssl._create_unverified_context = ssl._create_default_https_context

Arguments = [Argument.casefold() for Argument in sys.argv]

Encrypted = any([
    "--tls" in Arguments,
    "--https" in Arguments
])

Debug = any([
    "--debug" in Arguments
])

Color = Utility.Color.TTY()

def Unit() -> Boolean:
    PendingDeprecationWarning(
        "Unit() Will be Removed in the Future"
    )

    Valid = False
    Validation = {}

    Assertion = os.environ.get("NEXUS_API_ASSERTION", False)

    if os.environ.get("NEXUS_API_UNIT_TESTING", False) or Assertion:
        Validation["Authentication"] = os.path.isfile(
            os.path.abspath(
                os.path.dirname(
                    __file__
                ) + os.sep + "ASGI"
                + os.sep + "Authentication"
                + os.sep + ".env"
            )
        )

        Validation["Environment"] = os.path.isfile(
            os.path.abspath(
                os.path.dirname(
                    __file__
                ) + os.sep + os.pardir
                + os.sep + ".env"
            )
        )

    assert (Valid := all(Validation.values())) if Assertion else ...

    return Valid

async def Environment(Semaphore: Lock):
    """
    Environment (Callable) -> None:

        Await `Parser` to have parsed and stored intended Environment
        Variables; continue through evaluation to ensure propogation.

    """

    await Semaphore.acquire() if not Semaphore.locked() else ...

    Stateful:   Callable = lambda: os.environ.get(ENVIRONMENT, False)
    Default:    Callable = lambda K, _ = None: os.environ.get(K, _)
    Update:     Callable = lambda K, V: os.environ.update({K: V})

    try:
        while Default(ENVIRONMENT, "STATELESS") != "STATEFUL":
            Update(ENVIRONMENT, Stateful()) if Stateful() else ASGI.wait(2.5)

    except Exception as Error: raise Error
    except KeyboardInterrupt:
        sys.stdout.write("\r" + "Asynchronous Interrupt ... "
             + "\n" + " - SIGKILL (1)" + "\n"
        ); exit(0)

    finally:
        Semaphore.release()

    sys.stdout.flush()

def Runtime():
    Entry = CLI.arguments()

    sys.stdout.write(Color.green("[Nexus-API]") + "%s"
        % Color.normalized(": %s" % "Awaiting Environment Lock ➜ ")
    )
    sys.stdout.flush()

    Semaphore = Lock()
    ASGI.run(Semaphore.acquire())

    Awaiter = ASGI.create_task(
        Environment(Semaphore)
    ); ASGI.queue(Awaiter)

    sys.stdout.write("Successful" + "\n")
    sys.stdout.flush()

    sys.stdout.write(Color.green("[Nexus-API]") + "%s"
        % Color.normalized(": %s" % "Retrieving Event-Loop ➜ ")
    )
    sys.stdout.flush()

    sys.stdout.write("ASGI" + "\n")
    sys.stdout.flush()

    Main(ASGI)

    sys.stdout.write("\r" + String(" " * os.get_terminal_size(sys.stdout.fileno()).columns if os.isatty(sys.stdout.fileno()) else 0) + "\r"),
    sys.stdout.flush()
    sys.stdout.write(
        "\n" + "[Nexus-API]" + " " +
        "Asynchronous Interrupt ... " + "\n" +
        " - SIGKILL (1)" + "\n"
    )

    exit(0)


def Main(ASGI):
    """ Application Entry Point """

    sys.stdout.write(Color.green("[Nexus-API]") + "%s"
        % Color.normalized(": %s" % "Calculating Compute ➜ ")
    ); sys.stdout.flush()

    Count = os.cpu_count()

    sys.stdout.write("%i" % Count + " " + "Available CPUs" + "\n")
    sys.stdout.flush()

    URL = String("https://" if Encrypted else "http://") + "localhost" + ":" + "3000" + "/Documentation" + "\n"

    sys.stdout.write(Color.green("[Nexus-API]") + "%s"
        % Color.normalized(": API ➜ " + URL)
    ); sys.stdout.flush()

    sys.stdout.write(Color.green("[Nexus-API]") + "%s"
        % Color.normalized(": %s" % "Flushing Input & Output Buffers ➜ ")
    ); sys.stdout.flush()

    sys.stdout.write("Cleared" + "\n")
    sys.stdout.flush()

    sys.stdout.write(Color.green("[Nexus-API]") + "%s"
        % Color.normalized(": %s" % "Updating Logger Setting(s) ➜ ")
    ); sys.stdout.flush()

    Logger = logging.basicConfig(level = logging.DEBUG) if Debug else logging.basicConfig()

    sys.stdout.write("[DEFAULT]" + "\n" if not Debug else "[DEBUG]" + "\n")
    sys.stdout.flush()

    Server = ASGI.create_task(
        Application.Server.serve(),
            name = "Nexus-API"
    )

    # PostgreSQL = ASGI.create_task(
    #     Driver.Async.Instantiate(),
    #         name = "PostgreSQL"
    # )

    # ASGI.queue(PostgreSQL)

    ASGI.queue(Server)


if __name__ == "__main__":
    Runtime()
