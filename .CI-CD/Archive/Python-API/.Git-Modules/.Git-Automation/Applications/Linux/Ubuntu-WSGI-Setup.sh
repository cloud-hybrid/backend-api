#!/usr/bin/env bash

SITE=$1

echo "                                                             "
echo " ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ "
echo " ┃                      WSGI Automation                    ┃ "
echo " ┃                      ---------------                    ┃ "
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
echo "                                                             "

set -x

chown ubuntu -R /opt
chmod 755 -R /opt

cd /opt 

wget https://projects.unbit.it/downloads/uwsgi-latest.tar.gz
mkdir UWSGI
tar zxvf uwsgi-latest.tar.gz -C UWSGI

cd /opt/UWSGI

make

sudo cp uwsgi /etc/nginx
sudo cp uwsgi ../

cd ..

./uwsgi --socket 127.0.0.1:9999 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:8888

sudo bash -c 'cat << EOF > "/etc/systemd/system/${SITE}.service"
[Unit]
Description=${SITE} UWSGI Web-Socket Service
Requires=network.target local-fs.target
After=network.target local-fs.target

[Service]
Type=simple
Restart=on-failure
RestartSec=5
StartLimitInterval=60s
StartLimitBurst=3
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/20r.gg/
ExecStartPre=git pull
ExecStart=uwsgi_python3 --socket 0.0.0.0:9999 --wsgi-file wsgi.py --master --callable application --processes 4 --threads 2 --stats 0.0.0.0:8888
ExecStop=/bin/kill -SIGINT $MAINPID
StandardOutput=file:/var/log/${SITE}-UWSGI.log
StandardError=file:/var/log/${SITE}-UWSGI-STDERR.log

[Install]
WantedBy=multi-user.target
EOF'

sudo systemctl enable ${SITE}.service
sudo systemctl start ${SITE}.service

# Previous Known-Working Command:
# ---> uwsgi_python3 --socket 0.0.0.0:9999 --wsgi-file wsgi.py --callable application --processes 4 --threads 2 --stats 0.0.0.0:8888