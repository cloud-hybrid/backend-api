#!/bin/bash --posix

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:   *.*   -*- #

set -e && set +x

#
# ========================================================================
# S3 Target Bucket SSM Parameters + Upload
# ========================================================================
#

# ------------------------------------------------------------------------
# Global Variable(s)
# ------------------------------------------------------------------------

CLI=(${@})

ORG="Cloud-Technology"
ENV="${1:-"Development"}"
SRV="ECS"
RCE="Nexus"

PRF="default"
REG="us-east-2"

CWD="$(cd "$(dirname "${0}")" >/dev/null 2>&1 ; pwd -P)"

# ------------------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------------------

[[ ! -f "${CWD}/.gitignore" ]] && printf "%s\n%s\n" ".Variables" ".Variables.Archive" > "${CWD}/.gitignore"
[[ -f "${CWD}/.Variables" ]] && mv "${CWD}/.Variables" "${CWD}/.Archive" || touch "${CWD}/.Archive"

Parameter () { printf "%s" "/${ORG}/${ENV}/${SRV}/${RCE}/${1}"; }

declare TYP="String"
declare REF="$(Parameter "Nexus-Cluster-TLS-Services-Certificate")"
declare VAL="arn:aws:acm:us-east-2:983281742669:certificate/6b219c7f-2741-4757-8126-3babca2ae759"

echo "Parameter Attributes"
echo "  - Location: ${REF}"
echo "  - Type: ${TYP}"

# aws ssm put-parameter --name "${REF}" \
#     --value "${VAL}"                  \
#         --type "${TYP}"               \
#             --profile "${PRF}"        \
#                 --region "${REG}"     \
#                     --overwrite       \
#     >> "${CWD}/.Archive"

# [[ "${?}" != "0" ]] && exit ${?}

# ===

declare TYP="String"
declare REF="$(Parameter "Nexus-Cluster-CFN-Template-S3-URI")"
declare VAL="s3://cloud-technology/CFN-Templates"

echo "Parameter Attributes"
echo "  - Location: ${REF}"
echo "  - Type: ${TYP}"

# aws ssm put-parameter --name "${REF}" \
#    --value "${VAL}"                   \
#        --type "${TYP}"                \
#            --profile "${PRF}"         \
#                --region "${REG}"      \
#                    --overwrite        \
#    >> "${CWD}/.Archive"
#
# [[ "${?}" != "0" ]] && exit ${?}

# ===

declare NAM="Nexus-Cluster-CFN-Template-S3-URI"
declare VAL="$(aws ssm get-parameter          \
    --name "$(Parameter "${NAM}")"            \
        --profile "${PRF}"  --region "${REG}" \
            | jq -r ".Parameter.Value")"

aws s3 cp "${CWD}/Stack.Yaml" "${VAL}/Nexus/API/Stack.Yaml"
