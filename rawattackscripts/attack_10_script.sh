#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

URLVAR=$1
USERVAR=$2

print_blue " Password policy testing"
ncrack_output=$(sudo ncrack -U $USERVAR -P /usr/share/wordlists/rockyou.txt $URLVAR)

# Save the ncrack results to an HTML file
echo "<html><body><h1>Password policy testing results:</h1><pre>$ncrack_output</pre></body></html>" > /var/www/html/index.html
