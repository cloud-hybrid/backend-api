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

sudo bash -c cat << EOF > /etc/nginx/sites-enabled/$1.conf
server {
    listen 80;
    listen [::]:80;
    server_name $1;
    root /var/www/${_DIRECTORY};
    index index.php index.html index.htm index.nginx-debian.html;

    client_max_body_size 0;

    underscores_in_headers  on;
    ignore_invalid_headers  off;
    ssi_silent_errors       on;
    server_tokens           off;

    include ssl.conf;
    include security.conf;

    sub_filter_once off;
    sub_filter 'server_url'      '\$request_uri';
    sub_filter 'remote_addr'     '\$remote_addr:\$remote_port';
    sub_filter 'server_date'     '\$time_local';
    sub_filter 'client_browser'  '\$http_user_agent';
    sub_filter 'request_id'      '\$request_id';
    sub_filter 'reference'       '\$http_referer';
    sub_filter 'status'          '\$status';

    location / {
        try_files \$uri \$uri/ /index.html;
    }

    location /status {
        stub_status;
    }

    location ~ ^/(?:build|tests|config|lib|3rdparty|templates|data)/ {
       deny all;
    }

    location ~* ^\.(jpg|jpeg|gif|css|png|js|ico)$ {
        expires max;
        access_log off;
    }

    location = /robots.txt {
        allow all;
        log_not_found off;
        access_log off;
    }

    location ~ /\.ht {
        access_log off;
        log_not_found off;
        deny all;
    }
}

EOF

_DIRECTORY=$(echo $1 | sed -E "s/\.(com|io|gg|ca|us|org|net)//g")

sudo mkdir -p "/var/www/${_DIRECTORY}"

sudo bash -c cat << EOF > /var/www/${_DIRECTORY}/index.html
<!DOCTYPE html>
<html>
    <head>
        <title>VPS Status</title>
        <link href="data:image/png;base64,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" rel="icon" type="image/png" />
        <style>
            body {
                margin: 0px;
                font: 20px 'RobotoRegular', Arial, sans-serif;
                font-weight: 100;
                height: 100%;
                color: #0f1419;
            }
            div.info {
                display: table;
                background: #e8eaec;
                padding: 20px 20px 20px 20px;
                border: 1px dashed black;
                border-radius: 10px;
                margin: auto;
                width: 85%;
            }
            div.info p {
                display: table-row;
                margin: 5px auto auto auto;
            }
            div.info p span {
                display: table-cell;
                padding: 10px;
            }
            img {
                width: 176px;
                margin: 36px auto 36px auto;
                display:block;
            }
            div.smaller p span {
                color: #3D5266;
            }
            h1, h2 {
                font-weight: 100;
            }
            div.check {
                padding: 0px 0px 0px 0px;
                display: table;
                margin: 36px auto auto auto;
                font: 12px 'RobotoRegular', Arial, sans-serif;
            }
            #footer {
                position: fixed;
                bottom: 36px;
                width: 100%;
            }
            #center {
                width: 400px;
                margin: 0 auto;
                font: 12px Courier;
            }
        </style>

        <script>
            var ref;
            function checkRefresh() {
                if (document.cookie == "refresh=1") {
                    document.getElementById("check").checked = true;
                    ref = setTimeout(function(){location.reload();}, 1000);
                } else {
                }
            }
            function changeCookie() {
                if (document.getElementById("check").checked) {
                    document.cookie = "refresh=1";
                    ref = setTimeout(function(){location.reload();}, 1000);
                } else {
                    document.cookie = "refresh=0";
                    clearTimeout(ref);
                }
            }
        </script>
    </head>

    <body onload="checkRefresh();">
        <img alt="Logo" src="data:image/png;base64,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"/>
        <div class="info">
            <p class="smaller"><span>URI:</span> <span>server_url</span></p>
            <p class="smaller"><span>Date:</span> <span>server_date</span></p>
            <p class="smaller"><span>Load-Balancer IP:</span> <span>remote_addr</span></p>
            <p class="smaller"><span>Request Code:</span> <span>status</span></p>
        </div>
        <div class="check">
            <input type="checkbox" id="check" onchange="changeCookie()"> Auto</input>
        </div>
        <div id="footer">
            <div id="center" align="center">
                Request ID: request_id<br/>
                © Cloud Hybrid LLC. 2020
            </div>
        </div>
    </body>
</html>

EOF

print "Correcting File & Directory Permissions"

find /etc/nginx -type d -exec chmod 755 {} \;
find /etc/nginx -type f -exec chmod 644 {} \;

sudo chown -R www-data:www-data /var/www/${_DIRECTORY}
sudo chown -R www-data:www-data /var/www/html

find /var/www/${_DIRECTORY} -type d -exec chmod 755 {} \;
find /var/www/${_DIRECTORY} -type f -exec chmod 644 {} \;
find /var/www/html -type d -exec chmod 755 {} \;
find /var/www/html -type f -exec chmod 644 {} \;

print "Validating NGINX Server Configuration"

sudo nginx -t

print "Restarting NGINX"

sudo systemctl restart nginx.service

print "Confirming NGINX Status"

sudo systemctl is-enabled nginx.service

sudo chown $USER -R /var/www
sudo chmod 755 -R /var/www

sudo chmod a+x ./Dynamic-DNS && sudo ./Dynamic-DNS $1 $2 $3

print "Creating SSL Certificate"

sudo certbot certonly \
    --agree-tos \
    --email development@cloudhybrid.io \
    --webroot \
    --webroot-path /var/www/html \
    --domains $1 \
        --non-interactive

print "Updating NGINX Server(s) with SSL Settings"

sudo bash -c cat << EOF > /etc/nginx/sites-enabled/$1.conf
server {
    listen 443 http2 ssl;
    listen [::]:443 http2 ssl;
    server_name $1;

    root /var/www/${_DIRECTORY};

    index index.php index.html index.htm index.nginx-debian.html;

    ssl_certificate /etc/letsencrypt/live/$1/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$1/privkey.pem;

    client_max_body_size 0;

    underscores_in_headers  on;
    ignore_invalid_headers  off;
    ssi_silent_errors       on;
    server_tokens           off;

    server_name_in_redirect on;

    include ssl.conf;
    include security.conf;

    sub_filter_once off;
    sub_filter 'server_hostname' '\$hostname';
    sub_filter 'server_url'      '\$request_uri';
    sub_filter 'remote_addr'     '\$remote_addr:\$remote_port';
    sub_filter 'server_date'     '\$time_local';
    sub_filter 'client_browser'  '\$http_user_agent';
    sub_filter 'request_id'      '\$request_id';
    sub_filter 'reference'       '\$http_referer';
    sub_filter 'status'          '\$status';

    location / {
        try_files \$uri \$uri/ /index.php;
    }

    location /status {
        stub_status;
    }

    location ~ ^/(?:build|tests|config|lib|3rdparty|templates|data)/ {
       deny all;
    }

    location ~* ^\.(jpg|jpeg|gif|css|png|js|ico)$ {
        expires max;
        access_log off;
    }

    location = /robots.txt {
        allow all;
        log_not_found off;
        access_log off;
    }

    location ~ /\.ht {
        access_log off;
        log_not_found off;
        deny all;
    }
}

server {
    listen *:80;
    listen [::]:80;

    server_name $1;

    root /var/www/${_DIRECTORY};
    index index.html index.htm index.nginx-debian.html;

    location / {
        return 301 https://$1\$request_uri;
    }
}

EOF

print "Testing NGINX Settings"

sudo nginx -t

print "Restarting NGINX"

sudo systemctl restart nginx.service

exit 0
