""" Database
------------
...
"""

import os
import sys
import json
import pprint
import sqlite3

OperationalSQLException = sqlite3.OperationalError

_FFLAG = True

sqlite3.enable_callback_tracebacks(_FFLAG)

String = str

class SQLOperationalError(OperationalSQLException):
    """ Inherited from exception `sqlite3.OperationalError`

    Exception raised for errors that are related to the database’s operation and not necessarily under the control of the programmer, e.g. an unexpected disconnect occurs, the data source name is not found, a transaction could not be processed, etc. OperationSQLException is a further deprivation from https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError.
    """

    def __init__(self, _Error: Exception, *argv, **kwargs):
        super().__init__(*argv)

        self.Message = "Cursor Look-Up Failure:" \
                    + "\n" \
                    + "Error:" \
                    + " " \
                    + String(_Error) \
                    + "\n" \
                    + "Traceback (Line-#):" \
                    + " " \
                    + "{}".format(_Error.__traceback__.tb_lineno) \
                    + "\n" \
                    + "Traceback (L-Stack):" \
                    + " " \
                    + "{}".format(_Error.__traceback__.tb_lasti) \
                    + "\n" \
                    + "Traceback (Frame):" \
                    + " " \
                    + "{}".format(_Error.__traceback__.tb_frame.__repr__()) \
                    + "\n"

        self.Tracebacks = _FFLAG
        self.SQLVersion = sqlite3.sqlite_version

    @staticmethod
    def Decoupled(instantiation: OperationalSQLException) -> dict:
        return {
            "Message-Log" : instantiation.Message,
            "Traceback-Flag" : instantiation.Tracebacks,
            "Version" : instantiation.SQLVersion,
            "Instantiation" : instantiation
        }

    def STDERR(self): pprint.pprint(self.Decoupled(self))