import os
import sqlite3

try:
    from Cloud.API.DB.Base import Database
except ModuleNotFoundError:
    from Base import Database

class Table(Database):
    """ Access.Table
    Table Layout:
    -------------
     - ID : Unique Record ID
     - Dashboard : Primary Dashboard Page Access
     - Control : Server Controls Access
     - Configuration : Server Configurations Access
     - Statistics : Server Statistics Access
     - Billing : Cloud-Hybrid Billing Access
     - AWSLink : Cloud-Hybrid AWS Access
     - Servers : Server-List Access
     - PEM : Server SSH Key Access
     - Documentation : General Documentation Access
     - Development : Development-related Page Access
     - Production : Production-related Page Access
     - Mordhau : Mordhau Server(s) Access
     - Squad : Squad Server(s) Access
     - Rust : Rust Server(s) Access
     - ARMA : ARMA Server(s) Access
     - SFTP : Server SFTP Access
     - Storage : Storage Access
     - _All : Root, all Access
     - Username : Associated ACL-Username
    """

    def __init__(self, table: str = "Access", *argv, **kwargs):        
        self.table: str = table

        super().__init__(table = table)

    def create(self, override = False, initialize = False):
        connection, cursor = self.connection()

        if override == True:
            cursor.execute("DROP TABLE IF EXISTS Access;")

        # --- Create Table --- #
        cursor.execute("""CREATE TABLE IF NOT EXISTS Access
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Dashboard INTEGER NOT NULL,
            Control INTEGER NOT NULL,
            Configuration INTEGER NOT NULL,
            Statistics INTEGER NOT NULL,
            Billing INTEGER NOT NULL,
            AWSLink INTEGER NOT NULL,
            Servers INTEGER NOT NULL,
            PEM INTEGER NOT NULL,
            Documentation INTEGER NOT NULL,
            Development INTEGER NOT NULL,
            Production INTEGER NOT NULL,
            Mordhau INTEGER NOT NULL,
            Squad INTEGER NOT NULL,
            Rust INTEGER NOT NULL,
            ARMA INTEGER NOT NULL,
            SFTP INTEGER NOT NULL,
            Storage INTEGER NOT NULL,
            _All INTEGER NOT NULL,
            Username TEXT NOT NULL UNIQUE);
        """)

        self.save(connection)

    def addRecord(self,
        Username: str,
        Dashboard: bool = True,
        Control: bool = True,
        Configuration: bool = True,
        Statistics: bool = True,
        Billing: bool = True,
        AWSLink: bool = True,
        Servers: bool = True,
        PEM: bool = True,
        Documentation: bool = True,
        Development: bool = True,
        Production: bool = True,
        Mordhau: bool = True,
        Squad: bool = True,
        Rust: bool = True,
        ARMA: bool = True,
        SFTP: bool = True,
        Storage: bool = True,
        ALL: bool = True):
        connection, cursor = self.connection()

        statement = """INSERT INTO Access VALUES ({ID},{Dashboard},{Control},{Configuration},{Statistics},{Billing},{AWSLink},{Servers},{PEM},{Documentation},{Development},{Production},{Mordhau},{Squad},{Rust},{ARMA},{SFTP},{Storage},{ALL},"{Username}")""".format(
            ID = "null",
            Dashboard = int(Dashboard),
            Control = int(Control),
            Configuration = int(Configuration),
            Statistics = int(Statistics),
            Billing = int(Billing),
            AWSLink = int(AWSLink),
            Servers = int(Servers),
            PEM = int(PEM), 
            Documentation = int(Documentation), 
            Development = int(Development),
            Production = int(Production), 
            Mordhau = int(Mordhau), 
            Squad = int(Squad), 
            Rust = int(Rust), 
            ARMA = int(ARMA),
            SFTP = int(SFTP),
            Storage = int(Storage),
            ALL = int(ALL),
            Username = Username
        )

        connection.execute(statement)

        self.save(connection)

        return self.last()

    def search(self, control: str, access: bool):
        connection, cursor = self.connection()

        try:
            cursor.execute("SELECT * FROM {} WHERE {}=?".format(
                self.table, control
            ), (int(access),))
            _data = cursor.fetchone()
        except sqlite3.OperationalError:
            self.create()
            cursor.execute("SELECT * FROM {} WHERE Instance=?".format(
                self.table, control
            ), (int(access),))
            _data = cursor.fetchone()

        try:
            return _data
        except Exception as error:
            return "Server DB Error: {}".format(
                error
            )
        finally:
            self.close(connection)

    def last(self):
        connection, cursor = self.connection()

        cursor.execute("SELECT * FROM Access ORDER BY ID DESC LIMIT 1;")

        _return = cursor.fetchone()[0]

        self.close(connection)

        return _return

def main():
    Table()
    Table().create(override = True)

if __name__ == "__main__":
    main()