from app import bot, db
from aiogram.types import Message
from config import admin_id
from qrcode_lok import qrcode_loker, create, delete_file_photo_user_2


async def send_to_admin(db):
    await bot.send_message(chat_id=admin_id, text="вроде работает и это уже четвёртый")


@db.message_handler(commands=["start"])
async def process_hi6_command(message: Message):
    await bot.send_message(chat_id=message.chat.id, text=f"Привет {message.from_user.first_name},"
                                                         f" я бот умеющий работать с qrcode,\n"
                                                         "что бы расшифрофать qrcode, пришлите мне его фото\n"
                                                         "что бы создать qrcode, просто введите требуемый текст или"
                                                         " ссылку")


@db.message_handler(content_types=['photo'])
async def handle_docs_photo(message: Message):
    await message.photo[0].download(f'test{message.from_user.id}-{message["message_id"]}.jpg')
    await bot.send_message(message.from_user.id, text=f"Ожидайте результат...")
    await message.reply(f"{qrcode_loker(message.from_user.id, message['message_id'])}")


@db.message_handler()
async def create_qrcode_2(message: Message):
    await create(message.text, message.from_user.id)
    await bot.send_photo(chat_id=message.chat.id, photo=open(f"form{message.from_user.id}.jpg", "rb"))
    await delete_file_photo_user_2(message.from_user.id)
