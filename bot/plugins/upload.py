import os
from pyrogram import Client, filters

from ..utils import uploader, generate_buttons, log_exception


@Client.on_message(filters.command("upload"))
async def upload_file(client, message):
    reply = message.reply_to_message
    if not reply or not reply.media:
        await message.reply_text(
            "Bu komutu bir medyaya yanıt olarak kullanmalısınız."
        )
        return

    is_secret = "-s" in message.command
    progress_msg = await message.reply_text("Medya indiriliyor...")
    file_path = None

    try:
        file_path = await reply.download()
        await progress_msg.edit_text("Medya yükleniyor...")

        file_url = await uploader.upload_file(file_path, secret=is_secret)

        await progress_msg.edit_text(
            "Medya başarıyla yüklendi!",
            reply_markup=generate_buttons(file_url)
        )
    except Exception as e:
        await progress_msg.edit_text(f"Hata oluştu: {str(e)}")
        log_exception(e)
    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
