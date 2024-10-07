#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

IPVAR=$1

print_blue " Vulnerability scanning"
sudo nmap -sV -sC -T4 -v $IPVAR -oX vulnerability-scan.xml

print_blue " Convert XML to HTML"
sudo xsltproc vulnerability-scan.xml -o index.html

sudo mv index.html ~/var/www/html
