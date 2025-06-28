## XRDP Installer for Ubuntu
This script installs XRDP on Ubuntu and fixes the issue with black screen. Run it as root

## Display Fix
Some apps will not boot due to conflict in settings

`export XAUTHORITY=~/.Xauthority`

`xauth generate :10 . trusted`

`firefox`
