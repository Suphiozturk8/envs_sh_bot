
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_buttons(uploaded_url: str):
    uploaded_url = f"{uploaded_url.replace("\n", "")}"
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Önizleme",
                    url=uploaded_url
                )
            ],
            [
                InlineKeyboardButton(
                    "Paylaş",
                    switch_inline_query=uploaded_url
                )
            ],
            [
                InlineKeyboardButton(
                    "Kopyala",
                    copy_text=uploaded_url
                )
            ]
        ]
    ) if uploaded_url else None
