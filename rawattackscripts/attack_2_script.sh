#!/bin/bash

# Get the target IP address and port number from command-line arguments
target_ip=$1
port_number=$2

# Run Nmap to identify the service and version
nmap_output=$(nmap -sV -p $port_number $target_ip)

# Extract the service name and version from the Nmap output
service_name=$(echo "$nmap_output" | grep -oP '(?<=open\s+)\w+')
version=$(echo "$nmap_output" | grep -oP '(?<=\sversion:\s)\S+')

# Check if service name and version were found
if [ -z "$service_name" ] || [ -z "$version" ]; then
  echo "Could not determine the service name or version."
  exit 1
fi

# Use searchsploit to find potential exploits
echo "Searching for exploits for $service_name $version..."
searchsploit_output=$(searchsploit $service_name $version)

# Display the searchsploit results
echo "Potential exploits for $service_name $version:"
echo "$searchsploit_output"

# Save the searchsploit results to a file
echo "$searchsploit_output" > searchsploit_results.txt
echo "Results saved to searchsploit_results.txt"
