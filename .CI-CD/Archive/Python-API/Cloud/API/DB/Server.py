import os
import sqlite3

try:
    from Cloud.API.DB.Base import Database
except ModuleNotFoundError:
    from Base import Database

class Table(Database):
    """ Service.Table
    Table Layout:
    -------------
     - ID : Unique Record ID
    """
    def __init__(self, table: str = "Server", *argv, **kwargs):
        self.table: str = table

        super().__init__(table = table)

    def create(self, override = False, initialize = False):
        connection, cursor = self.connection()

        if override == True:
            cursor.execute("DROP TABLE {};".format(
                self.table
            ))

        # --- Create Table --- #
        cursor.execute("""\
            CREATE TABLE IF NOT EXISTS {}
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL UNIQUE,
            Service TEXT NOT NULL UNIQUE,
            Service_File TEXT NOT NULL UNIQUE,
            Directory TEXT NOT NULL UNIQUE,
            Settings TEXT NOT NULL UNIQUE,
            Instance TEXT NOT NULL,
            HostID INTEGER,
            FOREIGN KEY(HostID) REFERENCES Host(ID)
            );
        """.format(self.table))

        self.save(connection)

    def addRecord(self, NAME: str, FILENAME: str, PATH: str, CONTENT: str, SERVERID: str):
        connection, cursor = self.connection()

        statement = """INSERT INTO {TABLE} VALUES ({ID},"{NAME}","{FILENAME}","{PATH}","{CONTENT}","{SERVERID}")""".format(
            TABLE = self.table,
            
            ID = "null",
            NAME = NAME,
            FILENAME = FILENAME,
            PATH = PATH,
            CONTENT = CONTENT,
            SERVERID = SERVERID
        )

        connection.execute(statement)

        self.save(connection)

    def search(self, ServerID: str):
        connection, cursor = self.connection()

        try:
            cursor.execute("SELECT * FROM Server WHERE ServerID=?", (ServerID,))
            _data = cursor.fetchone()
        except sqlite3.OperationalError:
            self.create()
            cursor.execute("SELECT * FROM Server WHERE ServerID=?", (ServerID,))
            _data = cursor.fetchone()

        try:
            return _data
        except Exception as error:
            return "Server DB Error: {}".format(
                error
            )
        finally:
            self.close(connection)

    def searchInstanceRecords(self, instance: str):
        connection, cursor = self.connection()

        try:
            cursor.execute("SELECT * FROM Server WHERE Instance=?", (instance,))
            _data = cursor.fetchall()
        except sqlite3.OperationalError:
            self.create()
            cursor.execute("SELECT * FROM Server WHERE Instance=?", (instance,))
            _data = cursor.fetchall()

        try:
            return _data
        except Exception as error:
            return "Server DB Error: {}".format(
                error
            )
        finally:
            self.close(connection)

    def searchInstanceServiceRecord(self, instance: str, service: str):
        connection, cursor = self.connection()

        try:
            cursor.execute("SELECT * FROM Server WHERE Instance=? AND Name=?", (instance, service))
            _data = cursor.fetchall()
        except sqlite3.OperationalError:
            self.create()
            cursor.execute("SELECT * FROM Server WHERE Instance=? AND Name=?", (instance, service))
            _data = cursor.fetchall()

        try:
            return _data
        except Exception as error:
            return "Server DB Error: {}".format(
                error
            )
        finally:
            self.close(connection)

    def searchRecordsByHostIDKey(self, key: int):
        connection, cursor = self.connection()

        try:
            cursor.execute("SELECT * FROM Server WHERE HostID=?", (key,))
            _data = cursor.fetchall()
        except sqlite3.OperationalError:
            self.create()
            cursor.execute("SELECT * FROM Server WHERE HostID=?", (key,))
            _data = cursor.fetchall()

        try:
            return _data
        except Exception as error:
            return "Server DB Error: {}".format(
                error
            )
        finally:
            self.close(connection)
