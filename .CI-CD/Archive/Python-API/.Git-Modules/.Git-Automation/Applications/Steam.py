#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

# Owner: Jacob B. Sanders
# Source: code.cloud-technology.io
# License: BSD 3-Clause License
# Copyright 2020 Cloud Hybrid & Affiliates
# Online IDE: https://repl.it/languages/python3

"""
Usage
=====
1. Navigate to the following link:
    - https://repl.it/languages/python3
2. Copy and paste the entirety of this
   script.
3. Click the button labled "Run".
"""

import json
import urllib.request

Admins = [
"LegacyAdmins=76561198000117133",   # FR1GHT
"LegacyAdmins=76561198132364921",   # heckingEDGY
"LegacyAdmins=76561198087919412",   # Kikinak
"LegacyAdmins=76561198051868607",   # Woohs
"LegacyAdmins=76561198117876947",   # Gunblast
"LegacyAdmins=76561198014463236",   # Noof
"LegacyAdmins=76561198139647290",   # єиѕιѕ
"LegacyAdmins=76561198236007414",   # Someone
"LegacyAdmins=76561198041972329",   # Dashoor
"LegacyAdmins=76561198197388197",   # Null-Byte
"LegacyAdmins=76561198370637452",   # Kulizen
"LegacyAdmins=76561198997637019",   # Segmentational
"LegacyAdmins=76561198119676403",   # Weenie
"LegacyAdmins=76561198088098008",   # Deze
"LegacyAdmins=76561198127067177",   # Xevuria
"LegacyAdmins=76561198084831525",   # Benghazi
"LegacyAdmins=76561198065887209",   # ßŁ₲ |KillsburyHoeboy
"LegacyAdmins=76561197994403841",   # Alice
"LegacyAdmins=76561198079441747",   # Yeetus
"LegacyAdmins=76561198016820211",   # Bandit
"LegacyAdmins=76561198093407344",   # Fredo
"LegacyAdmins=76561198069239211",   # Pope
"LegacyAdmins=76561198272121021",   # Mace
"LegacyAdmins=76561198214524733",   # Helo
"LegacyAdmins=76561197986907335",   # Jesus
"LegacyAdmins=76561198161992998",   # Doodle
"LegacyAdmins=76561198093067796",   # Sir Galahad
"LegacyAdmins=76561198061693868",   # Bumble
"LegacyAdmins=76561198158764587",   # hobo!
"LegacyAdmins=76561198070264149",   # Ankawi
"LegacyAdmins=76561198872208319"    # Idekae
]

CSV = ",".join(index.replace("LegacyAdmins=", "") for index in Admins.split())
List = CSV.split(",")
JSON = json.loads(urllib.request.urlopen("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=81A5077961FD8E2D1D478E315D73A5CC&steamids={}".format(CSV)).read().decode("UTF-8"))["response"]["players"]

Players = [Player["personaname"] for Player in JSON]

print("\n".join(List[Player] + ": " + Players[Player] for Player in range(0, len(Players) - 1)))