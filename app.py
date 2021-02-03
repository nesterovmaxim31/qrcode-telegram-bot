from aiogram import Bot, Dispatcher, executor
import asyncio
from config import Bot_Token
loop = asyncio.get_event_loop()
bot = Bot(Bot_Token, parse_mode="HTML")
db = Dispatcher(bot, loop)

if __name__ == "__main__":
    from handler import db, send_to_admin
    executor.start_polling(db, on_startup=send_to_admin)