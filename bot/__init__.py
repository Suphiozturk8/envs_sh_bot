
from pyrogram import Client, enums

from .config import BotConfig


bot: Client = Client(
    name=BotConfig.NAME,
    api_id=BotConfig.API_ID,
    api_hash=BotConfig.API_HASH,
    bot_token=BotConfig.BOT_TOKEN,
    parse_mode=enums.ParseMode.MARKDOWN,
    plugins=dict(root="bot/plugins"),
)
