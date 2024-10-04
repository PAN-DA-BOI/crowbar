#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

IPVAR=$1

print_blue " Port scanning"
sudo nmap -p- -T4 -v $IPVAR -oX port-scan.xml

print_blue " Convert XML to HTML"
sudo xsltproc port-scan.xml -o index.html

sudo mv index.html ~/var/www/html

print_blue " Open HTML report in Firefox"
sudo firefox port-scan.html
