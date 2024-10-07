#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

URLVAR=$1

print_blue " SQL injection testing"
sqlmap_output=$(sudo sqlmap -u $URLVAR --batch --random-agent)

# Save the sqlmap results to an HTML file
echo "<html><body><h1>SQL injection testing results:</h1><pre>$sqlmap_output</pre></body></html>" > /var/www/html/index.html
echo "Results saved to /var/www/html/index.html"
