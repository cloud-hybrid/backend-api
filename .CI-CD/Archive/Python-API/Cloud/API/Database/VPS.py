""" Database
------------
...
"""

from . import *

_SQLOperationalError = StandardError.SQLOperationalError

@Data(frozen = False, repr = True)
class Record:
    """ Record

    A predefined, unfrozen `dataclass` consisting of a given structure:
        - ID:           String(str)     - Description
        - Instance:     String(str)     - Description
        - Provider:     String(str)     - Description
        - Name:         String(str)     - Description
        - IP:           String(str)     - Description
        - Locality:     String(str)     - Description
        - DNS:          String(str)     - Description
        - Internal:     String(str)     - Description
        - CPU:          Integer(int)    - Description
        - RAM:          Union(float|int)
                                        - Description
        - Hypervisor:   String(str)     - Description
        - Username:     String(str)     - Description
        - Token:        String(str)     - Description
        - Secret:       String(str)     - Description
        - SSH_Key:      String(str)     - Description
        - Region:       String(str)     - Description
        - Output:       String(str)     - Description
        - Account:      String(str)     - Description
        - Console:      String(str)     - Description
        - Organization: String(str)     - Description

        - module:       Python(str)     - Desciption
        - rename:       Boolean(bool)   - Description

    """

    __slots__ = (
        "ID",
        "UUID",
        "Name",
        "AWSAccount",
        "AWSToken",
        "AWSKey",
        "AWSOutput",
        "AWSRegion",
        "AWSConsole",
        "PublicIP",
        "PublicDomain",
        "PrivateIP",
        "PrivateDomain",
        "SSHUsername",
        "SSHPublicKey",
        "SSHPrivateKey",
        "HardwareCPU",
        "HardwareRAM",
        "HardwareHypervisor",
        "Provider",
        "Organization",
        "HostID",
        "HostUUID",
        "HostName",
        "Table"
    )

    ID: Integer
    UUID: String
    Name: String
    AWSAccount: String
    AWSToken: String
    AWSKey: String
    AWSOutput: String
    AWSRegion: String
    AWSConsole: String
    PublicIP: String
    PublicDomain: String
    PrivateIP: String
    PrivateDomain: String
    SSHUsername: String
    SSHPublicKey: String
    SSHPrivateKey: String
    HardwareCPU: String
    HardwareRAM: String
    HardwareHypervisor: String
    Provider: String
    Organization: String
    HostID: String
    HostUUID: String
    HostName: String

    Table: Dictionary

    @staticmethod
    def instantiate(*data) -> Dictionary:
        try:
            record = Record(*data[0], {})

            Pool, AWS, Hardware, SSH, Host = {}, {}, {}, {}, {}

            AWS["AWS-Account"]      = record.AWSAccount
            AWS["AWS-Access-Token"] = record.AWSToken
            AWS["AWS-Access-Key"]   = record.AWSKey
            AWS["AWS-Output"]       = record.AWSOutput
            AWS["AWS-Region"]       = record.AWSRegion
            AWS["AWS-Console"]      = record.AWSConsole

            SSH["SSH-Username"]     = record.SSHUsername
            SSH["SSH-Public-Key"]   = record.SSHPublicKey
            SSH["SSH-Private-Key"]  = record.SSHPrivateKey

            Hardware["Hardware-Hypervisor"] = record.HardwareHypervisor
            Hardware["Hardware-CPU"]        = record.HardwareCPU
            Hardware["Hardware-RAM"]        = record.HardwareRAM

            Pool["Networking-Public-IP"]        = record.PublicIP
            Pool["Networking-Private-IP"]       = record.PrivateIP
            Pool["Networking-Public-Domain"]    = record.PublicDomain
            Pool["Networking-Private-Domain"]   = record.PrivateDomain

            Host["Host-ID"]         = record.HostID
            Host["Host-UUID"]       = record.HostUUID
            Host["Host-Name"]       = record.HostName

            record.Table = {
                **{
                    "ID"   : record.ID,
                    "Name" : record.Name,
                    "UUID" : record.UUID,
                    "Provider" : record.Provider,
                    "Organization" : record.Organization
                }, **{
                    **{**Pool, **Hardware},
                    **{**SSH,  **AWS},
                    **Host
                }
            }

            return record.Table

        except Exception as Error:
            print("Record (VPS) Caught Exception: ", Error, "\n", "Data: {}".format(data)); return None

    @staticmethod
    def instantiations(*data):
        if len(data) == 1:
            try:
                return Record.instantiate(*data)
            except Exception as Error:
                print("Record.instantiation (VPS) Caught Exception: ", Error, "\n", "Data: {}".format(data)); return None
        elif len(data) > 1:
            try:
                return [Record.instantiate(Item) for Item in data]
            except Exception as Error:
                print("Record.instantiations (VPS) Caught Exception: ", Error, "\n", "Data: {}".format(data)); return None
        else:
            if Table.total() == 0:
                return None
            else:
                raise ValueError("Record (VPS) *.instantiations Error: data cannot be empty")

    def __repr__(self) -> String:
        return Dedentation("""\
        ID: {ID}
        - Hash-Key: ID
        - Dot-Product: Object.ID
        Name: {Name}
        - Hash-Key: Name
        - Dot-Product: Object.Name
        UUID: {UUID}
        - Hash-Key: UUID
        - Dot-Product: Object.UUID
        Provider: {Provider}
        - Hash-Key: Provider
        - Dot-Product: Object.Provider
        Host ID: {HostID}
        - Hash-Key: Host-ID
        - Dot-Product: Object.HostID
        Host UUID: {HostUUID}
        - Hash-Key: Host-UUID
        - Dot-Product: Object.HostUUID
        Host Name: {HostName}
        - Hash-Key: Host-Name
        - Dot-Product: Object.HostName
        Organization: {Organization}
        - Hash-Key: Organization
        - Dot-Product: Object.Organization
        Public IP: {PublicIP}
        - Hash-Key: Networking-Public-IP
        - Dot-Product: Object.PublicIP
        Private IP: {PrivateIP}
        - Hash-Key: Networking-Private-IP
        - Dot-Product: Object.PrivateIP
        Domain Name: {DomainName}
        - Hash-Key: Networking-Public-Domain
        - Dot-Product: Object.PublicDomain
        Hostname: {Hostname}
        - Hash-Key: Networking-Private-Domain
        - Dot-Product: Object.PrivateDomain
        Hypervisor: {Hypervisor}
        - Hash-Key: Hardware-Hypervisor
        - Dot-Product: Object.HardwareHypervisor
        CPU Count: {CPUCount}
        - Hash-Key: Hardware-CPU
        - Dot-Product: Object.HardwareCPU
        SSH Username: {SSHUsername}
        - Hash-Key: SSH-Username
        - Dot-Product: Object.SSHUsername
        Account (AWS): {AWSAccount}
        - Hash-Key: AWS-Acccount
        - Dot-Product: Object.AWSAccount
        Token (AWS): {AWSToken}
        - Hash-Key: AWS-Access-Token
        - Dot-Product: Object.AWSToken
        Key (AWS): {AWSKey}
        - Hash-Key: AWS-Access-Key
        - Dot-Product: Object.AWSKey
        Output (AWS): {AWSOutput}
        - Hash-Key: AWS-Output
        - Dot-Product: Object.AWSOutput
        Region (AWS): {AWSRegion}
        - Hash-Key: AWS-Region
        - Dot-Product: Object.AWSRegion
        Console (AWS): {AWSConsole}
        - Hash-Key: AWS-Console
        - Dot-Product: Object.AWSConsole
        """.format(
                ID = self.ID,
                Name = self.Name,
                UUID = self.UUID,
                Provider = self.Provider,
                Organization = self.Organization,
                PublicIP = self.PublicIP,
                PrivateIP = self.PrivateIP,
                DomainName = self.PublicDomain,
                Hostname = self.PrivateDomain,
                Hypervisor = self.HardwareHypervisor,
                CPUCount = self.HardwareCPU,
                SSHUsername = self.SSHUsername,
                AWSAccount = self.AWSAccount,
                AWSToken = self.AWSToken,
                AWSKey = self.AWSKey,
                AWSOutput = self.AWSOutput,
                AWSRegion = self.AWSRegion,
                AWSConsole = self.AWSConsole,
                HostID  = self.HostID,
                HostName = self.HostName,
                HostUUID = self.HostUUID
            )
        ).strip().replace("        ", "")

class Table(Base):
    """ VPS.Table """

    def __init__(self, table: String = "VPS", *argv, **kwargs):
        self.table: String = table

        super().__init__(table = table)

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
CREATE TABLE "VPS-Instance" (
	"Name"	TEXT NOT NULL UNIQUE,
	"UUID"	TEXT NOT NULL UNIQUE,
	"Account"	TEXT NOT NULL DEFAULT 'N/A',
	"Token"	TEXT NOT NULL DEFAULT 'N/A',
	"Key"	TEXT NOT NULL DEFAULT 'N/A',
	"Output"	TEXT NOT NULL DEFAULT 'JSON',
	"Geography"	TEXT NOT NULL DEFAULT 'US-Central',
	"Console"	TEXT NOT NULL DEFAULT 'https://cloudhybrid.signin.aws.amazon.com/console',
	"Public-IP"	TEXT NOT NULL DEFAULT 'N/A',
	"Private-IP"	TEXT NOT NULL DEFAULT 'N/A',
	"Public-Domain"	TEXT NOT NULL DEFAULT 'N/A',
	"Private-Domain"	TEXT NOT NULL DEFAULT 'localhost',
	"Local-Host"	TEXT NOT NULL DEFAULT '127.0.0.1',
	"Link-Local"	TEXT NOT NULL DEFAULT '169.254.169.250',
	"SSH-Username"	TEXT NOT NULL DEFAULT 'bionic',
	"SSH-Public-Key"	TEXT NOT NULL DEFAULT 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKQ1gWPAUmUH2GCFPc4kSW42YygYlDcp7Z5M/siVrBwVFAdZ0d1zHvsCrV9r3xkx1uKmaS+FvJMTYWtfoWtqJAeO0Pn0rpiufEwaA0OY847S2YL7bF93SbTaCGY0dhrvZ7Wwu+pMCq7Vo0RmQXBslmPQXa6h6wZLNM+Us3HNtfy0g9ImUQIFQ6KlC8V4Ke0BIlr4kA2wtf25i6GqelYGQTZ8pjxPyZJPMyWy+qhrKGzA+bDpHp/EGES6j4EqfHm2IU2SWVC+22owZR8vr1X7kadJsK07CWg1gqMuIuxk7UiEkwIzJdlYTqHJsIW2OocHdiLCsz0PhDoXmihTcLwcd2LBhpgow1O4qQifB3WwGKhyiTNy1WB42U/1NOYdypOcKZVGm3J/P9DcvBk6SYaffhsNlHGWyr+z2HcfMjJggEQCXhwV9kRsmR6TkRoisVndajXDlN38eOynUJteAYmqrrO6o89ysaB2+LkP29JHUSe5Mt+seacImgx4N4x5R8xAM=',
	"SSH-Private-Key"	TEXT NOT NULL DEFAULT '-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
',
	"Hardware-CPU"	INTEGER NOT NULL DEFAULT 0,
	"Hardware-RAM"	INTEGER NOT NULL DEFAULT 0,
	"Hardware-Hypervisor"	TEXT NOT NULL DEFAULT 'KVM',
	"Provider"	TEXT NOT NULL DEFAULT 'Cloud-Hybrid',
	"Organization"	TEXT NOT NULL DEFAULT 'Cloud-Hybrid',
	PRIMARY KEY("Name")
) WITHOUT ROWID;
            );
        """.format(
            _Table              = self.table,
            _AWS_Account        = DefaultAWSAccount,
            _AWS_Token          = DefaultAWSAccessID,
            _AWS_Key            = DefaultAWSAccessKey,
            _AWS_Output         = DefaultAWSOutput,
            _AWS_Region         = DefaultAWSRegion,
            _AWS_Console        = DefaultAWSConsole,
            _SSH_PUBLIC_KEY     = DefaultSSHPublicKey,
            _SSH_PRIVATE_KEY    = DefaultSSHPrivateKey
        ))

        self.save(connection)

    def updateIPAddresses(self):
        raise NotImplementedError

    def insert(self,
        UUID: String,
        NAME: String,
        AWSACCOUNT:     str = None,
        AWSTOKEN:       str = None,
        AWSKEY:         str = None,
        AWSOUTPUT:      str = None,
        AWSREGION:      str = None,
        AWSCONSOLE:     str = None,
        PUBLICIP:       str = None,
        PUBLICDOMAIN:   str = None,
        PRIVATEIP:      str = None,
        PRIVATEDOMAIN:  str = None,
        SSHUSERNAME:    str = None,
        SSHPUBLICKEY:   str = None,
        SSHPRIVATEKEY:  str = None,
        HARDWARECPU:    int = None,
        HARDWARERAM:        float   = None,
        HARDWAREHYPERVISOR: String     = None,
        PROVIDER:       str = None,
        ORGANIZATION:   str = None):
        """ ...
        ...
        """
        connection, cursor = self.connection()

        statement = """INSERT INTO {TABLE} VALUES ({ID},"{_UUID}","{Name}","{Account}","{Token}","{Key}","{Output}","{Region}","{Console}","{IP}","{Domain}","{LAN}","{Localhost}","{SSHUsername}","{SSHPublicKey}","{SSHPrivateKey}",{CPU},{RAM},"{Hypervisor}","{Provider}","{Organization}")""".format(
            TABLE = self.table,
            ID = "null",
            _UUID   = UUID                  if not None else "N/A",
            Name    = NAME                  if not None else "N/A",
            Account = AWSACCOUNT            if not None else "N/A",
            Token   = AWSTOKEN              if not None else "N/A",
            Key     = AWSKEY                if not None else "N/A",
            Output  = AWSOUTPUT             if not None else "N/A",
            Region  = AWSREGION             if not None else "N/A",
            Console = AWSCONSOLE            if not None else "N/A",
            IP      = PUBLICIP              if not None else "N/A",
            Domain  = PUBLICDOMAIN          if not None else "N/A",
            LAN     = PRIVATEIP             if not None else "N/A",
            Localhost = PRIVATEDOMAIN       if not None else "N/A",
            SSHUsername = SSHUSERNAME       if not None else "N/A",
            SSHPublicKey = SSHPUBLICKEY     if not None else "N/A",
            SSHPrivateKey = SSHPRIVATEKEY   if not None else "N/A",
            CPU = HARDWARECPU               if not None else "N/A",
            RAM = HARDWARERAM               if not None else "N/A",
            Hypervisor = HARDWAREHYPERVISOR if not None else "N/A",
            Provider = PROVIDER             if not None else "N/A",
            Organization = ORGANIZATION     if not None else "N/A"
        )

        try: connection.execute(statement)
        except sqlite3.IntegrityError as Error:
            if "UNIQUE constraint failed" in "{}".format(Error):
                print("VPS Instance Already Exists")
            else: raise Error
        finally:
            try:
                if self.dry == True or dry == True:
                    connection.rollback()
            except Exception as Error:
                print("Unknown VPS Exception: {}".format(
                    Error
                ))
            finally:
                self.save(connection)

    @classmethod
    def record(cls, instance: str) -> Record:
        connection, cursor = Table("VPS").connection()
        cursor.execute("SELECT * FROM VPS WHERE UUID=?", Singleton(instance).instantiation())
        record = Record.instantiate(*cursor.fetchall())
        Table("VPS").close(connection)

        return record

    @classmethod
    def records(cls) -> [Record]:
        connection, cursor = Table("VPS").connection()
        cursor.execute("SELECT * FROM VPS")
        records = Record.instantiations(*cursor.fetchall())
        Table("VPS").close(connection)

        return records if type(records) == type([]) else [records]

    @classmethod
    def search(cls, instance: String) -> Record:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT * FROM VPS WHERE UUID=?", Singleton(instance).instantiation())
            data = Record.instantiate(*cursor.fetchall())
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

        except Exception as Error:
            print("SQL Lookup Error (VPS): {}".format(Error))

    @classmethod
    def getID(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT ID FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getRecordViaID(cls, ID: Integer) -> Record:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT * FROM VPS WHERE ID=?", Singleton(ID).instantiation())
            data = Record.instantiate(*cursor.fetchall())
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

        except Exception as Error:
            print("SQL Lookup Error (VPS): {}".format(Error))

    @classmethod
    def getSSHPrivateKey(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT SSH-Private-Key FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getSSHPublicKey(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT SSH-Public-Key FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getSSHUsername(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT SSH-Username FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getProvider(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Provider FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getPublicIP(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Public-IP FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getPublicDomain(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Public-Domain FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getPrivateIP(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Private-IP FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getPrivateDomain(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Private-Domain FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getHardwareHypervisor(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Hardware-Hypervisor FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getHardwareCPU(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Hardware-CPU FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getHardwareRAM(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Hardware-RAM FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getName(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Name FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getOrganization(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Organization FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

    @classmethod
    def getConsole(cls, instance: String) -> String:
        try:
            connection, cursor = Table("VPS").connection()
            cursor.execute("SELECT Console FROM VPS WHERE Instance=?", Singleton(instance).instance())
            data = cursor.fetchone()[0]
            Table("VPS").close(connection)
            return data

        except OperationalSQLException as Error:
            _error = _SQLOperationalError(Error)
            _error.STDERR()
            return _error

def main():
    from pprint import pprint

    Tabular = Table()

    try:
        Tabular.insert(
            INSTANCE = "i-03e647bf27b006b2f",
            PROVIDER = "AWS",
            NAME = "Mordhau-Server-1",
            IP = "3.90.96.219",
            _IP = "172.31.27.50",
            DNS = "ec2-3-90-96-219.compute-1.amazonaws.com",
            _DNS = "ip-172-31-27-50.ec2.internal",
            CPU = 4,
            RAM = 10,
            HYPERVISOR = "HVM",
            USERNAME = "ubuntu",
            TOKEN = "AKIA6J4BIWNGXAF6DJCR",
            SECRET = "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",
            KEY = "...",
            REGION = "US-East-1",
            OUTPUT = "JSON",
            ACCOUNT = "Cloud-Hybrid",
            CONSOLE = "https://cloudhybrid.signin.aws.amazon.com/console",
            ORGANIZATION = "20th Regiment of Foot"
        )
    except sqlite3.IntegrityError as Error:
        if "UNIQUE constraint failed" in "{}".format(Error):
            print("VPS Instance Already Exists")
        else: raise Error

    print(Tabular.search("i-03e647bf27b006b2f"))
    print(Tabular.search("i-NULL"))
    print(Tabular.search("i-03e647bf27b006b2f").Account)

    print(type(Tabular.search("i-03e647bf27b006b2f")))
    print(type(Tabular.search("i-03e647bf27b006b2f").Name))

    print(Tabular.getConsole("i-03e647bf27b006b2f"))
    print(Tabular.getDNS("i-03e647bf27b006b2f"))
    print(Tabular.getHypervisor("i-03e647bf27b006b2f"))
    print(Tabular.getID("i-03e647bf27b006b2f"))
    print(Tabular.getIP("i-03e647bf27b006b2f"))
    print(Tabular.getName("i-03e647bf27b006b2f"))
    print(Tabular.getOrganization("i-03e647bf27b006b2f"))
    print(Tabular.getPrivateDNS("i-03e647bf27b006b2f"))
    print(Tabular.getPrivateIP("i-03e647bf27b006b2f"))
    print(Tabular.getProvider("i-03e647bf27b006b2f"))
    print(Tabular.getSSHKey("i-03e647bf27b006b2f"))
    print(Tabular.getUsername("i-03e647bf27b006b2f"))

    print(Tabular.total)

    pprint(Tabular.records())

if __name__ == "__main__":
    main()