#!/usr/bin/env bash

# TODO - Handle for operating systems that aren't Ubuntu
apt-get -y update

# Install python3's package manger
apt-get -y install python3-pip

# Install `virtualenv`
pip3 install virtualenv

# Create virtual environment
virtualenv -p python3 --no-site-packages run/lib

# Activate the virtual environment
source run/lib/bin/activate

# Install the application's dependencies
pip3 install -r setup/requirements.txt

# Install a firewall
apt-get -y install firewalld

# Enable the firewall if-and-when a power cycle occurs
systemctl enable firewalld

# Open a port number
firewall-cmd --add-port=5000/tcp --permanent

# Add HTTP as a service
firewall-cmd --add-service=http --permanent

# Update the firewall's settings
systemctl reload firewalld
