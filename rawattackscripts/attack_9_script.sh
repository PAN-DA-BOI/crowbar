#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

print_blue " Wireless network scanning"
sudo iwlist wlan0 scan | grep -E 'ESSID|Address' > wireless-scan.txt
