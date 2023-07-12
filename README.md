# BTCPay Balance Telegram Bot

This Telegram bot retrieves the on-chain treasury balance from a BTCPay Server and sends it as a response to a command.

## Prerequisites

Before running the bot, make sure you have the following prerequisites:

- Python 3.7 or above
- BTCPay Server account with an API key
- Telegram bot token

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/btcpay-balance-telegram-bot.git

2. Install the required packages using pip:

pip install -r requirements.txt

3. Update the configuration:

Open the bot.py file.
Replace "YOUR TG TOKEN" with your Telegram bot token.
Replace "URL", "APIKEY", "STOREID", and "BTC" with your BTCPay Server details.

## Usage
To start the bot, run the following command:

python bot.py

## Available Commands
/balance: Retrieves the on-chain treasury balance from the BTCPay Server.

## License

Feel free to customize it according to your specific requirements and add any additional sections or information.
