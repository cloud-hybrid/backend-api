#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner:    Jacob B. Sanders
# Source:   code.cloud-technology.io
# License:  BSD 2-Clause License

"""
OAuth2-based Authentication via Password (Hashed), Bearer + JWT

In order to generate a URL-safe token:

    >>> # --> Bash $ openssl rand -hex 32
    >>> # ... Python Composition
    >>>
    >>> import subprocess
    >>> import shlex
    >>> import sys
    >>>
    >>> Command = "openssl rand -hex 32"
    >>> _ = subprocess.Popen(shlex.split(Command),
    ...     stderr      =   subprocess.PIPE,
    ...     stdin       =   subprocess.DEVNULL,
    ...     stdout      =   subprocess.PIPE,
    ...     shell       =   False,
    ...     encoding    =   "UTF-8"
    ... )
    >>>
    >>> while _.wait(30): _.poll()
    >>>
    >>> sys.stdout.write(_.communicate()[0].splitlines().pop())

Security -- Password-Flow
=========================

-   The password "flow" is one of the ways ("flows") defined in OAuth2, to handle security and
    authentication.
-   OAuth2 was designed so that the backend or API could be independent of the server that
    authenticates the user.
-   But in this case, the same FastAPI application will handle the API and the authentication.

Summary
-------
-   The user types the username and password in the frontend, and hits Enter.
-   The frontend (running in the user's browser) sends that username and password to a specific URL
    in our API (declared with tokenUrl="token").
-   The API checks that username and password, and responds with a "token".
    -   A "token" is just a string with some content that we can use later to verify this user.
    -   Normally, a token is set to expire after some time.
        -   So, the user will have to log in again at some point later.
        -   And if the token is stolen, the risk is less. It is not like a permanent key.
-   The frontend stores that token temporarily somewhere.
-   The user clicks in the frontend to go to another section of the frontend web app.
-   The frontend needs to fetch some more data from the API.
    -   But it needs authentication for that specific endpoint.
    -   So, to authenticate with our API, it sends a header Authorization with a value of Bearer
        plus the token.

Validating a JWT
----------------
When validating a JWT, the following steps are performed.  The order
of the steps is not significant in cases where there are no
dependencies between the inputs and outputs of the steps.  If any of
the listed steps fail, then the JWT MUST be rejected -- that is,
treated by the application as an invalid input.

Procedure:

    1. Verify that the JWT contains at least one period ('.')
    character.

    >>> import re
    >>>
    >>> regex = r"^.*?(\.{1})"
    >>> jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    >>> matches = re.finditer(regex, jwt, re.MULTILINE)
    >>>
    >>> for index, match in enumerate(matches, start = 1):
    >>>     print("Match {0} was found at {1}-{2}: {3}".format(
    ...         index,
    ...         match.start(),
    ...         match.end(),
    ...         match.group()
    ...     ))
    >>>     for group in range(0, len(match.groups())):
    >>>         group = group + 1
    >>>         print("Group {0} found at {1}-{2}: {3}".format(
    ...             group,
    ...             match.start(group),
    ...             match.end(group),
    ...             match.group(group)
    ...         ))

    2.  Let the Encoded JOSE Header be the portion of the JWT before the
    first period ('.') character.

    3.  Base64url decode the Encoded JOSE Header following the
    restriction that no line breaks, whitespace, or other additional
    characters have been used.

    4.  Verify that the resulting octet sequence is a UTF-8-encoded
    representation of a completely valid JSON object conforming to
    RFC 7159 [RFC7159]; let the JOSE Header be this JSON object.

    5.  Verify that the resulting JOSE Header includes only parameters
    and values whose syntax and semantics are both understood and
    supported or that are specified as being ignored when not
    understood.

    6.  Determine whether the JWT is a JWS or a JWE using any of the
    methods described in Section 9 of [JWE].

    7.  Depending upon whether the JWT is a JWS or JWE, there are two
    cases:

        *   If the JWT is a JWS, follow the steps specified in [JWS] for
        validating a JWS.  Let the Message be the result of base64url
        decoding the JWS Payload.

        *   Else, if the JWT is a JWE, follow the steps specified in
        [JWE] for validating a JWE.  Let the Message be the resulting
        plaintext.

    8.  If the JOSE Header contains a "cty" (content type) value of
    "JWT", then the Message is a JWT that was the subject of nested
    signing or encryption operations.  In this case, return to Step
    1, using the Message as the JWT.

    9.  Otherwise, base64url decode the Message following the
    restriction that no line breaks, whitespace, or other additional
    characters have been used.

    10. Verify that the resulting octet sequence is a UTF-8-encoded
    representation of a completely valid JSON object conforming to
    RFC 7159 [RFC7159]; let the JWT Claims Set be this JSON object.

    Finally, note that it is an application decision which algorithms may
    be used in a given context.  Even if a JWT can be successfully
    validated, unless the algorithms used in the JWT are acceptable to
    the application, it SHOULD reject the JWT.

References
----------
- https://fastapi.tiangolo.com/tutorial/security/first-steps/

"""

# =============================================================================
# Standard Library
# =============================================================================

import os
import sys
import typing
import pkgutil
import datetime
import textwrap
import dataclasses

# =============================================================================
# External
# =============================================================================

import json

import fastapi
import fastapi.security

import jose
import jose.jwt

import passlib.context

import pydantic

import starlette.config
import starlette.exceptions
import starlette.responses

# =============================================================================
# Local Imports
# =============================================================================

import Server

# =============================================================================
# Type Declarations & Importable(s)
# =============================================================================

String = str
Integer = int
Boolean = bool
Dictionary = dict
Array = tuple
List = list

Any = typing.Any
Optional = typing.Optional
Date = datetime.datetime
Delta = datetime.timedelta

Cryptext = passlib.context.CryptContext

Model = pydantic.BaseModel
Field = pydantic.Field
Secret = pydantic.SecretStr
URL = pydantic.HttpUrl

JWTError = jose.jwt.JWTError
JWT = jose.jwt

CWD = os.path.abspath(os.path.dirname(__file__))

Configuration = starlette.config.Config(env_file = CWD + os.sep + ".env")

JSON = json # ... starlette.responses.UJSONResponse

Error = starlette.exceptions.HTTPException

Environment = lambda _, default, typecast: Configuration.get(_, typecast, default)

Security = fastapi.security
Status = fastapi.status
Base = Server.Base
Body = fastapi.Body

Application = Base(host = "0.0.0.0", port = 3000)

Data = json.loads(pkgutil.get_data("API", "Environment.json"))
Package = Data["Authentication"]

# =============================================================================
# Packaged Exports
# =============================================================================

import abc

class Request(abc.ABCMeta):
    """
    Implicit Instance Idiom
    """

    Prefix = "/API"

    Tags = [
        "Authentication"
    ]

    Generator = Application.Generator

    __dict__ = None
    __slots__ = ()
    __call__ = ()
    __new__ = ()

Format = textwrap.dedent

@dataclasses.dataclass(frozen = True, unsafe_hash = True, init = False)
class Vault:
    """
    ...

    Properties:
        Key: (String) - Secret, URL-Safe Token.
            - Default: ******
        Algorithm: (String) - Cryptography, Hashing Algorithm.
            - Default: "HS256"
        Expiration: (Integer) - Expiration Time, in Minutes.
            - Default: 60 Minutes
    """

    Key: String = Package.get("Key")
    Algorithm: String = Package.get("Algorithm")
    Expiration: Integer = Integer(Package.get("Expiration"))

__all__ = [
    "String",
    "Integer",
    "Boolean",
    "Dictionary",
    "Array",
    "List",
    "Any",
    "Application",
    "Optional",
    "Date",
    "Delta",
    "Cryptext",
    "Model",
    "Field",
    "Secret",
    "URL",
    "JWTError",
    "JWT",
    "CWD",
    "Configuration",
    "Environment",
    "Security",
    "Status",
    "Vault",
    "Request",
    "Format",
    "Base",
    "JSON",
    "Body",
    "Error"
]
