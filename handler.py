from app import bot, db
from aiogram.types import Message
from config import admin_id
# from qrcode_lok import qrcode_loker, delete_file_photo_user


async def send_to_admin(db):
    await bot.send_message(chat_id=admin_id, text="вроде работает и это уже четвёртый")


@db.message_handler(commands=["start"])
async def process_hi6_command(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Привет")


# @db.message_handler(content_types=['photo'])
# async def handle_docs_photo(message: Message):
#     await message.photo[0].download(f'test{message.from_user.id}.jpg')
#     await bot.send_message(message.from_user.id, text="Ожидайте результат...")
#     M = await qrcode_loker(message.from_user.id)
#     await bot.send_message(message.from_user.id, text=f"{M}")
#     await delete_file_photo_user(message.from_user.id)
