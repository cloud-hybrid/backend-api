#!/usr/bin/env bash

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:    *    -*- #

set -e

if [ -n "$1" ]; then
    echo "Domain: $1"
else
    echo "Domain Name Argument Required"
    exit -1
fi

if [ -n "$2" ]; then
    echo "Username: $2"
else
    echo "Dynamic DNS Username Argument Required"
    exit -1
fi

if [ -n "$3" ]; then
    echo "Domain: $3"
else
    echo "Dynamic DNS Password Argument Required"
    exit -1
fi

print () {
    local input="$1"

    echo "${input}"
    echo ""

    sleep 2.0
}

echo ""
echo " ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ "
echo " ┃                         Automation                      ┃ "
echo " ┃                      ----------------                   ┃ "
echo " ┃   The following source file(s) contains confidential,   ┃ "
echo " ┃  proprietary information. Unauthorized use is strictly  ┃ "
echo " ┃    prohibited. No portions may be copied, reproduced,   ┃ "
echo " ┃      or incorporated outside of this domain without     ┃ "
echo " ┃         Cloud Hybrid LLC's prior written consent.       ┃ "
echo " ┃                                                         ┃ "
echo " ┃            Copyright (C) 2020, Cloud Hybrid.            ┃ "
echo " ┃                   All rights reserved.                  ┃ "
echo " ┃                                                         ┃ "
echo " ┃   ┌───────────┬─────────────────────────────────────┐   ┃ "
echo " ┃   │  License  │          (Private-Use Only)         │   ┃ "
echo " ┃   ├───────────┼─────────────────────────────────────┤   ┃ "
echo " ┃   │  Creator  │           Jacob B. Sanders          │   ┃ "
echo " ┃   ├───────────┼─────────────────────────────────────┤   ┃ "
echo " ┃   │   Email   │    jacob.sanders@cloudhybrid.io     │   ┃ "
echo " ┃   └───────────┴─────────────────────────────────────┘   ┃ "
echo " ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ "
echo ""

print "Ensuring DDClient Installation"

PKG="ddclient"
STATUS=$(dpkg-query -W --showformat='${Status}\n' $PKG | grep "install ok installed")
if [ "" = "$STATUS" ]; then
    print "Installing DDClient"
    set +e
    sudo DEBIAN_FRONTEND=noninteractive apt install ddclient --assume-yes --ignore-hold
    set -e
fid

print "Setting Dynamic IP Variables"

sudo cp /etc/ddclient.conf /etc/ddclient.backup

sudo bash -c cat << EOF >> /etc/ddclient.conf
protocol=dyndns2
use=web
server=domains.google.com
ssl=yes
login=$2
password='$3'
$1

EOF

set +e

sudo ddclient restart

set -e

exit 0