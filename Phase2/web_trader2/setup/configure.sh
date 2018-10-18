#!/usr/bin/env bash

scp -r ~/desktop/byte_academy/web_trader2 root@167.99.52.144:/tmp

ssh root@167.99.52.144

cd /tmp

mv web_trader2/ /root

cd

apt-get -y install firewalld

firewalld-cmd --add-port=5000/tcp --permanent

systemctl reload firewalld

cd web_trader2

python3 run/wsgi.py



