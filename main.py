import asyncio
import sys
import logging
from os import getenv


from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# from handlers import bot_msg
from handlers.bot_msg import start_router
from callback.bot_clb_msg import cbl_router

from decouple import config

TOKEN: str = config("BOT_TOKEN", default=None)
if TOKEN is '':
    print("Enter ur TOKEN in .env")

dp = Dispatcher()




async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp.include_routers(
        start_router,
        cbl_router
    )

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    
    await bot.send_message(
        chat_id=897794210,
        text='server started')

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())