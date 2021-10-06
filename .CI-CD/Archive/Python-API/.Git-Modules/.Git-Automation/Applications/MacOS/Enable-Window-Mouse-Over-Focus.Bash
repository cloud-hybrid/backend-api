#!/bin/bash --posix

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  .Bash  -*- #

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

#
# =================================================================================================
# MacOS Kernel Window Mouse-Over-Focus Enablement
# =================================================================================================
#
# --> Enables the MacOS kernel to poll mouse events -- such as allowing mouse or trackpad
#     movement to activate a hovered window or screen.
#
# Reference List & Source(s)
# -------------------------------------------------------------------------------------------------
# -
#
# Usage & Example(s)
# -------------------------------------------------------------------------------------------------
# chmod a+x Enable-Window-Mouse-Over-Focus.Bash \
#     && ./Enable-Window-Mouse-Over-Focus.Bash
#

#
# -------------------------------------------------------------------------------------------------
# Terminal Formatting
# -------------------------------------------------------------------------------------------------
# Hide Terminal Mouse Cursor
# >>> tput civis
#
# Normalize Mouse Cursor
# >>> tput cnorm && tput cvvis
#

( tput civis ) || $()

EOM="\\33[0m"

R="\\33[91m" # --> Red
G="\\33[32m" # --> Green
B="\\33[34m" # --> Blue

Y="\\33[33m" # --> Yellow
Z="\\33[90m" # --> Grey

X="\\33[0m" # --> Reset
D="\\33[2m" # --> Dim
L="\\33[4m" # --> Link
H="\\33[1m" # --> Bold (Highlight)
I="\\33[3m" # --> Italicize
S="\\33[7m" # --> Select

U="\\033[4m" # --> Underline

# -------------------------------------------------------------------------------------------------
# F-String STDOUT Functions
# -------------------------------------------------------------------------------------------------

OOP () {
    grep "${1}" /Environment.Properties \
        | cut -d'=' -f2 | \
            sed -e 's/^"//' -e 's/"$//'
}

Tabular ()      { printf "%s" "    "; }

Dim ()          { printf "%s" "${@}"; }
Bold ()         { printf "%s" "${@}"; }
Underline ()    { printf "%s" "${@}"; }

Error ()        { printf "%s\n" "${@}"; }
Auxiliary ()    { printf "%s\n" "${@}"; }
Success ()      { printf "%s\n" "${@}"; }
Warning ()      { printf "%s\n" "${@}"; }

Clear ()        { printf "%s" "${@}"; }

Print ()        { printf "%s\n" "${@}"; }

Tab ()          { printf "\\t%s" "${@}"; }
Line ()         { printf "\\n%s" "${@}"; }
Focus ()        { printf "%s" "${@}"; }

# - - - - - - - - -
# Threaded Output
# - - - - - - - - -

Output () {
    printf "\r\n%s ... \r\n" "$(printf "\e[A\e[K\n")${1}" \
        && export EOM="${1}"
}

Complete ()        { printf "${G}%s ✓ \r\n${X}" "$(printf "\e[A\e[K\n")${1}"; }
Problem ()         { printf "${Y}%s ✕ \r\n${X}" "$(printf "\e[A\e[K\n")${1}"; }
Supplement ()      { printf "${B}%s ⓘ \r\n${X}" "$(printf "\e[A\e[K\n")${1}"; }

# -------------------------------------------------------------------------------------------------
# Global Variables
# -------------------------------------------------------------------------------------------------

CWD="$( cd "\$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# -------------------------------------------------------------------------------------------------
# Program Entry Point(s)
# -------------------------------------------------------------------------------------------------

System () {
    SYSTEM="$( uname -s )"

    case "${SYSTEM}" in
        Linux*)
            MACHINE="Linux"
                ;;
        Darwin*)
            MACHINE="MacOS"
                ;;
        CYGWIN*)
            MACHINE="Cygwin"
                ;;
        MINGW*)
            MACHINE="MinGw"
                ;;
        *)  MACHINE="N/A"
    esac

    export SYSTEM="${MACHINE}" && return 0
}

Main () { System

    [[ "${SYSTEM}" != "MacOS" ]] && return 1
    [[ "${SYSTEM}" == "MacOS" ]] && \
        Auxiliary "Enabling Mouse Shift-Focus-On-Hover Polling" \
            && defaults write com.apple.Terminal \
                FocusFollowsMouse -bool true

    return 0
}

Main && exit 0