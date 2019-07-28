# Responsible for the management of the telegram bot
from requests import get
from time import sleep
import configuration

class Telegram():
    def __init__(self):
        config = configuration.load_config()
        self.bot_token = config["bot_token"]
        self.channel_token = config["channel_token"]

    def sendMessage(self, message):
        # Send messages to telegram
        params = {"chat_id": self.channel_token, "text": message}
    	get("https://api.telegram.org/bot{}/sendMessage".format(self.bot_token), params=params)
        # Sleep for 0.04 seconds because telegram API limits bot message limit to 30 per second; 0.04 second interval reduces it to 25 per second
    	sleep(0.04)
