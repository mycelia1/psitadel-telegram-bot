import telegram
from telegram.ext import Updater, CommandHandler
import requests

# Telegram Bot API token
telegram_bot_token = "YOUR TG TOKEN"

# BTCPay Server details
btcpay_server_url = "URL"
api_key = "APIKEY"
store_id = "STOREID"
cryptoCode = "BTC"

# Define the command handler for the /btcpay_balance command
def balance_command(update, context):
    chat_id = update.effective_chat.id

    # Query the balance using the BTCPay Server API
    url = f"{btcpay_server_url}/api/v1/stores/{store_id}/payment-methods/onchain/{cryptoCode}/wallet"
    headers = {
        "Authorization": f"token {api_key}"
    }
    response = requests.get(url, headers=headers)
    balance = response.json()["balance"]
    unconfirmed_balance = response.json()["unconfirmedBalance"]
    confirmed_balance = response.json()["confirmedBalance"]

    # Send the balance as a response to the user
    context.bot.send_message(chat_id=chat_id, text=f"On-Chain Treasury Balance: {balance}")

# Create the Telegram bot and set up the command handler
bot = telegram.Bot(token=telegram_bot_token)
updater = Updater(bot=bot)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("balance", balance_command))

# Start the bot
updater.start_polling()
