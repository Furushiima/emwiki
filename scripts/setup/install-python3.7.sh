#!/bin/bash

# Move to Working Directory
cd "$(dirname "$0")/../.."

# Main
sudo apt-get install -y python3.7-dev

wget https://www.python.org/ftp/python/3.7.13/Python-3.7.13.tar.xz
tar xvf Python-3.7.13.tar.xz
cd Python-3.7.13
./configure
sudo make altinstall
cd ..
rm -rf Python-3.7.13

sudo apt install python3-pip
