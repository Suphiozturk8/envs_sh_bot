
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")


class BotConfig:
    NAME = config.get("telegram", "name")
    API_ID = config.getint("telegram", "api_id")
    API_HASH = config.get("telegram", "api_hash")
    BOT_TOKEN = config.get("telegram", "bot_token")
