#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

HASHVAR=$1

print_blue " Password cracking"
sudo hashcat -m 0 -a 3 $HASHVAR /usr/share/wordlists/rockyou.txt --show
