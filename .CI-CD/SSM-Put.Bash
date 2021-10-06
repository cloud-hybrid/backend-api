#!/bin/bash --posix

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:   *.*   -*- #

set -e && set +x

#
# ========================================================================
# CFN Stack SSM Parameters Script
# ========================================================================
# * Note, "VAL" Assignments should been Sanitized (Removed) Upon
#   Completion. Later Usage requires "VAL" Re-Assignment.
#

# ------------------------------------------------------------------------
# Global Variable(s)
# ------------------------------------------------------------------------

CLI=(${@})

ORG="Cloud-Technology"
ENV="${1:-"Development"}"
SRV="Compute"
RCE="GitLab"

PROFILE="default"
REGION="us-east-2"

CWD="$(cd "$(dirname "${0}")" >/dev/null 2>&1 ; pwd -P)"

# ------------------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------------------

Parameter () { printf "%s" "/${ORG}/${ENV}/${SRV}/${RCE}/${1}"; }

declare TYP="String"
declare REF="$(Parameter "${1}")"
declare VAL="${2}"

aws ssm put-parameter --overwrite     \
    --name "${REF}" --value "${VAL}"  \
        --type "String"               \
            --profile "${PROFILE}"    \
                --region "${REGION}"

exit ${?}
