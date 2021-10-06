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
# AWS CFN Estimation
# ========================================================================
# --> Short Snippet for Usage w/CICD Jobs
#
# Reference List & Source(s)
# ------------------------------------------------------------------------
# [1] - [AWS-CLI]:  https://docs.aws.amazon.com/cli/latest/reference/ \
#                       cloudformation/estimate-template-cost.html
#

# --------------------
# Terminal Formatting 
# --------------------

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

# --------------------------
# F-String STDOUT Functions
# --------------------------

Error ()        { printf "${R}%s${_}\n" "${@}"; }
Auxiliary ()    { printf "${B}%s${_}\n" "${@}"; }
Success ()      { printf "${G}%s${_}\n" "${@}"; }

Print ()        { printf "${EOM}%s${EOM}\n" "${@}"; }

# --------
# Globals
# --------

CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# ------------------------------------------------------------------------
# Program Entry Point(s) && Main
# ------------------------------------------------------------------------

Validate () {
    if  [[ "${#}" != "${CONCISE}"   \
        || "${#}" != "${EXTENDED}"  \
        || "${#}" != "${PROFILED}"  \
        || "${#}" != "${COMPLETE}" ]]
    then
        printf "%s\n" "Incorrect Number of Arguments"
        printf "%s\n" "Usage (4 Total Use-Cases):"
        printf "\t%s\n" "${0} [Stack].Yaml"
        printf "\t%s\n" "${0} [Stack].Yaml [Parameters].json"
        printf "\t%s\n" "${0} [Stack].Yaml [Parameters].json [Profile]"
        printf "\t%s\n" "${0} [Stack].Yaml [Parameters].json [Profile] [Region]"

        printf "%s" "Exiting (-1, 255)" \
            && exit -1
    else
        if [ "${#}" -lt "${PROFILED}" ]; then
            PROFILE="default" &&    \
                REGION="default"    \
                    || exit ${?}
        elif [[ "${#}" == "${PROFILED}" ]]; then
            PROFILE="${3}" &&       \
                REGION="default"    \
                    || exit ${?}
        else
            PROFILE="${3}" &&       \
                REGION="${4}"       \
                    || exit ${?}
        return 0
    fi
}

Environment () {
    if [ -n $(command -v aws) ]; then
        python3 -m pip install awscli \
            || python -m pip install awscli
        return ${?}
    else
        return 0
    fi
}

Profile () {
    if [ "${#}" -ge "${PROFILED}" ]; then
        aws sts get-caller-identity     \
            --profile "${PROFILE}" &&   \
                return ${?}
    else
        aws sts get-caller-identity     \
            --profile "${PROFILE}" &&   \
                return ${?}
    fi
}

Main () {
    TEMPLATE="file://${1}"

    if [[ ! -z "${2}" ]]; then
        PARAMETERS="${2}"
        aws cloudformation estimate-template-cost   \
            --template-body "file://${TEMPLATE}"    \
            --parameters "file://${PARAMETERS}"     \
                --profile "${PROFILE}"              \
                --region "${REGION}"
        return ${?}
    else
        aws cloudformation estimate-template-cost   \
            --template-body "file://${TEMPLATE}"    \
                --profile "${PROFILE}"              \
                --region "${REGION}"
        return ${?}
    fi
}

Validate    || Error "${?}" && exit ${?}
Environment || Error "${?}" && exit ${?}
Profile     || Error "${?}" && exit ${?}

Main; Auxiliary "Return Code: (${?})" \
    && exit ${?}
