#!/usr/bin/env bash

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:    *    -*- #

# ========================================================================
# --> SSL Certificate Management Executable (UTF-8, Script)
# ========================================================================
# - Usage: sudo chmod a+x ./SSL-Certificate && sudo \
#		./SSL-Certificate [Domain]
#     --> Where `Domain` is the desired *base* FQDN. The `Domain`
#         parameter should not not have `*.` or "www." pre-fixed; the
#         following script will append the www context accordingly.
#

set -e

if [ -n "$1" ]; then
    echo "Domain: $1"
else
    echo "Domain Name Argument Required"
    exit 255
fi

sudo dnf install epel-release -y

sudo dnf install certbot -y

# @Note --> Ensure to have A record pointing to IP prior to calling

cat << EOF | sudo tee "/etc/nginx/sites-enabled/${1}.conf"
server {
    listen 80;
    listen [::]:80;
    server_name ${1} www.${1};
    root /var/www/html;
    index index.php index.html index.htm index.nginx-debian.html;

    client_max_body_size 0;

    underscores_in_headers  on;
    ignore_invalid_headers  off;
    ssi_silent_errors       on;
    server_tokens           off;

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

sudo nginx -t
sudo nginx -s reload

find /etc/nginx -type d -exec chmod 755 {} \;
find /etc/nginx -type f -exec chmod 644 {} \;

find /var/www/html -type d -exec chmod 755 {} \;
find /var/www/html -type f -exec chmod 644 {} \;

find /usr/share/nginx/html -type d -exec chmod 755 {} \;
find /usr/share/nginx/html -type f -exec chmod 644 {} \;

sudo certbot certonly \
    --agree-tos \
    --email development@cloudhybrid.io \
    --webroot \
    --webroot-path /var/www/html \
    --domains $1 \
        --domains "www.${1}" \
            --non-interactive

cat << EOF | sudo tee "/etc/nginx/sites-enabled/${1}.conf"
server {
    listen 80;
    listen [::]:80;

    server_name ${1} www.${1};

    root /var/www/html;

    return 301 https://\$host\$request_uri;
}

server {
    listen 443 ssl http2;
    server_name ${1} www.${1};

    ssl_certificate /etc/letsencrypt/live/${1}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/${1}/privkey.pem;

    root /var/www/html;

    client_max_body_size 0;

    underscores_in_headers  on;
    ignore_invalid_headers  on;
    ssi_silent_errors       off;
    server_tokens           on;

    location / {
        http2_push_preload on;
        proxy_intercept_errors off;
        proxy_ignore_client_abort on;
        include uwsgi_params;
        include ssl.conf;
        include security.conf;
        include proxy.conf;
        proxy_pass http://172.16.128.100:5000;
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