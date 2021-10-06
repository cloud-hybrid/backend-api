""" \
Host
----

"""

import os
import sys

from . import *

@Data(frozen = False, repr = True)
class Record:
    """\
    Database Record Type
    ====================

    Sub-Class(es):
    - Data (dataclass)
    - Object (namedTuple)
    """

    __slots__ = (
        "ID",
        "UUID",
        "Name",
        "Provider",
        "Local",
        "Public",
        "DNS",
        "CPU",
        "RAM",
        "Hypervisor",
        "Username",
        "Token",
        "Key",
        "SSH",
        "Organization"
    )

    ID: Integer
    UUID: String
    Name: String
    Provider: String
    Local: String
    Public: String
    DNS: String
    CPU: String
    RAM: String
    Hypervisor: String
    Username: String
    Token: String
    Key: String
    SSH: String
    Organization: String

    @staticmethod
    def instantiate(*data):
        try:
            return Record(*data[0])
        except Exception as Error:
            print("Record (Metal) Caught Exception: ", Error, "\n", "Data: {}".format(data[0])); return None

    @staticmethod
    def instantiations(*data):
        if len(data) == 1:
            try:
                return Record(*data)
            except Exception as Error:
                print("Record.instantiation (Metal) Caught Exception: ", Error, "\n", "Data: {}".format(data)); return None
        elif len(data) > 1:
            try:
                return [Record.instantiate(Item) for Item in data]
            except Exception as Error:
                print("Record.instantiations (Metal) Caught Exception: ", Error, "\n", "Data: {}".format(data)); return None
        else:
            if Table.total() == 0:
                return None
            else:
                raise ValueError("Record (Metal) *.instantiations Error: data cannot be empty")

class Table(Base):
    """ Host.Table """

    def __init__(self, table: str = "Host", *argv, **kwargs):
        super().__init__(table = table)

        self.table: str = table

        if "--dry-run" in argv or kwargs.get("dry", None) == True or kwargs.get("dry_run", None) == True:
            self.dry = True
        else:
            self.dry = False

    def create(self, override = False, initialize = False):
        connection, cursor = self.connection()

        if override == True:
            cursor.execute("DROP TABLE {};".format(
                self.table
            ))

        cursor.execute("""\
		CREATE TABLE "{}" (
            "ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "UUID"	TEXT NOT NULL UNIQUE,
            "Provider"	TEXT NOT NULL DEFAULT 'Cloud-Hybrid',
            "Name"	TEXT NOT NULL UNIQUE,
            "Local"	TEXT NOT NULL DEFAULT '169.0.0.0',
            "Public"	TEXT NOT NULL DEFAULT '24.118.115.252',
            "DNS"	TEXT NOT NULL DEFAULT 'N/A',
            "CPU"	INTEGER NOT NULL DEFAULT 0,
            "RAM"	INTEGER NOT NULL DEFAULT 0,
            "Hypervisor"	TEXT NOT NULL DEFAULT 'KVM',
            "Username"	TEXT NOT NULL DEFAULT 'bionic',
            "Token"	TEXT NOT NULL DEFAULT 'N/A',
            "Key"	TEXT NOT NULL DEFAULT 'N/A',
            "SSH"	TEXT NOT NULL DEFAULT 'N/A',
            "Organization"	TEXT NOT NULL DEFAULT 'Cloud-Hybrid'
        );
        """.format(self.table))

        self.save(connection)

    def updateIPAddresses(self):
        raise NotImplementedError

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

        connection, cursor = self.connection()
        statement = "DELETE FROM Host WHERE id=?"
        cursor.execute(statement, Singleton(ID).instance())
        self.save(connection)

    def insert(self, UUID: str, PROVIDER: str, NAME: str, LOCAL: str, PUBLIC: str, DNS: str, CPU: int, RAM: float, HYPERVISOR: str, USERNAME: str, TOKEN: str, KEY: str, SSH: str, ORGANIZATION: str, dry: bool = False):
        connection, cursor = self.connection()

        statement = """INSERT INTO {TABLE} VALUES ({ID},"{UUID}","{Name}","{Provider}","{Local}","{Public}","{DNS}",{CPU},{RAM},"{Hypervisor}","{Username}","{Token}","{Key}","{SSH}","{Organization}")""".format(
            TABLE = self.table,
            ID = "null",
            UUID = UUID,
            Provider = PROVIDER     if not None else "Cloud-Hybrid",
            Name = NAME             if not None else "N/A",
            Local = LOCAL           if not None else "169.0.0.1",
            Public = PUBLIC         if not None else "24.118.115.252",
            DNS = DNS               if not None else "N/A",
            CPU = CPU               if not None else 0,
            RAM = RAM               if not None else 0,
            Hypervisor = HYPERVISOR if not None else "KVM",
            Username = USERNAME     if not None else "bionic",
            Token = TOKEN           if not None else "N/A",
            Key = KEY               if not None else "N/A",
			SSH = SSH 				if not None else "N/A",
            Organization = ORGANIZATION if not None else "Cloud-Hybrid"
        )

        try: connection.execute(statement)
        except SQL.IntegrityError as Error:
            if "UNIQUE constraint failed" in "{}".format(Error):
                print("Metal Host Already Exists")
            else: raise Error
        finally:
            try:
                if self.dry == True or dry == True:
                    connection.rollback()
            except Exception as Error:
                print("Unknown Host (Metal) Exception: {}".format(
                    Error
                ))
            finally:
                self.save(connection)

    @classmethod
    def records(cls) -> [Record]:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT * FROM Host")
        records = Record.instantiations(*cursor.fetchall())
        Table("Host").close(connection)

        return records

    @classmethod
    def record(cls, instance: str) -> Record:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT * FROM Host WHERE UUID=?", Singleton(instance).instantiation())
        record = Record.instantiate(*cursor.fetchall())
        Table("Host").close(connection)

        return record

    @classmethod
    def search(cls, instance: str) -> Record:
        try:
            connection, cursor = Table("Host").connection()
            cursor.execute("SELECT * FROM Host WHERE UUID=?", Singleton(instance).instantiation())
            record = Record.instantiate(*cursor.fetchall())
            Table("Host").close(connection)

            return record

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

        except Exception as Error:
            print("SQL Lookup Error (Metal): {}".format(Error))

    @classmethod
    def getID(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT ID FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getSSHKey(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT KEY FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getUsername(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT USERNAME FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getProvider(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT PROVIDER FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getIP(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT Public FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getPrivateIP(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT Local FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getDNS(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT DNS FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getHypervisor(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT HYPERVISOR FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getName(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT Name FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

    @classmethod
    def getProvider(cls, instance: str) -> String:
        connection, cursor = Table("Host").connection()
        cursor.execute("SELECT PROVIDER FROM Host WHERE UUID=?", Singleton(instance).instance())
        data = cursor.fetchone()[0]
        Table("Host").close(connection)

        return data

def main():
    from pprint import pprint

    Tabular = Table()

    import uuid

    UUID = uuid.uuid4()

    try:
        Tabular.insert(
            UUID = UUID,
            NAME = "Ares",
            PROVIDER = "Cloud-Hybrid",
            LOCAL = "10.0.1.5",
            PUBLIC = "24.118.115.252",
            DNS = "N/A",
            CPU = 16,
            RAM = 1024 * 24,
            HYPERVISOR = "KVM",
            USERNAME = "snow",
            TOKEN = "N/A",
            SSH = """\
-----BEGIN OPENSSH PRIVATE KEY-----
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
/UU1PqbF8CbPAAAAAy4uLgECAwQFBgc=
-----END OPENSSH PRIVATE KEY-----\
""",
			KEY = "...",
            ORGANIZATION = "Cloud-Hybrid"
        )
        print(Tabular.total)

        pprint(Tabular.records())

    except SQL.IntegrityError as Error:
        if "UNIQUE constraint failed" in "{}".format(Error):
            print("Record Already Exists")
        else: raise Error


if __name__ == "__main__":
    main()