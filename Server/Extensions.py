"""
...
"""

import os
import io
import re
import abc
import gzip
import html
import json
import pprint
import sys
import typing
import asyncio
import inspect
import logging
import traceback
import contextlib
import dataclasses

import httptools

import Utility.Color as Color

Colors = Color.TTY()

# import orjson
import fastapi
import pydantic

import uvicorn.config

import starlette.routing
import starlette.middleware
import starlette.middleware.cors
import starlette.middleware.trustedhost
import starlette.middleware.authentication
import starlette.middleware.gzip
import starlette.responses

from starlette.datastructures import URL
from starlette.responses import RedirectResponse
from starlette.datastructures import Headers, MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send

Serialization = {
    "skipkeys":               True,
    "ensure_ascii":           False,
    "check_circular":         True,
    "allow_nan":              True,
    "indent":                 4,
    "separators":             (", ", ": "),
    "sort_keys":              True
}

# Option = orjson.OPT_APPEND_NEWLINE | orjson.OPT_INDENT_2

TRACE_LOG_LEVEL = 10

ABC = abc.ABC
Method = abc.abstractmethod
ABCM = abc.abstractclassmethod
Function = abc.abstractstaticmethod
Property = abc.abstractproperty

Optional = typing.Optional
List = typing.List

Application = fastapi.FastAPI
Router = fastapi.APIRouter

Route = starlette.routing.BaseRoute

Middleware = starlette.middleware.Middleware

CORS = starlette.middleware.cors.CORSMiddleware
Authentication = starlette.middleware.authentication.AuthenticationMiddleware
Hosts = starlette.middleware.trustedhost.TrustedHostMiddleware
GZIP = starlette.middleware.gzip.GZipMiddleware

JSON = starlette.responses.JSONResponse

# ... starlette.responses.UJSONResponse
# @Task Test fastapi.responses.ORJSONResponse

Settings = uvicorn.config.Config

Server = uvicorn.Server

Model = pydantic.BaseModel

# Dump = lambda _: orjson.loads(orjson.dumps(str(_), option = Option))
Dump = lambda _: json.loads(json.dumps(str(_)))

Static = staticmethod

@dataclasses.dataclass(init = True)
class Type:
    Scope: Scope
    Receive: Receive
    Send: Send

# class Handler(ASGIApp):
#     def __init__(self, app: ASGIApp):
#         """ ... """
#
#         self.app = app
#
#     async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
#         stack = scope.get("fastapi_astack")
#         try:
#             context = contextlib.ExitStack().enter_context(stack)
#         except Exception as Error:
#             if type(Error) == AttributeError:
#                 if "__exit__" in ("%s" % Error):
#                     sys.stdout.write(
#                         Colors.red("%s" % "[Nexus-API]" + Colors.reset("- Stack Reentrancy Frame Caught") + "\n")
#                     )
#                 else:
#                     Frame =  inspect.getframeinfo(inspect.currentframe())
#
#                     print("%s" % "[ERROR] - Unhandled Exception Caught" + "\n")
#                     print("%s" % "        - %i" % Frame.lineno + "\n")
#                     print("%s" % "        - %s" % Frame.filename + "\n")
#
#                     print("%s" % "[ERROR] - Please Contact Maintainer, jacob.sanders@cloudhybrid.io" + "\n")
#
#                     raise Error
#             else:
#                 Frame =  inspect.getframeinfo(inspect.currentframe())
#
#                 message = "Please Handle ASGI Error w/Interface Implementation Directly"
#
#                 print("%s" % "[ERROR] - Unhandled Exception Caught" + "\n")
#                 print("%s" % "        - %i" % Frame.lineno + "\n")
#                 print("%s" % "        - %s" % Frame.filename + "\n")
#
#                 print("%s" % "        - %s" % message + "\n")
#
#                 raise Error
#         else:
#             with stack:
#                 print("%s" % stack)
#         finally:
#             return

# class Mount(Router, ABC):
#     """
#     ...
#     """
#
#     def __init__(self, prefix: Optional[List[Route]],
#         *, tags: list = None, **kwargs):
#         super(Mount, self).__init__(
#             prefix = prefix,
#             tags = tags,
#             **kwargs
#         )

# class HTTPs:
#     """
#     ...
#     """
#
#     def __init__(self, app: ASGIApp):
#         """ ... """
#
#         self.app = app
#
#     async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
#         """ ... """
#
#         if scope["type"] in ("http", "websocket") and scope["scheme"] in ("http", "ws"):
#             url = URL(scope = scope)
#             redirect_scheme = {"http": "https", "ws": "wss"}[url.scheme]
#             netloc = url.hostname if url.port in (80, 443) else url.netloc
#             url = url.replace(scheme = redirect_scheme, netloc = netloc)
#             response = RedirectResponse(url, status_code = 307)
#             await response(scope, receive, send)
#         else:
#             try:
#                 await self.app(scope, receive, send)
#             except KeyError as Error:
#                 String = str(Error).split(".")[-1].replace("'", "")[:-1]
#                 Message = Colors.red(
#                     "%s" % "[Nexus-API]"
#                 ) + " - " + Colors.normalized(
#                     "Schema Validation Exception"
#                     + ":" + " "
#                     + Colors.underline(String)
#                 ) + "\n"
#
#                 Message = Colors.yellow(
#                     "%s" % "[Nexus-API]"
#                 ) + " - " + Colors.normalized(
#                     "Ensure Schema is Inheriting from a Pydantic Base Class"
#                 ) + "\n"
#
#                 sys.stdout.write(Message)
#
#                 raise Error
#                 await Handler(self.app)(scope, receive, send)
#                 Frame =  inspect.getframeinfo(inspect.currentframe())
#                 print(scope, receive, send)
#
#                 print("Supressed Error" + "(" + "%i" % Frame.lineno + ", " + Frame.filename)
#                 print("   - Please Handle ASGI Error w/Interface Implementation Directly")


class GZipResponder:
    """
    ...
    """

    def __init__(self, app: ASGIApp, minimum_size: int) -> None:
        self.app = app
        self.minimum_size = minimum_size
        self.send = self.unattached
        self.initial_message = {}
        self.started = False
        self.gzip_buffer = io.BytesIO()
        self.gzip_file = gzip.GzipFile(mode = "wb", fileobj = self.gzip_buffer)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        self.send = send
        await self.app(scope, receive, self.send_with_gzip)

    async def send_with_gzip(self, message: Message) -> None:
        message_type = message["type"]
        if message_type == "http.response.start":
            self.initial_message = message
        elif message_type == "http.response.body" and not self.started:
            self.started = True
            body = message.get("body", b"")
            more_body = message.get("more_body", False)
            if len(body) < self.minimum_size and not more_body:
                await self.send(self.initial_message)
                await self.send(message)
            elif not more_body:
                self.gzip_file.write(body)
                self.gzip_file.close()
                body = self.gzip_buffer.getvalue()

                headers = MutableHeaders(raw = self.initial_message["headers"])
                headers["Content-Encoding"] = "gzip"
                headers["Content-Length"] = str(len(body))
                headers.add_vary_header("Accept-Encoding")
                message["body"] = body

                await self.send(self.initial_message)
                await self.send(message)
            else:
                headers = MutableHeaders(raw = self.initial_message["headers"])
                headers["Content-Encoding"] = "gzip"
                headers.add_vary_header("Accept-Encoding")
                del headers["Content-Length"]

                self.gzip_file.write(body)
                message["body"] = self.gzip_buffer.getvalue()
                self.gzip_buffer.seek(0)
                self.gzip_buffer.truncate()

                await self.send(self.initial_message)
                await self.send(message)

        elif message_type == "http.response.body":
            body = message.get("body", b"")
            more_body = message.get("more_body", False)

            self.gzip_file.write(body)
            if not more_body:
                self.gzip_file.close()

            message["body"] = self.gzip_buffer.getvalue()
            self.gzip_buffer.seek(0)
            self.gzip_buffer.truncate()

            await self.send(message)
        else:
            await self.send(message)

    @staticmethod
    async def unattached(message):
        raise RuntimeError("send awaitable not set")

class GZipMiddleware:
    """
    ...
    """

    def __init__(self, app: ASGIApp, minimum_size: int = 500) -> None:
        self.app = app
        self.minimum_size = minimum_size

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            headers = Headers(scope = scope)
            if "gzip" in headers.get("Accept-Encoding", ""):
                responder = GZipResponder(self.app, self.minimum_size)
                await responder(scope, receive, send)
                return

        await self.app(scope, receive, send)

# class MessageLoggerMiddleware:
#     """
#     ...
#     """
#
#     def __init__(self, app):
#         self.app = app
#
#         self.task_counter = 0
#
#         self.logger = logging.getLogger("uvicorn.asgi")
#
#         self.trace = lambda message, *args, **kwargs: logging.getLogger("uvicorn.asgi").log(10, message, *args, **kwargs)
#         self.debug = lambda message, *args, **kwargs: logging.getLogger("uvicorn.asgi").log(20, message, *args, **kwargs)
#         self.warning = lambda message, *args, **kwargs: logging.getLogger("uvicorn.asgi").log(30, message, *args, **kwargs)
#
#     async def log(self, message: dict = None, egress = False, ingress = False):
#         """
#         Return an ASGI message, with any body-type content omitted and replaced
#             with a placeholder.
#
#         Speed Benefit of Join vs. Format:
#             - http://bugs.python.org/msg180449
#         """
#
#         if message.get("type", None) == "http":
#             content = {}
#             try:
#                 content["Headers"] = "\n%s" % "\n".join(
#                     (" - {}: {}".format(index[0].title().decode(), index[1].decode())) for index in
#                     message.get("headers", None))
#             except TypeError as Error:
#                 ...
#             finally:
#                 content["Path"]    = message.get("path", None)
#                 content["Server"]  = message.get("server", None)
#                 content["Client"]  = message.get("client", None)
#                 content["Scheme"]  = message.get("scheme", None)
#                 content["Method"]  = message.get("method", None)
#                 content["Version"] = message.get("http_version", None)
#                 content["Query-String"]   = message.get("query_string", None)
#
#                 for key, value in content.items():
#                     sys.stdout.write("[Nexus-API]" + ": " + "%s: %s" % (key, value) + "\n")
#                     self.trace("%s: %s" % (key, value))
#
#         return message
#
#     async def __call__(self, scope, receive, send):
#         self.task_counter += 1
#
#         prefix = "ASGI: (Task - %i)" % self.task_counter
#
#         async def inner_receive():
#             return await receive()
#
#         async def inner_send(message):
#             return await send(message)
#
#         try:
#             await self.app(scope, inner_receive, inner_send)
#         except BaseException as Error:
#             raise Error from None
#
#         await self.log(scope)
