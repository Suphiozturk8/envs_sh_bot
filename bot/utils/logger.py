
import logging
import traceback

from ..config import BotConfig


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)

logger = logging.getLogger(BotConfig.NAME)


def log_exception(exc: Exception):
    tb = traceback.format_exc()
    logger.error(f"Hata: {exc}\n{tb}")
