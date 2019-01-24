#!/bin/sh

echo "Init Connection to OPEN_VPN"

#Maybe will ask the user to input the sudo password
sudo -i openvpn nl-free-01.protonvpn.com.tcp.ovpn 

#open sql shell and executes sql commands
username=$(sqlite3 ../database/bot.db "SELECT USERNAME FROM TB_OPEN_VPN_CREDENTIALS")
password=$(sqlite3 ../database/bot.db "SELECT PASSWORD FROM TB_OPEN_VPN_CREDENTIALS")
echo $username
echo $password