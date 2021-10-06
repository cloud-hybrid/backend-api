#!/bin/bash --posix

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

#
# ========================================================================
# CentOS-8 Virt-Installer
# ========================================================================
# Examples)
# >>> $ ./Create-VM.Bash Test-VM 4 4096 25 \
# ...       172.16.128.150  \
# ...       255.255.0.0     \
# ...       172.16.0.1
#
# >>> $ ./Create-VM.Bash Test-VM 4 4096 25 172.16.128.150 255.255.0.0 172.16.0.1
#

# --------------------
# Terminal Formatting
# --------------------

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

Error ()        { printf "${R}%s${EOM}\n" "${@}"; sleep 0.3875; }
Auxiliary ()    { printf "${B}%s${EOM}\n" "${@}"; sleep 0.3875; }
Success ()      { printf "${G}%s${EOM}\n" "${@}"; sleep 0.3875; }

Print ()        { printf "${EOM}%s${EOM}\n" "${@}"; sleep 0.3875; }
Prompt ()       { printf "${EOM}%s${EOM}: " "${@}"; sleep 0.3875; }

# --------
# Globals
# --------

NGINX="1.17.8"

PCRE="8.44"
OPENSSL="1.1.1g"
ZLIB="1.2.11"

CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

PUBLIC_IP="$(curl https://ipecho.net/plain)"

# ------------------------------------------------------------------------
# Program Entry Point(s) && Main
# ------------------------------------------------------------------------

Auxiliary "Updating System"

sudo yum update --assumeyes
sudo yum upgrade --assumeyes

Auxiliary "Installing Development Tools"

sudo yum --assumeyes groupinstall "Development Tools"

Auxiliary "Installing EPEL Packages"

sudo yum install --assumeyes epel-release

Auxiliary "Installing NGINX Dependencies"

sudo yum install -y perl    \
    perl-devel              \
    libxslt                 \
    libxslt-devel           \
    libxml2                 \
    libxml2-devel           \
    gd                      \
    gd-devel                \
    GeoIP                   \
    GeoIP-devel

sudo yum install -y --assumeyes socat

sudo yum install --assumeyes perl   \
    libperl-dev                     \
    libgd3                          \
    libgd-dev                       \
    libgeoip1                       \
    libgeoip-dev                    \
    libxml2                         \
    libxml2-dev                     \
    libxslt1.1                      \
    libxslt1-dev                    \
    geoip-bin

Auxiliary "Installing Tree"

sudo yum install --assumeyes tree

Auxiliary "Installing WGET"

sudo yum install --assumeyes wget

cd ${CWD}

Auxiliary "Installing NGINX"

# sudo curl "http://nginx.org/download/nginx-${VERSION}.tar.gz" \
#     --output "NGINX-Source.tar.gz" && sudo mkdir -p NGINX-Source \
#         && sudo tar xf NGINX-Source.tar.gz -C NGINX-Source \
#             --strip-components 1

wget https://nginx.org/download/nginx-${NGINX}.tar.gz && tar zxvf nginx-${NGINX}.tar.gz

# sudo curl "https://ftp.pcre.org/pub/pcre/pcre-${PCRE}.tar.gz" \
#     --output "PCRE.tar.gz" && sudo mkdir -p PCRE \
#         && sudo tar xf PCRE.tar.gz -C PCRE \
#             --strip-components 1

wget https://ftp.pcre.org/pub/pcre/pcre-${PCRE}.tar.gz && tar zxvf pcre-${PCRE}.tar.gz

# sudo curl "https://www.zlib.net/zlib-${ZLIB}.tar.gz" \
#     --output "Z-LIB.tar.gz" && sudo mkdir -p Z-LIB \
#         && sudo tar xf Z-LIB.tar.gz -C Z-LIB \
#             --strip-components 1

wget https://www.zlib.net/zlib-${ZLIB}.tar.gz && tar xzvf zlib-${ZLIB}.tar.gz

# sudo curl "https://www.openssl.org/source/openssl-${OPENSSL}.tar.gz" \
#     --output "Open-SSL.tar.gz" && sudo mkdir -p Open-SSL \
#         && sudo tar xf Open-SSL.tar.gz -C Open-SSL \
#             --strip-components 1

wget https://www.openssl.org/source/openssl-${OPENSSL}.tar.gz && tar zxvf openssl-${OPENSSL}.tar.gz

cd ${CWD}

Auxiliary "Removing Installation Sources"

rm -rf *.tar.gz

cd ${CWD}/nginx-${NGINX}

tree -L 2 .

Auxiliary "Compiling NGINX Source"

sudo yum group install "Development Tools" --assumeyes

sudo yum group install "Development Tools" --assumeyes || sudo yum groupinstall "Development Tools" --assumeyes

sudo yum install perl-ExtUtils-Embed --assumeyes

./configure --prefix=/etc/nginx                                 \
    --sbin-path=/usr/sbin/nginx                                 \
    --modules-path=/usr/lib/nginx/modules                       \
    --conf-path=/etc/nginx/nginx.conf                           \
    --error-log-path=/var/log/nginx/error.log                   \
    --pid-path=/var/run/nginx.pid                               \
    --lock-path=/var/run/nginx.lock                             \
    --user=nginx                                                \
    --group=nginx                                               \
    --build=CentOS                                              \
    --builddir=nginx-${NGINX}                                   \
    --with-select_module                                        \
    --with-poll_module                                          \
    --with-threads                                              \
    --with-file-aio                                             \
    --with-http_ssl_module                                      \
    --with-http_v2_module                                       \
    --with-http_realip_module                                   \
    --with-http_addition_module                                 \
    --with-http_xslt_module=dynamic                             \
    --with-http_image_filter_module=dynamic                     \
    --with-http_geoip_module=dynamic                            \
    --with-http_sub_module                                      \
    --with-http_dav_module                                      \
    --with-http_flv_module                                      \
    --with-http_mp4_module                                      \
    --with-http_gunzip_module                                   \
    --with-http_gzip_static_module                              \
    --with-http_auth_request_module                             \
    --with-http_random_index_module                             \
    --with-http_secure_link_module                              \
    --with-http_degradation_module                              \
    --with-http_slice_module                                    \
    --with-http_stub_status_module                              \
    --with-http_perl_module=dynamic                             \
    --with-perl_modules_path=/usr/lib64/perl5                   \
    --with-perl=/usr/bin/perl                                   \
    --http-log-path=/var/log/nginx/access.log                   \
    --http-client-body-temp-path=/var/cache/nginx/client_temp   \
    --http-proxy-temp-path=/var/cache/nginx/proxy_temp          \
    --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp      \
    --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp          \
    --http-scgi-temp-path=/var/cache/nginx/scgi_temp            \
    --with-mail=dynamic                                         \
    --with-mail_ssl_module                                      \
    --with-stream=dynamic                                       \
    --with-stream_ssl_module                                    \
    --with-stream_realip_module                                 \
    --with-stream_geoip_module=dynamic                          \
    --with-stream_ssl_preread_module                            \
    --with-compat                                               \
    --with-pcre=../pcre-${PCRE}                                 \
    --with-pcre-jit                                             \
    --with-zlib=../zlib-${ZLIB}                                 \
    --with-openssl=../openssl-${OPENSSL}                        \
    --with-openssl-opt=no-nextprotoneg                          \
    --with-debug

make

sudo make install

Auxiliary "Installing PHP"

sudo amazon-linux-extras install -y php7.2

Auxiliary "Creating System User"

sudo useradd --system               \
    --home /var/cache/nginx         \
    --shell /sbin/nologin           \
    --comment "NGINX System User"   \
        --user-group nginx

sudo mkdir -p /var/cache/nginx

Auxiliary "Installing NGINX Source Binaries to System"

sudo make install

Auxiliary "Creating Web-Server Directories"

sudo mkdir -p /etc/nginx/conf.d     \
    /etc/nginx/snippets             \
    /etc/nginx/sites-available      \
    /etc/nginx/sites-enabled

cd ${CWD} && Success "Successful"

Auxiliary "Linking NGINX Modules"

sudo ln -s /usr/lib64/nginx/modules /etc/nginx/modules

Success "Symbolics Created"

Auxiliary "Validating NGINX"

sudo nginx -V

echo && Success "Successful"

Auxiliary "Creating Cache Directories"

sudo mkdir -p /var/cache/nginx/client_temp \
    /var/cache/nginx/fastcgi_temp \
    /var/cache/nginx/proxy_temp \
    /var/cache/nginx/scgi_temp \
    /var/cache/nginx/uwsgi_temp

sudo chmod 700 /var/cache/nginx/*

Auxiliary "Creating the NGINX System Service"

sudo mkdir -p "/etc/systemd/system"

cat << 'EOF' | sudo tee /etc/systemd/system/nginx.service
[Unit]
Description=nginx - high performance web server
Documentation=https://nginx.org/en/docs/
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/var/run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t -c /etc/nginx/nginx.conf
ExecStart=/usr/sbin/nginx -c /etc/nginx/nginx.conf
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
EOF

sudo service start nginx.service && sudo service enable nginx.service

Auxiliary "Creating Webroot Directories & Correcting Permissions"

sudo mkdir -p /var/www/html
sudo mkdir -p /usr/share/nginx/html
sudo mkdir -p /var/log/nginx

sudo cp /etc/nginx/html/* /var/www/html

sudo chmod -R 755 /var/www/html/

sudo touch /var/log/nginx/access.log
sudo touch /var/log/nginx/error.log

sudo chmod 640 /var/log/nginx/*

Success "Files & Directories Provisioned Successfully"

Auxiliary "Re-Creating NGINX Server Configuration File"

sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.default

cat << EOF | sudo tee /etc/nginx/nginx.conf
user nginx;

pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

worker_processes 4;
worker_priority -1;
worker_rlimit_nofile 8192;
worker_cpu_affinity 0001 0010 0100 1000;

error_log /var/log/nginx/error.log;

events {
    multi_accept on;
    worker_connections 4096;
    use epoll;
}

http {
    charset utf-8;
    sendfile on;
    aio threads;
    aio_write on;

    tcp_nopush on;
    tcp_nodelay on;
    server_tokens off;
    log_not_found off;
    types_hash_max_size 2048;

    client_max_body_size 0;
    client_body_timeout 30;

    send_timeout 10;

    keepalive_timeout 15;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*.conf;
    include /etc/nginx/mime.types;

    default_type application/octet-stream;

    log_format main      '\$remote_addr - \$remote_user [\$time_local]  '
    '"\$request" \$status \$bytes_sent '
    '"\$http_referer" "\$http_user_agent" '
    '"\$gzip_ratio"';

    log_format download  '\$remote_addr - \$remote_user [\$time_local]  '
    '"\$request" \$status \$bytes_sent '
    '"\$http_referer" "\$http_user_agent" '
    '"\$http_range" "\$sent_http_content_range"';

    ssl_session_cache shared:le_nginx_SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets off;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS';
    ssl_prefer_server_ciphers on;

    ssl_dhparam /etc/nginx/dhparam.pem;

    ssl_stapling on;
    ssl_stapling_verify on;

    ssl_ecdh_curve secp521r1:secp384r1:prime256v1;

    resolver 1.1.1.1 1.0.0.1 8.8.8.8 8.8.4.4 208.67.222.222 208.67.220.220 valid=60s;
    resolver_timeout 5s;

    gzip                    on;
    gzip_disable            'msie6';
    gzip_vary               on;
    gzip_min_length         128;
    gzip_buffers            128 32k;
    gzip_comp_level         6;
    gzip_proxied            any;
    gzip_types              text/plain text/css text/x-component
                            text/xml application/xml application/xhtml+xml application/json
                            image/x-icon image/bmp image/svg+xml application/atom+xml
                            text/javascript application/javascript application/x-javascript
                            application/pdf application/postscript
                            application/rtf application/msword
                            application/vnd.ms-powerpoint application/vnd.ms-excel
                            application/vnd.ms-fontobject application/vnd.wap.wml
                            application/x-font-ttf application/x-font-opentype;

    add_header 'Access-Control-Allow-Origin' 'Origin' always;
    add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, OPTIONS' always;
    add_header 'Access-Control-Max-Age' 1728000 always;
    add_header 'Access-Control-Allow-Credentials' 'true';

    add_header Strict-Transport-Security 'max-age=31536000; includeSubdomains; preload' always;

    add_header 'X-Frame-Options' 'SAMEORIGIN' always;
    add_header 'X-Content-Type-Options' 'nosniff' always;
    add_header 'X-XSS-Protection' '1; mode=block' always;
    add_header 'X-Robots-Tag' none always;
}

EOF

sudo mkdir -p /var/www/_letsencrypt

cat << EOF | sudo tee /etc/nginx/ssl.conf
location ^~ /.well-known/acme-challenge/ {
    root /var/www/html;
}

EOF

cat << EOF | sudo tee /etc/nginx/security.conf
location ~ /\.(?!well-known) {
    deny all;
}

EOF

cat << EOF | sudo tee /etc/nginx/python.conf
uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;
EOF

cat << EOF | sudo tee /etc/nginx/proxy.conf
proxy_redirect   off;

proxy_http_version      1.1;
proxy_cache_bypass      \$http_upgrade;

proxy_set_header Upgrade        \$http_upgrade;
proxy_set_header Connection     "upgrade";

proxy_set_header Host               \$http_host;

proxy_set_header X-Real-Host        \$http_host;
proxy_set_header X-Real-IP          \$remote_addr;
proxy_set_header X-Real-Port        \$remote_port;
proxy_set_header X-Real-Referrer    \$http_referer;

proxy_set_header X-Access-Token     \$http_x_access_token;

proxy_set_header X-Forwarded-For    \$proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto  \$scheme;

proxy_set_header  X-Access-Control-Allow-Origin       \$query_string;
proxy_set_header  X-Access-Control-Allow-Methods      \$request_method;
proxy_set_header  X-Access-Control-Max-Age            \$content_type;
proxy_set_header  X-Access-Control-Allow-Credentials  \$content_length;

proxy_set_header  X-Frame-Options           \$request_uri;
proxy_set_header  X-Document-URI            \$document_uri;
proxy_set_header  X-Server-Protocol         \$server_protocol;
EOF

cat << EOF | sudo tee /etc/nginx/sites-enabled/default.conf
server {
    listen 80;
    listen [::]:80;
    server_name $PUBLIC_IP _;
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

cat << EOF | sudo tee /var/www/html/index.html
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
                
?
? Cloud Hybrid LLC. 2020
            </div>
        </div>
    </body>
</html>

EOF

Success "Complete"

Auxiliary "Generating dhparam.pem"

sudo openssl dhparam -out /etc/nginx/dhparam.pem 2048

Success "Generation Complete"

Auxiliary "Correcting File & Directory Permissions"

find /etc/nginx -type d -exec chmod 755 {} \;
find /etc/nginx -type f -exec chmod 644 {} \;

find /var/www/html -type d -exec chmod 755 {} \;
find /var/www/html -type f -exec chmod 644 {} \;

find /usr/share/nginx/html -type d -exec chmod 755 {} \;
find /usr/share/nginx/html -type f -exec chmod 644 {} \;

Success "Corrected"

Auxiliary "Validating NGINX Server Configuration"

sudo nginx -t

Success "Validated"

Auxiliary "Reloading System Daemon(s)"

sudo service daemon-reload

Success "Reloaded"

Auxiliary "Enabling NGINX upon Reboot"

sudo service enable nginx.service

Success "Enabled"

Auxiliary "Starting NGINX"

sudo service start nginx.service

Success "Started"

Auxiliary "Confirming NGINX Status"

sudo service is-enabled nginx.service

sudo chmod 755 -R /var/www

sudo yum update
sudo service httpd stop
sudo yum remove php*
sudo yum remove httpd*
sudo yum clean all
sudo yum upgrade -y
# sudo yum install httpd24
sudo yum install -y php73 php73-gd php73-xml php73-xmlrpc php73-fpm php73-mysqli --assumeyes --skip-broken
# sudo yum install mod24_ssl

cat << 'EOF' | sudo tee /etc/init.d/nginx
#!/bin/sh
#
# nginx - this script starts and stops the nginx daemon
#
# chkconfig:   - 85 15
# description:  NGINX is an HTTP(S) server, HTTP(S) reverse \
#               proxy and IMAP/POP3 proxy server
# processname: nginx
# config:      /etc/nginx/nginx.conf
# config:      /etc/sysconfig/nginx
# pidfile:     /var/run/nginx.pid

# Source function library.
. /etc/rc.d/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0

nginx="/usr/sbin/nginx"
prog=$(basename $nginx)

NGINX_CONF_FILE="/etc/nginx/nginx.conf"

[ -f /etc/sysconfig/nginx ] && . /etc/sysconfig/nginx

lockfile=/var/lock/subsys/nginx

make_dirs() {
   # make required directories
   user=`$nginx -V 2>&1 | grep "configure arguments:.*--user=" | sed 's/[^*]*--user=\([^ ]*\).*/\1/g' -`
   if [ -n "$user" ]; then
      if [ -z "`grep $user /etc/passwd`" ]; then
         useradd -M -s /bin/nologin $user
      fi
      options=`$nginx -V 2>&1 | grep 'configure arguments:'`
      for opt in $options; do
          if [ `echo $opt | grep '.*-temp-path'` ]; then
              value=`echo $opt | cut -d "=" -f 2`
              if [ ! -d "$value" ]; then
                  # echo "creating" $value
                  mkdir -p $value && chown -R $user $value
              fi
          fi
       done
    fi
}

start() {
    [ -x $nginx ] || exit 5
    [ -f $NGINX_CONF_FILE ] || exit 6
    make_dirs
    echo -n $"Starting $prog: "
    daemon $nginx -c $NGINX_CONF_FILE
    retval=$?
    echo
    [ $retval -eq 0 ] && touch $lockfile
    return $retval
}

stop() {
    echo -n $"Stopping $prog: "
    killproc $prog -QUIT
    retval=$?
    echo
    [ $retval -eq 0 ] && rm -f $lockfile
    return $retval
}

restart() {
    configtest || return $?
    stop
    sleep 1
    start
}

reload() {
    configtest || return $?
    echo -n $"Reloading $prog: "
    killproc $prog -HUP
    retval=$?
    echo
}

force_reload() {
    restart
}

configtest() {
  $nginx -t -c $NGINX_CONF_FILE
}

rh_status() {
    status $prog
}

rh_status_q() {
    rh_status >/dev/null 2>&1
}

case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart|configtest)
        $1
        ;;
    reload)
        rh_status_q || exit 7
        $1
        ;;
    force-reload)
        force_reload
        ;;
    status)
        rh_status
        ;;
    condrestart|try-restart)
        rh_status_q || exit 0
            ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload|configtest}"
        exit 2
esac
EOF

sudo /etc/init.d/php-fpm start

Success "NGINX Installer Complete" &&
    exit 0
