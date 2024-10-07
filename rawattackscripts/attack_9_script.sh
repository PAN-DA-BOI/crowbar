#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

print_blue " Wireless network scanning"
sudo iwlist wlan0 scan | grep -E 'ESSID|Address' > /var/www/html/wireless-scan.txt

# Convert the wireless scan results to HTML format
wireless_output=$(cat /var/www/html/wireless-scan.txt)
html_output=$(echo "$wireless_output" | awk '{print "<p>"$0"</p>"}')

# Save the HTML output to the index.html file
echo "<html><body><h1>Wireless network scanning results:</h1>$html_output</body></html>" > /var/www/html/index.html
echo "Results saved to /var/www/html/index.html"
