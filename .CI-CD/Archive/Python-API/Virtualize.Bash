#!/bin/bash --posix

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

# Owner: Jacob B. Sanders
# Source: code.cloud-technology.io
# License: BSD 3-Clause License

# Copyright 2020, Jacob B. Sanders

#
# ========================================================================
# Axon Installer
# ========================================================================
# --> [Short-Description]
# 
# [Long-Description ... ]
#
# Reference List & Source(s)
# ------------------------------------------------------------------------
# [1] - [Link-Title]: [https://cloudhybrid.io]
# 
# Usage & Example(s)
# ------------------------------------------------------------------------
# $ ./[Bash-Script-Name]
#
# ... [Prompt]: [User-Input]
#
# >>> /Volumes/IO-Core/Business/Cloud-Hybrid/...
# >>> └── 2020
# >>>     ├── April
# >>>     ├── August
# >>>     ├── December
# >>>     ├── February
# >>>     ├── January
# >>>     ├── July
# >>>     ├── June
# >>>     ├── March
# >>>     ├── May
# >>>     ├── November
# >>>     ├── October
# >>>     └── September
#
# >>> 13 directories, 0 files
#
# >>> Complete
# 

#
# ----------------------------------
# Terminal Formatting
# ----------------------------------
# Hide Terminal Mouse Cursor
# >>> $ tput civis
#
# Normalize Mouse Cursor
# >>> $ tput cnorm && tput cvvis
#

tput civis

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

# --------------------------
# F-String STDOUT Functions
# --------------------------

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
Message ()      { printf "\n$(Bullet)%s" "${1}$(printf "\e[A\e[K\n")"; }
Title ()        { printf "$(Clear)%s\n" "${@}"; }

# --------
# Globals
# --------

CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

SYSTEM="$(uname)"

# ------------------------------------------------------------------------
# Program Entry Point(s) && Main
# ------------------------------------------------------------------------

Write () {
local DOMAIN_NAME="${1}"
local COMPANY_NAME="${2}"
local SHORT_NAME="${3}"

cat << EOF | tee "${CWD}/Environment.Properties"
#!/usr/bin/file *.Properties

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

# Source: code.cloud-technology.io
# Creator: Jacob B. Sanders
# License: BSD 3-Clause License

# Copyright 2020, Jacob B. Sanders

#
# ========================================================================
# Global Environment Properties
# ========================================================================
#

Global.Company.FQDN="${DOMAIN_NAME}"
Global.Company.Name="${COMPANY_NAME}"
Global.Company.Abbreviation="${SHORT_NAME}"

# ------------------------------------------------------------------------
# ---> Subsidary Properties
# ------------------------------------------------------------------------

# ... #

# ------------------------------------------------------------------------
# ---> AWS API Properties
# ------------------------------------------------------------------------

AWS.API.Link-Local="169.128.255.254"

EOF
}

Source () {
    export FQDN="$(OOP Global.Company.FQDN)"
    export NAME="$(OOP Global.Company.Name)"
    export ABBREVIATION="$(OOP Global.Company.Abbreviation)"
}

if [[ "${#}" != "3" ]]
then
    Error "Incorrect Number of Arguments"
    Print "Usage:"
    Auxiliary   "    ${0} [FQDN (Domain-Name)] [Company-Name] [Company-Shortname]"
    echo
    Print       "Example)"
    Auxiliary   "    ${0} cloudhybrid.io 'Cloud Hybrid LLC.' Cloud-Hybrid"
    echo
    Print "Exiting (-1, 255)" \
        && exit -1
else
    Print "Writing *.Properties File" \
        && Write "${1}" "${2}" "${3}" \
            && Source

    Auxiliary "FQDN: ${FQDN}"
    Auxiliary "Company: ${NAME}"
    Auxiliary "Company Short-Name: ${ABBREVIATION}"
fi 

Virtualization () {
    if [ ! -d "${CWD}/.venv" ]; then
        Error "Virtual-Environment (.venv) Does Not Exist"
        Auxiliary "Creating Virtual Environment"
        Print "Installing Latest Version"
        python3.8 -m pip install virtualenv --force
        Print "Creating .venv Directory"
        python3.8 -m virtualenv "${CWD}/.venv"
        Success "Virtual Environment Created"
    fi

    return 0
}

PIP () {
    if [ -z "$( command -v $(python3 -m pip) )" ]; then
        Success "Python-3 PIP Validated"
    else
        sudo apt install --yes \
            python3.8 \
            python3.8-dbg \
            python3.8-dev \
            python3.8-venv \
                python3-pip \
        || sudo yum install \
            python3 \
            python3-dbg \
            python3-dev \
            python3-venv \
                python3-pip \
                    --assumeyes \
        || if [[ "${SYSTEM}" == "Darwin" ]]; then
            Auxiliary "Please Install Python3 & Python3-pip"
            exit 0
        fi
    fi

    return 0
}

Validation () {
    Auxiliary "Validating Python-3 System Installation"
    if [ ! -n "$(command -v python3)" ]; then
        PIP && Success "Python-3 Validated"
    fi

    Success "Python-3 Package Management Validated"

    return 0 
}

Initialize () { source "${CWD}/.venv/bin/activate"
    Print "Upgrading Package Management (PIP)"
    python -m pip install --upgrade pip
    Auxiliary "Version: $(printf "%s" $(python --version))"
    Print "Building Package(s)"
    python setup.py build
    Auxiliary "Freezing Requirements"
    python -m pip freeze > requirements.txt
    Auxiliary "Installing Against Requirements"
    python -m pip install -r requirements.txt
    Auxiliary "Performing System Installation"
    python setup.py install
    Auxiliary "Checking Isolation"
    python -m pip check --verbose --isolated
}

Main () { 
    Validation \
        && Virtualization \
            && Initialize

    printf "%s" "Start WSGI Server (Y/N): "; read RESPONSE

    if [[ "${RESPONSE}" == "Y" || "${RESPONSE}" == "y" ]]; then
        uwsgi --virtualenv "${CWD}/.venv" \
            --yaml WSGI.Yaml
    fi
}

Main && Success "Complete"
