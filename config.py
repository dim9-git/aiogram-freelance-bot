import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

WEB_SERVER = os.getenv("WEB_SERVER")
PORT = os.getenv("PORT")

WEBHOOK_PATH = f"/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEB_SERVER}{WEBHOOK_PATH}"
