import os
import sqlite3

from collections import namedtuple as Tuple

class Database(object):
    def __init__(self, table: str = None, _file: str = "Cloud-API.db", *argv, **kwargs):
        self.table: str = table

        self.file = _file

        self.db = os.path.dirname(os.path.realpath(__file__)
            ) + "/" + "{}".format(
                self.file)

        if not os.path.isfile(self.db):
            self.create()

        lambda FLAG: map(setattr(self, "{}".format(FLAG), True, argv))

        # --> Attributions (Assigned via key-worded arguments in the initializer's parameters)
        map(setattr, kwargs.items())

    def last(self, *argv, **kwargs): raise NotImplementedError


    def connection(self):
        self.db = os.path.dirname(os.path.realpath(__file__)
            ) + "/" + "{}".format(
                self.file)

        _connection = sqlite3.connect(self.db)
        return (_connection, _connection.cursor())

    def close(self, _connection):
        _connection.close()

    def save(self, _connection):
        _connection.commit()
        _connection.close()

    def create(self, *argv, **kwargs): raise NotImplementedError
    def addRecord(self, *argv, **kwargs): raise NotImplementedError
    def search(self, *argv, **kwargs): raise NotImplementedError

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
    def records(self) -> list:
        connection, cursor = self.connection()

        _return = []

        try:
            for record in connection.execute("SELECT * FROM {};".format(
                self.table
            )):
                _return.append(record)
        except sqlite3.OperationalError:
            self.create()
            for record in connection.execute("SELECT * FROM {};".format(
                self.table
            )):
                _return.append(record)

        return _return

    @property
    def Tables(self) -> dict:
        from pprint import pprint
        """ Tables
        ----------
            Property value that returns all records associated with a given database.
        """

        connection, cursor = self.connection()

        _return = {}
        _property = {}

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        tables = cursor.fetchall()
        
        for table in tables:
            cursor.execute("SELECT * FROM {};".format(
                str(table[0])
            ))

            _return[str(table[0])] = {
                "Data" : cursor.fetchall()
            }

            _return["{}-Total-Records".format(
                    table[0]
                )] = { 
                    "Total-Records" : 
                    cursor.execute("SELECT COUNT(*) FROM {}".format(
                        table[0]
                    )).fetchone()[0]
                }

            _return["{}-Database".format(
                    table[0]
                )] = { "Database-File" : self.file }

            _property[str(table[0])] = {
                **_return[str(table[0])], 
                **_return["{}-Total-Records".format(
                    table[0]
                )],
                **_return["{}-Database".format(
                    table[0]
                )]
            }

        return _property
    
    @property
    def Tablenames(self) -> list:
        """ Tablenames
        --------------
            Property value that returns the table names within a given database.
        """

        connection, cursor = self.connection()

        _return = []

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        tables = cursor.fetchall()
        
        for table in tables: _return.append(table[0])

        return _return

def main(): ()

if __name__ == "__main__":
    main()