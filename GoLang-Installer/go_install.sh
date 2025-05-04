#!/bin/bash

# Define blue color
BLUE='\033[1;34m'
NC='\033[0m'

# Print message in pleasant blue
echo -e "${BLUE}This script needs to be run as root${NC}"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
  echo "Please run this script as root."
  exit 1
fi

mkdir ~/go_installer
cd ~/go_installer
wget https://go.dev/dl/go1.24.2.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.24.2.linux-amd64.tar.gz
echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile
source /etc/profile

echo -e "${BLUE}Done! Sometimes you need to refresh the shell${NC}"
