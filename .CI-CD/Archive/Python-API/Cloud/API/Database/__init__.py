#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

import Cloud
import Cloud.API
import Cloud.API.Imports

from Cloud.API.Imports import *

from . import StandardError

class Base(object):
    """ Base(object)

    Base Database-Table Configuration Object.

    - table (String): N/A
    - _file (SQLlite3 *.DB): Primary Database Blob

    Methods
    =======

    `.connection()`
    ---------------
    High-Level version of `SQL.connect`'s method for return a connection object.
    Simply, `.connection()`returns such a connection object and a `cursor` object in the form of
    a tuple.

    `.total()`
    ----------
    Returns the total (`int`) amount of records found in a given table.
    """

    def __init__(self, table: str = None, _file: str = "Cloud-Hybrid.db", *argv, **kwargs):
        self.table: str = table

        self.file = _file

        self.db = os.path.dirname(os.path.realpath(__file__)
            ) + "/" + "{}".format(
                self.file)

        if not os.path.isfile(self.db):
            self.create()

        lambda FLAG: map(setattr(self, "{}".format(FLAG), True, argv))

        map(setattr, kwargs.items())

    def delete(self, ID: int):
        """ Delete a record

        In order to get the ID of a record, refer to the module's local documentation for ID look-up.

        Parameters:
        `ID`: int - The record's Row-ID.

        The following method is not implemented at an abstraction level
        due to how Python reads strings from C-level SQL Statements. Essentially,
        copy and paste the following where `table` is replaced with the applicable
        database table.

        >>> connection, cursor = self.connection()
        >>> statement = "DELETE FROM `table` WHERE id=?"
        >>> cursor.execute(statement, Singleton(ID))
        >>> connection.commit()
        """

        raise NotImplementedError


    def last(self, *argv, **kwargs): raise NotImplementedError

    def connection(self) -> tuple:
        """ connection(self)

        Establishes an instantiated table's database connection & DB cursor.
        """
        self.db = os.path.dirname(os.path.realpath(__file__)
            ) + "/" + "{}".format(
                self.file)

        _connection = SQL.connect(self.db)
        return (_connection, _connection.cursor())

    def close(self, _connection) -> None:
        """ close(self, _connection)

        Terminates any instaniated connections.

        - _connection (SQL.Connection): Takes a connection object as input
        """

        _connection.close()

    def save(self, _connection) -> None:
        """ save(self, _connection)

        Commits any executed changes and writes to the database.

        - _connection (SQL.Connection): Takes a connection object as input
        """

        _connection.commit()
        _connection.close()

    @classmethod
    def UUID(cls):
        return "{}".format(uuid.uuid4()).upper()

    @property
    def total(self):
        connection, cursor = self.connection()
        cursor.execute("SELECT COUNT(*) FROM {}".format(self.table))
        total = cursor.fetchone()[0]
        self.close(connection)
        return total

    @staticmethod
    def binarize(_file):
        with open(_file, "rb") as F:
            blob = F.read()

        return blob

    @staticmethod
    def formatDatetime(value: str):
        return value.split(" ")[0]

    @property
    def records(self):
        connection, cursor = self.connection()

        _return = []

        try:
            for record in connection.execute("SELECT * FROM {};".format(
                self.table
            )):
                _return.append(record)
        except SQL.OperationalError:
            self.create()
            for record in connection.execute("SELECT * FROM {};".format(
                self.table
            )):
                _return.append(record)

        return _return
