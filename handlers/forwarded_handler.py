from aiogram import types, F
from loader import bot
from config import CHANNEL_ID
from data.words import blacklisted_words

from . import router

def is_blacklisted(text: str) -> bool:
    for word in blacklisted_words:
        if word.lower() in text.lower():
            return True
    return False


@router.message(F.forward_from)
async def forwarded_handler(message: types.Message):
    if message.forward_from is None:
        await message.reply("This is not a forwarded message")
        return

    if is_blacklisted(message.text):
        return

    await bot.forward_message(
        chat_id=CHANNEL_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )