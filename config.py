import os
from dotenv import load_dotenv

load_dotenv()

CHANNEL_ID = os.getenv("CHANNEL_ID")

BOT_TOKEN = os.getenv("BOT_TOKEN")

BASE_WEBHOOK_URL = os.getenv("BASE_WEBHOOK_URL")
PORT = os.getenv("PORT")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

WEBHOOK_PATH = f"/{BOT_TOKEN}"
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"