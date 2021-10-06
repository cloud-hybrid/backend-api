#(!)/usr/bin/env bash --posix

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

# Source:   code.cloud-technology.io
# Creator:  Jacob B. Sanders
# License:  BSD 3-Clause License

# Copyright 2020, Jacob B. Sanders - Cloud Hybrid LLC. & Affiliates

# ------------------------------------------------------------------------
# Git-Module Installer
# ------------------------------------------------------------------------

export URL="https://code.cloud-technology.io"

export ERROR_GIT_CLONE=( 100 "Git Clone Failure" )
export ERROR_GIT_SUBMODULES=( 101 "No Git Submodules Specified" )

# --> Modules

export MODULES=()

export MODULE=(
    ${URL}/Automata/.IO.git
    ".IO"
); MODULES+=(${MODULE[@]})
export MODULE=(
    "${URL}/Automata/Badge-Generator.git"
    ".Badges"
); MODULES+=(${MODULE[@]})
export MODULE=(
    "${URL}/Automata/Git-Template.git"
    ".Git-Template"
); MODULES+=(${MODULE[@]})
export MODULE=(
    "https://github.com/github/gitignore.git"
    ".Git-Ignore"
); MODULES+=(${MODULE[@]})

(( TOTAL = ${#MODULES[@]} ))

[[ "${TOTAL}" == "0" ]] && printf "%s\n" \
    "${ERROR_GIT_SUBMODULES[1]}" && exit \
        ${ERROR_GIT_SUBMODULES[0]}

rm -r -f .git && git init .

echo "Downloading Modules ..." && echo

for (( INDEX = 0; INDEX < ${TOTAL}; INDEX = INDEX + 2 )); do
    rm -r -f "${MODULES[$(( ${INDEX} + 1 ))]}"

    git clone --recurse-submodules \
        "${MODULES[$(( ${INDEX} ))]}" \
        "${MODULES[$(( ${INDEX} + 1 ))]}"

    echo && git submodule add --force "${MODULES[$(( ${INDEX} ))]}" \
        "${MODULES[$(( ${INDEX} + 1 ))]}" && echo

    git submodule sync --recursive "${MODULES[$(( ${INDEX} + 1 ))]}"

done

git submodule update --init --recursive

#
# --> Optional
# cp .IO/.Git-IO/.Git-Commit-Message-Hook.Bash .git/hooks/commit-msg
# chmod a+x .git/hooks/commit-msg
#
# --> Optional
# cp .IO/.Git-IO/.Git-Pre-Push.Bash .git/hooks/pre-push
# chmod a+x .git/hooks/pre-push
#

echo -n "Remote URL (Append '.git' to the URI) [ENTER]: " && read TARGET

git lfs install && git config "lfs.${TARGET}/info/lfs.locksverify" true

cat << 'EOF' > ./.gitattributes
*.iso 	filter=lfs diff=lfs merge=lfs -text
*.mp4 	filter=lfs diff=lfs merge=lfs -text
*.zip 	filter=lfs diff=lfs merge=lfs -text
*.app 	filter=lfs diff=lfs merge=lfs -text
*.jar 	filter=lfs diff=lfs merge=lfs -text
*.tar 	filter=lfs diff=lfs merge=lfs -text
*.gz 	  filter=lfs diff=lfs merge=lfs -text
*.tz 	  filter=lfs diff=lfs merge=lfs -text
*.psd 	filter=lfs diff=lfs merge=lfs -text
*.rar 	filter=lfs diff=lfs merge=lfs -text
*.pdf   filter=lfs diff=lfs merge=lfs -text
*.pkg   filter=lfs diff=lfs merge=lfs -text
*.dmg   filter=lfs diff=lfs merge=lfs -text
EOF

git add --all && git commit -m "Git Initialization"

git remote add origin "${TARGET}"

git checkout -B Development && git add --all && git commit -m "Initialization - ${TARGET}"

git push --set-upstream "${TARGET}" "Development"

echo " - ${PWD}" && exit 0

