import inspect
import json
import sys
import os

import devtools

from . import *

from . import User
from . import Token

OAuth2 = Token.Type

from fastapi import Query, Header, Body

import pprint

import sqlalchemy.orm
import Database.SQL

import Database.User.Models.Nexus as Model

import Database.User.Interfaces.User.API
import Database.User.Interfaces.User.CRUD


import jose.exceptions

import API.ASGI.Authentication.OAPI
import API.ASGI.Authentication.OAPI.Models

from datetime import datetime, timedelta
from typing import Optional, Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, OAuth2PasswordRequestFormStrict, SecurityScopes, OAuth2AuthorizationCodeBearer
from jose import JWTError, jwt, ExpiredSignatureError
from passlib.context import CryptContext as Cryptic
from pydantic import BaseModel

from API.ASGI.Authentication.User import (
    Input, Authorization
)

Authorizer = Authorization

from fastapi import Form

import Database.User.Schemas.Nexus

import fastapi.responses

# JSON = fastapi.responses.ORJSONResponse

from jose import jwt

import starlette.responses
import starlette.requests

JSON = starlette.responses.JSONResponse

import Utility.Color as Color

import Database.User.Interfaces.User
from Database.User.Interfaces.User.API import (
    Model as User
)

import Database.User.Schemas.Nexus

Colors = Color.TTY()

Scheme = OAuth2PasswordBearer(tokenUrl = "/API/Authentication/Token", scheme_name = "Nexus-API-Authentication",
    scopes = {"Development": "Administrative"}, description = "[...]")

def Verify(Password: Union[str, bytes], Hash: Union[str, bytes]):
    sys.stdout.write(
        Colors.yellow(
            "%s" % "[Nexus-API]"
        ) + ": " + Colors.italic("(Ingress) ")
        + "... Validating"
        + Colors.normalized("\n")
    );
    sys.stdout.flush()

    Verification = Interface.PWD.verify_and_update(secret = Password, hash = Hash, category = "Authentication")

    return Verification

def Hash(Password: Union[str, bytes]) -> Database.User.Schemas.Nexus.Schema:
    return Interface.PWD.hash(Password)

async def Extract(Username: str) -> Database.User.Models.Nexus.Table:
    """
    ...
    """

    Extraction = await Database.User.Interfaces.User.CRUD.SQL.Read(Username = Username)

    return Extraction

async def Authenticate(Username: str, Password: str) -> User.Schema:
    """
    ...
    """

    sys.stdout.write(
        Colors.yellow(
            "%s" % "[Nexus-API]"
        ) + ": " + Colors.italic("(Ingress) ")
        + "... Entering Event Handler"
        + Colors.normalized("\n")
    );
    sys.stdout.flush()

    async def _(Username = Username):
        sys.stdout.write(
            Colors.yellow(
                "%s" % "[Nexus-API]"
            ) + ": " + Colors.italic("(Ingress) ")
            + "... Querying Database"
            + Colors.normalized("\n")
        );
        sys.stdout.flush()

        if Response := await Database.User.Interfaces.User.API.HTTP.Account(Username):
            User = Interface.Table(Response, Database.User.Schemas.Nexus.Shard)
            Password: Secret = User.Password
            return "%s" % Password.get_secret_value()
        else: return None

    Verification = Verify(Password = Password, Hash = await _(Username))

    sys.stdout.write(
        Colors.yellow("[Nexus-API]")
        + ": " + Colors.italic("(Ingress) ")
        + Colors.green(Colors.bold("Successful") + Colors.normalized("\n")) if Verification[0] is True else Colors.red(
            "[Nexus-API]"
        ) + ": " + Colors.italic("(Ingress)") + " " + "... {0}".format(
            Colors.bold(Colors.red(String(Verification[0]))
            )) + Colors.normalized("\n")
    );
    sys.stdout.flush()

    return await Database.User.Interfaces.User.API.HTTP.Account(Username) if Verification[0] is True else None

def Generate(Data: dict, Expiration: Optional[Delta] = None, Issuer = "Nexus-API"):
    Source = Data.copy()

    if Expiration:
        Expire = Date.utcnow() + Expiration
    else:
        Expire = Date.utcnow() + Delta(minutes = Vault.Expiration)

    Source.update({"exp": Expire})

    return JWT.encode(Source, "%s" % Vault.Key, algorithm = Vault.Algorithm.upper())

class Interface(Request):
    """
    ...
    """

    Route = "/API"

    PWD = Cryptic(schemes = ["bcrypt"], deprecated = "auto")

    Scope = "Token"

    Generator = Application.Generator(prefix = Base.Route.join([Route, "Authentication"]))

    Methods = [
        "GET", "POST"
    ]

    Vault = Vault

    Responses = {
        200:    {
        }, 201: {
        }, 202: {
        }, 400: {
        }, 401: {
        }, 404: {
        }, 422: {
        }
    }

    @staticmethod
    def Derive(Object, _K, _D):
        try:
            Interface.__getattribute__(Object, _K)
        except:
            return _D

    @staticmethod
    def Decode(Token: String):
        try:
            return jwt.decode(Token, "%s" % Vault.Key, algorithms = Vault.Algorithm).get("sub")
        except ExpiredSignatureError as Error:
            sys.stdout.write(
                Colors.red(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                    Colors.underline(
                        "Authentication (Open-API) Failure - Expired JWT Token"
                    ) + Colors.normalized("\n")
                )
            );
            sys.stdout.flush()

            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Expired JWT Token",
                headers = {"WWW-Authenticate": "Bearer"},
            )

    @staticmethod
    @Generator.get("/Session", response_model = Token.JWT)
    async def Session(T = Depends(Scheme)):
        """
        ...
        """

        try:
            Payload = jwt.decode(T, "%s" % Vault.Key, algorithms = [Vault.Algorithm])
            Username: str = Payload.get("sub")

            if Username is None:
                raise HTTPException(
                    status_code = status.HTTP_401_UNAUTHORIZED,
                    detail = "Form Username Malformation Error",
                    headers = {"WWW-Authenticate": "Bearer"},
                )
            Data = Token.Data(Username = Username)
        except jose.exceptions.ExpiredSignatureError as Error:
            sys.stdout.write(
                Colors.red(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                    Colors.underline(
                        "Authentication (Open-API) Failure - Expired JWT Token"
                    ) + Colors.normalized("\n")
                )
            );
            sys.stdout.flush()

            raise Error

        except Exception as Error:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Credential JWT Validation Error",
                headers = {"WWW-Authenticate": "Bearer"},
            )

        User = await Extract(Username = Data.Username)

        if User is None:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "User Not Found Error",
                headers = {"WWW-Authenticate": "Bearer"},
            )

        Expiration = timedelta(minutes = Vault.Expiration)

        T = Generate(
            Data = {"sub": User.Username}, Expiration = Expiration
        );
        Type = "bearer"

        Schema = Token.Type(access_token = T, token_type = Type)
        return JSON(
            Authorizer(
                **{"JWT": Schema.access_token, "Type": Schema.token_type.capitalize()}
            ).dict(),
            200, {
                "X-Guarantee-Token":      Schema.access_token,
                "X-Guarantee-Type":       Schema.token_type.capitalize(),
                "X-Guarantee-Server":     "Nexus-API-Service",
                "X-Guarantee-User":       "%s" % User.Username,
                "X-Guarantee-Account-ID": "%s" % User.ID,
                "X-Guarantee-Scopes":     "%s" % "[Under-Development]"
            }
        )

        return Response

    @staticmethod
    @Generator.post("/Authenticate")
    async def Basic(Data: OAuth2PasswordRequestForm = Depends()):
        """
        Basic Authentication

        Request Submission (Authorization Header)

            >>> Username: Segmentational
            >>> Password: ******

        """

        sys.stdout.write(
            Colors.yellow(
                "%s" % "[Nexus-API]"
            ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                Colors.underline(
                    "Authentication (Open-API) Request Event"
                ) + Colors.normalized("\n")
            )
        );
        sys.stdout.flush()

        try:
            User = await Authenticate(Username = Data.username, Password = Data.password)
            sys.stdout.write(
                Colors.yellow(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ") + "Open-API - " + Colors.bold(Data.username)
                + Colors.normalized("\n")
            );
            sys.stdout.flush()

            if not User:
                raise HTTPException(
                    status_code = status.HTTP_401_UNAUTHORIZED,
                    detail = "Incorrect Username or Password",
                    headers = {"WWW-Authenticate": "Bearer"},
                )

            Expiration = timedelta(minutes = Vault.Expiration)

            JWT = Generate(
                Data = {"sub": User.Username}, Expiration = Expiration
            );
            Type = "bearer"

        except OSError as Error:
            print(devtools.Debug(Error))

        except Exception as Error:
            sys.stdout.write(
                Colors.red(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                    Colors.underline(
                        "Authentication (Open-API) Failure Event"
                    ) + Colors.normalized("\n")
                )
            );
            sys.stdout.flush()

            sys.stdout.write(
                Colors.red(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ")
                + "User - " + Colors.bold(Data.username)
                + Colors.normalized("\n")
            );
            sys.stdout.flush()

            raise Error

        Scopes = SecurityScopes([
            "Test"
        ])

        return Token.Type(access_token = JWT, token_type = Type, scopes = Scopes.scopes)

    @staticmethod
    @Generator.post("/Token")
    async def JWT(Data: OAuth2PasswordRequestForm = Depends()):
        """
        Open-API Standard

        Basic Standard, Strict Request Submission (Authorization Header)

            >>> Token URL: /API/Authentication/Token
            >>> Flow: password
            >>> Username: Segmentational
            >>> Password: ******
            >>> Client credentials location: basic
            >>> client_secret: ******

        Basic Standard, Strict Request Submission (Request-Body)

            >>> Token URL: /API/Authentication/Token
            >>> Flow: password
            >>> Username: Segmentational
            >>> Password: ******
            >>> Client credentials location: request-body
            >>> client_secret: ******
        """

        sys.stdout.write(
            Colors.yellow(
                "%s" % "[Nexus-API]"
            ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                Colors.underline(
                    "Authentication (Open-API) Request Event"
                ) + Colors.normalized("\n")
            )
        );
        sys.stdout.flush()

        try:
            User = await Authenticate(Username = Data.username, Password = Data.password)
            sys.stdout.write(
                Colors.yellow(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ") + "Open-API - " + Colors.bold(Data.username)
                + Colors.normalized("\n")
            );
            sys.stdout.flush()

            if not User:
                raise HTTPException(
                    status_code = status.HTTP_401_UNAUTHORIZED,
                    detail = "Incorrect Username or Password",
                    headers = {"WWW-Authenticate": "Bearer"},
                )

            Expiration = timedelta(minutes = Vault.Expiration)

            JWT = Generate(
                Data = {"sub": User.Username}, Expiration = Expiration
            );
            Type = "bearer"

        except OSError as Error:
            if "Multiple exceptions" in String(Error):
                if "Errno 61" in String(Error):
                    # -->  Likely Local & Database isn't Started

                    sys.stdout.write(
                        Colors.red(
                            "%s" % "[Nexus-API]"
                        ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                            Colors.bold(
                                Colors.underline("Multi-Exception (61)")
                            ) + Colors.normalized("\n")
                        )
                    );
                    sys.stdout.flush()

                    sys.stdout.write(
                        Colors.red(
                            "%s" % "[Nexus-API]"
                        ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                            Colors.normalized(
                                "... Check Local Database Status"
                            ) + Colors.normalized("\n")
                        )
                    );
                    sys.stdout.flush()

                    raise HTTPException(
                        status_code = status.HTTP_503_SERVICE_UNAVAILABLE,
                        detail = "Authentication Service Error",
                        headers = {"WWW-Authenticate": "Bearer"},
                    )

        except Exception as Error:
            sys.stdout.write(
                Colors.red(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                    Colors.underline(
                        "Authentication (Open-API) Failure Event"
                    ) + Colors.normalized("\n")
                )
            );
            sys.stdout.flush()

            sys.stdout.write(
                Colors.red(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ")
                + "User - " + Colors.bold(Data.username)
                + Colors.normalized("\n")
            );
            sys.stdout.flush()

            raise Error

        Scopes = SecurityScopes(Data.scopes)

        return Token.Type(access_token = JWT, token_type = Type, scopes = Scopes.scopes)

    @staticmethod
    @Generator.options("/Guarantee", status_code = 200)
    async def Preflight():
        return 200

    @staticmethod
    @Generator.post("/Guarantee", response_model = Optional[Dictionary])
    async def Serial(Data: Input):
        sys.stdout.write(
            Colors.yellow(
                "%s" % "[Nexus-API]"
            ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                Colors.underline(
                    "Authentication Request Event"
                ) + Colors.normalized("\n")
            )
        );
        sys.stdout.flush()

        try:
            if Data.Grant == "Password":
                sys.stdout.write(
                    Colors.yellow("%s" % "[Nexus-API]")
                    + ": " + Colors.italic("(Ingress) ")
                    + "Guarantee - %s" % Colors.bold(
                        Data.Username
                    ) + Colors.normalized("\n")
                );
                sys.stdout.flush()

                Account = await Authenticate(Username = Data.Username, Password = Data.Password)
                devtools.debug(Account)
                User = Interface.Table(Account, Database.User.Schemas.Nexus.Shard)
            else:
                raise NotImplementedError

            if not User:
                raise HTTPException(
                    status_code = status.HTTP_401_UNAUTHORIZED,
                    detail = "Incorrect Username or Password",
                    headers = {"WWW-Authenticate": "Bearer"},
                )

            Expiration = timedelta(minutes = Vault.Expiration)

            T = Generate(
                Data = {"sub": User.Username}, Expiration = Expiration
            );
            Type = "bearer"

        except Exception as Error:
            sys.stdout.write(
                Colors.red(
                    "%s" % "[Nexus-API]"
                ) + ": " + Colors.italic("(Ingress) ") + Colors.bold(
                    "%s" % Colors.bold(Data.Username)
                ) + " - " + Colors.italic("Failed Authentication Attempt")
                + Colors.normalized("\n")
            );
            sys.stdout.flush()

            raise Error

        Schema = Token.Type(access_token = T, token_type = Type)

        return JSON(
            Authorization(
                **{"JWT": Schema.access_token, "Type": Schema.token_type.capitalize()}
            ).dict(),
            200, {
                "X-Guarantee-Token":      Schema.access_token,
                "X-Guarantee-Type":       Schema.token_type.capitalize(),
                "X-Guarantee-Server":     "Nexus-API-Service",
                "X-Guarantee-User":       "%s" % User.Username,
                "X-Guarantee-Account-ID": "%s" % User.ID,
                "X-Guarantee-Scopes":     "%s" % "[Under-Development]"
            }
        )

    @Generator.post("/Deserialized")
    async def Deserialize(Authorization: String = Header(None)):
        """
        ...
        """

        Type = Database.User.Schemas.Nexus.Shard

        sys.stdout.write(
            Colors.yellow(
                "%s" % "[Nexus-API]"
            ) + ": " + Colors.italic("(Ingress) ")
            + Colors.underline("JWT Deserialization Event")
            + "\n"
        );
        sys.stdout.flush()

        if Authorization is not None:
            sys.stdout.write(
                Colors.yellow("%s" % "[Nexus-API]")
                + ": " + Colors.italic("(Ingress) ")
                + "Partial - %s" % Colors.bold(
                    Authorization.split(".")[-1]
                ) + Colors.normalized("\n")
            );
            sys.stdout.flush()
        else:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Authenticated Session Query Attempt",
                headers = {"WWW-Authenticate": "Bearer"}
            )

        if Account := await Database.User.Interfaces.User.API.HTTP.Account(Interface.Decode(Authorization)):
            User = Interface.Table(Account, Type)

            sys.stdout.write(
                Colors.yellow("%s" % "[Nexus-API]")
                + ": " + Colors.italic("(Ingress) ")
                + "User - %s" % Colors.bold(
                    User.Username
                ) + Colors.normalized("\n")
            );
            sys.stdout.flush()

            Schema = Token.Type(access_token = Authorization, token_type = "bearer")

            return JSON(
                Authorizer(
                    **{"JWT": Schema.access_token, "Type": Schema.token_type.capitalize()}
                ).dict(),
                200, {
                    "X-Guarantee-Token":      Schema.access_token,
                    "X-Guarantee-Type":       Schema.token_type.capitalize(),
                    "X-Guarantee-Server":     "Nexus-API-Service",
                    "X-Guarantee-User":       "%s" % User.Username,
                    "X-Guarantee-Account-ID": "%s" % User.ID,
                    "X-Guarantee-Scopes":     "%s" % "[Under-Development]"
                }
            )

        else:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Authenticated Session Query Attempt",
                headers = {"WWW-Authenticate": "Bearer"}
            )

    @Generator.post("/Information", response_model = Database.User.Schemas.Nexus.Identifier)
    async def Information(JWT: String):
        """
        ...
        """

        try: User = await Database.User.Interfaces.User.API.HTTP.Account(Interface.Decode(JWT))
        except Exception as Error:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Authenticated Session Query Attempt",
                headers = {"WWW-Authenticate": "Bearer"},
            )

        try:
            return User.pop()
        except AttributeError as Error:
            print("Error -- @Task")
            devtools.debug(Error)
            devtools.debug(User)
            return User

    @classmethod
    def Table(cls, Input, Type):
        if type(Input) == type([]):
            Object = vars(Input[0])
        else:
            Object = vars(Input)

        return Type(**Object)

Application.API.include_router(Interface.Generator,
    default_response_class = JSON,
    tags = [
        "Authentication"
    ]
)

__all__ = [
    "Interface"
]
