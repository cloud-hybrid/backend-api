"""

"""

import os
import uuid
import hashlib
import sqlite3

from sqlite3 import OperationalError

try:
    from Cloud.API.DB.Base import Database
except ModuleNotFoundError:
    from Base import Database

try:
    from Cloud.API.DB.Access import Table as Access
except ModuleNotFoundError:
    from Access import Table as Access

from pprint import pprint

from Cloud.API.DB.User import Card

from Cloud.API.DB.__secret__ import USERNAME, PASSWORD, EMAIL, DISPLAY



class Table(Database):
    """ Users.Table
    Table Layout:
    -------------
     - ID : Unique Record ID
    """
    def __init__(self, table = "User", *argv, **kwargs):
        self.table = table

        # self.create(override = False, initialize = False)

        super().__init__(table = table)

    def create(self, override = False, initialize = False):
        connection, cursor = self.connection()

        if override == True:
            cursor.execute("DROP TABLE {};".format(
                self.table
            ))

        # --- Create Table --- #
        cursor.execute("""CREATE TABLE IF NOT EXISTS {}
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL UNIQUE,
            Email TEXT NOT NULL UNIQUE,
            Display TEXT NOT NULL,
            Password TEXT NOT NULL,
            Firstname TEXT NOT NULL,
            Lastname TEXT NOT NULL,
            Joindate TEXT NOT NULL,
            Last_Login TEXT NOT NULL,
            Phone TEXT NOT NULL,
            Occupation TEXT NOT NULL,
            Biography TEXT NOT NULL,
            Avatar BLOB NOT NULL,
            AccessID INTEGER,
            FOREIGN KEY(AccessID) REFERENCES Access(ID));
        """.format(self.table))

        self.save(connection)

    def addRecord(self, USERNAME: str, EMAIL: str, DISPLAY: str, PASSWORD: str, FIRSTNAME: str, LASTNAME: str, PHONE: str, OCCUPATION: str, BIO: str, BLOB: str, ACCESSID: int):
        # self.create(override = False, initialize = False)

        connection, cursor = self.connection()

        _BLOB = memoryview(BLOB)

        statement = """INSERT INTO User VALUES ({ID},"{USERNAME}","{EMAIL}","{DISPLAY}","{PASSWORD}", "{FIRSTNAME}", "{LASTNAME}", datetime("now"), datetime("now"), "{PHONE}", "{OCCUPATION}", "{BIO}", ?, {ACCESSID})""".format(
            ID = "null",

            USERNAME = USERNAME,
            EMAIL = EMAIL,
            DISPLAY = DISPLAY,
            PASSWORD = PASSWORD,
            FIRSTNAME = FIRSTNAME,
            LASTNAME = LASTNAME,
            PHONE = PHONE,
            OCCUPATION = OCCUPATION,
            BIO = BIO,
            BLOB = "{}".format(_BLOB),
            ACCESSID = ACCESSID
        )
        connection.execute(statement, (_BLOB.tobytes(),))
        self.save(connection)

    def users(self, limit: int = 20):
        connection, cursor = self.connection()

        users = []

        for user in connection.execute("SELECT * FROM User LIMIT {}".format(limit)):
            users.append(
                User(data = {
                    "Display-Name" : user[3],
                    "Joined" : Database.formatDatetime(user[7]),
                    "Phone" : user[8],
                    "Biography" : user[10],
                    "Image" : user[11]
                })
            )

        return users

    def simpleCards(self, limit: int = 20):
        connection, cursor = self.connection()

        users = []

        for user in connection.execute("SELECT * FROM User LIMIT 20"):
            users.append(
                Card(data = {
                    "Display-Name" : user[3],
                    "Joined" : Database.formatDatetime(user[7]),
                    "Phone" : user[8],
                    "Biography" : user[10],
                    "Image" : user[11]
                })
            )

        self.close(connection)

        return users

    def search(self, username: str, password: str):
        connection, cursor = self.connection()

        cursor.execute("SELECT ID, username, password FROM User WHERE username=?", (username,))
        _id, _username, _password = cursor.fetchone()

        try:
            if _password == password:
                print("FOUND")
                return _id, _username
            else: 
                print("NULL")
                return "NULL"
        except Exception as e:
            print(e)
            print(e.args)
            print("NULL")
            return "NULL"
        finally:
            cursor.close()
            connection.close

    def last(self):
        connection, cursor = self.connection()

        cursor.execute("SELECT * FROM User ORDER BY ID DESC LIMIT 1;")

        _return = cursor.fetchone()[0]

        self.close(connection)

        return _return

def main():
    DB = Table()
    DB.create(override = True)
    _UID = uuid.uuid4()

    # FEMALE = Database.binarize(os.path.dirname(os.path.realpath(__file__)) + "/" + "{}".format("female.png"))
    
    MALE = DB.binarize(os.path.dirname(os.path.realpath(__file__)) + "/" + "{}".format("male.png"))
    Username = USERNAME

    ACL = Access()

    ACL_RECORD = ACL.addRecord(USERNAME)
    
    DB.addRecord(
        USERNAME = USERNAME,
        EMAIL = EMAIL,
        DISPLAY = DISPLAY,
        PASSWORD = PASSWORD,
        FIRSTNAME = "Jacob", 
        LASTNAME = "Sanders", 
        PHONE = "763-218-4129", 
        OCCUPATION = "Computer Engineer", 
        BIO = "N/A",
        BLOB = MALE,
        ACCESSID = ACL_RECORD)

    # for iterator in range(0, 10000):
    #     _UID = uuid.uuid4()
    #     print(iterator)
    #     if iterator % 2 == 0:
    #         DB.addRecord(
    #             USERNAME = "username-{}".format(_UID),
    #             EMAIL = "email-{}@cloudhybrid.io".format(_UID),
    #             DISPLAY = "display-{}".format(_UID),
    #             PASSWORD = hashlib.sha256(
    #                 "{}".format(
    #                     "password-{}".format(_UID)
    #                 ).encode("UTF-8")).hexdigest(),
    #             FIRSTNAME = "FIRST-{}".format(_UID), 
    #             LASTNAME = "LAST-{}".format(_UID), 
    #             PHONE = "1-111-555-0000", 
    #             OCCUPATION = "Engineer", 
    #             BIO = "Fun Engineer",
    #             BLOB = FEMALE)
    #     else: 
    #         DB.addRecord(
    #             USERNAME = "username-{}".format(_UID),
    #             EMAIL = "email-{}@cloudhybrid.io".format(_UID),
    #             DISPLAY = "display-{}".format(_UID),
    #             PASSWORD = hashlib.sha256(
    #                 "{}".format(
    #                     "password-{}".format(_UID)
    #                 ).encode("UTF-8")).hexdigest(),
    #             FIRSTNAME = "FIRST-{}".format(_UID), 
    #             LASTNAME = "LAST-{}".format(_UID), 
    #             PHONE = "1-111-555-0000", 
    #             OCCUPATION = "Analyst", 
    #             BIO = "Boring analyst",
    #             BLOB = MALE)

if __name__ == "__main__":
    main()