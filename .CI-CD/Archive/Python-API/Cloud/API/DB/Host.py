import os
import sqlite3

try:
    from Cloud.API.DB.Base import Database
except ModuleNotFoundError:
    from Base import Database

class Table(Database):
    """ Host.Table
    Table Layout:
    -------------
     - ID : Unique Record ID
    """

    def __init__(self, table: str = "Host", *argv, **kwargs):
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
            Instance TEXT NOT NULL UNIQUE,
            Name TEXT NOT NULL UNIQUE,
            Username TEXT NOT NULL,
            Token TEXT NOT NULL,
            Secret TEXT NOT NULL,
            Key TEXT NOT NULL,
            Region TEXT NOT NULL,
            Output TEXT NOT NULL,
            Account TEXT NOT NULL
            );
        """.format(self.table))

        self.save(connection)

    def addRecord(self, INSTANCE: str, NAME: str, USERNAME: str, TOKEN: str, SECRET: str, KEY: str, REGION: str, OUTPUT: str, ACCOUNT: str):
        connection, cursor = self.connection()

        statement = """INSERT INTO {TABLE} VALUES ({ID},"{INSTANCE}","{NAME}","{USERNAME}","{TOKEN}","{SECRET}","{KEY}","{REGION}","{OUTPUT}","{ACCOUNT}")""".format(
            TABLE = self.table,
            
            ID = "null",
            NAME = NAME,
            TOKEN = TOKEN,
            SECRET = SECRET,
            INSTANCE = INSTANCE,
            USERNAME = USERNAME,
            KEY = KEY,
            REGION = REGION, 
            OUTPUT = OUTPUT, 
            ACCOUNT = ACCOUNT
        )

        connection.execute(statement)

        self.save(connection)

    def search(self, instance: str):
        connection, cursor = self.connection()

        try:
            cursor.execute("SELECT * FROM Host WHERE Instance=?", (instance,))
            _data = cursor.fetchone()
        except sqlite3.OperationalError:
            self.create()
            cursor.execute("SELECT * FROM Host WHERE Instance=?", (instance,))
            _data = cursor.fetchone()

        try:
            return _data
        except Exception as error:
            return "Host Table Error: {}".format(
                error
            )
        finally:
            self.close(connection)

    def SSHKey(self, instance: str):
        connection, cursor = self.connection()

        try:
            cursor.execute("SELECT KEY FROM Host WHERE Instance=?", (instance,))
            _data = cursor.fetchone()
        except sqlite3.OperationalError:
            self.create()
            cursor.execute("SELECT KEY FROM Host WHERE Instance=?", (instance,))
            _data = cursor.fetchone()

        try:
            return _data
        except Exception as error:
            return "Host Table Error: {}".format(
                error
            )
        finally:
            self.close(connection)

    def searchInstanceUserRecord(self, instance: str):
        connection, cursor = self.connection()

        try:
            cursor.execute("SELECT USERNAME FROM Host WHERE Instance=?", (instance,))
            _data = str(cursor.fetchone()[0])
        except sqlite3.OperationalError:
            self.create()
            cursor.execute("SELECT USERNAME FROM Host WHERE Instance=?", (instance,))
            _data = str(cursor.fetchone()[0])

        try:
            return _data
        except Exception as error:
            return "Host DB Error: {}".format(
                error
            )
        finally:
            self.close(connection)
