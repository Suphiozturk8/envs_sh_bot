
from pyrogram import Client, filters

from ..utils import uploader, generate_buttons, log_exception


@Client.on_message(filters.command("shorten"))
async def shorten_url(client, message):
    cmd = message.command
    if len(cmd) < 2:
        return await message.reply_text(
            "Lütfen bir URL girin.\n"
            "Örnek: /shorten https://example.com"
        )

    url = cmd[1]
    progress_msg = await message.reply_text("URL kısaltılıyor...")

    try:
        short_url = await uploader.shorten_url(url)
        await progress_msg.edit_text(
            "URL başarıyla kısaltıldı!",
            reply_markup=generate_buttons(short_url)
        )
    except Exception as e:
        await progress_msg.edit_text(f"Hata oluştu: {str(e)}")
        log_exception(e)


@Client.on_message(filters.command("upload_url"))
async def upload_from_url(client, message):
    cmd = message.command
    if len(cmd) < 2:
        return await message.reply_text(
            "Lütfen bir URL girin."
            "\nÖrnek: /upload_url https://example.com/image.jpg"
        )

    url = cmd[1]
    is_secret = "-s" in cmd
    progress_msg = await message.reply_text("URL'den medya yükleniyor...")

    try:
        uploaded_url = await uploader.upload_url(url, secret=is_secret)
        await progress_msg.edit_text(
            "URL başarıyla yüklendi!",
            reply_markup=generate_buttons(uploaded_url)
        )
    except Exception as e:
        await progress_msg.edit_text(f"Hata oluştu: {str(e)}")
        log_exception(e)
