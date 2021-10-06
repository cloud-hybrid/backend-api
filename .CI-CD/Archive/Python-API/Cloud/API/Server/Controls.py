#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

"""\
Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

# --- Internal Imports --- #

from . import *

from Cloud.API.DB.Base import Database
from Cloud.API.DB.Host import Table as Hosts
from Cloud.API.DB.Configuration import Table as Configurations
from Cloud.API.DB.Server import Table as Servers

import Cloud.API.Database.Metal as Metal
import Cloud.API.Database.VPS as VPS
import Cloud.API.Database.Server as Server

class Master(Base):
    """ The Master System Responsible for the Entire Cloud Application """

    Generator = Blueprint("Control", __name__)
    Route = Base.Route + "Control"
    Methods = Base.Methods

    System = platform.system()

    Description = """\
       ... ... ...
    """

    OS = (platform.system(), (
        "Darwin",
        "Linux",
        "Windows"
    ))

    Metadata = {**{
        "Description"   : "{}".format(Description),
        "Title"         : "{}".format(Generator.name.replace("-", " ").title()),
        "Generator"     : "{}".format(Generator.name),
        "Page"          : "{}".format(Generator.name.casefold())
    }, **Base.Metadata}

    Commands = {
        "Shutdown"  : ["shutdown", "-f", "-s", "-t", "30"],
        "Restart"   : ["shutdown", "-f", "-r", "-t", "30"],
        "Host"      : ({
            "VM" : ({
                "All"                   : ["virsh", "list", "--all", "--name", "--uuid"],

                "Online-Status"         : ["virsh", "list", "--name", "--uuid"],
                "Inactive-Status"       : ["virsh", "list", "--inactive", "--name", "--uuid"],
                "Running-Status"        : ["virsh", "list", "--state-running", "--name", "--uuid"],
                "Inactive-Status"       : ["virsh", "list", "--state-shutoff", "--name", "--uuid"],
                "Other-Status"          : ["virsh", "list", "--state-other", "--name", "--uuid"],

                "Auto-Start-Enabled"    : ["virsh", "list", "--autostart", "--name", "--uuid"],
                "No-Auto-Start-Enabled" : ["virsh", "list", "--no-autostart", "--name", "--uuid"],

                "Start"                 : ["virsh", "start"],
                "Autostart"             : ["virsh", "autostart"]
            })
        })
    }

    assert platform.system() == "Darwin" or platform.system() == "Linux"

    Root = True if os.getenv("USER") == "root" else False

    Sudo = True if Root else \
        True if os.getenv("SUDO_USER") == "root" else \
            True if os.getenv("SUDO_USER") == os.getlogin() else \
                False 

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @staticmethod
    @Generator.route(Route + "/", methods = Methods, strict_slashes = False)
    # @Authenticate
    def Index(internal: bool = False, json = True, mime: String = "Application/JSON") -> Response(type(JTYPE)):
        """ General `Control` API Extensions

        Attributes:
            APIs (Dictionary): `Management` (Control) nested APIs valued to their respective
                Web-URL location.

        Returns:
            Response (JSON): Returns a WSGI Response object containing Flask's *.jsonify
                JSON object.
        """

        Instantiation = Management()

        # === Local Namespace Arguments === #
        Arguments = {
            "internal" : (
                ("Type", "Boolean"),
                ("Default", False),
                ("Description", "Internal Usage Only - Affects Authentication Methods & Object Return Type"),
                ("Current", internal)
            ),
            "json" : (
                ("Type", "Boolean"),
                ("Default", False),
                ("Description", "Return JSON Output"),
                ("Current", json)
            ),
            "mime" : (
                ("Type", "String"),
                ("Default", False),
                ("Description", "Browser Mimetype Setting"),
                ("Current", mime)
            ),
        }

        # === Nested API Endpoint(s) === #
        APIs = {
            "{}".format(
                Settings.Domain + Management.Generator.name)
            : "{}".format(Management.Route),
            "Start": ["{}".format(
                Settings.Domain + Management.Route
                + "/" + "Start")],
            "Stop": ["{}".format(
                Settings.Domain
                + Management.Route + "/" + "Stop")],
            "Restart": ["{}".format(
                Settings.Domain
                + Management.Route + "/" + "Restart")]
        }

        # === Additional Information === #
        Information = {
            "System" : Instantiation.system,
            "Supported": Instantiation.supported,
            "Systems": Instantiation.systems
        }

        if internal == True:
            return JSON.dumps({
                "API" : APIs,
                "Information": Properties,
                "Arguments" : Arguments
            })
        elif json == True:
            return Response(
                JTYPE({
                    "API" : APIs, "Information": Information, "Arguments" : Arguments
                }),
            status = 200, mimetype = mime).response
        else:
            return Template(
                "./API.html",
                Metadata = {
                    **Instantiation.Metadata, **{"Title": "{} API Endpoint(s)".format(Instantiation.Generator.name)}
                }, API = APIs,
                Information = Information,
                Arguments = Arguments
            )

    @staticmethod
    @Generator.route(Route + "/" + "Restart", methods = Methods, strict_slashes = False)
    def Restart(internal: bool = False, json = True, mime: String = "Application/JSON") -> Response(type(JTYPE)):
        subprocess.Popen(shlex.split("sudo shutdown -r +1"),
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            shell = False)

        return Event(request, 200, ("Restarting", "Successful")).Response

    @staticmethod
    @Generator.route(Route + "/" + "Stop", methods = Methods, strict_slashes = False)
    def Stop(internal: bool = False, json = True, mime: String = "Application/JSON") -> Response(type(JTYPE)):
        """ Power-On (VPS|Server) API

        Attributes:
            Provider (String): The name of the server/service provider. Providers such as
                AWS have a Commandline-Interface (CLI) for managing state of EC2 (VPS)
                instances -- State meaning the power-state (On, Off, Restart). Whereas
                Cloud-Hybrid will provide a Foreign Key Link to look up the physical host
                the VPS is residing on.
        """

        Instantiation = Management()

        Keys = JSON.dumps({
            "ID" : ({
                "Key":      ("id", "ID"),
                "Value":    ("")
            }),
            "Internal" : ({
                "Key": ("Internal", "internal", "INTERNAL", ""),
                "Value": (
                    ("1", 1, "true", "TRUE", "True"),
                    ("0", 0, "false", "FALSE", "False"),
                    ("False")
                )
            }),
            "JSON" : ({
                "Key": ("JSON", "json", ""),
                "Value": (
                    ("1", 1, "true", "TRUE", "True"),
                    ("0", 0, "false", "FALSE", "False"),
                    ("Default Implementation Not Programatically Determined")
                )
            }),
            "Mimetype" : ({
                "Key" : "mime",
                "Value": ("*", "Application/JSON")
            })
        })

        Optionals = JSON.dumps({
            "Internal" : ({
                "Key": ("Internal", "internal", "INTERNAL", ""),
                "Default": False
            }),
            "JSON" : ({
                "Key": ("JSON", "json", ""),
                "Default": "Default Implementation Not Programatically Determined"
            }),
            "Mimetype" : ({
                "Key" : "mime",
                "Default": ("*", "Application/JSON")
            }),
            "Type" : ("VPS", "Server", "Service"),
            "VPS": ("ID", "UUID", "Name"),
            "Server": ("ID", "UUID", "Server-Name"),
            "Service": ("ID", "UUID", "Server-Name")
        })

        # === Request Arguments === #
        Arguments = Dictionary(request.values)

        if Arguments == {} or Arguments == None or Arguments is None:
            Status = 400

            _Response = "Bad Request"
            _Type = "Error"
            _Message = "Invalid Request Arguments"

            Return = JTYPE({
                "Status" : Status,
                "Type" : _Type,
                "Response": _Response,
                "Message": _Message,
                "Body": [
                    "Expected Keys: {}".format(
                        JSON.loads(Keys) if Keys else "[]"
                    ), "Optionals: {}".format(JSON.loads(Optionals) if Optionals else "[]")
                ], "Keys": Keys if Keys else (),
                "Optionals": Optionals if Optionals else (),
                "URL": "{}".format(request.url),
                "Path": "{}".format(request.path),
                "Full-Path": "{}".format(request.full_path),
                "Arguments": "{}".format(Dictionary(request.values))
            }), Status

        return Return

    # @staticmethod
    # @Generator.route(Route + "/" + "Start", methods = Methods)
    # @Authenticate
    # def Start(internal: bool = False, mime: str = "application/json") -> Response(type({})):
    #     """ Start the target server. """

    #     if request.method == "HEAD" and request.args.get("Server", None) != None:
    #         print("{} - Internal Server Message: Starting Instance {}".format(
    #             str(datetime.datetime.now().time()),
    #             request.args.get("Server")
    #         ))
    #         _EC2 = EC2Instance()
    #         source, code = _EC2.instanceStart(value = request.args.get("Server"))
    #         _EC2.awaitInstanceStart(source)
    #         return Response(json.dumps(code["StartingInstances"][0]["CurrentState"]), status = code["ResponseMetadata"]["HTTPStatusCode"], mimetype = "application/json")

    #     else: return Response("501", status = code["ResponseMetadata"]["HTTPStatusCode"])

    # @staticmethod
    # @Generator.route(Route + "/" + "Stop", methods = Methods)
    # @Authenticate
    # def Shutdown(internal: bool = False, mime: str = "application/json") -> Response(type({})):
    #     """ Start the target server. """

    #     if request.method == "HEAD" and request.args.get("Server", None) != None:
    #         print("{} - Internal Server Message: Stopping Instance {}".format(
    #             str(datetime.datetime.now().time()),
    #             request.args.get("Server")
    #         ))
    #         _EC2 = EC2Instance()
    #         source, code = _EC2.instanceStop(value = request.args.get("Server"))
    #         _EC2.awaitInstanceStop(source)
    #         return Response(json.dumps(code["StoppingInstances"][0]["CurrentState"]), status = code["ResponseMetadata"]["HTTPStatusCode"], mimetype = "application/json")

    #     else: return Response("501", status = code["ResponseMetadata"]["HTTPStatusCode"])

    # @staticmethod
    # @Generator.route(Route + "/" + "Reboot", methods = Methods)
    # @Authenticate
    # def Reboot(internal: bool = False, mime: str = "application/json") -> Response(type({})):
    #     """ Start the target server. """
    #     try:
    #         if request.method == "HEAD" and request.args.get("Server", None) != None:
    #             print("{} - Internal Server Message: Restarting Instance {}".format(
    #                 str(datetime.datetime.now().time()),
    #                 request.args.get("Server")
    #             ))
    #             _EC2 = EC2Instance()
    #             source, code = _EC2.instanceRestart(value = request.args.get("Server"))
    #             _EC2.awaitInstanceRestart(source)
    #             return Response(code["ResponseMetadata"]["HTTPStatusCode"], status = code["ResponseMetadata"]["HTTPStatusCode"], mimetype = "application/json")

    #         else: return Response("501", status = code["ResponseMetadata"]["HTTPStatusCode"])
    #     except:
    #         if request.method == "HEAD" and request.args.get("Server", None) != None:
    #             print("{} - Internal Server Message: Starting Instance {}".format(
    #                 str(datetime.datetime.now().time()),
    #                 request.args.get("Server")
    #             ))
    #             _EC2 = EC2Instance()
    #             source, code = _EC2.instanceStart(value = request.args.get("Server"))
    #             _EC2.awaitInstanceStart(source)
    #             return Response(json.dumps(code), status = code["ResponseMetadata"]["HTTPStatusCode"])

    #         else: return Response("501", status = code["ResponseMetadata"]["HTTPStatusCode"])
