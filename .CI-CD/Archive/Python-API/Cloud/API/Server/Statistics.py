""" Statistics
==============

Various server hardware statistics, accessible via REST-based endpoints.

"""

from . import *

class System(Base):
    Generator = Blueprint("System", __name__)
    Route = Base.Route + "System"
    Methods = Base.Methods

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @staticmethod
    @Generator.route(Route, methods = Methods)
    def Index(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        if internal == False: return JTYPE({
            "CPU"   : System.CPU(internal = True),
            "RAM"   : System.RAM(internal = True),
            "Disk"  : System.Disk(internal = True),
            "Uptime" : System.Uptime(internal = True),
            "Network" : System.Network(internal = True)
            
        })

        elif internal == True: return {
            "CPU"   : System.CPU(internal = True),
            "RAM"   : System.RAM(internal = True),
            "Disk"  : System.Disk(internal = True),
            "Uptime" : System.Uptime(internal = True),
            "Network" : System.Network(internal = True)
        }

        else: return Response(str({
            "CPU"   : System.CPU(internal = True),
            "RAM"   : System.RAM(internal = True),
            "Disk"  : System.Disk(internal = True),
            "Uptime" : System.Uptime(internal = True),
            "Network" : System.Network(internal = True)
        }), status = 200, mimetype = mime)

    @staticmethod
    @Generator.route(Route + "/" + "CPU", methods = Methods)
    def CPU(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ Various CPU Statistics

        - statistics:           General CPU statistics.
        - cores:                Total physical cores.
        - threads:              Total Threads, a function of hyper-threads/core.
        - frequencies:          Processor(s) clock speeds.
        - frequency:            Processor(s) clock speeds.
        - percentages:          Processor(s) clock speeds, utilization, as
                                percentage(s).
        - percentage:           Processor(s) clock speeds, utilization, as
                                percentage(s).
        - timings:              Processor(s) timing(s).
        - timing:               Processor(s) timing(s).
        - timing_percentages:   Processor(s) timing(s) as a percentage(s).
        - timing_percentage:    Processor(s) timing(s) as a percentage(s).

        """

        statistics = getCPUStatistics()

        cores = getCPUCount(logical = False)
        threads = getCPUCount(logical = True)

        frequencies = getCPUFrequencies(percpu = True)
        frequency = getCPUFrequencies(percpu = False)

        percentages = getCPUPercentage(percpu = True)
        percentage = getCPUPercentage(percpu = False)

        timings = getCPUTimings(percpu = True)
        timing = getCPUTimings(percpu = False)

        timing_percentages = getCPUTimingPercentages(percpu = True)
        timing_percentage = getCPUTimingPercentages(percpu = False)

        if internal == False: return JTYPE({
            "Statistics" : statistics,
            "Cores" : cores,
            "Threads" : threads,
            "Frequencies" : frequencies,
            "Frequency" : frequency,
            "Percentages" : percentages,
            "Percentage" : percentage
        })

        elif internal == True: return {
            "Statistics" : statistics,
            "Cores" : cores,
            "Threads" : threads,
            "Frequencies" : frequencies,
            "Frequency" : frequency,
            "Percentages" : percentages,
            "Percentage" : percentage
        }

    @staticmethod
    @Generator.route(Route + "/" + "RAM", methods = Methods)
    def RAM(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ Various RAM Statistics

        Please note, the derived statistics, while including the RAM information, also includes
        SWAP.

        - statistics: (NamedTuple)
            - total:        Total physical memory available.
            - available:    Unused physical memory.
            - percent:      Total physical memory used, represented as
                            a percentage.
            - used:         Total physical memory used.
            - free:         Zero-outted physical memory.

        """

        statistics = getRAMInformation()
        conversion = 1000000000 # --> Giga-Bytes (GB)

        total       = statistics[0] / conversion
        available   = statistics[1] / conversion
        used        = statistics[3] / conversion
        free        = statistics[4] / conversion

        percent     = statistics[2]

        if internal == False: return JTYPE({
            "Total"         : total,
            "Available"     : available,
            "Percentage"    : percent,
            "Used"          : used,
            "Free"          : free
        })

        elif internal == True: return {
            "Total"         : total,
            "Available"     : available,
            "Percentage"    : percent,
            "Used"          : used,
            "Free"          : free
        }

    @staticmethod
    @Generator.route(Route + "/" + "Disk", methods = Methods)
    def Disk(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ Various Disk Statistics

        - total: Total storage available.
        - free:  Available storage memory.
        - used:  Used storage memory.

        """
        _total, _used, _free = Disk.disk_usage("/")
        conversion = 1000000000 # --> Giga-Bytes (GB)

        total = _total / conversion
        used = _used / conversion
        free = _free / conversion

        if internal == False: return JTYPE({
            "Total" : total,
            "Used" : used,
            "Free" : free
        })

        elif internal == True: return {
            "Total" : total,
            "Used" : used,
            "Free" : free
        }

    @staticmethod
    @Generator.route(Route + "/" + "Uptime", methods = Methods)
    def Uptime(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ System uptime epoch (Central-Time).

        - system_time: (Epoch).
            - date: Epoch date.
            - time: Central-Time.

        """

        system_uptime = getSystemUptime()
        date = str(system_uptime).split()[0]
        time = str(system_uptime).split()[1]

        if internal == False: return JTYPE({
            "Start"     : str(system_uptime),
            "Date"      : date,
            "Time"      : time,
            "Days"      : getTotalSystemUptime() / 60 / 60 / 24,
            "Hours"     : getTotalSystemUptime() / 60 / 60,
            "Minutes"   : getTotalSystemUptime() / 60,
            "Seconds"   : getTotalSystemUptime()
        })

        elif internal == True: return {
            "Start"     : str(system_uptime),
            "Date"      : date,
            "Time"      : time,
            "Days"      : getTotalSystemUptime() / 60 / 60 / 24,
            "Hours"     : getTotalSystemUptime() / 60 / 60,
            "Minutes"   : getTotalSystemUptime() / 60,
            "Seconds"   : getTotalSystemUptime()
        }

    def getDiscordUserPermissions(self, username: str) -> str:
        """ Discord User Permissions
        Input: UserID (str) ....

        Returns Discord User Permissions
        """

        return ""

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
            tcp_connections         = getNetworkConnections() (kind = "TCP".casefold()).__len__()
            tcp4_connections        = getNetworkConnections(kind = "TCP4".casefold()).__len__()
            tcp6_connections        = getNetworkConnections(kind = "TCP6".casefold()).__len__()

            udp_connections         = getNetworkConnections(kind = "UDP".casefold()).__len__()
            udp4_connections        = getNetworkConnections(kind = "UDP4".casefold()).__len__()
            udp6_connections        = getNetworkConnections(kind = "UDP6".casefold()).__len__()
        except Exception as Error:
            print("Caught Exception: (TCP + UDP Connections)")
            print(str(Error.args))

            tcp_connections         = bytes("N/A".encode("UTF-8"))
            tcp4_connections        = bytes("N/A".encode("UTF-8"))
            tcp6_connections        = bytes("N/A".encode("UTF-8"))

            udp_connections         = bytes("N/A".encode("UTF-8"))
            udp4_connections        = bytes("N/A".encode("UTF-8"))
            udp6_connections        = bytes("N/A".encode("UTF-8"))

        try:
            public_ipv4 = subprocess.Popen(
                shlex.split("dig +short myip.opendns.com @resolver1.opendns.com"),
                stdin = subprocess.DEVNULL,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                shell = False,
                text = True
            ).communicate()[0].strip().replace('"', "").split(" ")
        except Exception as Error:
            print("Caught Exception: (Public-IPv4)")
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
