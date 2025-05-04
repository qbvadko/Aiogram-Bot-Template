import os
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("TOKEN")

BOT_PROPERTIES = DefaultBotProperties(
    disable_notification=True, 
    link_preview_is_disabled=True
)

BOT_COMMANDS = {
    '/start': '',
}
