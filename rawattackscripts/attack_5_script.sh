#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

URLVAR=$1

print_blue " Web application scanning"
sudo wget -r -p -k $URLVAR
sudo nikto -h $URLVAR -o nikto-scan.html

print_blue " Open HTML report in Firefox"
sudo firefox nikto-scan.html
