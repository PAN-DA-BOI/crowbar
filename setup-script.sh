#!/bin/bash

print_blue() {
    echo -e "\e[34m$1\e[0m"
}

print_blue " Update package lists"
sudo apt-get update
sudo apt-get upgrade

print_blue " install python"
sudo apt-get install python3.6
wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.3a.tar.gz
tar xvzf RPi.GPIO-0.5.3a.tar.gz
cd RPi.GPIO-0.5.3a
sudo python setup.py install
cd
sudo rm -rf RPi.GPIO-0.5.3a/
rm Rpi.GPIO-0.5.3a.tar.gz 

print_blue " install exploitdb"
sudo apt -y install exploitdb
sudo apt install nmap

print_blue " Install Apache2"
sudo apt-get install apache2 -y

print_blue " Install PHP and Apache2 PHP module"
sudo apt-get install php libapache2-mod-php -y

print_blue " Install MariaDB server"
sudo apt-get install mariadb-server -y

print_blue " Secure MariaDB installation (non-interactive)"
sudo mysql_secure_installation <<EOF

n
y
y
y
y
EOF

print_blue " Install PHP MySQL module"
sudo apt-get install php-mysql -y

print_blue " Restart Apache2 service"
sudo service apache2 restart

print_blue " Install OpenSSH server"
sudo apt-get install openssh-server -y

print_blue " Start and enable SSH service"
sudo systemctl start ssh
sudo systemctl enable ssh

print_blue " Modify SSH configuration"
sudo sed -i s/^PasswordAuthentication no/PasswordAuthentication yes/ /etc/ssh/sshd_config
sudo sed -i s/^ChallengeResponseAuthentication yes/ChallengeResponseAuthentication no/ /etc/ssh/sshd_config

print_blue " Restart SSH service"
sudo systemctl restart ssh

print_blue "no desktop mode."
sudo systemctl set-default multi-user
sudo systemctl set-default graphical
sudo apt purge --autoremove xfce4* kali-desktop-xfce libxfce4*



print_blue "Setup completed successfully."
print_blue "RESTARTING"
sudo shutdown -r now

