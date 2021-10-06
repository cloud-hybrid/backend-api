"""
...
"""

import os
import ssl
import sys
import pkgutil
import datetime

import tempfile

import starlette.config

from dataclasses import dataclass

from Server.Extensions import *

import API.Constants
import Server.Transmission as Transmission
from fastapi import WebSocket, WebSocketDisconnect

from fastapi.responses import HTMLResponse

from fastapi.middleware.cors import CORSMiddleware

import fastapi.responses

Version = {}

Integer = int
Boolean = bool
String = str
Default: API.Constants.Default = API.Constants.Default

Port = API.Constants.PORT
Host = API.Constants.HOSTNAME
TLS = API.Constants.HTTPS

Silent = API.Constants.SILENT

Environment = API.Constants.Environment
JSON = starlette.responses.JSONResponse

Data = {
    "Version": pkgutil.get_data(__package__, "VERSION").decode("UTF-8"),
    "PEM": pkgutil.get_data(__package__, "Key.PEM"),
    "Certificate": pkgutil.get_data(__package__, "Development.crt"),
    "Key": pkgutil.get_data(__package__, "Development.key"),
    "PFX": pkgutil.get_data(__package__, "Development.pfx")
}

@dataclass
class Health:
    Status: str = "Online"
    Time: int = datetime.datetime.utcnow().timestamp()

    def Schema(self):
        return {
            "Status": self.Status,
            "Time": self.Time
        }

class Base:
    """
    ...
    """

    Route = "/"

    Encrypted = any([
        "--TLS" in sys.argv,
        "--HTTPS" in sys.argv,
        "--HTTPs" in sys.argv,
        "--https" in sys.argv
    ])

    Debug = any([
        "--Routes" in sys.argv,
        "--routes" in sys.argv,
        "--List" in sys.argv,
        "--list" in sys.argv,
        "--Endpoints" in sys.argv,
        "--endpoints" in sys.argv,
        "--Debug" in sys.argv,
        "--debug" in sys.argv
    ])

    API: fastapi.FastAPI = fastapi.FastAPI(title = "Cloud-ASGI",
        default_response_class = JSON,
        debug = False,
        docs_url = Route + "Documentation",
        redoc_url = Route,
        version = Data.get("Version")
    )

    API.add_middleware(CORSMiddleware,
        allow_credentials   = False,
        allow_methods       = ["*"],
        allow_headers       = [
            "*",
            "X-Guarantee-Token",
            "X-Guarantee-Type",
            "X-Guarantee-Server",
            "X-Guarantee-User",
            "X-Guarantee-Scopes"
        ],
        expose_headers      = ["*"],
        max_age             = 30,
        allow_origins       = ["*"]
    )

    API.add_middleware(GZipMiddleware)
    API.add_middleware(Transmission.Track)

    Generator: Router = Router
    Generator.redirect_slashes = True
    Generator.dependencies = {  }

    def __init__(self, *argv, **kwargs): ...

    @property
    def Server(self, Application = None):
        """
        ...
        """

        File = tempfile.NamedTemporaryFile("wb+", delete = False)
        File.write(Data.get("PEM"))
        File.close()

        Certificate = tempfile.NamedTemporaryFile("wb+", delete = False)
        Certificate.write(Data.get("Certificate", ""))
        Certificate.close()

        Key = tempfile.NamedTemporaryFile("wb+", delete = False)
        Key.write(Data.get("Key", ""))
        Key.close()

        PFX = tempfile.NamedTemporaryFile("wb+", delete = False)
        PFX.write(Data.get("PFX", ""))
        PFX.close()

        Edge = True if Data.get("PFX", False) else False
        Protocol = "https" if self.Encrypted else "http"
        Hostname = "localhost" if self.Encrypted else "0.0.0.0"
        Port = Integer(os.environ.get("NEXUS_API_PORT", Default.Port))

        Configuration = Server(
            Settings(app = self.API if Application is None else Application,
                host = Hostname,
                port = Port,
                use_colors = True,
                log_level = "TRACE".casefold() if self.Debug else None,
                log_config = self.Logger,
                access_log = self.Debug,
                debug = self.Debug,
                workers = os.cpu_count(),
                root_path = self.Route,
                headers = [("Server", "Nexus")],
                forwarded_allow_ips = "*",
                timeout_keep_alive = 10,
                timeout_notify = 15,
                http = "auto",
                lifespan = "on",
                backlog = 8192,
                ssl_keyfile = os.fspath(Key.name) if Edge else os.fspath(File.name) if self.Encrypted else None,
                ssl_certfile = os.fspath(Certificate.name) if Edge else os.fspath(File.name) if self.Encrypted else None,
                ssl_keyfile_password = os.fspath(PFX.name) if Edge else None,
                # ... env_file = ...,
                # ... interface = "asgi3",
                # ... ssl_version = 2,
                # ... ssl_cert_reqs = 0
            ))

        return Configuration

    @property
    def Logger(self):
        return {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(levelprefix)s %(message)s",
                    "use_colors": None,
                },
                "access": {
                    "()": "uvicorn.logging.AccessFormatter",
                    "fmt": '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
                },
            },
            "handlers": {
                "default": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stderr",
                },
                "access": {
                    "formatter": "access",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {
                "uvicorn": {"handlers": ["default"], "level": "ERROR"},
                "uvicorn.error": {"level": "ERROR"},
                "uvicorn.access": {"handlers": ["access"], "level": "ERROR", "propagate": True},
            },
        }

    @staticmethod
    @API.get(Route + "Health", tags = ["General"], status_code = 200, response_model = Health)
    async def Health():
        """\
        # Health-Check #

        The `ASGI` Web-Application will return a JSON, 200 Response upon
        Initialization.

        ## References ##
        - [Cloud-Technology.IO](https://cloud-technology.io)
        """

        return { "Status": "Online" }

    @staticmethod
    async def HTML(**kwargs) -> HTMLResponse:
        return await HTMLResponse(**kwargs)

Application = Base(host = "0.0.0.0", port = 3000)

__all__ = [
    "Base",
    "Application"
]
