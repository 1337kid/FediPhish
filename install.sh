#!/bin/bash
echo ".::FediPhish SETUP::."
if ! command -v tar &> /dev/null
then
    echo "Tar is not installed, installing it for you"
    sudo apt install tar
    clear
fi
if ! command -v php &> /dev/null
then
    echo "PHP is not installed, installing it for you"
    sudo apt install php
    clear
fi
#======
echo "Setting up"
mkdir $HOME/.FediPhish
tar -zxvf ./core/web.tar.gz -C $HOME/.FediPhish
cp ./core/login.php $HOME/.FediPhish/web
mkdir $HOME/.FediPhish/server
# move py file to /usr/bin
sudo cp ./fediphish.py /usr/bin/fediphish
sudo chmod +x /usr/bin/fediphish
echo "Installed FediPhish on your device"
echo "command to run FediPhish : fediphish"