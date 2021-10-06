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
# =================================================================================================
# [Insert-Name-Here]
# =================================================================================================
#
# --> [Short]
#
# [Long]
#
# Reference List & Source(s)
# -------------------------------------------------------------------------------------------------
# - General Node-JS Container Setup: https://nodejs.org/en/docs/guides/nodejs-docker-webapp/
# - Production Use-Cases should use `npm install --save [...]`, whereas
#   Development environments `npm install --save-dev [...]`.
#
# Usage & Example(s)
# -------------------------------------------------------------------------------------------------
# $ ./[Bash-Script-Name]
#
# ... Optional(s):  ./[Bash-Script-Name]
# ...               ./[Bash-Script-Name] Argument-1
# ...               ./[Bash-Script-Name] Argument-1 Argument-2 Argument-(n)
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

tput civis || ( tput cnorm && tput cvvis )

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
S="\\33[7m" # --> Select

U="\\033[4m" # --> Underline

I=(
"┃●         ┃"
"┃ ●        ┃"
"┃  ●       ┃"
"┃   ●      ┃"
"┃     ●    ┃"
"┃      ●   ┃"
"┃       ●  ┃"
"┃        ● ┃"
"┃         ●┃"
"┃        ● ┃"
"┃       ●  ┃"
"┃      ●   ┃"
"┃     ●    ┃"
"┃    ●     ┃"
"┃   ●      ┃"
"┃  ●       ┃"
"┃ ●        ┃")

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

Error ()        { printf "${R}%s${X}\n" "${@}"; }
Auxiliary ()    { printf "${B}%s${X}\n" "${@}"; }
Success ()      { printf "${G}%s${X}\n" "${@}"; }
Warning ()      { printf "${Y}%s${X}\n" "${@}"; }

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

Warn ()            { printf "${Y}%s \r\n${X}" "$(printf "\e[A\e[K\n")${1}"; }
Complete ()        { printf "${G}%s ✓ \r\n${X}" "$(printf "\e[A\e[K\n")${1}"; }
Problem ()         { printf "${R}%s ✕ \r\n${X}" "$(printf "\e[A\e[K\n")${1}"; }
Supplement ()      { printf "${1} \t\t\t ${B}%s \r\n${X}" "$(printf "\e[A\e[K\n")${1}"; }


# -------------------------------------------------------------------------------------------------
# Global Variables
# -------------------------------------------------------------------------------------------------

CWD="$( cd "\$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SEMAPHORE="FILE.LOCK"
LOCK="${CWD}/${SEMAPHORE}"

# --> Parse[d] Variable(s) Initialization

Parse () {
    while [[ ${#} > 0 ]]; do
        case "${1}" in
            -a|--action)
                shift
                Supplement "$(echo "${1}" | sed -e 's/^[^=]*=//g')" && sleep 1.5
                shift
                ;;
            -u|--Update)
                shift
                export UPDATE=True
                ;;
            -c|--Container)
                shift
                export CONTAINER=$(echo "${1}" | sed -e 's/^[^=]*=//g')
                shift
                ;;
            -h|--help)
                shift
                Warning "                                                       "
                Warning "${0} [-f|--Flag] [-k|--Key] [-v|--Value]               "
                Warning "                                                       "
                Warning "[F]lags: Boolean Triggers.                             "
                Warning "    -h, --help         Show Help Message. Defaults to  "
                Warning "                       '0' (false).                    "
                Warning "                                                       "
                Warning "Parameters: [K]ey-[V]alue Arguments, Space Delimited.  "
                Warning "    -a, --action       Arbitrary Key-Value Pair.       "
                Warning "                                                       "
                sleep 1.0 && exit 0
                ;;
            *)
                shift
                Error "                                                       "
                Error "${0} [-f|--Flag] [-k|--Key] [-v|--Value]               "
                Error "                                                       "
                Error "[F]lags: Boolean Triggers.                             "
                Error "    -h, --help         Show Help Message. Defaults to  "
                Error "                       '0' (false).                    "
                Error "                                                       "
                Error "Parameters: [K]ey-[V]alue Arguments, Space Delimited.  "
                Error "    -a, --action       Arbitrary Key-Value Pair.       "
                Error "                                                       "
                sleep 1.0 && exit 1
                ;;
        esac
    done
}

Semaphore () {
    touch "${LOCK}"

    while ps -p ${1} &>/dev/null; do
        for ((i = 0; i < ${#I[@]}; i++)); do
            printf "\r%s\r" "${I[$i]}" >&1
            sleep 0.115
        done
    done; trap - EXIT

    rm -r -f "${LOCK}" && return 0

}

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

Install () {
    [[ -z "${SUDO_USER}" ]]     \
        && ./configure && make && make install
    [[ ! -z "${SUDO_USER}" ]]   \
        && ./configure && make && sudo make install

    return ${?}
}

XCode () {
    local SYSTEM="$(System)"

    if [ -z "$(xcode-select -p)" ]; then
        if [[ "${SYSTEM}" == "MacOS" ]]; then
            xcode-select --install
        fi
    fi

    return ${?}
}

Brew () {
    local SYSTEM="$( System )"

    if [ -z "$( command -v brew )" ]; then
        if [[ "${SYSTEM}" == "MacOS" ]]; then
            if [ -z "${SUDO_USER}" ]; then
                /bin/bash -c "$( curl -fsSL "${HOMEBREW}" )"
            else
                sudo su - "${SUDO_USER}" -c /bin/bash -c \
                    "$( curl -fsSL "${HOMEBREW}" )"
            fi
        else
            if [ -z "${SUDO_USER}" ]; then
                mkdir homebrew && curl -L                               \
                    "https://github.com/Homebrew/brew/tarball/master"   \
                        | tar xz --strip 1 -C "homebrew"
            else
                sudo su - "${SUDO_USER}" -c mkdir homebrew && curl -L   \
                    "https://github.com/Homebrew/brew/tarball/master"   \
                        | tar xz --strip 1 -C homebrew
            fi
        fi
    else
        Success "Homebrew Already Installed"
    fi

    return ${?}
}

# ------------------------------------------------------------------------
# Program Entry Point(s) && Main
# ------------------------------------------------------------------------

Format () {
    printf "%s" "${1}" | tr "[:upper:]" "[:lower:]"
}

Release () {
    printf "%s" "$(( $(cat ${CWD}/VERSION) + 1 ))"
}

Version () {
    printf "%s" "$(cat ${CWD}/VERSION)"
}

Environment () {
    Auxiliary "Sourcing Environment Variables"

    source "${CWD}/.env"            \
        && Success " - Successful"  \
        || return ${?}

    TARGET="${REGISTRY_URL}/$(Format ${REGISTRY_PATH})"

    return ${?}
}

Purge () {
    [[ -z "${1}" ]] && Auxiliary "Purging Local Docker Containers" \
        && docker system prune --all --force \
            && docker images purge --all \
                && Success " - Successful"
    return ${?}
}

Registry () {
    Auxiliary "Signing Into Registry"
    Print " - URI: ${REGISTRY_URL}"
    Print " - Username: ${REGISTRY_USERNAME}"
    Print " - Token: [REDACTED]"

    docker login "${REGISTRY_URL}"          \
        --username "${REGISTRY_USERNAME}"   \
            --password "${REGISTRY_TOKEN}"

    [[ "${?}" == "0" ]] && local RETURN="0" && \
        Success " - Successful";
    [[ "${?}" != "0" ]] && local RETURN="${?}" && \
        Error " - Sign-In Failure: ${RETURN}"

    return ${RETURN}
}

Alpine () {
    Auxiliary "Building Alpine Base Image"

    docker build --file "Alpine.Dockerfile"         \
        --tag "${TARGET}/${OS}/${BASE}:${VERSION}"  \
            --tag "${OS}-${BASE}:${VERSION}" .      \
                && Success " - Successful"

    return ${?}
}

NGINX () {
    Auxiliary "Building NGINX Image"

    docker build --file "NGINX.Dockerfile"              \
        --tag "${TARGET}/${OS}/${NGINX}:${VERSION}"     \
            --tag "${OS}-${NGINX}:${VERSION}" .         \
                && Success " - Successful"

    return ${?}
}

Build () { Alpine && NGINX && return ${?}; }

Update () {
    Auxiliary "Updating Latest Version(s)" \
        && local VERSION="${1}"

    # --> Alpine Container Image
    docker build --file "Alpine.Dockerfile"             \
        --tag "${TARGET}/${OS}/${BASE}:latest"          \
            --tag "${OS}-${BASE}:${VERSION}" .          \
                && Success " - Successful"

    Auxiliary "Uploading Container - ${OS}:${BASE}:${VERSION}" \
        && docker push "${TARGET}/${OS}/${BASE}:latest"     \
        && Success " - Registry Upload Successful" && echo  \
            || ( [[ "${?}" == "0" ]] && Error               \
                "Registry Upload Error: ${?}"               \
                    && return ${?} )

    # --> NGINX Container Image
    docker build --file "NGINX.Dockerfile"              \
        --tag "${TARGET}/${OS}/${NGINX}:latest"         \
            --tag "${OS}-${NGINX}:${VERSION}" .         \
                && Success " - Successful"

    Auxiliary "Uploading Container - ${OS}:${NGINX}:${VERSION}" \
        && docker push "${TARGET}/${OS}/${NGINX}:latest"    \
        && Success " - Registry Upload Successful" && echo  \
            || ( [[ "${?}" == "0" ]] && Error               \
                "Registry Upload Error: ${?}"               \
                    && return ${?} )

    printf "%s" "${VERSION}" > "${CWD}/VERSION" && return ${?}
}

Upload () {
    Print "Overwriting Registry Images" \
        && local VERSION="${1}"

    # --> Alpine Container Image
    Auxiliary "Uploading Container - ${OS}:${BASE}:${VERSION}" \
        && docker push "${TARGET}/${OS}/${BASE}:${VERSION}"    \
        && Success " - Registry Upload Successful"  \
            || ( [[ "${?}" == "0" ]] && Error       \
                "Registry Upload Error: ${?}"       \
                    && exit ${?} )

    # --> NGINX Container Image
    Auxiliary "Uploading Container - ${OS}:${NGINX}:${VERSION}" \
        && docker push "${TARGET}/${OS}/${NGINX}:${VERSION}"    \
        && Success " - Registry Upload Successful"      \
            || ( [[ "${?}" == "0" ]] && Error           \
                "Registry Upload Error: ${?}"           \
                    && exit ${?} )
}


Main () {
    Output "Parsing Input" && sleep 1
    [[ "${@}" ]] || exit 1
    Complete "${EOM}"

    Output "Checking Update Flag" && sleep 1
    [[ -z "${UPDATE}" ]] || exit 1
    Complete "${EOM}"

    Output "Validating Container Target" && sleep 1
    [[ -z "${CONTAINER}" ]] || exit 1
    Complete "${EOM}"

#    [[ "${1}" == "Update" ]] && VERSION="$( Release )"
#    [[ "${1}" != "Update" ]] && VERSION="$( Version )"
#
#    Environment || exit ${?}
#    Purge       || exit ${?}
#    Registry    || exit ${?}
#    Build       || exit ${?}

    rm -r -f "${LOCK}" && return ${?}
}

( Main "${@}" ) & Semaphore ${!}

( tput cnorm && tput cvvis )

exit 0
#
#Main () {
#    [[ "${1}" == "Update" ]] && VERSION="$( Release )"
#    [[ "${1}" != "Update" ]] && VERSION="$( Version )"
#
#    Environment || exit ${?}
#    Purge       || exit ${?}
#    Registry    || exit ${?}
#    Build       || exit ${?}
#
#
#    [[ "${LOCK}" == "${VERSION}" ]] && Upload "${VERSION}"
#    [[ "${LOCK}" != "${VERSION}" ]] && Upload "${VERSION}" \
#        && Update   "${VERSION}"
#
#    return ${?}
#}
#
#Main ${@} && exit ${?}
