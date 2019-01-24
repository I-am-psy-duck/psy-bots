#!/bin/sh

echo "Init Connection to OPEN_VPN"
sleep 1
echo "Getting OpenVPN credentials . . ."
#open sql shell and executes sql commands and stores to variables
username=$(sqlite3 ../database/bot.db "SELECT USERNAME FROM TB_OPEN_VPN_CREDENTIALS")
password=$(sqlite3 ../database/bot.db "SELECT PASSWORD FROM TB_OPEN_VPN_CREDENTIALS")

cd server-configs
#Maybe will ask the user to input the sudo password

echo "Username: ${username}"
echo "Password: ${password}"

sudo openvpn nl-free-01.protonvpn.com.tcp.ovpn 


