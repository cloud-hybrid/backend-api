import os
import sqlite3

try:
    from Cloud.API.DB.Base import Database
except ModuleNotFoundError:
    from Base import Database

class Table(Database):
    """ Configuration.Table
    Table Layout:
    -------------
     - ID : Unique Record ID
    """
    def __init__(self, table: str = "Configuration", _file: str = "Cloud-API.db", *argv, **kwargs):
        self.table: str = table

        super().__init__(table = table)

    def create(self, override = False):
        connection, cursor = self.connection()

        if override == True:
            cursor.execute("DROP TABLE {};".format(
                self.table
            ))

        # --- Create Table --- #
        cursor.execute("""\
            CREATE TABLE IF NOT EXISTS {}
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Description NOT NULL,
            Path TEXT NOT NULL,
            Content TEXT NOT NULL,
            ServerID INTEGER,
            FOREIGN KEY(ServerID) REFERENCES Server(ID));
        """.format(self.table))

        self.addRecord("Mordhau-D-1-Game", "Mordhau's General Game Configuration File for the Dueling Server (1) Service", "/home/ubuntu/mordhau/Mordhau/Saved/Config/LinuxServer/Game.ini", MORDHAU_GAME_INI_DUELS, SERVERID)
        self.addRecord("Mordhau-D-1-Engine", "Mordhau's General Engine Configuration File for the Dueling Server (1) Service", "/home/ubuntu/mordhau/Mordhau/Saved/Config/LinuxServer/Engine.ini", MORDHAU_ENGINE_INI_DUELS, SERVERID)

        self.addRecord("Mordhau-C-1-Game", "Mordhau's General Game Configuration File for the Competitive Server (1) Service", "/home/ubuntu/mordhau-competitve/Mordhau/Saved/Config/LinuxServer/Game.ini", MORDHAU_GAME_INI_C_1, SERVERID)
        self.addRecord("Mordhau-C-1-Engine", "Mordhau's General Engine Configuration File for the Competitive Server (1) Service", "/home/ubuntu/mordhau-competitve/Mordhau/Saved/Config/LinuxServer/Engine.ini", MORDHAU_ENGINE_INI_C_1, SERVERID)

        self.addRecord("Mordhau-C-2-Game", "Mordhau's General Game Configuration File for the Competitive Server (2) Service", "/home/ubuntu/mordhau-competitve-2/Mordhau/Saved/Config/LinuxServer/Game.ini", MORDHAU_GAME_INI_C_2, SERVERID)
        self.addRecord("Mordhau-C-2-Engine", "Mordhau's General Game Configuration File for the Competitive Server (2) Service", "/home/ubuntu/mordhau-competitve-2/Mordhau/Saved/Config/LinuxServer/Engine.ini", MORDHAU_ENGINE_INI_C_2, SERVERID)

        self.save(connection)

    def addRecord(self, NAME: str, DESCRIPTION: str, PATH: str, CONTENT: str, SERVERID: str):
        connection, cursor = self.connection()

        statement = """INSERT INTO {TABLE} VALUES ({ID},"{NAME}","{DESCRIPTION}","{PATH}","{CONTENT}","{SERVERID}")""".format(
            TABLE = self.table,

            ID = "null",
            NAME = NAME,
            DESCRIPTION = DESCRIPTION,
            PATH = PATH,
            CONTENT = CONTENT,
            SERVERID = SERVERID
        )

        connection.execute(statement)

        self.save(connection)

    def search(self, ServerID: str):
        connection, cursor = self.connection()

        cursor.execute("SELECT * FROM Configuration WHERE ServerID=?", (ServerID,))
        _data = cursor.fetchall()

        try:
            return _data
        except Exception as error:
            return "Server DB Error: {}".format(
                error
            )
        finally:
            self.close(connection)

    def configuration(self, ServerID: str, file):
        connection, cursor = self.connection()

        cursor.execute("SELECT * FROM Configuration WHERE ServerID=? AND Name=?", (ServerID, file,))
        _data = cursor.fetchall()

        try:
            return _data
        except Exception as error:
            return "Server DB Error: {}".format(
                error
            )
        finally:
            self.close(connection)

def main():
    Table()
    print(Table().records)
    print(Table().total)

if __name__ == "__main__":
    main()