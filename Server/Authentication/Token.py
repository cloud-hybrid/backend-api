"""
...
"""

from . import *

from typing import Union, Optional

import dataclasses
import pydantic

from fastapi.security import SecurityScopes

Scheme = pydantic.BaseModel

__module__ = __name__

Serialization = {
    "skipkeys":               True,
    "ensure_ascii":           True,
    "check_circular":         True,
    "allow_nan":              True,
    "indent":                 4,
    "separators":             (", ", ": "),
    "sort_keys":              True,
    "encode_html_chars":      True,
    "escape_forward_slashes": True
}

Dump = lambda _: JSON.dumps(_, **Serialization)

class Standard(Scheme):
    aud: String
    iat: String
    exp: String
    nbf: String
    iss: String
    sub: String
    jti: String

class Model(Scheme):
    """
    ...
    """

    class Configuration(Scheme.Config):
        """
        ...
        """

        title = None

        orm_mode = False

        allow_population_by_field_name = True

        json_loads = JSON.loads
        json_dumps = Dump

class Type(Model):
    access_token: str
    token_type: str
    scopes: Optional[Union[str, list]] = None

    class Config(Model.Configuration):
        title = "O-Authentication-2-Schema"

class Bearer(Model):
    Token: str

    class Config(Model.Configuration):
        title = "Token-Bearer-Schema"

class JWT(Model):
    """
    ...
    """

    Token: String
    Type: String

class Serial(Model):
    JWT: String
    Type: String

class Basic(Model):
    """
    ...
    """

    ID: String
    Token: String
    Type: String
    Username: String

class Password(Model):
    """
    ...
    """

    Username: String
    Password: String

class Data(Model):
    """
    ...
    """

    Username: Optional[String] = None

__all__ = [
    "JWT",
    "Data",
    "Basic",
    "Password"
]
