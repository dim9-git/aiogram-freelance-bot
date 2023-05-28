from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import handlers

bot = Bot(token=BOT_TOKEN)
Bot.set_current(bot)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

handlers.setup(dp)
