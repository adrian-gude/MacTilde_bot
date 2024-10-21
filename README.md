# Telegram Notification Bot

This project provides two Python scripts that interact with the Telegram API to send notifications and respond to user commands via a Telegram bot.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
  - [Script 1: Sending Notifications](#script-1-sending-notifications)
  - [Script 2: Telegram Bot with Commands](#script-2-telegram-bot-with-commands)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The project demonstrates how to:

1. Send a message to a Telegram chat using a bot (`notify.py`).
2. Create a Telegram bot that responds to commands (`bot.py`).

These scripts can be used as a foundation for more complex Telegram bot functionalities or automated notification systems.

## Features

- **Send Notifications**: Programmatically send messages to a specified Telegram chat.
- **Environment Variables**: Securely manage sensitive data like API tokens and chat IDs using `.env` files.

## Prerequisites

- Python 3.7 or higher
- A Telegram account
- Access to the Telegram Bot API token (from [@BotFather](https://telegram.me/BotFather))
- `pip` package manager

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/telegram-notification-bot.git
   cd telegram-notification-bot

2. **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python3 -m venv venv
    source venv/bin/activate 

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt 

4. **Create a Telegram Bot**
    - Open Telegram and search for @BotFather.
    - Start a conversation and send /newbot.
    - Follow the instructions to create a new bot.
    - Copy the API token provided by BotFather.

5. **Set Up Environment Variables**
    - Create a .env file in the project root directory.
    ```bash 
    TELEGRAM_TOKEN_API=your_bot_token_here
    TELEGRAM_CHAT_ID=your_chat_id_here
    ```
    - Replace your_bot_token_here with the token you got from BotFather.
    - To get TELEGRAM_CHAT_ID, you can run the bot and use the /getid command (explained below).

## Usage
**Script 1: Sending Notifications**

This script (notify.py) allows you to send a message to a specific Telegram chat using your bot.

**Steps to Use:**
- Ensure TELEGRAM_CHAT_ID is set in your .env file.
If you don't know your chat_id, you can run the bot script first and use the /getid command.
- Run the Script
```bash
python notify.py
```
- Check Your Telegram
- You should receive a message saying "Hello, world!" from your bot.


Integrate notify() in Other Scripts

You can import the notify function into other Python scripts to send notifications upon completion of tasks or errors.

```bash 
from notify import notify
notify("Task completed successfully!")
```
**Script 2: Telegram Bot with Commands**

This script (bot.py) creates a Telegram bot that responds to specific commands.

Steps to Use:

- Run the Script
```
python bot.py
```
- Interact with Your Bot on Telegram
    - /start: Sends a greeting message.
    - /notify: Replies with "Notification sent!".
    - /getid: Sends your chat ID, which you can use in the .env file for TELEGRAM_CHAT_ID.
- Running Continuously

The script must be running for the bot to respond.
Consider using a server or a service like Heroku or PythonAnywhere to keep the bot running.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

##
Note: Replace placeholders like yourusername, repository URLs, and adjust sections like Contributing and License according to your actual project details.

Furthermore, you may want to add error handling, logging, or expand the bot's functionality for production use.

If you have any questions or need further assistance, feel free to reach out!