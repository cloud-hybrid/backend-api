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
ENV="Development"
SRV="Compute"
RCE="GitLab"

PROFILE="default"
REGION="us-east-2"

CWD="$(cd "$(dirname "${0}")" >/dev/null 2>&1 ; pwd -P)"

# ------------------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------------------

Parameter () { printf "%s" "/${ORG}/${ENV}/${SRV}/${RCE}/${1}"; }


declare REF="$(Parameter "${1}")"

aws ssm get-parameter --name "$(Parameter "${1}")"  \
    --profile "${PROFILE}"  --region "${REGION}"    \
        | jq -r ".Parameter.Value"

exit ${?}
