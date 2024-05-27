from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer("Kim bu?")

@dp.message_handler(content_types='sticker')
async def emoji_handler(message: types.Message):
    await message.answer(":Smile")



@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def emoji_handler(message: types.Message):
    await message.answer("Contact")


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def emoji_handler(message: types.Message):
    await message.answer("Yaxshi eshitilmadi!")

