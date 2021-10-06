#!/bin/bash --posix

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

#
# ========================================================================
# Python & Open-SSL MacOS Installer
# ========================================================================
# --> Open-SSL Dependency Compilation & Python-3.8.3 Build + Install
#
# Reference List & Source(s)
# ------------------------------------------------------------------------
# [1] - Applescript Python: https://wiki.python.org/moin/MacPython/AppscriptModule
# [2] - Deploying MacOS Python Application: http://undefined.org/python/#py2app
#

# --------------------
# Terminal Formatting
# --------------------

_='\33[0m'

BOLD='\33[1m'
ITALIC='\33[3m'
LINK='\33[4m'
BLINK='\33[5m'
UNDERLINE='\033[4m'
SELECTED='\33[7m'
DIM='\33[2m'

R='\33[91m'
G='\33[32m'
B='\33[34m'

# --------------------------
# F-String STDOUT Functions
# --------------------------

Error ()        { printf "${R}%s${_}\n" "${@}"; }
Auxiliary ()    { printf "${B}%s${_}\n" "${@}"; }
Success ()      { printf "${G}%s${_}\n" "${@}"; }
Print ()        { printf "${_}%s${_}\n" "${@}"; }

# --------
# Globals
# --------

CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# ------------------------------------------------------------------------
# Program Entry Point(s) && Main
# ------------------------------------------------------------------------

SSL () { # return 0
    local VERSION="1.1.1g"

    local PROGRAM="OpenSSL"

    mkdir -p "${HOME}/Distribution/"
    mkdir -p "${HOME}/Distribution/Builds"
    mkdir -p "${HOME}/Distribution/Builds/${PROGRAM}"
    mkdir -p "${HOME}/Distribution/Builds/${PROGRAM}/Source"
    mkdir -p "${HOME}/Distribution/Builds/${PROGRAM}/${VERSION}"

    local SOURCE="${HOME}/Distribution/Builds/${PROGRAM}/Source"
    local BUILD="${HOME}/Distribution/Builds/${PROGRAM}/${VERSION}"
    local DISTRIBUTION="${HOME}/Distribution/${PROGRAM}"

    cd "${BUILD}" && curl \
        "https://www.openssl.org/source/openssl-${VERSION}.tar.gz" \
            | tar zxvf -

    cd openssl-* && ./Configure \
        darwin64-x86_64-cc \
            no-hw --prefix="${SOURCE}" \
            --openssldir="${BUILD}" \
                && make install

    rm -r -f "${SOURCE}" \
        && rm -r -f "${DISTRIBUTION}"

    mv "${BUILD}" "${DISTRIBUTION}"

    cd "${CWD}" && Byte-Alert "OpenSSL Build Complete" && return 0 \
        || return 0
}

Python () {
    local PROGRAM="Python"
    local VERSION="3.8.3"

    mkdir -p "${HOME}/Distribution/"
    mkdir -p "${HOME}/Distribution/${PROGRAM}"
    mkdir -p "${HOME}/Distribution/${PROGRAM}/${VERSION}"

    local ROOT_DIR="${HOME}/Distribution/${PROGRAM}"
    local SOURCE="${HOME}/Distribution/${PROGRAM}/${VERSION}"

    cd "${SOURCE}" && curl --output "${PROGRAM}.pkg" \
        "https://www.python.org/ftp/python/${VERSION}/python-${VERSION}-macosx10.9.pkg"

    sudo su - "$USER" -c "sudo /usr/sbin//installer -pkg ${SOURCE}/${PROGRAM}.pkg -target /Applications -verbose"

    /Applications/Python\ 3.8/Install\ Certificates.command \
        && sudo su - "$USER" -c \
            "sudo chmod a+x \
                /Applications/Python\ 3.8/Update\ Shell\ Profile.command"

    cd "${CWD}" && Byte-Alert "Python Build Complete" && return 0 \
        || return 0
}

Main () {
    SSL && Python
}; Main && exit 0
