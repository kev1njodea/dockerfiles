#!/bin/bash

# Gather system information
HOSTNAME=$(hostname)
UPTIME=$(uptime -p)
MEMORY=$(free -h | grep Mem | awk '{print $3 "/" $2}')
DISK=$(df -h / | grep / | awk '{print $3 "/" $2}')
CPU_LOAD=$(top -bn1 | grep "load average:" | awk '{print $10 $11 $12}')

# Format the message
MESSAGE="Hostname: $HOSTNAME
Uptime: $UPTIME
Memory Usage: $MEMORY
Disk Usage: $DISK
CPU Load: $CPU_LOAD"

# Send the notification
curl -d "$MESSAGE" localhost/mytopic
