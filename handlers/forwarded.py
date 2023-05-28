from aiogram import types
from pathlib import Path
from config import CHANNEL_ID
from utils.pull import pull_words

data_file_path = str((Path(__file__).parent / '../data_files/blacklist.txt').resolve())
blacklist = pull_words(data_file_path)


def blacklisted(message):
    for word in blacklist:
        if word.lower() in message.lower():
            return True
    return False


async def handle_forwarded(message: types.Message):
    if message.forward_from is not None:
        from loader import bot
        await bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=message.chat.id, message_id=message.message_id)
        return
    await message.reply("This is not a forwarded message")


def setup(dp):
    dp.register_message_handler(handle_forwarded, is_forwarded=True)
