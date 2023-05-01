# UniversalWakeOnLan (UWOL) - Coming soon


### <p align="center"><strong><font size="60">Note: This project is currently under construction.</font></strong></p>

<p align="center">
  
  <img src="https://raw.githubusercontent.com/ugurcandede/Under-Construction/master/under%20building/Capture.PNG" alt="Alt text">
</p>


UniversalWakeOnLan is a script designed to wake up your device remotely from anywhere in the world with the help of Telegram API. It is compatible with Opnsense routers.

I made a guide on [how to setup your telegram bot](https://github.com/fullopsec/TelegramAlerts)

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
- Network card that support Wake-on-LAN on the machines you want to wake.

## Installation - NOT available yet
1. Clone the repository: `git clone https://github.com/fullopsec/UniversalWakeOnLan.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a new Telegram bot and get the bot token.
4. Set the bot token and machines names/MAC in the `config.ini` file.
5. Create a Cron Job to run the script every 10 seconds

## How it works
1. Send a wake up command to Telegram channel.
2. The python bot receives the command and sends a WOL packet to the machine.

## Disclaimer
Use this script at your own risk. The author is not responsible for any damages or losses caused by the use of this script.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
