#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

#
# ========================================================================
# ...
# ========================================================================
#

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

from . import *

class Interface(Base):
    Generator = Blueprint("Steam", __name__)
    Route = Base.Route + "Steam"
    Methods = Base.Methods

    URL = "http://api.steampowered.com"
    Version = "v1"
    ID = "76561198997637019"
    Account = "Segmentational"
    Token = "81A5077961FD8E2D1D478E315D73A5CC"

    ApplicationIDs = {
        "Bannerlord"        : 261550,
        "Mordhau"           : 629760,
        "Mordhau-Server"    : 629800,
        "Vagrant"           : 598700,
        "Squad"             : 393380,
        "Rust"              : 252490,
        "Tarkov"            : 771400,
        "Rocket-League"     : 252950,
        "6ix"               : 359550,
        "Halo"              : 976730,
        "Planet-Side"      : 218230
    }

    ApplicationNames = {
        261550  : "Bannerlord",
        629760  : "Mordhau",
        629800  : "Mordhau-Server",
        598700  : "Vagrant",
        393380  : "Squad",
        252490  : "Rust",
        771400  : "Tarkov",
        252950  : "Rocket-League",
        359550  : "6ix",
        976730  : "Halo",
        218230  :  "Planet-Side"
    }

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @staticmethod
    @Generator.route(Route, methods = Methods, strict_slashes = False)
    def Index(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        if request.method == "GET":
            if internal == False: return Response(json.dumps({
                "Endpoints" : Steam.Endpoints(internal = True),
                "Application-List" : { "URL" : request.url + "/" + "Application-List" },
                "Status" : Steam.Status(internal = True)
            }), status = 200, mimetype = mime)

            elif internal == True: return {
                "Endpoints" : Steam.Endpoints(internal = True),
                "Application-List" : Route + "/" + "Application-List",
                "Status" : Steam.Status(internal = True)
            }

        elif request.method == "OPTIONS":
            return Response(json.dumps({
                "Interfaces" : [
                    request.url + "/" + "Endpoints",
                    request.url + "/" + "Status",
                    request.url + "/" + "Application-List"

                ]
            }), status = 200, mimetype = mime)


    @staticmethod
    @Generator.route(Route + "/" + "Endpoints", methods = Methods, strict_slashes = False)
    def Endpoints(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ \
        Cloud Hybrid Steam-API Interface
        --------------------------------

        API-Key
        =======
        - Token: `81A5077961FD8E2D1D478E315D73A5CC`
        - Account: `Segmentational`
        - SteamID: `76561198997637019`
        - Domain: `https://cloudhybrid.io`
        """

        URL = "http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v1/?key={}&steamid={}".format(Steam.Token, Steam.ID)

        Handler = urllib3.PoolManager()

        Payload = Handler.request("GET", URL)

        Data = json.loads(Payload.data.decode('utf-8'))

        Interfaces = [
            "ISteamApps",
            "ISteamBroadcast",
            "ISteamCDN",
            "ISteamDirectory",
            "ISteamEconomy"
            "ISteamNews"
            "ISteamRemoteStorage",
            "ISteamUser",
            "ISteamUserAuth",
            "ISteamUserOAuth",
            "ISteamUserStats",
            "ISteamWebAPIUtil",
            "ISteamWebUserPresenceOAuth",
            "IGameServersService",
            "IBroadcastService",
            "IContentServerConfigService",
            "IContentServerDirectoryService",
            "IPublishedFileService",
            "IEconService",
            "IPlayerService",
            "IGameNotificationsService",
            "IInventoryService",
            "IStoreService",
            "ICheatReportingService"
        ]

        _return = {
            "Data": {
                "Total" : len(Data["apilist"]["interfaces"]),
                "ID" : Steam.ID,
                "Account" : Steam.Account,
                "Token" : Steam.Token
            },
            "API" : {
                "Interfaces" : [],
                "Map" : {}
            }
        }

        for endpoint in range(0, len(Data["apilist"]["interfaces"])):
            name = Data["apilist"]["interfaces"][endpoint]["name"]
            if name in Interfaces:
                _return["API"]["Interfaces"].append(name)
                _return["API"]["Map"][name] = Data["apilist"]["interfaces"][endpoint]["methods"]

        if internal == False: return JTYPE(
            _return
        )

        elif internal == True: return _return

    @staticmethod
    @Generator.route(Route + "/" + "Application-List", methods = Methods, strict_slashes = False)
    def Applications(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ \
        Application ID List
        """

        Mapping = "ISteamApps/GetAppList"

        URL = "{}/{}/{}/?key={}&steamid={}".format(Steam.URL, Mapping, Steam.Version, Steam.Token, Steam.ID)

        Handler = urllib3.PoolManager()

        Payload = Handler.request("GET", URL)

        Raw = json.loads(Payload.data.decode('utf-8'))["applist"]["apps"]["app"]

        _return = {
            "Data": {
                "Total" : len(Raw),
                "ID" : Steam.ID,
                "Account" : Steam.Account,
                "Token" : Steam.Token
            },
            "Applications" : Raw
        }

        if internal == False: return JTYPE(
            _return
        )

        elif internal == True: return _return

    @staticmethod
    @Generator.route(Route + "/" + "Status", methods = Methods, strict_slashes = False)
    def Status(internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ \
        Steam Server Status
        """

        Mapping = "ISteamWebAPIUtil/GetServerInfo"

        URL = "{}/{}/{}/?key={}&steamid={}".format(Steam.URL, Mapping, Steam.Version, Steam.Token, Steam.ID)

        Handler = urllib3.PoolManager()

        Payload = Handler.request("GET", URL)

        Data = json.loads(Payload.data.decode('utf-8'))

        _return = {
            "Status" : "Online" if Payload.status == 200 else "Offline",
            "Response" : Payload.status,
            "Time" : Data["servertimestring"]
        }

        if internal == False: return JTYPE(
            _return
        )

        elif internal == True: return _return

    @staticmethod
    @Generator.route(Route + "/" + "News", methods = Methods, strict_slashes = False)
    def News(application: "String | List" = None, total: int = 10, internal: bool = False, mime: str = "application/json") -> Response(type({})):
        """ \
        Steam News
        """

        Mapping = "ISteamNews/GetNewsForApp"

        Handler = urllib3.PoolManager()

        Data = {}

        if type(application) == type(list) or application == None:
            clean = re.compile('<.*?>')
            strip = re.compile(r'\[img].*?\[/img]')
            subtract = re.compile(r'\[.*?\].*?\[/.*?\]')

            if application == None: application = Steam.ApplicationIDs.values()
            else: application = [ Steam.ApplicationIDs[item] for item in application]
            for item in application:
                URL = "{}/{}/{}/?appid={}&count={}&key={}&steamid={}".format(
                    Steam.URL,
                    Mapping,
                    "v2",
                    item,
                    total,
                    Steam.Token,
                    Steam.ID
                )

                Payload = Handler.request("GET", URL)
                Object = json.loads(Payload.data.decode("utf-8"))
                Name = Steam.ApplicationNames[item]
                Data["{}".format(Name)] = []

                for Item in Object["appnews"]["newsitems"]:
                    Item["contents"] = re.sub(strip, "", Item["contents"])
                    Item["contents"] = re.sub(subtract, "", Item["contents"])
                    Data["{}".format(Name)].append({
                        "Title"             : Item["title"],
                        "Application-ID"    : Item["appid"],
                        "Date"              : str(datetime.datetime.utcfromtimestamp(Item["date"])),
                        "External"          : Item["is_external_url"],
                        "Content"           : re.sub(clean, "", "{}".format(Item["contents"])).replace("*", " ")[: 300] + " [...]" if len(Item["contents"]) >= 300 else Item["contents"].replace("*", " "),
                        "Extended"          : Item["contents"],
                        "URL"               : Item["url"],
                        "Author"            : Item["author"].title(),
                    })

        else:
            URL = "{}/{}/{}/?appid={}&count={}&key={}&steamid={}".format(
                Steam.URL,
                Mapping,
                "v2",
                Steam.ApplicationIDs[application],
                total,
                Steam.Token,
                Steam.ID
            )

            Payload = Handler.request("GET", URL)
            Data[Steam.ApplicationNames[item]] = json.loads(Payload.data.decode('utf-8'))

        _return = {
            "Data": {
                "Total" : len(Data),
                "ID" : Steam.ID,
                "Account" : Steam.Account,
                "Token" : Steam.Token
            },
            "News" : Data
        }

        if internal == False: return JTYPE(
            _return
        )

        elif internal == True: return _return
