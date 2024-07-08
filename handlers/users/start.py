import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from keyboards.default.menuKeyboard import language_choices, get_main_menu_keyboard, remove_kb
from utils import naming
from data.config import ADMINS


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = await db.select_specific_user(telegram_id=message.from_user.id)
    # print(user)
    
    msg = ''
    lang_msg = ''
    msg += 'Assalomu alaykum, Xush Kelibsiz! \n'
    msg += 'Здраствуйте, добро пожаловать!'
    lang_msg += 'Bot faqat dostavkachilar uchun! \n'
    lang_msg += 'Бот предназначен только для курьеров!'
    
    if not user:
        await message.answer(lang_msg, reply_markup=remove_kb)

    else:
        user_lang = user['language']

        await message.answer(naming.main_menu_response[user_lang], reply_markup=get_main_menu_keyboard(user_lang))
        await PersonalData.main_menu.set()


