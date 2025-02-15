from aiogram import types
from config import CHANNEL_ID 

from data.words import blacklisted_words  


def is_blacklisted(message):
    for word in blacklisted_words:
        if word.lower() in message.lower():
            return True
    return False


async def forwarded_message_handler(message: types.Message):
    from loader import bot
    
    if message.forward_from is not None:
        if is_blacklisted(message.text):
            return
        await bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    else:
        await message.reply("This is not a forwarded message")


def setup(dp):
    dp.register_message_handler(forwarded_message_handler, is_forwarded=True)
