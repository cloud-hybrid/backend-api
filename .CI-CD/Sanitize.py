import os
import sys
import json
import pprint
import shutil
import configparser

CWD = os.path.abspath(os.path.dirname(__file__))

Glob = sys.argv.pop()

Copy = Configuration = CWD + os.sep + Glob
Title = Copy = Glob.split(".")[0]
Sanitation = ".".join([Title, "Sanitized", "ini"])

Source = open(Configuration, "r")
Target = open(os.path.join(CWD, Sanitation), "w+")
API    = open(os.path.join(CWD, "API" + os.sep + ".".join([Title, "json"])), "w+")

Parser = configparser.ConfigParser()
Parser.read(Configuration)

Data = {}
Secrets = []

for Section in Parser.sections():
    Data[Section] = {}
    for Key, Value in Parser[Section].items():
        if Key.title() == "Secret":
            Secrets.extend(Value.lstrip().rstrip().split())
        else:
            Data[Section][Key.title()] = Value

for Line in Source.readlines():
    Contents = Line
    for Secret in Secrets:
        if Secret in Contents:
            Contents = Contents.replace(Secret, "*" * len(Secret))
    Target.write(Contents)

Source.close()
Target.close()

JSON = json.dump(Data, API, separators = (", ", ": "), indent = 4, sort_keys = True)
