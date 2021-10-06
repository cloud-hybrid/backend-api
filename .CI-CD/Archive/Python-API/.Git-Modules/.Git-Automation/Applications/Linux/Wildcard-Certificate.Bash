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

print () {
    local input="$1"

    echo "${input}"
    echo ""

    sleep 2.0
}

print "Installing Certificate Service"

sudo add-apt-repository ppa:certbot/certbot --enable-source --yes

sudo apt install certbot \
    --show-progress \
    --show-upgraded \
    --install-recommends \
    --ignore-hold \
    --assume-yes

print "Creating SSL Certificate"

sudo certbot certonly \
    --agree-tos \
    --email development@cloudhybrid.io \
    --manual \
    --preferred-challenges dns \
    --server https://acme-v02.api.letsencrypt.org/directory \
    --manual-public-ip-logging-ok \
    -d "*.${1}"