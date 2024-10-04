#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

URLVAR=$1

print_blue " SQL injection testing"
sudo sqlmap -u $URLVAR --batch --random-agent
