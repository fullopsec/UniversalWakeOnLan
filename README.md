# UniversalWakeOnLan (UWOL)




<p align="center">
  

  

[![Video](https://img.youtube.com/vi/jX26s1SrdWM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jX26s1SrdWM)


</p>



UniversalWakeOnLan is a script designed to wake up your computers remotely from anywhere in the world with the help of Telegram API. It is compatible with Opnsense Firewalls, Windows and linux.

I made a guide on [how to setup your telegram bot and get your tokens](https://github.com/fullopsec/TelegramAlerts)

Disclaimer:
This script was made in a hurry and could be greatly improved,  modify it as you wish!

## Features
- Wake up your device remotely from anywhere in the world.
- Give names to your machines and wake them up one by one.
- Wake all your machines.
- Easy to set up and use.



## Requirements
- Telegram account
- Telegram bot token
- Python 3.x
- An "always up" machine in the same local network as the devices to wake (can be a Raspberry Pi). 
- The "always up" machine must have internet access.
- Active Network card that support Wake-on-LAN on the machines you want to wake.

## Installation 
Video Tutorial: https://www.youtube.com/watch?v=jX26s1SrdWM
1. Clone the repository: `git clone https://github.com/fullopsec/UniversalWakeOnLan.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. [Create a Telegram bot and get the bot token.](https://www.youtube.com/watch?v=-bmppdlnxEQ&feature=youtu.be)
4. Set the bot token, timer and machines names/MAC in the python script file.
5. Create a Cron Job to run the script every x seconds.

## How it works
1. Send a wake up command to Telegram channel.
2. The python bot receives the command and sends a WOL packet to the machine.

## Disclaimer
Use this script at your own risk. The author is not responsible for any damages or losses caused by the use of this script.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
