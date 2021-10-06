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

    echo ""
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

print "Calculating Regular Expression Substitutions"

DIRECTORY=$(echo $1 | sed -E "s/\.(com|io|gg|ca|us|org|net)//g")

print "Making Directories"

sudo mkdir -p "/var/www/${DIRECTORY}"

print "Setting Permissions"

find /var/www -type d -exec chmod 755 {} \;
find /var/www -type f -exec chmod 644 {} \;

sudo chown -R www-data:www-data /var/www/${DIRECTORY}
sudo chown -R www-data:www-data /var/www/html

print "Initializing Web-Server Record"

sudo bash -c cat << EOF > /etc/nginx/sites-enabled/${1}.conf
server {
    listen 443 http2 ssl;
    listen [::]:443 http2 ssl;
    server_name ${1};

    root /var/www/${DIRECTORY};

    index index.php index.html index.htm index.nginx-debian.html;

    ssl_certificate /etc/letsencrypt/live/${1}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/${1}/privkey.pem;

    client_max_body_size 0;

    underscores_in_headers  on;
    ignore_invalid_headers  off;
    ssi_silent_errors       on;
    server_tokens           off;

    server_name_in_redirect on;

    include ssl.conf;
    include security.conf;
    include proxy.conf;

    location / {
        http2_push_preload on;

        autoindex on;
        autoindex_format json;
        autoindex_localtime on;
    }
}

server {
    listen *:80;
    listen [::]:80;

    server_name ${1};

    root /var/www/${_DIRECTORY};
    index index.html index.htm index.nginx-debian.html;

    location / {
        return 301 https://${1}\$request_uri;
    }
}

EOF

print "Validating Changes"

sudo nginx -t

exit 0