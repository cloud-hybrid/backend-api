#!/bin/bash --posix

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

# License - BSD 3-Clause License

# ...
# ... The Idea is Simple [^1]
# ... --------------------------------------------------------------------
# ... Publish & Share Information Online and Make Available Everyone.
# ...    — Dick K.P. Yue, Professor, MIT School of Enineering
# ...

# 
# ========================================================================
# [Executable-Title-Name] | [Synopsis]
# ========================================================================
# - Author:   Jacob B. Sanders
# - Notice:   Copyright 2020
# - License:  BSD 3-Clause License
# 
# [Description ... ]
#
# Reference List & Source(s)
# ------------------------------------------------------------------------
# [1] - [MIT Open Source]: https://ocw.mit.edu/help/get-started-with-ocw/
#

# ------------------------------------------------------------------------
# Global Declarations
# ------------------------------------------------------------------------

CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SYSTEM="$(uname)"
ARGUMENTS="3"

# ------------------------------------------------------------------------
# Terminal Formatting & Output 
# ------------------------------------------------------------------------

EOM="\33[0m"

BOLD="\33[1m"
ITALIC="\33[3m"
LINK="\33[4m"
BLINK="\33[5m"
UNDERLINE="\033[4m"
SELECTED="\33[7m"
DIM="\33[2m"

R="\33[91m"
G="\33[32m"
B="\33[34m"

Error ()        { printf "${R}%s${EOM}\n" "${@}"; sleep 1.0; }
Auxiliary ()    { printf "${B}%s${EOM}\n" "${@}"; sleep 1.0; }
Success ()      { printf "${G}%s${EOM}\n" "${@}"; sleep 1.0; }

Print ()        { printf "${EOM}%s${EOM}\n" "${@}"; sleep 1.0; }

#
# ------------------------------------------------------------------------
# *.Properties Parsing (OOP Function)
# ------------------------------------------------------------------------
# 
# --- Example-File.Properties ---
# 
# ... #!/bin/bash --posix
# ...
# ... # -*- Coding: UTF-8 -*- #
# ... # -*- System: Linux -*- #
# ... # -*- Usage:   *.*  -*- #
# ... 
# ... # ===================================================================
# ... # Global Environment Properties
# ... # ===================================================================
# ...
# ... Global.Company.Name="Global-Enterprises"
# ...
#
# ($) OOP "Global.Company.Name"
# >>> Global-Enterprises
#

OOP () {
    grep "${1}" ${CWD}/Environment.Properties \
        | cut -d'=' -f2 | \
            sed -e 's/^"//' -e 's/"$//'
}

# ========================================================================
# Primary Entry-Point & Main Function(s)
# ========================================================================

Main () { # --> [Insert-Code-Here] 
    Print "Starting ${CWD}" && \
        Auxiliary "  - Input: ${@}"

    if [[ "${?}" == "0" ]]; then
        Success "${@} - Successful (${?})" \
            && return 0
    elif [[ "${?}" == "130" ]]; then
        Auxiliary "${@} - User Signal EXIT (${?})" \
            && return 0
    else
        local _SIGINT=${?}
        Error "${@} - Non-Zero Response (${_SIGINT})" \
            && return ${_SIGINT}
    fi
}

Main ${@} && Success "${#} exit ${?}
