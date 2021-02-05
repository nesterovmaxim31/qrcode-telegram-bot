import cv2
import os
from pyzbar.pyzbar import decode


async def qrcode_loker(user_id):
    img = cv2.imread(f"test{user_id}.JPG")
    code = decode(img)
    D = 0
    for h in code:
        D = h.data.decode("utf-8")
    if not D:
        return "К сожалению мы не смогли расшифровать ваш qrcode.\nПопробуйте сделать повторное фото с" \
               " масимально точность"
    else:
        return D


async def delete_file_photo_user(user_id):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'test{user_id}.jpg')
    os.remove(path)
