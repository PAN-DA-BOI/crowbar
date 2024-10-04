#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

IPVAR=$1

print_blue " Network scan"
sudo nmap -T5 -A -v $IPVAR -oX network-map.xml

print_blue " Convert XML to HTML"
sudo xsltproc network-map.xml -o index.html

sudo mv index.html ~/var/www/html

print_blue " Open HTML report in Firefox"
sudo firefox network-map.html
