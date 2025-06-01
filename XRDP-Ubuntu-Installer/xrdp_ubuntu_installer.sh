#!/bin/bash

sudo apt update && sudo apt install -y xrdp xfce4 xfce4-goodies
echo "startxfce4" | sudo tee /etc/xrdp/startwm.sh
sudo chmod +x /etc/xrdp/startwm.sh
sudo systemctl restart xrdp
sudo apt install -y xorgxrdp
sudo chown xrdp:xrdp /home/$USER/.Xauthority
sudo adduser xrdp ssl-cert
sudo systemctl restart xrdp
echo "exec /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &" >> ~/.xsession
#sudo reboot
