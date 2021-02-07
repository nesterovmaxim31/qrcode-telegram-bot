import cv2
import os
from pyzbar import pyzbar
import qrcode


def qrcode_loker(user_id):
    img = cv2.imread(f"test{user_id}.jpg")
    code = pyzbar.decode(img)
    D = 0
    for h in code:
        D = h.data.decode("utf-8")
    if not D:
        return "К сожалению мы не смогли расшифровать ваш qrcode.\nПопробуйте сделать повторное фото с" \
               " масимально точность"
    else:
        return D


async def create(text, user_id):
    qrcode_img = qrcode.make(text)
    qrcode_img.save(f"form{user_id}.jpg")


async def delete_file_photo_user(user_id):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'test{user_id}.jpg')
    os.remove(path)
