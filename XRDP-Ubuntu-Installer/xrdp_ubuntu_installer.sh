#!/bin/bash

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Use: sudo $0"
    exit 1
fi

echo "Updating package lists..."
apt update -y

echo "Installing XRDP..."
apt install -y xrdp

echo "Enabling and starting XRDP service..."
systemctl enable xrdp
systemctl start xrdp

echo "Checking XRDP status..."
systemctl status xrdp --no-pager

echo "Adding XRDP user to ssl-cert group..."
adduser xrdp ssl-cert
systemctl restart xrdp

echo "Configuring firewall to allow RDP (port 3389)..."
ufw allow 3389/tcp
ufw reload

echo "Installing XFCE desktop environment..."
apt install -y xfce4 xfce4-goodies

echo "Configuring default session for all users..."
echo "startxfce4" | tee /etc/skel/.xsession ~/.xsession > /dev/null

echo "Restarting XRDP service..."
systemctl restart xrdp

echo "Enabling XRDP to start at boot..."
systemctl enable xrdp

echo "Verifying XRDP is listening on port 3389..."
netstat -tulpn | grep xrdp

echo "XRDP installation and configuration complete!"
echo "You can now connect using an RDP client to this machine."
