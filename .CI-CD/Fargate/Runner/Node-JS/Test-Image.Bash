#!/bin/bash --posix

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:   *.*   -*- #

set -euo pipefail

[[ "${@}" =~ "--debug" || "${@}" =~ "--Debug" ]] && set -x

SIGNALS=(
    128 # (0) - Invalid Root User
    129 # (1) - Invalid Node-JS Runtime
    130 # (2) - Invalid Gitlab Runner Runtime
)

# ---------------------------------------------------------------------------- #
# Verify Root User Permissions                                                 #
# ---------------------------------------------------------------------------- #

echo "Checking User ..."

[[ "${USER}" == "root" ]] || exit ${SIGNALS[0]}

# ---------------------------------------------------------------------------- #
# Verify Node-JS ABI                                                           #
# ---------------------------------------------------------------------------- #

echo "Testing Node-JS Runtime ..."

node --version

[[ "${?}" == 0 ]] || exit ${SIGNALS[1]}

# ---------------------------------------------------------------------------- #
# Verify Runner ABI                                                            #
# ---------------------------------------------------------------------------- #

echo "Testing Gitlab-Runner Runtime ..."

gitlab-runner --version

[[ "${?}" == 0 ]] || exit ${SIGNALS[2]}
