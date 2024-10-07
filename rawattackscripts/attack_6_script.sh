#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

HASHVAR=$1

print_blue " Password cracking"
hashcat_output=$(sudo hashcat -m 0 -a 3 $HASHVAR /usr/share/wordlists/rockyou.txt --show)

# Save the hashcat results to an HTML file
echo "<html><body><h1>Password cracking results:</h1><pre>$hashcat_output</pre></body></html>" > /var/www/html/index.html
echo "Results saved to /var/www/html/index.html"
