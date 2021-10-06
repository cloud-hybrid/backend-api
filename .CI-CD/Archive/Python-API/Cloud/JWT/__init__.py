#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

"""
JSON Web Token Interface

"""


__title__ = "JWT"
__version__ = "1.0.0"
__author__ = ""
__license__ = "MIT"
__copyright__ = "Copyright"


from .api_jws import PyJWS
from .api_jwt import (
    PyJWT,
    decode,
    encode,
    get_unverified_header,
    register_algorithm,
    unregister_algorithm,
)
from .exceptions import (
    DecodeError,
    ExpiredSignature,
    ExpiredSignatureError,
    ImmatureSignatureError,
    InvalidAlgorithmError,
    InvalidAudience,
    InvalidAudienceError,
    InvalidIssuedAtError,
    InvalidIssuer,
    InvalidIssuerError,
    InvalidSignatureError,
    InvalidTokenError,
    MissingRequiredClaimError,
    PyJWTError,
)
