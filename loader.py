from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, Router

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
router = Router()
