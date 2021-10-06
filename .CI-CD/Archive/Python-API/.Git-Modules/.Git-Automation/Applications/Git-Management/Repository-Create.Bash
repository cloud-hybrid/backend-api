#!/bin/bash --posix

# -*- Coding: UTF-8 -*-
# -*- System: Linux -*-
# -*- Usage:   *.*  -*-

# Owner: Jacob B. Sanders
# Source: code.cloud-technology.io
# License: BSD 3-Clause License

#
# Copyright 2020, Jacob B. Sanders - Cloud Hybrid LLC. & Affiliates
#
# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:
#
# 1.  Redistributions of source code must retain the above copyright notice, this list of
#     conditions and the following disclaimer.
#
# 2.   Redistributions in binary form must reproduce the above copyright notice, this list of
#      conditions and the following disclaimer in the documentation and/or other materials
#      provided with the distribution.
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

#
# ========================================================================
# Git-Create Script
# ========================================================================
# Usage & Example(s)
# ------------------------------------------------------------------------
# >>> ./Repository-Create.Bash [ HTTPS || SSH ] [ HOST ] [ NAMESPACE ] [ REPOSITORY ]
# EX) ./Repository-Create.Bash HTTPS code.cloud-technology.io Node Fargate-Node-JS
#
# >>> echo "Y" | ./Git-Create.Bash [ HTTPS || SSH ] [ HOST ] [ NAMESPACE ] [ REPOSITORY ]
#
# ... /Cloud/Development/...
# ... └── License
# ...     ├── Directory
# ...     │     └── True
# ...     └── LICENSE
#

# --------------------
# Terminal Formatting
# --------------------

EOM="\\33[0m"

R="\\33[91m" # --> Red
G="\\33[32m" # --> Green
B="\\33[34m" # --> Blue

Y="\\33[33m" # --> Yellow
Z="\\33[90m" # --> Grey

X="\\33[0m"  # --> Reset
D="\\33[2m"  # --> Dim
L="\\33[4m"  # --> Link
H="\\33[1m"  # --> Bold (Highlight)
I="\\33[3m"  # --> Italicize
S="\\33[7m"  # --> Select

U="\\033[4m" # --> Underline

# --------------------------
# F-String STDOUT Functions
# --------------------------

OOP() {
    grep "${1}" Environment.Properties |
        cut -d'=' -f2 |
        sed -e 's/^"//' -e 's/"$//'
}

Print()     { printf "%s\n" "${@}";     }

Clear()     { printf "%s" "${@}";       }

Tabular()   { printf "%s" "    ";       }
Dim()       { printf "%s" "${@}";       }
Bold()      { printf "%s" "${@}";       }
Underline() { printf "%s" "${@}";       }
Error()     { printf "%s\n" "${@}";     }
Auxiliary() { printf "%s\n" "${@}";     }
Success()   { printf "%s\n" "${@}";     }
Warning()   { printf "%s\n" "${@}";     }
Tab()       { printf "\\t%s" "${@}";    }
Line()      { printf "\\n%s" "${@}";    }
Focus()     { printf "%s" "${@}";       }

Message()   { printf "\n$(Bullet)%s" "${1}$(printf "\e[A\e[K\n")"; }

Title()     { printf "$(Clear)%s\n" "${@}"; }

Format ()   { printf "%s" "${1}" | tr "[:upper:]" "[:lower:]"; }

# -----------------
# Global Variables
# -----------------

COLON="$( Dim ": " )"
ELLIPSI="$( Dim " ... " )"
CWD="$( cd "\$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# ---------------------
# User Input Arguments
# ---------------------

SCHEMA="$( Format "${1}" )"
HOST="$( Format "${2}" )"
NAMESPACE="$( Format "${3}" )"
PROJECT="${4}"
DIRECTORY="${5}"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

URI=()

[[ "${SCHEMA}" == "https" ]] &&
    URI+=("https://")
[[ "${SCHEMA}" == "ssh" ]] &&
    URI+=("git@")
[[ "${SCHEMA}" == "" ]] &&
    URI+=("https://")

[[ "${HOST}" == "" ]] &&
    URI+=("code.cloud-technology.io")
[[ "${HOST}" != "" ]] &&
    URI+=("${HOST}")

[[ "${NAMESPACE}" == "" ]] &&
    URI+=("/")
[[ "${NAMESPACE}" != "" ]] &&
    URI+=("/${NAMESPACE}/")

[[ "${PROJECT}" == "" ]] &&
    URI+=("")
[[ "${PROJECT}" != "" ]] &&
    URI+=("${PROJECT}")

REPO="${URI[0]}${URI[1]}${URI[2]}${URI[3]}${URI[4]}.git"

git init . && git add . && git commit -m "Initialization"

echo "Repository: ${REPO}" &&
    printf "%s" "Continue (Y\N): "
read CONTINUE; CONTINUE="$( Format "${CONTINUE}" )"

[[ "${CONTINUE}" == "y" ]] && cd "${DIRECTORY}" &&
    git push --set-upstream \
        "${REPO}" "master"
