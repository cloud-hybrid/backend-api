#!/bin/bash --posix

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:   *.*   -*- #

set -euo pipefail

[[ "${@}" =~ "--debug" || "${@}" =~ "--Debug" ]] && set -x

SIGNALS=(
    128 # (0) - SSH Public Key SSH_PUBLIC_KEY env Variable
    129 # (1) - Invalid Sudo Permissions
    130 # (2) - Invalid ${@} Input Arguments
)

[[ -z "${SSH_PUBLIC_KEY}" ]] && exit ${SIGNALS[0]}
[[ ! -d ~/.ssh ]] && mkdir -p ~/.ssh

echo $SSH_PUBLIC_KEY > ~/.ssh/authorized_keys

unset SSH_PUBLIC_KEY

/usr/sbin/sshd -D
