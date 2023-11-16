#!/bin/sh

# Thanks https://julienharbulot.com/cron-windows.html

# Start cron
printf "%s\n" "$(date)"  >> /tmp/wsl_startup.log
sudo /etc/init.d/cron start
