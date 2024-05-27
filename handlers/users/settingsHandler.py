from aiogram import types
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from utils import naming
from loader import dp, db
from keyboards.default.menuKeyboard import language_choices, remove_kb, get_main_menu_keyboard
from keyboards.default.settingsKeyboard import get_settings_keyboard


@dp.message_handler(state=PersonalData.settings)
async def settingsHandler(message: types.Message):
    print('In settings')
    msg = message.text
    user = await db.select_user(telegram_id=message.from_user.id)
    user_lang = user['language']

    if msg == naming.CHANGE_LANGUAGE[user_lang]:
        await message.answer(naming.choose_lang[user_lang], reply_markup=language_choices)
        await PersonalData.change_language.set()

    elif msg == naming.CHANGE_BIRTH_DATE[user_lang]:
        await message.answer(naming.BIRTH_DATE_MSG[user_lang], reply_markup=remove_kb)
        await PersonalData.change_birth_date.set()
    elif msg == naming.CANCEL[user_lang]:
        await message.answer(naming.main_menu_response[user_lang], reply_markup=get_main_menu_keyboard(user_lang))
        await PersonalData.main_menu.set()
    else:
        await message.answer(naming.error_msg[user_lang])

