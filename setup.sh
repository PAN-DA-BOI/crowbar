#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

print_blue "Update package lists"
sudo apt-get update
sudo apt-get upgrade -y

print_blue "Install necessary tools"
sudo apt-get install -y nmap xsltproc hashcat sqlmap dirb ncrack exploitdb python3

print_blue "Install Apache2"
sudo apt-get install -y apache2

print_blue "Install PHP and Apache2 PHP module"
sudo apt-get install -y php libapache2-mod-php

print_blue "Install MariaDB server"
sudo apt-get install -y mariadb-server

print_blue "Secure MariaDB installation (non-interactive)"
sudo mysql_secure_installation <<EOF
n
y
y
y
y
EOF

print_blue "Install PHP MySQL module"
sudo apt-get install -y php-mysql

print_blue "Enable necessary Apache modules"
sudo a2enmod rewrite

print_blue "Restart Apache2 service"
sudo systemctl restart apache2

print_blue "Enable and start Apache service"
sudo systemctl enable apache2
sudo systemctl start apache2

print_blue "Install OpenSSH server"
sudo apt-get install -y openssh-server

print_blue "Start and enable SSH service"
sudo systemctl start ssh
sudo systemctl enable ssh

print_blue "Modify SSH configuration"
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/^ChallengeResponseAuthentication yes/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config

print_blue "Restart SSH service"
sudo systemctl restart ssh

print_blue "Remove desktop environment"
sudo apt purge --autoremove -y raspberrypi-ui-mods lightdm

print_blue "Install necessary packages for running a Python script on boot"
sudo apt-get install -y python3-pip xinit

print_blue "Install any necessary Python packages"
pip3 install --user <any-required-packages>

print_blue "Configure main.py to run on startup"
echo "[Desktop Entry]
Type=Application
Name=Main Python Script
Exec=/usr/bin/python3 /path/to/your/main.py
StartupNotify=false" | sudo tee /etc/xdg/autostart/main.desktop

print_blue "Make the script executable"
sudo chmod +x /etc/xdg/autostart/main.desktop

print_blue "Setup completed successfully."
print_blue "RESTARTING"
sudo shutdown -r now
