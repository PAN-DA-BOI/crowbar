#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

URLVAR=$1

print_blue " Directory brute forcing"
sudo dirb $URLVAR /usr/share/wordlists/dirb/common.txt -o dirb-scan.txt
