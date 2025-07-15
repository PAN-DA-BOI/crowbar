#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

print_blue "Update package lists"
sudo apt-get update
sudo apt-get upgrade -y

print_blue "Install Python"
sudo apt-get install -y python3.6
wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.3a.tar.gz
tar xvzf RPi.GPIO-0.5.3a.tar.gz
cd RPi.GPIO-0.5.3a
sudo python3 setup.py install
cd ..
rm -rf RPi.GPIO-0.5.3a
rm RPi.GPIO-0.5.3a.tar.gz

print_blue "Install necessary tools"
sudo apt-get install -y nmap xsltproc hashcat sqlmap dirb ncrack exploitdb

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

print_blue "Set default to multi-user mode"
sudo systemctl set-default multi-user
sudo systemctl set-default graphical

print_blue "Remove desktop environment"
sudo apt purge --autoremove -y xfce4* kali-desktop-xfce libxfce4*

print_blue "Setup completed successfully."
print_blue "RESTARTING"
sudo shutdown -r now
