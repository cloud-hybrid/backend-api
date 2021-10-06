#!/bin/bash --posix

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:   *.*   -*- #

#
# ==================================================================
# MacOS Installer
# ==================================================================
# @Task: Mention use of the following script for 'Creating Bootable
#        *.ISO USB Drives
#

# --------------------
# Terminal Formatting 
# --------------------

EOM='\33[0m'

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

Error ()        { printf "${R}%s${EOM}\n" "${@}"; }
Auxiliary ()    { printf "${B}%s${EOM}\n" "${@}"; }
Success ()      { printf "${G}%s${EOM}\n" "${@}"; }

Print ()        { printf "${EOM}%s${EOM}\n" "${@}"; }

# --------
# Globals
# --------

# --- #
CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
# --- #

URL="https://releases.ubuntu.com/20.04/ubuntu-20.04-live-server-amd64.iso"
ETCHER="https://www.balena.io/etcher/"

# ------------------------------------------------------------------------
# Program Entry Point(s) && Main
# ------------------------------------------------------------------------

Safari () {
osascript << EOD
tell application "Safari"
    open location "$1"
    activate
end tell
EOD
}

Safari "https://ubuntu.com/tutorials/create-a-usb-stick-on-macos#1-overview"

cd "${CWD}/ISO" \
    && wget "${URL}" \
    && Safari "${ETCHER}"

