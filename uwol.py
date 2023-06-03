#!/usr/bin/env python3
"""
# Developed by: Fullopsec
# Version: 1.0
# Release Date: 29/05/23
# License: MIT License

Copyright (c) [2023] [Fullopsec]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
- The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

# Dependencies:
# wakeonlan 3.0.0


# Contact:
# https://github.com/fullopsec/UniversalWakeOnLan
"""


#DISCLAIMER
#This a quick and DIRTY program made in a hurry. Modify it as you want, I'll review your code and push it to the main brach if it works well.



import requests
import time
import os
import subprocess
import json
import re
from wakeonlan import send_magic_packet  #pip3 install wakeonlan
#what command you want to use as the trigger to wake your computers
wakeonlan = "Wake"
#keyword for waking all machines (ex: all for "Wake all")
wakeall = "all"
# number of seconds after which the wake up call will be invalid (to prevent detecting it forever)
# Always add +1 or +2 second. if your cron check every 60 seconds, put 61 in the timer to take network and processing delay into account.
timer=61
#are you using the os-wol plugin AND running this script in an opnsense firewall?  
#Because the python wakeonlan does not work on opnsense.  True will send os subsystem commands
os_wol_plugin = False
#regex pattern for ipv4
ipv4_extract_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"
MAC_PATTERN="^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"


#Your Telegram BOT API INFO
# Video on how to create your bot: https://www.youtube.com/watch?v=-bmppdlnxEQ
BOT_TOKEN = "Your Bot Token"
GROUP_ID = "Your Group/channel ID"


#List all the computers you want to be able to wake up with a name and their MAC adress 
#Example:
#COMPUTER_NAME="MAC_ADDRESS"
opnsense="68:95:AC:4D:8C:B1"
node2="AF:53:D2:CE:88:C0"
node3="63:D3:D0:AB:FE:91"
node4="18:64:D2:5D:C8:E6"

#USAGE EXAMPLE (send in telegram): Wake node4

def send_to_telegram(message):
    API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    try:
        response = requests.post(API_URL, json={'chat_id': GROUP_ID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

def get_messages():
    response = requests.get("https://api.telegram.org/bot"+BOT_TOKEN+"/getUpdates", stream=True)
    return(response)


def format_messages(response):
    final = json.loads(response.text)
    Dict = final['result']

    for obj in Dict:
        date = obj['channel_post']['date']   #time message was sent
        text = obj['channel_post']['text']   #content of message
        verify_message(date,text)


def verify_message(date,text):
    timenow = int(time.time())           #current time
    if int(timenow) < int(date)+timer:      #Checking that message is not too old, if you have problems check the telegram time compared to yours, it should not differ.
        if wakeall not in text:             #if wakeall keywork detected or not
            if wakeonlan in text:
                text = text.split(" ")
                match=False
                for i in text:
                    if i in globals():
                        print(i+" : Machine recognised!")
                        match=True
                        boot_machine(i)
                        
                if match == False:  #if no machines of the name put in Telegram exist
                    x = 0
                    for i in text:
                        if i == wakeonlan:
                            del text[x]
                            print("Machine name " + str(text) +" not recognised, please add your machine name in the python script as a variable (COMPUTER_NAME='MAC_ADDRESS')")
                        x = x+1
        else: 
            print("Wake order for all machines detected!")
            for i in globals():
                var_list = re.findall(MAC_PATTERN, str(i))
                all_var_values = globals()[i]   #Getting all global variables values from string of their variable name (extremely dirty)
                mac_list = re.findall(MAC_PATTERN, str(all_var_values))
                for x in mac_list:
                    boot_all(x,i)
def boot_all(mac,name):
    print("Waking up "+mac)
    send_magic_packet(mac)
    if os_wol_plugin == True:
        broad = subprocess.check_output("/sbin/ifconfig -a | awk '/(broadcast)/ {print $6}'", shell=True)  #get the broadcast address
        broadcast_list = re.findall(ipv4_extract_pattern, str(broad)) # returns broadcast adress in a list
        for i in broadcast_list:            #Firing in every broadcast address
            print("Broadcasting on: "+i)
            os.system("wol -h "+i+" " +mac)
    #send_to_telegram("Magic packet sent to "+name)

def boot_machine(machine):
    try:
        machine_mac = globals()[machine]  #Getting Mac value from string of the machine variable name (extremely dirty)
        print(machine+" Has machine MAC: "+ machine_mac)
        send_magic_packet(machine_mac)      #send magic packet with python wakeonlan

        if os_wol_plugin == True:
            broad = subprocess.check_output("/sbin/ifconfig -a | awk '/(broadcast)/ {print $6}'", shell=True)  #get the broadcast address  (need to imporve this or an update could break it)
            
            broadcast_list = re.findall(ipv4_extract_pattern, str(broad)) # returns broadcast adress in a list

            for i in broadcast_list:
                print("Broadcasting on: "+i)
                os.system("wol -h "+i+" " +machine_mac)        #Command used by Opnsense os-wol plugin to send the packet, we send it to all broadcast addresses

            

        print("Magic packet sent to "+machine)
        send_to_telegram("Magic packet sent to "+machine)
    except Exception as e:
        print(e)
        
def main():
    response = get_messages()
    format_messages(response)
main()


