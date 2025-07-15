#!/bin/bash
sudo apt-get update
sudo apt-get install -y nmap xsltproc hashcat sqlmap dirb ncrack apache2
sudo apt-get install -y exploitdb
sudo a2enmod rewrite
sudo systemctl enable apache2
sudo systemctl start apache2