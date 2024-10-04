#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

URLVAR=$1
USERVAR=$2

print_blue " Password policy testing"
sudo ncrack -U $USERVAR -P /usr/share/wordlists/rockyou.txt $URLVAR
