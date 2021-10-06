#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

"""

"""

import os
import sys
import sqlite3

sqlite3.enable_callback_tracebacks(True)

OperationalSQLException = sqlite3.OperationalError

from Cloud.API.Database.Initialize import Base, \
    dataclass, \
        Tuple, \
            Singleton, \
                String, \
                    Integer

from . import *

_SQLOperationalError = StandardError.SQLOperationalError

@Data(frozen = False, repr = True)
class Record(object):
    """ \
    Record

    A predefined, unfrozen `dataclass`

    - ID:           Integer(int)    - A unique identifier associated with a given record's
                                    table data.
    - UUID:         String(str)     - A unique identifier associated with a given record's
                                    associated service; the record's UUID is a unique value in
                                    the Server Table and is a sufficient look-up method.

    VPS [Array(Tuple)]
    ------------------
        - VPS-ID:       Integer(int)    - FOREIGN KEY("VPS-ID") REFERENCES "VPS"("ID"):
                                          A shared identifier associated with a given record's
                                          associated VPS ID.
        - VPS-UUID:     String(str)     - FOREIGN KEY("VPS-UUID") REFERENCES "VPS"("UUID")
                                          A shared identifier associated with a given record's
                                          associated VPS UUID; the VPS UUID is a unique value in
                                          the VPS Table and is a sufficient look-up method.
        - VPS-Name:     String(str)     - FOREIGN KEY("VPS-Name") REFERENCES "VPS"("Name"):
                                          A shared identifier associated with a given record's
                                          associated VPS Name; the VPS Name may not be a suitable
                                          record look-up method.

    Service [Array(Tuple)]
    ----------------------
        - Service-Name: String(str)     - The name of the service associated with a given Server record.
                                          Examples include "NGINX" or "Apache" for web-servers,
                                          "Mordhau Duels Server (1)", etc. for game-related servers.
                                          "Server" in the case of a database record relates to the
                                          process, otherwise named "service", that's running on a
                                          physical server, otherwise named "VPS" or "Instance". Lastly,
                                          the Service-Name attribute is often the "Description" found
                                          when analyzing the Service-File daemon or process.
        - Service-File: String(str)     - The file-name & extension of the file responsible for
                                          creating either a daemon or process(es) for a given service
                                          at VPS start-up, and repsonsible for management + logging
                                          of such the service. Examples include "NGINX.service" for
                                          linux, Systemd-based systems. The Service-File attribute should
                                          be unique as both a record attribute and file-system file.
        - Service-Path: String(str)     - The system's full-path, including the Service-File, associated
                                          with a given service. An example would include: "/etc/systemd/
                                          system/Mordhau.service" for a game-related server.

    Server [Array(Tuple)]
    ---------------------
        - Server-Name:  String(str)     - A name for the system's service that's suitable for managing &
                                          identifying such services through either a website CMS or
                                          dashboard, or perhaps an in-game server browser. The Server-Name
                                          attribute should contain the same name as "folder" or directory
                                          name where service-related files are stored; however, with dashes
                                          "-" characters superceded by " ", and unique characters if applicable.
        - Server-Type: String(str)      - In the case of a service (server) for a game such as Mordhau,
                                          the Server-Type attribute becomes "Gaming"; examples with a service
                                          such as MySQL or Flask, the Server-Type would be assigned "API".
        - Server-Directory: String(str) - The system's full path, root directory associated with the VPS'
                                          filesystem where service-related files & configurations are located;
                                          the Server-Name included, but without any special characters or
                                          spacing.

    Deployment [Array(Tuple)]
    -------------------------
        - Deployment-URL:   String(str) - A URL that contains an endpoint where automation or pipelines can
                                          trigger upon update(s). Often, in the context of Cloud-Hybrid,
                                          GitLab *.git-related URLs will be used.
        - Deployment-User:  String(str) - A Usertname that may be used when triggering a deployment for a
                                          given record's Deployment-URL; often times the Deployment-User
                                          attribute is derived in parallel to a Deployment-Token, and via
                                          a non-basic-auth authentication method.
        - Deployment-Token: String(str) - A Token associated with a given deployment trigger that's used as
                                          a method of validation and/or authentication.

    - Purpose       String(str)     - A generalized description or Key-Word that further adds uniqueness or
                                    identifiability to a given Server record.
    """

    __slots__ = (
        "UUID",
        "Name",
        "Type",
        "vpsID",
        "vpsUUID",
        "vpsName",
        "serviceName",
        "serviceFile",
        "servicePath",
        "serverDirectory",
        "deploymentURL",
        "deploymentUser",
        "deploymentToken",
        "purpose",

        "Table"
    )
    UUID: String
    Name: String
    Type: String
    vpsID: Integer
    vpsUUID: String
    vpsName: String
    serviceName: String
    serviceFile: String
    servicePath: String
    serverDirectory: String
    deploymentURL: String
    deploymentUser: String
    deploymentToken: String
    purpose: String

    Table: Dictionary

    @staticmethod
    def instantiate(*data) -> Dictionary:
        try:
            record = Record(*data[0], {})

            VPS, Service, Server, Deployment = {}, {}, {}, {}

            Server["Name"] = record.Name
            Server["Type"] = record.Type
            
            VPS["VPS-ID"] = record.vpsID
            VPS["VPS-UUID"] = record.vpsUUID
            VPS["VPS-Name"] = record.vpsName

            Service["Service-Name"] = record.serviceName
            Service["Service-File"] = record.serviceFile
            Service["Service-Path"] = record.servicePath

            Server["Server-Directory"] = record.serverDirectory

            Deployment["Deployment-URL"] = record.deploymentURL
            Deployment["Deployment-User"] = record.deploymentUser
            Deployment["Deployment-Token"] = record.deploymentToken

            record.Table = {
                **{
                    "UUID" : record.UUID,
                    "Name" : record.Name,
                    "Type" : record.Type,
                    "Purpose" : record.purpose
                }, **{
                    **{**VPS,       **Service},
                    **{**Server,    **Deployment}
                }
            }

            return record.Table

        except Exception as Error:
            print("Record (Server) Caught Exception [{}]: ".format(Error), Error, "\n", "Data: {}".format(data)); return None

    @staticmethod
    def instantiations(*data):
        if len(data) == 1:
            try:
                return Record.instantiate(*data)
            except Exception as Error:
                print("Record.instantiation (Server) Caught Exception: ", Error, "\n", "Data: {}".format(data)); return None
        elif len(data) > 1:
            try:
                return [Record.instantiate(Item) for Item in data]
            except Exception as Error:
                print("Record.instantiations (Server) Caught Exception: ", Error, "\n", "Data: {}".format(data)); return None
        else:
            if Table.total() == 0:
                return None
            else:
                raise ValueError("Record (Server) *.instantiations Error: data cannot be empty")

    # def __repr__(self) -> String:
    #     return Dedentation("""
    #         DESCRIPTOR: {vpsID}
    #         - Hash-Key: vpsID
    #         - Dot-Product: Object.vpsID
    #         DESCRIPTOR: {vpsUUID}
    #         - Hash-Key: vpsUUID
    #         - Dot-Product: Object.vpsUUID
    #         DESCRIPTOR: {vpsName}
    #         - Hash-Key: vpsName
    #         - Dot-Product: Object.vpsName
    #         DESCRIPTOR: {serviceName}
    #         - Hash-Key: serviceName
    #         - Dot-Product: Object.serviceName
    #         DESCRIPTOR: {serviceFile}
    #         - Hash-Key: serviceFile
    #         - Dot-Product: Object.serviceFile
    #         DESCRIPTOR: {servicePath}
    #         - Hash-Key: servicePath
    #         - Dot-Product: Object.servicePath
    #         DESCRIPTOR: {serverName}
    #         - Hash-Key: serverName
    #         - Dot-Product: Object.serverName
    #         DESCRIPTOR: {serverType}
    #         - Hash-Key: serverType
    #         - Dot-Product: Object.serverType
    #         DESCRIPTOR: {serverDirectory}
    #         - Hash-Key: serverDirectory
    #         - Dot-Product: Object.serverDirectory
    #         DESCRIPTOR: {deploymentURL}
    #         - Hash-Key: deploymentURL
    #         - Dot-Product: Object.deploymentURL
    #         DESCRIPTOR: {deploymentUser}
    #         - Hash-Key: deploymentUser
    #         - Dot-Product: Object.deploymentUser
    #         DESCRIPTOR: {deploymentToken}
    #         - Hash-Key: deploymentToken
    #         - Dot-Product: Object.deploymentToken
    #     """.format(
    #             vpsID = self.vpsID,
    #             vpsUUID = self.vpsUUID,
    #             vpsName = self.vpsName,
    #             serviceName = self.serviceName,
    #             serviceFile = self.serviceFile,
    #             servicePath = self.servicePath,
    #             serverName = self.serverName,
    #             serverType = self.serverType,
    #             serverDirectory = self.serverDirectory,
    #             deploymentURL = self.deploymentURL,
    #             deploymentUser = self.deploymentUser,
    #             deploymentToken = self.deploymentToken
    # ).strip().replace("        ", "")

class Table(Base):
    """ Server.Table """

    def __init__(self, table = "Server", *argv, **kwargs):
        self.table = table
        super().__init__(table = table)

    @classmethod
    def UUID(cls): return super().UUID()

    def create(self, override = False, initialize = False):
        connection, cursor = self.connection()

        if override == True:
            cursor.execute("DROP TABLE {};".format(
                self.table
            ))

        # --- Create Table --- #
        cursor.execute("""CREATE TABLE "{}" (
        CREATE TABLE "Server" (
            "UUID"	TEXT NOT NULL UNIQUE,
            "Name"	TEXT NOT NULL PRIMARY KEY UNIQUE,
            "Type"	TEXT NOT NULL,
            "VPS-ID"	INTEGER NOT NULL,
            "VPS-UUID"	TEXT NOT NULL,
            "Service-Name"	TEXT,
            "Service-File"	TEXT,
            "Service-Path"	TEXT,
            "Server-Directory"	TEXT NOT NULL,
            "Deployment-URL"	TEXT,
            "Deployment-User"	TEXT,
            "Deployment-Token"	TEXT,
            "Purpose"	TEXT,
            FOREIGN KEY("VPS-ID") REFERENCES "VPS"("ID"),
            FOREIGN KEY("VPS-UUID") REFERENCES "VPS"("UUID"),
            FOREIGN KEY("VPS-Name") REFERENCES "VPS"("Name")
        );
        """.format(self.table))

        self.save(connection)

    def insert(self,
        serverName: String = None,
        serverType: String = None,
        vpsUUID: String = None,
        vpsName: String = None,
        serviceName: String = None,
        serviceFile: String = None,
        servicePath: String = None,
        serverDirectory: String = None,
        deploymentURL: String = None,
        deploymentUser: String = None,
        deploymentToken: String = None,
        purpose: String = None):
        """ ...
        ...
        """
        connection, cursor = self.connection()

        statement = """INSERT INTO {TABLE} VALUES ("{_Name}","{_Type}","{_UUID},{_vpsID},"{_vpsUUID}","{_vpsName}","{_serviceName}","{_serviceFile}","{_servicePath}","{_serverDirectory}","{_deploymentURL}","{_deploymentUser}","{_deploymentToken}","{_purpose}")""".format(
            TABLE   = self.table,

            _Name         = serverName if not None else "N/A",
            _Type         = serverType if not None else "N/A",

            _UUID   = "SERVER" + "-" + Table.UUID(),

            _vpsID      = vpsID,
            _vpsUUID    = vpsUUID,
            _vpsName    = vpsName,

            _serviceName = serviceName if not None else "null",
            _serviceFile = serviceFile if not None else "null",
            _servicePath = servicePath if not None else "null",

            _serverDirectory    = serverDirectory if not None else "N/A",

            _deploymentURL      = deploymentURL if not None else "N/A",
            _deploymentUser     = deploymentUser if not None else "N/A",
            _deploymentToken    = deploymentToken if not None else "N/A",

            _purpose    = purpose if not None else "N/A"
        )

        try: connection.execute(statement)
        except sqlite3.IntegrityError as Error:
            if "UNIQUE constraint failed" in "{}".format(Error):
                print("Server Record Already Exists")
                print("Error: {}".format(Error))
            else:
                raise Error
        finally:
            try:
                if self.dry == True or dry == True:
                    connection.rollback()
            except Exception as Error:
                print("Unknown Server SQL Exception: {}".format(
                    Error
                ))
            finally:
                self.save(connection)

    @classmethod
    def record(cls, uuid: str) -> Record:
        connection, cursor = Table("Server").connection()
        cursor.execute("SELECT * FROM Server WHERE UUID=?", Singleton(uuid).instantiation())
        record = Record.instantiate(*cursor.fetchall())
        Table("Server").close(connection)

        return record

    @classmethod
    def records(cls) -> [Record]:
        connection, cursor = Table("Server").connection()
        cursor.execute("SELECT * FROM Server")
        records = Record.instantiations(*cursor.fetchall())
        Table("Server").close(connection)

        return records if type(records) == type([]) else [records]

    @classmethod
    def search(cls, uuid: String) -> Record:
        try:
            connection, cursor = Table("Server").connection()
            cursor.execute("SELECT * FROM Server WHERE UUID=?", Singleton(instance).instantiation())
            data = Record.instantiate(*cursor.fetchall())
            Table("Server").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

        except Exception as Error:
            print("SQL Lookup Error (Server): {}".format(Error))

    @classmethod
    def getName(cls, uuid: String) -> String:
        try:
            connection, cursor = Table("Server").connection()
            cursor.execute("SELECT Name FROM Server WHERE UUID=?", Singleton(uuid).instance())
            data = cursor.fetchone()[0]
            Table("Server").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error