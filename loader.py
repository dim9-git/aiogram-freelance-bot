from config import BOT_TOKEN
from aiogram import Bot, Dispatcher

import handlers

bot = Bot(token=BOT_TOKEN)
Bot.set_current(bot)
dp = Dispatcher(bot)

handlers.setup(dp)
