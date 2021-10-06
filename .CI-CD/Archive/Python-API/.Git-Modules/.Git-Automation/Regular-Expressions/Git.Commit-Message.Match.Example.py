#!/usr/bin/env python3

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  *.Yaml -*- #

# Owner:    Jacob B. Sanders
# Source:   code.cloud-technology.io
# License:  BSD 3-Clause License

#
# Copyright 2020 Jacob B. Sanders - Cloud Hybrid LLC. & Affiliates
#
# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:
#
# 1.  Redistributions of source code must retain the above copyright notice, this list of
#     conditions and the following disclaimer.
#
# 2.  Redistributions in binary form must reproduce the above copyright notice, this list of
#     conditions and the following disclaimer in the documentation and/or other materials
#     provided with the distribution.
#
# 3.  Neither the name of the copyright holder nor the names of its contributors may be used
#     to endorse or promote products derived from this software without specific prior written
#     permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.

#
# =================================================================================================
# Git Commit Message Parsing                                          (Regular Expression Example)
# =================================================================================================
#

import re

Expression = R"^.*?((\[|\])({0})(\[|\]))\s*?(-|:|\s\s*?)?(\[|\])?\W*(.*$)".format(
    "Coverage|Code-Quality|Syntax"
)

Collection = "\n".join(_ for _ in [
    "[Coverage] Single ' ' Split",
    "Project Build & [Coverage] - Reporting",
    "[Syntax] : Reporting"
])

Flags = re.IGNORECASE | re.MULTILINE | re.UNICODE | re.VERBOSE

Regression = re.finditer(Expression, Collection, Flags)

for enumeration, match in enumerate(Regression, start = 1):
    print("Match-{Index} \t {Start}-{End} \t\t {Match}".format(
        Index   = enumeration,
        Start   = match.start(),
        End     = match.end(),
        Match   = "'" + match.group() + '"'
            if match.group() else ''
    ))
    for Group in range(1, len(match.groups()) + 1):
        if match.group(Group): print(
        "Group-{Enumeration}.{Index} \t {Start}-{End} \t\t {Group}".format(
            Enumeration = enumeration,
            Index   = Group,
            Start   = match.start(Group),
            End     = match.end(Group),
            Group   = '"' + match.group(Group) + '"'
                if match.group(Group) else "''"
        ), end = "\n")

    print()
