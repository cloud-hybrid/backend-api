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
Message ()      { printf "\n$(Bullet)%s" "${1}$(printf "\e[A\e[K\n")"; }
Title ()        { printf "$(Clear)%s\n" "${@}"; }

# -------------------------------------------------------------------------------------------------
# Global Variables
# -------------------------------------------------------------------------------------------------

CWD="$( cd "\$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

HOMEBREW="https://raw.githubusercontent.com/Homebrew/install/master/install.sh"

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

AWS () {
    export _AWS_TOKEN=$(curl --silent -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds:21600")

    curl --silent -H "X-aws-ec2-metadata-token:${_AWS_TOKEN}" --verbose "http://169.254.169.254/latest/meta-data/"

    export LOCAL_HOSTNAME="$(curl --silent http://169.254.169.254/latest/meta-data/local-hostname)"
    export PUBLIC_IPV4="$(curl --silent http://169.254.169.254/latest/meta-data/public-ipv4)"
    export INSTANCE_ID="$(curl --silent http://169.254.169.254/latest/meta-data/instance-id)"
    export META_HOSTNAME="$(curl --silent http://169.254.169.254/latest/meta-data/hostname)"
    export IAM_INFO="$(curl --silent http://169.254.169.254/latest/meta-data/iam/info)"
    export SECURITY_GROUPS="$(curl --silent http://169.254.169.254/latest/meta-data/security-groups)"
    export DOMAIN="$(curl --silent http://169.254.169.254/latest/meta-data/services/domain)"
    export INSTANCE_TYPE="$(curl --silent http://169.254.169.254/latest/meta-data/instance-type)"
    export AMI_ID="$(curl --silent http://169.254.169.254/latest/meta-data/ami-id)"
    export USER_DATA="$(curl --silent http://169.254.169.254/latest/user-data)"

    export AWS_IAM_ROLE="$( curl --silent --location "http://169.254.169.254/latest/meta-data/iam/security-credentials/ ")"
    export AWS_ACCESS_KEY_ID="$(curl --silent --location "http://169.254.169.254/latest/meta-data/iam/security-credentials/${AWS_IAM_ROLE}/" | jq -r '.AccessKeyId')"
    export AWS_SECRET_ACCESS_KEY="$(curl --silent --location "http://169.254.169.254/latest/meta-data/iam/security-credentials/${AWS_IAM_ROLE}/" | jq -r '.SecretAccessKey')"
    export AWS_SECURITY_TOKEN="$(curl --silent --location "http://169.254.169.254/latest/meta-data/iam/security-credentials/${AWS_IAM_ROLE}/" | jq -r '.Token')"

    export AWS_SESSION_TOKEN="${AWS_SECURITY_TOKEN}"

    aws configure set aws_access_key_id "${AWS_ACCESS_KEY_ID}"
    aws configure set aws_secret_access_key "${AWS_SECRET_ACCESS_KEY}"
    aws configure set aws_session_token "${AWS_SESSION_TOKEN}"

    return ${?}
}

Install () {
    if [ -z "${SUDO_USER}" ]; then
        ./configure && make && make install
    else
        ./configure && make && sudo make install
    fi

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
                sudo su - "${SUDO_USER}" -c /bin/bash -c "$( curl -fsSL "${HOMEBREW}" )"
            fi
        else
            if [ -z "${SUDO_USER}" ]; then
                mkdir homebrew && curl -L "https://github.com/Homebrew/brew/tarball/master" | tar xz --strip 1 -C "homebrew"
            else
               sudo su - "${SUDO_USER}" -c mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
            fi
        fi
      else
        Success "Homebrew Already Installed"
    fi

    return ${?}
}

Main () {
    ( Brew && return ${?} ) \
           || return ${?}
}

( Main  || ( tput cnorm && tput cvvis ) ) \
        && ( tput cnorm && tput cvvis ) ; \
        exit ${?}
