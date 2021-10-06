#!/usr/bin/env bash

sudo apt update -y \
    && sudo apt full-upgrade -y \
    && sudo apt autoremove -y \
    && sudo apt clean -y \
    && sudo apt autoclean -y

sudo apt install software-properties-common \
    build-essential \
    python-dev \
    python3 \
    python3-doc \
    python3-examples \
    python3-dev \
    python3-doc \
    python3-dbg \
    python3.8 \
    python3.8-dbg \
    python3.8-dev \
    python3.8-venv \
        --show-progress \
        --show-upgraded \
        --install-recommends \
        --ignore-hold \
        --assume-yes

print "Installing Programming & Networking Tools"

sudo apt install net-tools \
    git \
    tree \
    zip \
    unzip \
    unzip \
    glances \
    wget \
    ufw \
        --show-progress \
        --show-upgraded \
        --install-recommends \
        --ignore-hold \
        --assume-yes

sudo add-apt-repository universe --enable-source --yes

echo "Y" | sudo ufw enable

sudo ufw allow 22
echo "Opened Port(s): 22"
sudo ufw allow 80
echo "Opened Port(s): 80"
sudo ufw allow 8080
echo "Opened Port(s): 8080"
sudo ufw allow 9000
echo "Opened Port(s): 9000"
sudo ufw allow 443
echo "Opened Port(s): 443"
sudo ufw allow 4443
echo "Opened Port(s): 4443"
sudo ufw allow 4380
echo "Opened Port(s): 4380"
sudo ufw allow 5000
echo "Opened Port(s): 5000"
sudo ufw allow 6000:6250/tcp
echo "Opened Port(s): 6000:6250/tcp"
sudo ufw allow 10000:11000/tcp
echo "Opened Port(s): 10000:11000/tcp"
sudo ufw allow 15000:15100/udp
echo "Opened Port(s): 15000:15100/udp"
sudo ufw allow 7777:8777/udp
echo "Opened Port(s): 7777:8777/udp"
sudo ufw allow 27000:27100/udp
echo "Opened Port(s): 27000:27100/udp"

sudo ufw reload
echo "Successfully Reloaded UFW"

echo "Creating Backup of SSH Settings" && echo

sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

SEPERATOR0=""
SEPERATOR1="# ===================== #"
SEPERATOR2="# Cloud-Hybrid Settings #"
SEPERATOR3="# ===================== #"
SEPERATORn=""

echo "Creating SSH-Server Security Notice" && echo

wget https://cloudhybrid.io/API/Server/Automation/SSH-Banner --output-document SSH-Banner.txt --show-progress

cat < SSH-Banner.txt > /etc/ssh/banner.txt

(echo $SEPERATOR0; echo $SEPERATOR1; echo $SEPERATOR2; echo $SEPERATOR3; echo $SEPERATORn) >> /etc/ssh/sshd_config

(echo "Banner /etc/ssh/banner.txt") >> /etc/ssh/sshd_config

echo "Reloading System SSH Service" && echo

sudo service ssh reload

echo "Disabling Login MOTD" && echo

touch .hushlogin

sudo apt update

# --------------------------------------------------------------------- #

echo "Installing Certificate Service" && echo

sudo add-apt-repository ppa:certbot/certbot --enable-source --yes

sudo apt install certbot \
    python-certbot-nginx \
        --show-progress \
        --show-upgraded \
        --install-recommends \
        --ignore-hold \
        --assume-yes

# sudo certbot --m development@cloudhybrid.io --agree-tos -n

# sudo certbot certonly --agree-tos --email admin@example.com --webroot -w /var/lib/letsencrypt/ -d example.com -d www.example.com

# sudo chown $USER -R /var/www

# sudo chmod 755 -R /var/www

echo "Installing NginX" && echo

sudo apt install nginx \
    nginx-extras \
        --show-progress \
        --show-upgraded \
        --install-recommends \
        --ignore-hold \
        --assume-yes

sudo systemctl enable nginx
sudo systemctl start nginx

sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.default

sudo bash -c 'cat << EOF > /etc/nginx/nginx.conf
user www-data;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;
worker_processes auto;
worker_rlimit_nofile 10000;

events {
    multi_accept on;
    worker_connections 10000;
    use epoll;
}

http {
    charset utf-8;
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    server_tokens on;
    log_not_found on;
    types_hash_max_size 2048;
    client_max_body_size 2048M;

    include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*.conf;
    include /etc/nginx/mime.types;

    default_type application/octet-stream;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log debug;

    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:50m;
    ssl_session_tickets off;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES;
    ssl_prefer_server_ciphers on;

    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 1.1.1.1 1.0.0.1 8.8.8.8 8.8.4.4 208.67.222.222 208.67.220.220 valid=60s;
    resolver_timeout 2s;

    gzip off;
}
EOF'

sudo bash -c 'cat << EOF > "/etc/nginx/sites-enabled/default"
server {
    listen 80;
    listen [::]:80;
    server_name _;
    root /usr/share/nginx/html/;
    index index.php index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ /index.php;
    }

    location ~ \.php$ {
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
        include snippets/fastcgi-php.conf;
    }

    location ~* \.(jpg|jpeg|gif|png|webp|svg|woff|woff2|ttf|css|js|ico|xml)$ {
        access_log        off;
        log_not_found     off;
        expires           360d;
    }

    location ~ /\.ht {
        access_log off;
        log_not_found off;
        deny all;
    }
}
EOF'

sudo nginx -t && sudo systemctl reload nginx

echo "Creating Storage-Cloud Server"
echo ""

sudo apt install mariadb-server \
    apt-transport-https \
        --show-progress \
        --show-upgraded \
        --install-recommends \
        --ignore-hold \
        --assume-yes

sudo systemctl start mariadb
sudo systemctl enable mariadb

mysql -u root <<-EOF 
UPDATE mysql.user SET Password=PASSWORD('password') WHERE User='root';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.db WHERE Db='test' OR Db='test_%';
FLUSH PRIVILEGES;
EOF

mysql -u root <<-EOF
CREATE DATABASE nextcloud;
CREATE USER Segmentational IDENTIFIED BY 'Kn0wledge!';
GRANT USAGE ON *.* TO Segmentational@localhost IDENTIFIED BY 'Kn0wledge!';
GRANT ALL privileges ON nextcloud.*  TO Segmentational@localhost identified by 'Kn0wledge!';
FLUSH PRIVILEGES;
quit;
EOF

sudo apt install php7.2 \
    php-common \
    php7.2-cli \
    php7.2-common \
    php7.2-json \
    php7.2-opcache \
    php7.2-readline \
    php7.2-mbstring \
    php7.2-gd \
    php7.2-curl \
    php-imagick \
    php7.2-mysql \
    php7.2-fpm \
    php7.2-zip \
    php7.2-xml \
    php7.2-bz2 \
    php7.2-intl \
        --show-progress \
        --show-upgraded \
        --install-recommends \
        --ignore-hold \
        --assume-yes

wget https://download.nextcloud.com/server/releases/nextcloud-18.0.2.zip

sudo unzip nextcloud-18.0.2.zip -d /var/www/html

sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html/nextcloud/

sudo systemctl enable php7.2-fpm
sudo systemctl start php7.2-fpm

sudo sed -i 's/memory_limit = 128M/memory_limit = 512M/g' /etc/php/7.2/fpm/php.ini
sudo systemctl reload php7.2-fpm

sudo sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 2048M/g' /etc/php/7.2/fpm/php.ini
sudo systemctl restart php7.2-fpm

sudo mv /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default.backup

cat << 'EOF' > /etc/nginx/sites-available/default.conf
server {
    listen 80;
    listen [::]:80;
    server_name _;
    root /var/www/html/nextcloud/;
    index index.php index.html index.htm index.nginx-debian.html;

    client_max_body_size 2048M;
    
    fastcgi_buffers 64 4K;

    access_log /var/log/nginx/20R-Cloud.access;
    error_log /var/log/nginx/20R-Cloud.error;

    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection '1; mode=block';
    add_header X-Robots-Tag none;
    add_header X-Download-Options noopen;
    add_header X-Permitted-Cross-Domain-Policies none;
    add_header Referrer-Policy no-referrer;

    add_header X-Frame-Options 'SAMEORIGIN';

    location / {
       rewrite ^ /index.php$uri;
    }

    location ~ ^/(?:build|tests|config|lib|3rdparty|templates|data)/ {
       deny all;
    }

    location ~ ^/(?:\.|autotest|occ|issue|indie|db_|console) {
       deny all;
    }

    location ~ ^/(?:index|remote|public|cron|core/ajax/update|status|ocs/v[12]|updater/.+|ocs-provider/.+|core/templates/40[34])\.php(?:$|/) {
        include fastcgi_params;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_param modHeadersAvailable true;
        fastcgi_param front_controller_active true;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
        fastcgi_intercept_errors on;
        fastcgi_request_buffering off;
    }

    location ~ ^/(?:updater|ocs-provider)(?:$|/) {
       try_files $uri/ =404;
       index index.php;
    }

    location = /.well-known/carddav {
        return 301 $scheme://$host/remote.php/dav;
    }

    location = /.well-known/caldav {
        return 301 $scheme://$host/remote.php/dav;
    }

    location ~* \.(?:css|js)$ {
        try_files $uri /index.php$uri$is_args$args;
        add_header Cache-Control 'public, max-age=7200';
        add_header X-Content-Type-Options nosniff;
        add_header X-XSS-Protection '1; mode=block';
        add_header X-Robots-Tag none;
        add_header X-Download-Options noopen;
        add_header X-Permitted-Cross-Domain-Policies none;
        add_header Referrer-Policy no-referrer;
        access_log off;
    }

    location ~* \.(?:svg|gif|png|html|ttf|woff|ico|jpg|jpeg)$ {
        try_files $uri /index.php$uri$is_args$args;
        access_log off;
    }

    location ~ /.well-known/acme-challenge {
        allow all;
    }
    
    location = /robots.txt {
        allow all;
        log_not_found off;
        access_log off;
    }

    location ~ \.php$ {
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
        include snippets/fastcgi-php.conf;
    }
   
    gzip off;

    location ~ /\.ht {
        access_log off;
        log_not_found off;
        deny all;
    }
}
EOF

sudo nginx -t

sudo ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

sudo nginx -t

sudo systemctl reload nginx

sudo mkdir -p /var/www/html/nextcloud-data

sudo chown -R www-data:www-data /var/www/html/nextcloud-data

sudo apt install golang-go --yes

wget https://github.com/ipfs/go-ipfs/releases/download/v0.6.0/go-ipfs_v0.6.0_linux-amd64.tar.gz

tar -xvzf go-ipfs_v0.6.0_linux-amd64.tar.gz

cd go-ipfs && sudo bash install.sh

ipfs --version

ipfs init --profile server

# @Task Program Method to use 'secret' => '...' Values
cat << EOF | sudo tee /var/www/nextcloud/config/config-target.php
<?php
$CONFIG = array (
  'instanceid' => 'ocb1zmp9ehq9',
  'passwordsalt' => 'T2eTMav1tifojgbmIRwVHrpSzQ/0Qe',
  'secret' => '8C/Zph62fAzsZGaMd8oKVQRKcQKvvWW/IdQmVaqT1mrgOczP',
  'trusted_domains' => 
  array (
    0 => '172.16.128.130',
    1 => 'cloud.cloudhybrid.io',
    2 => 'cloud.cloud-technology.io',
    3 => 'cloud.20r.gg',
  ),
  'datadirectory' => '/var/www/html/nextcloud/data',
  'dbtype' => 'mysql',
  'version' => '18.0.7.1',
  'overwrite.cli.url' => 'http://172.16.128.130',
  'dbname' => 'nextcloud',
  'dbhost' => 'localhost',
  'dbport' => '',
  'dbtableprefix' => 'oc_',
  'dbuser' => 'Segmentational',
  'dbpassword' => 'Kn0wledge!',
  'installed' => true,
  'updater.secret' => '$2y$10$NfDYslFtY69tbODnY2D32.4311EcGFbbyE.vEv.mV3YBAPMRlEoeG',
  'theme' => '',
  'maintenance' => false,
  'loglevel' => 2,
  'trusted_proxies' =>
  array (
    0 => '172.16.128.125',
    1 => '172.16.128.130'
  ),
  'skeletondirectory' => '',
);
EOF

sudo apt install samba --yes

sudo ufw allow "Samba"

sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.backup

sudo apt install smbclient --yes

sudo apt install cifs-utils --yes


cat << EOF | sudo tee /bin/Sambda
#!/bin/sh

#
# /etc/rc.d/init.d/smb - starts and stops SMB services.
#
# The following files should be synbolic links to this file:
# symlinks: /etc/rc.d/rc1.d/K35smb  (Kills SMB services on shutdown)
#           /etc/rc.d/rc3.d/S91smb  (Starts SMB services in multiuser mode)
#           /etc/rc.d/rc6.d/K35smb  (Kills SMB services on reboot)
#

. /etc/rc.d/init.d/functions

. /etc/sysconfig/network

[ \${NETWORKING} = "no" ] && exit 0

case "\$1" in
    start)
    echo -n "Starting SMB services: "
    daemon smbd -D  
    daemon nmbd -D 
    echo
    touch /var/lock/subsys/smb
    ;;
    stop)
    echo -n "Shutting down SMB services: "
    killproc smbd
    killproc nmbd
    rm -f /var/lock/subsys/smb
    echo ""
    ;;
    *)
    echo "Usage: smb {start|stop}"
    exit 1
esac
EOF

sudo chmod a+x /bin/Sambda

sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.backup

sudo mkdir -p /mnt/Cloud-Mount

sudo mkdir -p /Cloud
sudo mkdir -p /Cloud/Profiles
sudo mkdir -p /Cloud/Cloud-Hybrid
sudo mkdir -p /Cloud/20R-Gaming

sudo useradd -M -d /Cloud/Cloud-Hybrid -s /usr/sbin/nologin -G sambashare Cloud-Hybrid
sudo useradd -M -d /Cloud/20R-Gaming -s /usr/sbin/nologin -G sambashare 20R-Gaming

sudo mount -t cifs -o username=Cloud-Hybrid //172.16.128.130 /mnt/Cloud-Mount
sudo mount -t cifs -o username=20R-Gaming //172.16.128.130 /mnt/Cloud-Mount

sudo chown Cloud-Hybrid:sambashare /Cloud/Cloud-Hybrid
sudo chown 20R-Gaming:sambashare /Cloud/20R-Gaming/

sudo chmod 2770 /Cloud/20R-Gaming
sudo chmod 2770 /Cloud/Cloud-Hybrid

sudo hostnamectl set-hostname Cloud

cat << EOF | sudo tee /etc/hosts
127.0.0.1       localhost
172.16.128.130  cloud.vps.cloudhbrid.io cloud

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
EOF

cat << EOF | sudo tee /etc/samba/smb.conf
[global]
	dns proxy = No
	interfaces = 172.16.128.30/16
	log file = /var/log/samba/log.sambda
	map to guest = Bad User
	max log size = 1000
	netbios name = "CLOUD"
	obey pam restrictions = Yes
	pam password change = Yes
	panic action = /usr/share/samba/panic-action %d
	passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
	passwd program = /usr/bin/passwd %u
	server role = standalone server
	server string = %h server (Samba, Ubuntu)
	unix password sync = Yes
	usershare allow guests = Yes
	wins support = Yes
	idmap config * : backend = tdb


[profiles]
	browseable = No
	comment = Users Profiles
	create mask = 0600
	directory mask = 0700
	path = /Cloud/Profiles


[Cloud]
	comment = Cloud Directories
	create mask = 0750
	guest ok = Yes
	path = /Cloud
	read only = No


[Cloud-Hybrid]
	comment = Cloud Hybrid Directories
	create mask = 0777
	directory mask = 0777
	path = /Cloud/Cloud-Hybrid
	read only = No


[20R-Gaming]
	comment = 20R Gaming Directories
	create mask = 0750
	guest ok = Yes
	path = /Cloud/20R-Gaming
	read only = No


[tmp]
	comment = Temporary File Space
	guest ok = Yes
	path = /tmp
	read only = No
EOF

sudo smbpasswd -a Cloud-Hybrid
sudo smbpasswd -a 20R-Gaming

sudo systemctl restart smbd
