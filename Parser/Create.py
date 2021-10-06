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

import sqlalchemy

import Database
import Database.SQL
import Database.Tables

from . import Action

class Tables:
    """
    ...
    """

    def __init__(self, *argv, **kwargs):
        map(setattr, kwargs.items())

    @staticmethod
    def SQL():
        """
        Database Provisioning Function
        """

        Sync = Database.SQL.URI.replace("+asyncpg", "")

        Engine = sqlalchemy.create_engine(Sync)

        for Table in Database.Tables.Meta:
            for Module in Table.values():
                Module.create_all(
                    Engine, checkfirst = True
                )

        exit(0)

    class Command(Action):
        """
        ...
        """

        def __call__(self, Parser, Namespace, Values, Options = None):
            """
            ...
            """

            setattr(Namespace, self.dest, lambda: Tables.SQL())

__all__ = [
    "Tables"
]
