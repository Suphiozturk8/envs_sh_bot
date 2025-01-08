
from pyrogram import idle

from . import bot
from .utils import logger


async def main():
    logger.info("Bot başlatılıyor...")
    await bot.start()
    logger.info("Bot başlatıldı.")
    await idle()
    logger.info("Bot durduruluyor...")
    await bot.stop()
    logger.info("Bot durduruldu.")


if __name__ == "__main__":
    bot.run(main())
