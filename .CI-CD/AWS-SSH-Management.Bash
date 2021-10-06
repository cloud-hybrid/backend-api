#!/usr/bin/env python3

# -*- Coding: UTF-8 -*-
# -*- System: Linux -*-
# -*- Usage:   *.*  -*-

# Copyright:    Public Domain
# License:      BSD 3-Clause License
# Creator:      Jacob B. Sanders

#
# ========================================================================
# SSH + AWS EC2 Key Upload & SSM Import Handler
# ========================================================================
# --> Simple CLI Interface for SSH Key Generation & Upload Handler for
# AWS SSM Parameter-Store.
#
# *** Important [^2]
# --> AWS SSH-Import-Policy Limits Keys to RSA + a Size of 2048 Maximum
#     in Total Size (Bytes).
#
# [^1] AWS Systems Manager Parameter Store provides secure, hierarchical
# storage for configuration data management and secrets management. Users
# can store data such as passwords, database strings, Amazon Machine Image
# (AMI) IDs, and license codes as parameter values. Additionally, Users
# can store values as plain text or encrypted data; reference Systems
# Manager parameters in scripts, commands, SSM documents, and configuration
# and automation workflows by using the unique name specified when the
# parameter was created.
#
# PS) There's a fun wait handler in the animated form of *Ping-Pong :D
#
# Reference List & Source(s)
# ------------------------------------------------------------------------
# [1] - https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html
# [2] - https://docs.aws.amazon.com/transfer/latest/userguide/API_ImportSshPublicKey.html
#

#
# Usage & Example(s)
# ------------------------------------------------------------------------
# $ ./AWS-SSH-Management.Bash [SSM-Parameter-Prefix (CFN Stack)] [AWS Profile]
#
# Example
# - - - - -
# $ ./AWS-SSH-Management.Bash "Deployment-Executor" "Development"
#
# >>> "▐   ●       ▌"
# ...
# >>> Generating public/private RSA key pair.
# ...
# >>> The key fingerprint is:
# ...
# >>> +---[RSA 2048]----+
# >>> |                 |
# >>> |                 |
# >>> |                 |
# >>> |                 |
# >>> |                 |
# >>> |                 |
# >>> |                 |
# >>> |                 |
# >>> |                 |
# >>> +----[SHA256]-----+
# ...
# >>> "▐        ●  ▌"
# ...
# >>> Overwrite Previous Import? (Y/N): y
# ...
# >>> Checked SSM Parameter (1/3) [Deployment-Executor-Key-Name]
# >>> Checked SSM Parameter (2/3) [Deployment-Executor-Key-Private]
# >>> Checked SSM Parameter (3/3) [Deployment-Executor-Key-Public]
# ...
# >>> Overwrite Previous SSM Imports? (Y/N): y
# ...
# >>> Successful Import (1/3) [Deployment-Executor-Key-Name]
# >>> Successful Import (2/3) [Deployment-Executor-Key-Private]
# >>> Successful Import (3/3) [Deployment-Executor-Key-Public]
# ...
# >>> Move SSH Resources to .SSH Directory? (Y\N): y
# ...
# >>> mv: replace '...', overriding mode 0400 (r--------)? y
# ...
# >>> SSH Management Process Complete
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

tput civis || true

#
# ------------------------------------------------------------------------
#   --> Globals
# ------------------------------------------------------------------------
# - CWD: Current Working (Executing) Directory
# - SIGNALS: Signal Error Return Codes
# - Loader: Ping-Ping :D
#

CWD="$(cd "$(dirname "${0}")" &>/dev/null 2>&1; pwd -P)"

SIGNALS=(
    128 # (0) - Invalid Root Permissions
    129 # (1) - Invalid Sudo Permissions
    130 # (2) - Invalid ${@} Input Arguments
    131 # (3) - Invalid Key-Name as Input Argument [1]
    132 # (4) - Invalid AWS Profile as Input Argument [2]
    133 # (5) - User Import-Key Exit Import Signal
)

Loader=(
"▐●          ▌"
"▐ ●         ▌"
"▐  ●        ▌"
"▐   ●       ▌"
"▐    ●      ▌"
"▐      ●    ▌"
"▐       ●   ▌"
"▐        ●  ▌"
"▐         ● ▌"
"▐          ●▌"
"▐         ● ▌"
"▐        ●  ▌"
"▐       ●   ▌"
"▐      ●    ▌"
"▐     ●     ▌"
"▐    ●      ▌"
"▐   ●       ▌"
"▐  ●        ▌"
"▐ ●         ▌")

#
# ------------------------------------------------------------------------
#   --> Permissions Validation
# ------------------------------------------------------------------------
# - Elevation (Function) - Evaluates Current Executing User & exits
#   if sudo == true || UID == 0
#

Elevation () {
	if [[ "${UID}" == "0" || "$(id -u)" == "0" ]]; then
		echo "Cannot Execute ${0} as Root"
		tput cnorm || true
        tput cvvis || true
		exit ${SIGNALS[0]}
	fi
    if [[ "${SUDO_USER}" != "" || "$(id -u)" == "0" ]]; then
		echo "Cannot Execute ${0} with Elevated Permissions"
		tput cnorm || true
        tput cvvis || true
        exit ${SIGNALS[1]}
    fi
}; Elevation

# ------------------------------------------------------------------------
#   --> Input Arguments
# ------------------------------------------------------------------------

[[ "${1}" == "" ]] || KEYNAME="${1}"
[[ "${1}" == "" ]] && echo "A Key-Name is Required as Input (${SIGNALS[3]})"
[[ "${1}" == "" ]] && tput cnorm || true
[[ "${1}" == "" ]] && tput cvvis || true
[[ "${1}" == "" ]] && exit ${SIGNALS[3]}

[[ "${2}" == "" ]] || PROFILE="${2}"
[[ "${2}" == "" ]] && echo "An AWS Profile is Required as Input (${SIGNALS[4]})"
[[ "${2}" == "" ]] && tput cnorm || true
[[ "${2}" == "" ]] && tput cvvis || true
[[ "${2}" == "" ]] && exit ${SIGNALS[4]}

if [[ -f "${CWD}/${KEYNAME}" ]]; then
	printf "%s" "Delete Previous Key-Pair? (Y/N): " ; \
	    read RESPONSE

	if [[ $RESPONSE == "y" ]] || [[ $RESPONSE == "Y" ]] \
		|| [[ $RESPONSE == "yes" ]] || [[ $RESPONSE == "Yes" ]]; then
		rm -f "${CWD}/${KEYNAME}"
		rm -f "${CWD}/${KEYNAME}.pub"
	else
		echo "Please Handle the Import-Key Process Accordingly"
		tput cnorm || true
        tput cvvis || true
		exit ${SIGNALS[5]}
	fi
fi

PAIR="${KEYNAME}-Key-Pair"

ssh-keygen -b 2048 -t RSA -f "${CWD}/${KEYNAME}" -C "$(uuidgen)" -N ""

(aws ssm put-parameter \
    --name "${KEYNAME}-Key-Name" \
    --type "String" \
    --tier "Standard" \
    --value "${KEYNAME}" \
    --overwrite \
    --profile "${PROFILE}"  \
) &>/dev/null &
PID=$!
while kill -0 $PID &>/dev/null; do
    for ((i = 0; i < ${#Loader[@]}; i++)); do
        printf "${Loader[$i]}\r"
        sleep 0.185
    done
done
trap - EXIT

(aws ssm put-parameter \
    --name "${KEYNAME}-Key-Private" \
    --type "String" \
    --tier "Standard" \
    --value "$(cat ${CWD}/${KEYNAME})" \
    --overwrite \
    --profile "${PROFILE}")>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
PID=$!
while kill -0 $PID &>/dev/null; do
    for ((i = 0; i < ${#Loader[@]}; i++)); do
        printf "${Loader[$i]}\r"
        sleep 0.185
    done
done
trap - EXIT

(aws ssm put-parameter \
    --name "${KEYNAME}-Key-Public" \
    --type "String" \
    --tier "Standard" \
    --value "$(cat ${CWD}/${KEYNAME}.pub)" \
    --overwrite \
    --profile "${PROFILE}")>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
PID=$!
while kill -0 $PID &>/dev/null; do
    for ((i = 0; i < ${#Loader[@]}; i++)); do
        printf "${Loader[$i]}\r"
        sleep 0.185
    done
done
trap - EXIT

echo "Regisering SSH Key(s)"
aws ec2 import-key-pair --public-key-material "$(cat "${KEYNAME}.pub")" \
    --key-name "${PAIR}" --profile "${PROFILE}" # --dry-run

mv "${CWD}/${KEYNAME}" "${HOME}/.ssh"
mv "${CWD}/${KEYNAME}.pub" "${HOME}/.ssh"

echo "Moved Key(s) to ~/.ssh Directory"

tput cnorm || true
tput cvvis || true

printf "%s\n" "SSH Management Process Complete"

exit ${?}
