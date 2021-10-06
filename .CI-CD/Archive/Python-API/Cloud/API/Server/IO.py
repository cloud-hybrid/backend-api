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

import io
import os
import sys
import shlex
import subprocess

from . import *

import Cloud.Constants

FQDN = Cloud.Constants.Domain

CLIMIT = Cloud.Constants.CLIMIT

Extensions = {
    "c" : "c",
    "class": "java",
    "CPP": "c",
    "cpp": "c",
    "csv": "excel",
    "cxx": "c",
    "CXX": "c",
    ".db": "sql",
    "dpj": "java",
    "font": "font",
    "h": "c",
    "H": "c",
    "hpp": "c",
    "hdl": "c",
    "html": "html",
    "install": "bash",
    "Install": "bash",
    "java": "java",
    "log": "log",
    "Log": "log",
    "pl": "pearl",
    "PL": "pearl",
    "py": "python",
    "PY": "python",
    "Bash": "bash",
    "bash": "bash",
    "sh": "bash",
    "SH": "bash",
    "Shell": "bash",
    "shell": "bash",
    "php": "php",
    "htm": "html",
    "j2": "jinja",
    "jinja": "jinja",
    "Template": "jinja",
    "template": "jinja",
    "Jinja2": "jijnja",
    "DB": "sql",
    "sqlite": "sql",
    "SQL": "sql",
    "pyw": "python",
    "css": "css",
    "js": "javascript",
    "JS": "javascript",
    "javascript": "javascript",
    "jsp": "java",
    "part": "html",
    "rss": "rss",
    "xhtml": "xhtml",
    "wsf": "powershell",
    "com": "cmd",
    "xml": "xml",
    "dbf": "sql",
    "swift": "swift",
    "Swift": "swift",
    "vb": "visualbasic",
    "xls": "excel",
    "bak": "utf8",
    "cfg": "toml",
    "toml": "toml",
    "yaml": "yaml",
    "Yaml": "yaml",
    "YAML": "yaml",
    "md": "markdown",
    "Markdown": "markdown",
    "MD": "markdown",
    "TOML": "toml",
    "ini": "toml",
    "INI": "toml",
    "conf": "toml"
}

class Tree(Base):
    Generator = Blueprint("IO", __name__)
    Route = Base.Route + "IO"

    Methods = Base.Methods

    Description = """\
       ... ... ...
    """

    Metadata = {**{
        "Description"   : "{}".format(Description),
        "Title"         : "{}".format(Generator.name.replace("-", " ").title()),
        "Generator"     : "{}".format(Generator.name),
        "Page"          : "{}".format(Generator.name.casefold())
    }, **Base.Metadata}

    JSON = {"Parameters": None, "Code": 204, "Files": None, "File": None, "Directories": None, "Directory": None, "System": None, "Message": None, "Easter-Egg": None, "Content": None}

    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

    @staticmethod
    @Generator.route(Route + "/" + "Files", methods = Methods)
    # @Authenticate
    def Files(M = Metadata, mime: str = "application/json") -> Response(type({})):
        Usage = "Under Development"

        Parameters = {(Key := String(key).capitalize()): Value for key, Value in Request.args.items()} 

        if not any(Parameters.values()): 
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Cannot Specify Null Parameter",
                "Usage": Usage}
            }

        Directory: String = Parameters.get("Directory", None) + "/"

        if Directory == None:
            return {**Tree.JSON, **{
                "Code": 204,
                "Parameters": Parameters,
                "Message": "Directory Not Found",
                "Usage": Usage}
            }
        elif os.path.isdir(Directory) == False:
            return {**Tree.JSON, **{
                "Code": 206,
                "Parameters": Parameters,
                "Message": "Directory Not Found"}
            }
        else: Directory = os.path.dirname(Directory)

        if Directory == "/" or Directory == "//":
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Cannot Parse Root Directory",
                "Directory": "/",
                "Easter-Egg": "Chinn := Teapot"}
            }
        elif String(Directory)[0] == "/":
            Files = {
                "Names": next(os.walk(Directory))[-1],
                "Path": ["{}{}{}".format(
                    Directory,
                    "/" if Directory[-1] != "/" else "",
                    File) for File in next(os.walk(Directory))[-1]]
            }
        elif "///" in Directory or Directory[:2] == "//":
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Invalid Compounded Slashes",
                "Directory": "/",
                "Easter-Egg": "Chinn := Teapot"}
            }
        else:
            Files = {
                "Names": next(os.walk(Directory))[-1],
                "Path": Tuple(map(os.path.abspath, next(os.walk(Directory))[-1]))
            }

        if Directory[-1] == "/" and Directory[0] == "/":
            Directories = Directory.split("/")[1:-1]
        elif Directory[-1] == "/" and Directory[0] != "/":
            Directories = Directory.split("/")[:-1]
        elif Directory[-1] != "/" and Directory[0] == "/":
            Directories = Directory.split("/")[1:]
        else:
            Directories = Directory.split("/")
            
        Response = {
            **Tree.JSON,
            **{
                "Parameters": Parameters,
                "Directory": "{}".format(Directory),
                "Directories": Directories,
                "Files": Files,
                "Code": 200
            }
        }

        return Response

    @staticmethod
    @Generator.route(Route + "/" + "Directory", methods = Methods)
    # @Authenticate
    def Directory(M = Metadata, mime: str = "application/json") -> Response(type({})):
        Usage = "Under Development"

        Parameters = {(Key := String(key).capitalize()): Value for key, Value in Request.args.items()} 

        if not any(Parameters.values()): 
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Cannot Specify Null Parameter",
                "Usage": Usage}
            }

        Directory: String = Parameters.get("Directory", None)

        if Directory == None:
            return {**Tree.JSON, **{
                "Code": 204,
                "Parameters": Parameters,
                "Message": "Directory Parameter Required",
                "Usage": Usage}
            }
        elif os.path.isdir(Directory) == False:
            return {**Tree.JSON, **{
                "Code": 206,
                "Parameters": Parameters,
                "Message": "Directory Not Found"}
            }
        elif Directory == "/" or Directory == "//":
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Cannot Parse Root Directory",
                "Directory": "/",
                "Easter-Egg": "Chinn := Teapot"}
            }
        elif "///" in Directory or Directory[:2] == "//":
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Invalid Compounded Slashes",
                "Directory": "/",
                "Easter-Egg": "Chinn := Teapot"}
            }
        else: Directory = os.path.dirname(Directory + "/")

        if String(Directory)[0] == "/":
            Directories = {
                "Names": next(os.walk(Directory))[-2],
                "Path": ["{}{}{}".format(
                    Directory,
                    "/" if Directory[-1] != "/" else "",
                    File) for File in next(os.walk(Directory))[-2]]
            }
        else:
            Directories = {
                "Names": next(os.walk(Directory))[-2],
                "Path": Tuple(map(os.path.abspath, next(os.walk(Directory))[-2]))
            }
            
        Response = {
            **Tree.JSON,
            **{
                "Parameters": Parameters,
                "Directory": "{}".format(Directory),
                "Directories": Directories,
                "Code": 200
            }
        }

        return Response

    @staticmethod
    @Generator.route(Route + "/" + "Directories", methods = Methods)
    # @Authenticate
    def Directories(M = Metadata, mime: str = "application/json") -> Response(type({})):
        Usage = "Under Development"

        Parameters = {(Key := String(key).capitalize()): Value for key, Value in Request.args.items()} 

        if not any(Parameters.values()): 
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Cannot Specify Null Parameter",
                "Usage": Usage}
            }

        Directory: String = Parameters.get("Directory", None)

        if Directory == None:
            return {**Tree.JSON, **{
                "Code": 204,
                "Parameters": Parameters,
                "Message": "Directory Parameter Required",
                "Usage": Usage}
            }
        elif os.path.isdir(Directory) == False:
            return {**Tree.JSON, **{
                "Code": 206,
                "Parameters": Parameters,
                "Message": "Directory Not Found"}
            }
        elif Directory == "/" or Directory == "//":
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Cannot Parse Root Directory",
                "Directory": "/",
                "Easter-Egg": "Chinn := Teapot"}
            }
        elif "///" in Directory or Directory[:2] == "//":
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Invalid Compounded Slashes",
                "Directory": "/",
                "Easter-Egg": "Chinn := Teapot"}
            }
        else: Directory = os.path.dirname(Directory + "/")

        if String(Directory)[0] == "/":
            Directories = {
                "Names": next(os.walk(Directory))[-2],
                "Path": ["{}{}{}".format(
                    Directory,
                    "/" if Directory[-1] != "/" else "",
                    File) for File in next(os.walk(Directory))[-2]]
            }
        else:
            Directories = {
                "Names": next(os.walk(Directory))[-2],
                "Path": Tuple(map(os.path.abspath, next(os.walk(Directory))[-2]))
            }
            
        Response = {
            **Tree.JSON,
            **{
                "Parameters": Parameters,
                "Directory": "{}".format(Directory),
                "Directories": Directories,
                "Code": 200
            }
        }

        return Response

    @staticmethod
    @Generator.route(Route + "/" + "Parse", methods = Methods)
    # @Authenticate
    def Parse(Directory: String = None, File: String = None, M = Metadata, mime: str = "application/json") -> Response(type({})):
        Usage = "Under Development"

        Parameters = {(Key := String(key.casefold()).capitalize()): Value for key, Value in Request.args.items()}

        if not any(Parameters.values()): 
            return {**Tree.JSON, **{
                "Code": 403,
                "Parameters": Parameters,
                "Message": "Cannot Specify Null Parameter",
                "Usage": Usage}
            }

        File = Parameters.get("File", File)
        Directory: String = Parameters.get("Directory", Directory)

        if File == None and Directory == None:
            return {**Tree.JSON, **{
                "Code": 204,
                "Parameters": Parameters,
                "Message": "File or Directory Parameter(s) Required",
                "Usage": Usage}
            }

        if File == None: Single = False
        elif File[0] == "/": Single = True
        else: Single = False

        Directory = Directory + "/" if Single == False else Directory

        if Single == False and Directory == None:
            return {**Tree.JSON, **{
                "Code": 204,
                "Parameters": Parameters,
                "Message": "Directory Parameter Required",
                "Usage": Usage}
            }
        elif Single == False and os.path.isdir(Directory) == False:
            return {**Tree.JSON, **{
                "Code": 206,
                "Parameters": Parameters,
                "Message": "Directory Not Found"}
            }
        elif Single == False: Directory = os.path.dirname(Directory)
        #elif Directory == "//" or Directory == "/" or Directory[:2] == "//":
        #    return {**Tree.JSON, **{
        #        "Code": 403,
        #        "Parameters": Parameters,
        #        "Message": "Cannot Parse Root Directory",
        #        "Directory": "/",
        #        "Easter-Egg": "Chinn := Teapot"}
        #    }
        else:
            Directory = "/".join(File.split("/")[:-1])
            File = File.split("/")[-1]

        Single = Parameters.get("Single", Single)

        if Single == True or Single == "True" or Single == "true":
            process = subprocess.Popen(
                shlex.split("curl --silent http://0.0.0.0:5000/API/Server/IO/Files?Directory={}".format(
                    Directory
                )),
                stdin = io.open("/dev/null", "wb"),
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                text = True,
                shell = False,
                encoding = "UTF-8",
                universal_newlines = True
            ); process.wait(timeout = 15)

            Output, Error = process.communicate()

            Abstraction: Dictionary = json.loads(Output)

            assert type(Response) == type(Dictionary)

            Paths = Abstraction["Files"]["Path"]
            Folder = Abstraction["Directory"]
            Blob = Folder + "/" + File

            if os.path.isfile(Blob):
                try:
                    File = io.open(Blob, "r")
                except PermissionError as Error:
                    print("Permission Denied: {}".format(
                        Error
                    ))
                Content = File.read()
                File.close()
                return {**Abstraction, **{
                    "Code": 200,
                    "Parameters": Parameters,
                    "Content": Content}
                }
            else:
                return {**Abstraction, **{
                    "Code": 206,
                    "Parameters": Parameters,
                    "Message": "File Not Found"}
                }
        else:
            process = subprocess.Popen(
                shlex.split("curl --silent http://0.0.0.0:5000/API/Server/IO/Files?Directory={}".format(
                    Directory
                )),
                stdin = io.open("/dev/null", "wb"),
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                text = True,
                shell = False,
                encoding = "UTF-8",
                universal_newlines = True
            ); process.wait(timeout = 15)

            Output, Error = process.communicate()

            Abstraction: Dictionary = json.loads(Output)

            assert type(Response) == type(Dictionary)

            Paths = Abstraction["Files"]["Path"]
            Contents = {}
            Types = {}

            for Blob in Paths:
                Name = Blob.split("/")[-1]
                Type = Name.split(".")[-1]
                try:
                    File = io.open(Blob, "r")
                except PermissionError as Error:
                    print("Permission Denied: {}".format(
                        Error
                    )); continue
                try:
                    Content = File.read()
                except UnicodeDecodeError as Error:
                    Content = "Binary (Invalid Encoding)"
                finally:
                    File.close()
                Contents[Name] = Content
                try:
                    Types[Name] = Extensions[Type] if len(Name.split(".")) == 2 else "toml"
                except KeyError as Error:
                    Types[Name] = None

            return {**Abstraction, **{
                    "Code": 200,
                    "Parameters": Parameters,
                    "Content": Contents,
                    "Mode": Types}
                }

    @staticmethod
    @Generator.route(Route + "/" + "Commit", methods = Methods)
    def Commit(M = Metadata, mime: str = "application/json") -> Response(type({})):
        if Request.method == "POST":
            Abstraction = json.loads(Request.data)
            
            File = io.open(
                Abstraction["Path"] \
                + "/" \
                + Abstraction["File"], "w"
            ); File.write(Abstraction["Content"])
            File.close()

            Reader = io.open(
                Abstraction["Path"] \
                + "/" \
                + Abstraction["File"], "r"
            ); Content = Reader.read()

            print(Content)

            return Response("Successful", status = 200)
        else:
            return Response("Invalid Method", status = 405)
