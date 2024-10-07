#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

URLVAR=$1

print_blue " Directory brute forcing"
sudo dirb $URLVAR /usr/share/wordlists/dirb/common.txt -o /var/www/html/dirb-scan.txt

# Convert the dirb results to HTML format
dirb_output=$(cat /var/www/html/dirb-scan.txt)
html_output=$(echo "$dirb_output" | awk '{print "<p>"$0"</p>"}')

# Save the HTML output to the index.html file
echo "<html><body><h1>Directory brute forcing results:</h1>$html_output</body></html>" > /var/www/html/index.html
echo "Results saved to /var/www/html/index.html"
