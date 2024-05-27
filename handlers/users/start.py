import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from keyboards.default.menuKeyboard import language_choices, get_main_menu_keyboard
from utils import naming
from data.config import ADMINS


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)

    msg = ''
    lang_msg = ''
    msg += 'Assalomu alaykum, Xush Kelibsiz! \n'
    msg += 'Здраствуйте, добро пожаловать!'
    lang_msg += 'Iltimos til tanlang! \n'
    lang_msg += 'Пожалуйста, выберите язык!'

    if not user:
        await message.answer(lang_msg, reply_markup=language_choices)
        await PersonalData.language.set()

    else:
        user_lang = user['language']

        await message.answer(naming.main_menu_response[user_lang], reply_markup=get_main_menu_keyboard(user_lang))
        await PersonalData.main_menu.set()


