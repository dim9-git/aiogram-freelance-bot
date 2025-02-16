import logging
import sys
 
from aiohttp import web
from aiogram import types, F, Bot
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from loader import bot, dp, router
from config import   CHANNEL_ID, WEBHOOK_URL, PORT,  WEBHOOK_SECRET, WEBHOOK_PATH

from data.words import blacklisted_words  

async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(WEBHOOK_URL, secret_token=WEBHOOK_SECRET)
 

async def on_shutdown(_):
    logging.warning('Shutting down..')
    await bot.delete_webhook()


def is_blacklisted(message):
    for word in blacklisted_words:
        if word.lower() in message.lower():
            return True
    return False


@router.message() 
async def forwarded_handler(message: types.Message):
    print("forwarded_handler")
    print(message)
    from loader import bot

    if message.forward_from is not None:
        await message.reply("This is a forwarded message")  
        return
    
    if is_blacklisted(message.text):
        return
    
    await bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=message.chat.id, message_id=message.message_id)

 


def main() -> None:
    dp.include_router(router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)
    # Register shutdown hook to delete webhook
    dp.shutdown.register(on_shutdown)

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )

    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    web.run_app(
        app,   
        host="0.0.0.0",
        port=int(PORT)
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()