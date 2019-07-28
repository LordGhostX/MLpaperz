# Responsible for the management of the message bot
from requests import get
from time import sleep, strftime
import configuration

class Telegram():
    def __init__(self):
        config = configuration.load_config()
        self.bot_token = config["bot_token"]
        self.channel_token = config["channel_token"]
        self.admin_id = config["admin_id"]

    def sendMessage(self, message, chat_id=None):
        # Send messages to telegram
        if not chat_id:
            chat_id = self.channel_token

        params = {"chat_id": chat_id, "text": message}
        get("https://api.telegram.org/bot{}/sendMessage".format(self.bot_token), params=params)
        # Sleep for 0.04 seconds because telegram API limits bot message to 30 per second; 0.04 second interval reduces it to 25 per second
        sleep(0.04)

    def alertAdmin(self):
        # Send messages to admin so he knows bot is alive
        timestamp = "{} {}".format(strftime("%D"), strftime("%T"))
        self.sendMessage("Checking In - {}".format(timestamp), self.admin_id)
