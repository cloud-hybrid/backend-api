#!/usr/bin/env bash

echo "                                                             "
echo " ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ "
echo " ┃                   Local-VPS Installer                   ┃ "
echo " ┃                   -------------------                   ┃ "
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

egrep -c '(vmx|svm)' /proc/cpuinfo # --> Should return 1

sudo apt install cpu-checker -y

sudo kvm-ok # Output should be 
# INFO: /dev/kvm exists
# KVM acceleration can be used

sudo apt install virt-manager \
    virt-viewer \
    libvirt-doc \
    libvirt0 \
    libvirt-clients \
    libvirt-daemon \
    libvirt-dev \
    libvirt-glib-1.0-0 \
    libvirt-glib-1.0-dev \
    virtinst \
    fakeroot \
    policycoreutils-python-utils \
    kvmtool \
    qemu \
    qemu-kvm \
    qemu-system \
    qemu-system-common \
    qemu-system-data \
    qemu-system-gui \
    qemu-system-misc \
    qemu-user \
    qemu-user-static \
    qemu-utils \
        --show-progress \
        --assume-yes \
        --ignore-hold

sudo adduser $USER libvirt
sudo adduser $USER libvirt-qemu

sudo service libvirtd start

sudo apt update -y

sudo apt install software-properties-common -y
sudo apt install build-essential -y
sudo apt install python-dev -y

sudo apt-get install build-essential -y
sudo apt-get install python-dev -y

sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot

sudo apt update -y
sudo apt-get update -y

sudo apt upgrade -y

sudo apt install python3.8 python3.8-dbg python3.8-dev python3.8-venv -y

sudo apt install glances -y

sudo apt install net-tools -y

echo "Y" | sudo ufw enable

sudo ufw start

sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 8080
sudo ufw allow 443
sudo ufw allow 4443
sudo ufw allow 4380
sudo ufw allow 5000
sudo ufw allow 6000:6250/tcp
sudo ufw allow 6000:6250/udp
sudo ufw allow 10000:11000/tcp
sudo ufw allow 10000:11000/udp

sudo ufw reload

sudo apt install nginx -y

sudo apt install nginx-extras -y

sudo systemctl enable nginx
sudo systemctl start nginx

sudo add-apt-repository ppa:certbot/certbot

sudo apt install certbot -y

sudo apt install python-certbot-nginx -y

sudo certbot --m development@cloudhybrid.io --agree-tos -n

sudo chown ubuntu -R /var/www

sudo chmod 755 -R /var/www