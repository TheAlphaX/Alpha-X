#!/bin/bash

clear

echo "╭━━━╮╭╮╱╱╱╭━━━╮╭╮╱╭╮╭━━━╮

┃╭━╮┃┃┃╱╱╱┃╭━╮┃┃┃╱┃┃┃╭━╮┃

┃┃╱┃┃┃┃╱╱╱┃╰━╯┃┃╰━╯┃┃┃╱┃┃

┃╰━╯┃┃┃╱╭╮┃╭━━╯┃╭━╮┃┃╰━╯┃

┃╭━╮┃┃╰━╯┃┃┃╱╱╱┃┃╱┃┃┃╭━╮┃

╰╯╱╰╯╰━━━╯╰╯╱╱╱╰╯╱╰╯╰╯╱╰╯

╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱

╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
"

# Termux session string generator for scorpion

echo Starting dependency installation in 5 seconds...

sleep 5

apt-get update

apt-get upgrade -y

pkg upgrade -y

pkg install python wget -y

wget https://raw.githubusercontent.com/TheAlphaX/AlphaX/main/resources/sessionstring/alphax-setup.py

pip install telethon

python alphax-setup.py
