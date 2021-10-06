#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

class API(Base):
    Generator = Blueprint("System", __name__)
    Route = Base.Route + "System"
    Methods = Base.Methods

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @staticmethod
    @Generator.route(Route + "/" + "Network", methods = Methods)
    def Network(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ Various Network Statistics

        - statistics: (NamedTuple)
            - bytes_sent:   Number of bytes sent.
            - bytes_recv:   Number of bytes received.
            - packets_sent: Number of packets sent.
            - packets_recv: Number of packets received.
            - errin:        Total number of errors while receiving.
            - errout:       Total number of errors while sending.
            - dropin:       Total number of incoming packets which were dropped.
            - dropout:      Total number of outgoing packets which were dropped
                            (always 0 on macOS and BSD).
            - tcp_connections:  Total number of TCP connections.
            - tcp_connections4: Total number of TCP connections over IPV4.
            - tcp_connections6: Total number of TCP connections over IPV6.
            - udp_connections:  Total number of UDP Connections.
            - udp4_connections: Total number of UDP connections over IPV4.
            - udp6_connections: Total number of UDP connections over IPV6.
            - public_ipv4:      Public IPv4 Address Pool.
            - private_ipv4:     Private IPv4 Address Pool.

        If *pernic* is True return the same information for every
        network interface installed on the system as a dictionary
        with network interface names as the keys and the namedtuple
        described above as the values.

        If *nowrap* is True it detects and adjust the numbers which overflow
        and wrap (restart from 0) and add "old value" to "new value" so that
        the returned numbers will always be increasing or remain the same,
        but never decrease.

        """

        statistics = getNetworkStatistics()
        conversion = 1000000 # --> Mega-Bytes (MB)

        bytes_sent          = int(statistics[0] / conversion)
        bytes_recv          = int(statistics[1] / conversion)
        packets_sent        = statistics[2]
        packets_recv        = statistics[3]
        errin               = statistics[4]
        errout              = statistics[5]
        dropin              = statistics[6]
        dropout             = statistics[7]

        try:
            tcp_connections         = getNetworkConnections(kind = "TCP".casefold()).__len__()
            tcp4_connections        = getNetworkConnections(kind = "TCP4".casefold()).__len__()
            tcp6_connections        = getNetworkConnections(kind = "TCP6".casefold()).__len__()

            udp_connections         = getNetworkConnections(kind = "UDP".casefold()).__len__()
            udp4_connections        = getNetworkConnections(kind = "UDP4".casefold()).__len__()
            udp6_connections        = getNetworkConnections(kind = "UDP6".casefold()).__len__()
        except Exception as Error:
            print("Caught Exception")
            print(str(Error.args))

            tcp_connections         = bytes("N/A".encode("UTF-8"))
            tcp4_connections        = bytes("N/A".encode("UTF-8"))
            tcp6_connections        = bytes("N/A".encode("UTF-8"))

            udp_connections         = bytes("N/A".encode("UTF-8"))
            udp4_connections        = bytes("N/A".encode("UTF-8"))
            udp6_connections        = bytes("N/A".encode("UTF-8"))

        try:
            public_ipv4 = subprocess.Popen(
                shlex.split("wget -q --output-document - https://ipecho.net/plain | awk '{print $1}'"),
                stdin = subprocess.DEVNULL,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                shell = False,
                text = True
            ).communicate()[0].strip().replace('"', "").split(" ")
        except Exception as Error:
            print("Caught Exception")
            print(str(Error.args))

            public_ipv4 = []
        try:
            command = [
                "ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'",
                "ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'"
            ]
            private_ipv4 = subprocess.Popen(
                shlex.split(command[0]),
                stdin = subprocess.DEVNULL,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                shell = False,
                text = True
            ).communicate()[0].strip().splitlines()
        except Exception as Error:
            print("Caught Exception: {}".format(Error))
            print("Exception caught during `private_ipv4 assignment")
            try:
                private_ipv4 = subprocess.Popen(
                    shlex.split(command[1]),
                    stdin = subprocess.DEVNULL,
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    shell = False,
                    text = True
                ).communicate()[0].strip().splitlines()
            except Exception as Error:
                print("Caught Exception: {}".format(Error))
                print("Exception (2) caught during `private_ipv4` assignment")
                private_ipv4 = bytes("N/A".encode("UTF-8"))
        try:
            connections = getNetworkConnections(kind = "All".casefold()).__len__()
        except Exception as Error:
            connections = bytes("N/A".encode("UTF-8"))

        _return = {
            "IO-Output" :   String(bytes_sent),
            "IO-Input" :    String(bytes_recv),
            "Packets-Output" :  String(packets_sent),
            "Packets-Input" :   String(packets_recv),
            "Packets-Input-Dropped" :   String(errin),
            "Packets-Output-Dropped" :  String(errout),
            "Error-Input" :     String(dropin),
            "Error-Output" :    String(dropout),
            "TCP-Connections" :         String(tcp_connections),
            "TCP-Connections-IPV4" :    String(tcp4_connections),
            "TCP-Connections-IPV6" :    String(tcp6_connections),
            "Connections" : String(connections),
            "UDP-Connections" : String(udp_connections),
            "UDP-Connections-IPV4" : String(udp4_connections),
            "UDP-Connections-IPV6" : String(udp6_connections),
            "Public-IP"       : String(public_ipv4)
        }

        if internal == False: return JTYPE(
            _return
        )

        elif internal == True: return _return
