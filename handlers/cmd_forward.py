from aiogram import types,  F
from config import CHANNEL_ID 
from loader import router
from data.words import blacklisted_words  


def is_blacklisted(message):
    for word in blacklisted_words:
        if word.lower() in message.lower():
            return True
    return False


@router.message(F.forward_from) 
async def cmd_forward(message: types.Message):
    from loader import bot

    if message.forward_from is not None:
        await message.reply("This is a forwarded message")  
        return
    
    if is_blacklisted(message.text):
        return
    
    await bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=message.chat.id, message_id=message.message_id)

 
