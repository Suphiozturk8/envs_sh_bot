from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from ..utils import generate_buttons, is_valid_envs_url


@Client.on_inline_query()
async def inline_handler(client, inline_query):
    url = inline_query.query.strip()

    if is_valid_envs_url(url):
        result = InlineQueryResultArticle(
            title="envs.sh için URL Paylaşımı",
            description="envs.sh URL'nizi herkesle kolayca paylaşın!",
            thumb_url="https://envs.sh/vD3.jpg",
            input_message_content=InputTextMessageContent(
                f"**[envs.sh]({url}) bağlantısı.**\n\n"
                "Bağlantıyı paylaşmak veya önizlemek için butonları kullanın.",
                disable_web_page_preview=True
            ),
            reply_markup=generate_buttons(url)
        )
    else:
        result = InlineQueryResultArticle(
            title="Geçersiz Sorgu",
            description="Lütfen paylaşmak için bir envs.sh URL'si girin.",
            thumb_url="https://envs.sh/vDl.png",
            input_message_content=InputTextMessageContent(
                "**Bu bot yalnızca envs.sh URL'leri için çalışır.**"
            )
        )

    await inline_query.answer([result], cache_time=5)
