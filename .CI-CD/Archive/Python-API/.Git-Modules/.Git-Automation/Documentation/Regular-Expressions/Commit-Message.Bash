#!/bin/bash --posix

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  *.Yaml -*- #

# Owner: Jacob B. Sanders
# Source: code.cloud-technology.io
# License: BSD 3-Clause License

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
# OF SUCH DAMAGE
#

#
# ========================================================================
# Git Pre-Commit Hook
# ========================================================================
#
# Git Hooks - https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
# --------------------------------------------------------------------------
# Like many other Version Control Systems, Git has a way to fire off custom
# scripts when certain important actions occur. There are two groups of these
# hooks: client-side and server-side. Client-side hooks are triggered by
# operations such as committing and merging, while server-side hooks run on
# network operations such as receiving pushed commits.
#
# By default, `git init` will fill the repository with several examples.
#
# Usage & Example(s)
# -------------------------------------------------------------------------------------------------
# 1. Place [Script-Name].Bash in a local repository's hooks directory as `commit-msg`
#    >>> mv [Script-Name].Bash .git/hooks/commit-msg
# 2. Enable Executable Permissions
#    >>> chmod a+x .git/hooks/commit-msg
# 3. Make a code change.
#    >>> touch Test.Yaml
# 4. Branch from 'master'.
#    >>> git checkout --branch "Feature-Git-Commit-Message" && git checkout "Feature-Git-Commit-Message"
# 5. Add changes.
#    >>> git add Test.Yaml || git add .
# 6. Commit code changes w/message.
#    >>> git commit -m "Added `Test.Yaml`"
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

Tabular ()      { printf "%s\n" "    ⮕  ${@}"; }
Point ()        { printf "%s\n" "    • ${@}";  }

Dim ()          { printf "%s" "${@}"; }
Bold ()         { printf "%s" "${@}"; }
Underline ()    { printf "%s" "${@}"; }

Error ()        { printf "${R}%s${X}\n" "${@}"; }
Auxiliary ()    { printf "${B}%s${X}\n" "${@}"; }
Success ()      { printf "${G}%s${X}\n" "${@}"; }
Warning ()      { printf "${Y}%s${X}\n" "${@}"; }

Clear ()        { printf "%s" "${@}"; }

Print ()        { printf "${1}%s${X}" "${2}"; }

Tab ()          { printf "\\t%s" "${@}"; }
Line ()         { printf "\\n%s" "${@}"; }
Focus ()        { printf "%s" "${@}"; }
Message ()      { printf "\n$(Bullet)%s" "${1}$(printf "\e[A\e[K\n")"; }
Title ()        { printf "$(Clear)%s\n" "${@}"; }

# -------------------------------------------------------------------------------------------------
# Global Variables
# -------------------------------------------------------------------------------------------------

CWD="$( cd "\$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# -------------------------------------------------------------------------------------------------
# Program Entry Point(s)
# -------------------------------------------------------------------------------------------------

# - - - - - - - - - - - -
# Command-Line Arguments
# - - - - - - - - - - - -

[[ -z "${1}" ]] && echo "A Commit Message is Required" \
    && echo "    >>> git commit -m 'Feature: Implemented Git-Commit Hook'" \
        && exit 1

# - - - |

# - - - - - - -
# Validations
# - - - - - - -

if [[ -z "$( command -v git-lfs )" ]]; then
    echo "Git-LFS is Required"
    echo
    echo "Please Install Git-LFS to Further Develop"
    echo " - https://git-lfs.github.com"
    echo

    exit 2
fi

# - - - |

BRANCH="$(git rev-parse --abbrev-ref HEAD)"

TYPES="Environment|Revert|Fix|Hot-Fix|Bug|Bug-Fix|Feature|Bump|Test|Build|No-Build|CI|Refactor|Style|Document|Merge|Versioning"
ALIASES="Reversion|Chore|N/A|Report|Features|Release|Debuggin|Refactoring|Styles|Styling|Documentation|Version"

REGEX="(((${TYPES}|${ALIASES})(\((\w{0,15})\))?))(\:.*\S.*)"

DIR="$( printf "%s" "$( git rev-parse --show-toplevel )" )"
URL="$( printf "%s" "$( git remote get-url origin )" )"
BASE="$( printf "%s" "$( basename "$(git remote get-url origin)" )" )"
AUTHOR="$( printf "%s" "$( git for-each-ref --format='%(authorname)' | sed -n 1p )" )"
DATETIME="$( date +'%d/%m/%Y' )"
FORMATTING="### %aD ### %n%n- Author: [%aN](mailto:%aE)%n- Commit: %s %n- Hash: %H %n"

COMMIT="$( cat "${DIR}/.git/COMMIT_EDITMSG" )"

echo

Point "Source: $( Print "${B}" "${DIR}" )"
Point "Branch: $( Print "${B}" "${BRANCH}" )"
Point "URL: $( Print "${B}" "${URL}" )"
Point "Repository: $( Print "${B}" "${BASE}" )"
Point "Timestamp $( Print "${B}" "${DATETIME}" )"

echo

( git add . ) 1>/dev/null 2>/dev/null

if ! grep -iqE "${REGEX}" <<< "${COMMIT}"; then
    Tabular "Validation(s): $( Error "Scope - Error (1/3)" )" && echo \
        && echo "Invalid Commit Convention(s)" \
            && exit 3
fi

Tabular "Validation(s): $( Success "Scope - Success (1/3)" )" && echo

if [[ "${BRANCH}" == "master" ]]; then
    Tabular "Validation(s): $( Warning "Master - Success (2/3)" )" && echo
else
    Tabular "Validation(s): $( Success "Master - Success (2/3)" )" && echo
fi

if (  [[ "${BRANCH}" == "Production"  ]] || \
      [[ "${BRANCH}" == "UAT"         ]] || \
      [[ "${BRANCH}" == "Staging"     ]]  )
then
    Tabular "Validation(s): $( Error "Branch - Error (3/3)" )" && echo \
        && echo "Cannot Directly Commit to a Protected Branch" \
          && exit 5
fi

Tabular "Validation(s): $( Success "Branch - Success (3/3)" )" && echo

#
# >>> Automated Changelog Generation
# ...     (Under Development)
# ===================================
# CHANGELOG="${DIR}/CHANGELOG.md"
# git --no-pager log --no-merges --format="${FORMATTING}" > "${CHANGELOG}"
# CHANGELOG_STATUS="$( git status --porcelain | grep -c "${CHANGELOG}" )"
# [[ "${CHANGELOG_STATUS}" == "1" ]] || git add "${CHANGELOG}" && git commit --all
#

[[ "${?}" == "0" ]] && Success "Commit Validation(s) Complete" \
    && echo "" && exit 0

[[ "${?}" != "0" ]] && Error "Commit Validation(s) Failed" \
    && echo "" && exit ${?}

