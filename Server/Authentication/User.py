"""
...
"""

from . import *

import pydantic

Scheme = pydantic.BaseModel

class Base(Model):
    """
    ...
    """

    Username: String
    Email: String
    Name: Optional[String] = None
    Disabled: Optional[Boolean] = None

class Record(Base):
    """
    An Established User in the Database
    """

    Password: String

class Input(Scheme):
    Username:   String
    Password:   String

    Grant:      String = "Password"

class Authorization(Scheme):
    JWT:    String

    Type:   String = "Bearer"

__all__ = [
    "User",
    "Record",
    "Input"
]
