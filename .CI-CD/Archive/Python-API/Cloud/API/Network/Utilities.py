import subprocess
import ipaddress

from flask import Flask, \
    request, \
    Response, \
    Blueprint, \
        stream_with_context

from . import *

import json

RED = lambda text: "\033[91m" + str(text) + "\33[0m"
GREEN = lambda text: "\033[92m" + str(text) + "\33[0m"

class Ping(Base):
    Generator = Blueprint("Ping", __name__)
    Route = Base.Route
    Methods = Base.Methods


    Network = "172.16.0.0"

    Domain = "{}".format(Settings.FQDN)
    Mask = "16"

    Subnet = list(ipaddress.IPv4Network("{}/{}".format(
        Network,
        Mask
    )))

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @staticmethod
    @Generator.route(Route, methods = Methods)
    def Index(mime: str = "application/json") -> Response(type({})):
        _return = []

        def _generate():
            for node in range(len(list(Ping.Subnet))):
                output = subprocess.Popen(
                    ["ping", "-c", "1", str(list(Ping.Subnet)[node])],
                    stdin = subprocess.DEVNULL,
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    shell = False
                ).communicate()[0]

                if "unreachable" in str(output.decode("UTF-8")).casefold():
                    print(GREEN(
                        (str(tuple(Ping.Subnet)[node]), "Available")
                    ))

                    _return.append(
                        (str(tuple(Ping.Subnet)[node]), "Available")
                    )
                elif "timed out" in str(output.decode("UTF-8")).casefold():
                    print(GREEN(
                        (str(tuple(Ping.Subnet)[node]), "Available")
                    ))

                    _return.append(
                        (str(tuple(Ping.Subnet)[node]), "Available")
                    )
                else:
                    print(RED(
                        (str(tuple(Ping.Subnet)[node]), "Unavailable")
                    ))

                    _return.append(
                        (str(tuple(Ping.Subnet)[node]), "Unavailable")
                    )

                yield json.dumps(_return)

        return Response(stream_with_context(_generate()),
            status = 200,
            mimetype = mime)

    @staticmethod
    @Generator.route(Route + "Ping", methods = Methods)
    def Pinger(mime: str = "text/plain") -> Response(type({})):
        IP = request.args.get("IP", default = None)
        try:
            if IP == None or IP == "": return Response("400 - NULL",
                status = 400,
                mimetype = mime)
            elif ipaddress.IPv4Address("{}".format(IP)) not in NETWORK:
                print(IP)
                return Response("406 - Invalid Address. Network Range: {}{}.".format(
                    BASE, SUBNET
                ),
                status = 406,
                mimetype = mime)
            else:
                output = subprocess.Popen(
                    ["ping", "-c", "1", "{}".format(IP)],
                    stdin = subprocess.DEVNULL,
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    shell = False
                ).communicate()[0]

                if "unreachable" in str(output.decode("UTF-8")).casefold():
                    return Response("200 - IP-Address is Available. (Ping := Unreachable)",
                        status = 200,
                        mimetype = mime)
                elif "timed out" in str(output.decode("UTF-8")).casefold():
                    return Response("200 - IP-Address is Available. (Ping := Time-Out)",
                        status = 200,
                        mimetype = mime)
                else:
                    return Response("409 - IP-Address is Unavailable.",
                        status = 409,
                        mimetype = mime)

        except ipaddress.AddressValueError as e:
            return Response("406 - Invalid Address. Network Range: 172.16.0.0/16.",
                status = 406,
                mimetype = mime)

    @staticmethod
    @Generator.route(Route + "Scanner", methods = Methods)
    def Scanner(mime: str = "application/json") -> Response(type({})):
        _return = []

        def _generate():
            for node in range(len(list(Ping.Subnet))):
                output = subprocess.Popen(
                    ["ping", "-c", "1", str(list(Ping.Subnet)[node])],
                    stdin = subprocess.DEVNULL,
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    shell = False
                ).communicate()[0]

                if "unreachable" in str(output.decode("UTF-8")).casefold():
                    print(GREEN(
                        (str(tuple(Ping.Subnet)[node]), "Available")
                    ))

                    _return.append(
                        (str(tuple(Ping.Subnet)[node]), "Available")
                    )
                elif "timed out" in str(output.decode("UTF-8")).casefold():
                    print(GREEN(
                        (str(tuple(Ping.Subnet)[node]), "Available")
                    ))

                    _return.append(
                        (str(tuple(Ping.Subnet)[node]), "Available")
                    )
                else:
                    print(RED(
                        (str(tuple(Ping.Subnet)[node]), "Unavailable")
                    ))

                    _return.append(
                        (str(tuple(Ping.Subnet)[node]), "Unavailable")
                    )

                yield json.dumps(_return)

        return Response(stream_with_context(_generate()),
            status = 200,
            mimetype = mime)
