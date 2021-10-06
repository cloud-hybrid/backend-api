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


```
>>> Defaults = {
...     "ENV": None,
...     "DEBUG": None,
...     "TESTING": False,
...     "PROPAGATE_EXCEPTIONS": None,
...     "PRESERVE_CONTEXT_ON_EXCEPTION": None,
...     "SECRET_KEY": None,
...     "PERMANENT_SESSION_LIFETIME": timedelta(days=31),
...     "USE_X_SENDFILE": False,
...     "SERVER_NAME": None,
...     "APPLICATION_ROOT": "/",
...     "SESSION_COOKIE_NAME": "session",
...     "SESSION_COOKIE_DOMAIN": None,
...     "SESSION_COOKIE_PATH": None,
...     "SESSION_COOKIE_HTTPONLY": True,
...     "SESSION_COOKIE_SECURE": False,
...     "SESSION_COOKIE_SAMESITE": None,
...     "SESSION_REFRESH_EACH_REQUEST": True,
...     "MAX_CONTENT_LENGTH": None,
...     "SEND_FILE_MAX_AGE_DEFAULT": timedelta(hours=12),
...     "TRAP_BAD_REQUEST_ERRORS": None,
...     "TRAP_HTTP_EXCEPTIONS": False,
...     "EXPLAIN_TEMPLATE_LOADING": False,
...     "PREFERRED_URL_SCHEME": "http",
...     "JSON_AS_ASCII": True,
...     "JSON_SORT_KEYS": True,
...     "JSONIFY_PRETTYPRINT_REGULAR": False,
...     "JSONIFY_MIMETYPE": "application/json",
...     "TEMPLATES_AUTO_RELOAD": None,
...     "MAX_COOKIE_SIZE": 4093
... }
```

Arrays
======
[`Arrays`] module defines an object type which can compactly represent an array of basic values:
- characters
- integers
- floats

Arrays are sequence types and behave very much like lists, except that the type of objects stored in them
is constrained. The type is specified at object creation time by using a type code, which is a single character.

"""

import sys; sys.pycache_prefix = ".PYC"

System = sys

import os
import json
import uuid
import array
import base64
import typing
import hashlib
import sqlite3
import builtins
import datetime
import textwrap
import collections
import dataclasses

import Cloud.JWT as JWT

_Type_Codes = array.typecodes

CLIMIT = 72

# === Web-Server === #
Company     = os.getenv("FQDN");            assert Company      != None
Shortname   = os.getenv("NAME");            assert Shortname    != None
FQDN        = os.getenv("ABBREVIATION");    assert FQDN         != None

Domain      = "https://{}".format(FQDN)
HTTP        = "http://0000"
Port        = 5000

# --- Type-Hinting --- #
Integer = builtins.int
Array   = array.array
Bytes   = builtins.bytes
String  = builtins.str
Tuple   = builtins.tuple
Pointer = builtins.memoryview
Object  = typing.NamedTuple
SQL     = sqlite3

Truth       = lambda Argument: String(Argument) in (True, 1, String(1), String(1).encode("UTF-8"), String(True), String(True).casefold(), String(True).encode("UTF-8"), String(True).upper())
NTruth      = lambda Argument: String(Argument) in (False, 0, String(0), String(0).encode("UTF-8"), String(False), String(False).casefold(), String(False).encode("UTF-8"), String(False).upper())

Dedentation = textwrap.dedent

# --- Base Types --- #

List        = list
Dictionary  = dict
Mapping     = map
Data        = dataclasses.dataclass
Item        = dataclasses.field
Field       = dataclasses.Field
JSON        = json

Base = Object("Base",
    Token   = Pointer,
    Key     = Pointer,
    JWN     = Pointer
)

JSID = bytes(list(map(ord, *zip(*"-".join(_ := map("".join, zip(*[iter("{}".format(uuid.uuid4().hex) + "{}".format(uuid.uuid1().hex))]*8))).upper()))))

class Cryptic(Base):
    """ \
    * Python +3.6 Required

    Object Abstract Constructor
    ===========================

    - https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/

    - https://docs.python.org/3/extending/newtypes.html

    Memoryviews in Python
    ---------------------
    `memoryview` objects allow Python code to access the internal data of an object that supports the buffer protocol without
    copying. The memoryview() function allows direct read and write access to an object's byte-oriented data without needing to
    copy it first.

    Buffers & Buffer Interfaces
    ---------------------------

    Certain objects available in Python wrap access to an underlying memory array or buffer.
    Such objects include the built-in bytes and bytearray, and some extension types like array.array.
    Third-party libraries may define similiar types for special purposes, such as image processing or numeric analysis.

    While each of these types have their own semantics, they share the common characteristic of being backed by a
    possibly large memory buffer. It is then desirable, in some situations, to access that buffer directly and without intermediate
    copying.

    Python provides such a facility at the C level in the form of the buffer protocol. This protocol has two sides (as buffers should):

    - Producer: A type can export a “buffer interface” which allows objects of that type to expose information about their underlying buffer.
                This interface is described in the section Buffer Object Structures.
    - Consumer: buffer, consumer types have several means that're are available to obtain a pointer to the raw underlying data of an object
                (for example a method parameter).

    In both cases, `PyBuffer_Release()` must be called when the buffer isn’t needed anymore. Failure to do so could lead to various issues
    such as resource leaks.

    Buffer structures (or simply “buffers”) are useful as a way to expose the binary data from another object to the Python programmer.
    They can also be used as a zero-copy slicing mechanism. Using their ability to reference a block of memory, it is possible to expose any
    data to the Python programmer quite easily. The memory could be a large, constant array in a C extension, it could be a raw block of memory
    for manipulation before passing to an operating system library, or it could be used to pass around structured data in its native, in-memory
    format.

    Class Instantiation
    -------------------

    ```
    >>> Base = Constructor("Cryptic",
    ...     Name = String,

    ...     Token = MemoryView[Bytes(String)],
    ...     Key = MemoryView[Bytes(String)],
    ...     JWN = MemoryView[Bytes(String)]
    ... )
    >>> class Cryptic(Base): ()
    >>> Instantiation = Cryptic(String, String, String)
    ```

    The resulting class has an extra `Fields` attribute that's
    subclassed from `NamedTuple.__annotations__`.

    ```
    >>> Hash.Fields
    { Algorithm: "String", Secret: memoryview(...) }
    ```

    Dot-Product Access
    ------------------

    ```
    >>> Hash = Vault("Hash",
    ...     Algorithm = str,
    ...     Secret = memoryview
    ... )
    ```

    Cross-site Request Forgery (CSRF)
    ---------------------------------
    To protect against cross-site request forgery, a unique token is generated when the user is presented with a form and then validating that
    token before the POST data is processed.

    1. Generate CSRF Token during a GET request to the Form.
    2. Inject token into a hidden input field that's apart of the Form.
    3. During the POST handling process, the CSRF token is first valided
       before any POST data has been processed.

    The contents of the CSRF string could be of a JWT... Is that still CSRF? Anyways, the
    contents of the token are derived from a specific, custom claim established in the User's
    JWT token, a time-based UUID-Hex, and then such a combination is finally hashed.

    """

    @staticmethod
    def JTI():
        return Cryptic.Serialize(bytes(list(map(ord, *zip(*"-".join(_ := map("".join, zip(*[iter("{}".format(uuid.uuid4().hex))]*8))).upper())))))

    @property
    def JSID(self):
        return bytes(
            List(Mapping(ord, *zip(
            *"-".join(
                _ := map(
                    "".join,
                    zip(*[iter("{}".format(
                        uuid.uuid4().hex) + "{}".format(
                            uuid.uuid1().hex)
                        )] * 8)
            )).upper()))))

    @staticmethod
    def Serialize(_: Bytes) -> String:
        try:
            return base64.urlsafe_b64encode(_).decode("UTF-8")
        except:
            return base64.urlsafe_b64encode(Cryptic.Dereference(_)).decode("UTF-8")

    @staticmethod
    def Deserialize(_: String) -> String:
        try:
            return base64.urlsafe_b64decode(_).decode("UTF-8")
        except TypeError as Error:
            base64.urlsafe_b64decode(Bytes(_)).decode("UTF-8")


    @staticmethod
    def Dereference(_: Pointer) -> Bytes:
        return Array("b", _).tobytes()

    @staticmethod
    def Reference(Object: String):
        """ Please note most implementations of `memoryview` objects create a Read-Only,
        Contiguous representation of a given Python object. The following method, rather,
        instantiates and asserts an immutable form from a given string: an abstraction
        that would be otherwise unknown if readonly or writable, or decoupled via lower
        level Python methods.

        Such is important during the loading of Flask, or any API implementing secrets
        whilst an application runs start-up sequences. For example, take a container
        deploying a web application; a C extension containing a given secret is instantiated
        as a structure with the RESTRICTED flag. Once the run-time program is ready,
        PyMemberDef's RESTRICTED flag is lifted, the value of the object is derived and
        encrypted, and then the memory address of the pointer is released. Such drastically
        decreases the ability to read the secret instantiated from the C module in plaintext.

        Additionally, if a malacious user were to access the host server and try to read the
        plaintext, the object could be a randomly generated value encrypted via a public
        symetric encryption key where the the private key is located off-site; upon a restart
        of a server, a simple pre-webserver could be spun up and accessed via HTML prompting
        for the private key coupled with the User's private password. Once validated, the pre-
        webserver is shutdown the runtime start-up sequences are able to begin.

        Example
        =======
        ```Python
        >>> import array; Array = import array & array.array
        >>> import builtins; Bytes = builtins.bytes

        >>> Mutable = memoryview(Array("b", map(ord, *zip(*"Hello"))))
        >>> Immutable = memoryview(bytes(map(ord, *zip(*"Hello"))))

        >>> print(Mutable.readonly & Mutable.contiguous)
        False
        >>> print(Immutable.readonly & Immutable.readonly)
        True
        ```
        """

        return Pointer(Bytes(map(ord, *zip(*Object))))

class Singleton:
    """ Singleton
    -------------

    Thread-Unsafe Helper Class.

    The target singleton should be decorated via `@Singleton` rather than
    instantiated as a subclass.

    The decorated class can define one `__init__` function that
    takes only the `self` argument; the decorated class cannot be subclassed
    from.

    """

    def __init__(self, target):
        self.target = target

    def instance(self):
        """ \
        Return a `Singleton` Instance
        -----------------------------
        Upon call, a Singleton will create a new instance of the decorated class
        via calling its `__init__` initializer. On all subsequent calls, the already created
        instance is returned.
        """

        try:
            return self.instance
        except AttributeError:
            return (self.target,)

    def instantiation(self): return (self.target,)

    def __call__(self):
        raise TypeError("Type Error: Member Access := `*.instance`")

# --- Flask --- #
UPLOAD_FOLDER                   = "/tmp"
DEBUG                           = True
SERVER_NAME                     = None #"{}".format(FQDN)
ENV                             = "Development".casefold()
MAX_CONTENT_LENGTH              = 16 * 1024 * 1024
SESSION_COOKIE_SECURE           = True
SESSION_COOKIE_SAMESITE         = "Lax"
TEMPLATES_AUTO_RELOAD           = True
TESTING                         = True
USE_X_SENDFILE                  = False
EXPLAIN_TEMPLATE_LOADING        = True

SECRET_KEY                      = "8fNcZeooxruODPkR-FqawAFR1l5P9bFU8rsk-j0aBOvAkbWbXdGx212ZV-uGLpilLMZ4xMSl77dqBs3K9ShkhDY-98g7MGahcBFlpqe-yImmp0HKN5XQUcLXBnKwe0eEfoxruODPkR-Fqaw"

# --- Jinja --- #
Jinja = {
    "CACHE"     : {},
    "OPTIONS"   : {},
    "RELOAD"    : TEMPLATES_AUTO_RELOAD
}

# --- AWS --- #
AWS_ACCESS_KEY_ID       = r"AKIA6J4BIWNGXAF6DJCR"
AWS_SECRET_ACCESS_KEY   = r"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"
AWS_DEFAULT_REGION      = "us-east-2"
AWS_DEFAULT_OUTPUT      = "json"

Vault: Cryptic = Cryptic(
    Cryptic.Serialize(
        Cryptic.Reference(
            "5XQUcLXBnKwe0eEfoxruOkbWbXdGx212ZV_uGLpilLM"
        )
    ),
    Cryptic.Serialize(
        Cryptic.Reference(
            "8fNcZeoAFR1l5P9bFU8rsk-j0aBOvAHKNZ4xMSl77dqBs3K9ShkhDY_98g7MGahcBFlpqe_yImmp0DPkR-Fqaw"
        )
    ),
    Cryptic.Serialize(
        Cryptic.Reference(
            "{}".format(hashlib.pbkdf2_hmac("SHA512", JSID, bytes(0), 1))
        )
    )
)

# --- Web-Server Settings --- #
Configuration = {
    "UPLOAD_FOLDER"                 : UPLOAD_FOLDER,
    "DEBUG"                         : DEBUG,
    "ENV"                           : ENV,
    "MAX_CONTENT_LENGTH"            : MAX_CONTENT_LENGTH,
    "SECRET_KEY"                    : SECRET_KEY,
    "SESSION_COOKIE_SAMESITE"       : SESSION_COOKIE_SAMESITE,
    "SESSION_COOKIE_SECURE"         : SESSION_COOKIE_SECURE,
    "EXPLAIN_TEMPLATE_LOADING"      : EXPLAIN_TEMPLATE_LOADING,
    "TEMPLATES_AUTO_RELOAD"         : TEMPLATES_AUTO_RELOAD,
    "TESTING"                       : TESTING,
    "USE_X_SENDFILE"                : USE_X_SENDFILE,
    "EXPLAIN_TEMPLATE_LOADING"      : EXPLAIN_TEMPLATE_LOADING,
    "SERVER_NAME"                   : SERVER_NAME
}

# --- Unicode Wrapper --- #
def Unicode(cls):
    cls.__unicode__ = cls.__str__
    cls.__str__ = lambda _: _.__unicode__().encode("UTF-8")
    return cls

# --- Responses --- #
HTTP_STATUS_CODES = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    306: "Switch Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Entity Too Large",
    414: "Request URI Too Long",
    415: "Unsupported Media Type",
    416: "Requested Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    449: "Retry With",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Failed",
}
