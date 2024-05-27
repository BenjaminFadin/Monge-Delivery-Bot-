from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


# @dp.message_handler(filters.Command('change_phonto'), filters.AdminFilter())
@dp.message_handler(commands='ban_user', is_chat_admin=True)
async def chat_admin_example(msg: types.Message):
    await msg.answer("Rasm almashtiramizmi?")

 