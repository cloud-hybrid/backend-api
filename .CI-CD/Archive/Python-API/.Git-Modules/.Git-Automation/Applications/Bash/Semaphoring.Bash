#!/bin/bash --posix

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  .Bash  -*- #

# Owner:    Jacob B. Sanders
# Source:   code.cloud-technology.io
# License:  BSD 3-Clause License

#
# Copyright 2020 Jacob B. Sanders - Cloud Hybrid LLC. & Affiliates
#
# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:
#
# 1.  Redistributions of source code must retain the above copyright notice, this list of
#     conditions and the following disclaimer.
#
# 2.  Redistributions in binary form must reproduce the above copyright notice, this list of
#     conditions and the following disclaimer in the documentation and/or other materials
#     provided with the distribution.
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
# Bash Semaphoring
# =================================================================================================
#
# Reference List & Source(s)
# -------------------------------------------------------------------------------------------------
# -
#
# Usage & Example(s)
# -------------------------------------------------------------------------------------------------
# chmod a+x Semaphoring.Bash \
#     && ./Semaphoring.Bash
#

set -e

CWD="$( cd "\$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
SEMAPHORE="FILE.LOCK"
LOCK="${CWD}/${SEMAPHORE}"

Status () { # Status Logic
    return 0
}

Semaphore () { # Time-Ceiling Handler

    ( printf "%s" "1" > "${LOCK}" ) &

    while ps -p ${!} || [[ ! -f "${LOCK}" ]]; do sleep 1; done

    for (( i=0; i<=60; i++ )); do
        echo "${i}" && sleep 60
        [[ ! -f  "${LOCK}" ]] \
            exit 0
    done

    rm -r -f "${LOCK}" && return 0

}

Main () {

    apk add curl

    unset "${TOKEN}"

    return 0

}

( ( Semaphore ) 2>/dev/null ) &

while ps -p ${!} 2>/dev/null; do
    Status && sleep 60
done; trap - EXIT

exit 0
