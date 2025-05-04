import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import BOT_TOKEN, BOT_COMMANDS, BOT_PROPERTIES
from handlers import common

async def on_startup(bot: Bot):
    ...

async def on_shutdown(bot: Bot):
    ...

async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=BOT_PROPERTIES)
    
    dp = Dispatcher(bot=Bot)
    dp.include_routers(common.router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    await bot.set_my_commands([
        BotCommand(command=c, description=d) for c, d in BOT_COMMANDS.items()
    ])
    await bot.set_chat_menu_button()
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
