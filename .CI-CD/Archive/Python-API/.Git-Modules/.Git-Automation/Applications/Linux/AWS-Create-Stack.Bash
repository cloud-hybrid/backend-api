#!/bin/bash --posix

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

#
# ========================================================================
# AWS Cloudformation Stack Handler
# ========================================================================
# --> Simple CLI Interface for CFN [Create|Update|Delete] Stack-Events.
# 
# In addition to interfacing `awscli`, the following script makes various
# abstractions and assumptions; such includes that the Cloudformation
# stack is defined in a `Stack.Yaml` file, parameters are passed via
# JSON in `Stack.json` & that certain `CAPABILITIES` are required.
#
# However, updating the following script to better align with other CFN
# resources... is not difficult.
#
# NOTE - when issuing CFN-related stack events, appending `--disable-rollback`
# unsuccessful inits will NOT delete the stack nor the instance/container(s);
# -- this is especially useful for debugging via an active resource.
#
# PS) There's a fun wait handler in the form of *Ping-Ping :D
#
# Reference List & Source(s)
# ------------------------------------------------------------------------
# [1] - [Embedding Variables](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-init.html)
# [2] - [Runner RPMs (YUM)](https://packages.gitlab.com/runner/gitlab-runner)
# [3] - [Proxy Settings (Gitlab Docs)](https://docs.gitlab.com/runner/configuration/proxy.html)
# [4] - [Source Packaging & Distribution](https://packagecloud.io/docs#os_distro_version)
# [5] - [YUM Repository Overview](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-configuring_yum_and_yum_repositories)
# [6] - [*.repo Variables](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-Using_Yum_Variables)
# [7] - [Gitlab Fargate](https://github.com/1Strategy/fargate-cloudformation-example/blob/master/fargate.yaml)
# [8] - [AWS Referenced Code Snippets (ECS)](https://github.com/aws-samples/ecs-refarch-cloudformation)
#

#
# Usage & Example(s)
# ------------------------------------------------------------------------
# $ ./Stack
# >>> "▐   ●       ▌"
# ...
# >>> "Complete"
# 
# General Cloudformation
# - - - - - - - - - - - -
# ---> Validation
# $ aws cloudformation validate-template \
# ...   --template-body "file://Stack.Yaml"
# >>> [JSON DATA IF SUCCESSFUL] && CODE 0
#
# Management [Create|Update|Delete]
# - - - - - - - - - - - - - - - - - -
# ---> Create
# $ aws cloudformation create-stack                  \
# ...   --stack-name "${STACK}"                      \
# ...   --template-body "file://${CWD}/${TEMPLATE}"  \
# ...   --parameters "file://${CWD}/${JSON}"         \
# ...       --capabilities CAPABILITY_NAMED_IAM      \
# ...           --disable-rollback
#
# ---> Update
# $ aws cloudformation update-stack                  \
# ...   --stack-name "${STACK}"                      \
# ...   --template-body "file://${CWD}/${TEMPLATE}"  \
# ...   --parameters "file://${CWD}/${JSON}"         \
# ...       --capabilities CAPABILITY_NAMED_IAM      \
# ...           --disable-rollback
#
# ---> Delete
# $ aws cloudformation delete-stack                  \
# ...   --stack-name "${STACK}"
#
# --> Wait While [Create || Update || Delete]
# $ aws cloudformation wait \
# ...   stack-[create|update|delete]-complete \
# ...       --stack-name "[Stack]"
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

tput civis

EOM='\33[0m'

BOLD='\33[1m'
ITALIC='\33[3m'
LINK='\33[4m'
BLINK='\33[5m'
UNDERLINE='\033[4m'
SELECTED='\33[7m'
DIM='\33[2m'

R='\33[91m'
G='\33[32m'
B='\33[34m'

# --------------------------
# F-String STDOUT Functions
# --------------------------

Error ()        { printf "${R}%s${EOM}\n" "${@}"; }
Auxiliary ()    { printf "${B}%s${EOM}\n" "${@}"; }
Success ()      { printf "${G}%s${EOM}\n" "${@}"; }
Print ()        { printf "${EOM}%s${EOM}\n" "${@}"; }

# --------
# Globals
# --------

TEMPLATE="${1}"
PROFILE="Cloud"
STACK="${2}"
JSON="${3}"
CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# ------------------------------------------------------------------------
# Program Entry Point(s) && Main
# ------------------------------------------------------------------------

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

Elevation () {
	if [[ "${UID}" == "0" ]]; then
		echo "User !:= root"
		exit -1
	fi
    if [ -n "${SUDO_USER}" ]; then
		echo "User !:= Sudo"
        exit -1
    fi
}; Elevation

Main () {
    aws cloudformation create-stack                  \
        --stack-name "${STACK}"                      \
        --template-body "file://${CWD}/${TEMPLATE}"  \
        --parameters "file://${CWD}/${JSON}"         \
            --capabilities CAPABILITY_NAMED_IAM      \
                --disable-rollback

    (aws cloudformation wait stack-create-complete \
        --stack-name "${STACK}") 1>&2 &

    while ps -p $PID 1>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log; do
        for ((i = 0; i < ${#Loader[@]}; i++)); do
            printf "${Loader[$i]}\r"
            sleep 0.185
        done
    done
}

if [ ! -n "$(command -v Byte-Alert)" ]; then
cat << EOF > /usr/local/bin/Byte-Alert
#!/bin/bash --posix

say "Byte... Alert: ${1}"

exit 0
EOF

chmod a+x /usr/local/bin/Byte-Alert \
    && export PATH="${PATH}:/usr/local/bin/"

fi

Main $1 && Byte-Alert "Cluster Waiter has Completed" \
    || Success

tput cnorm && tput cvvis
