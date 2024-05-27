from aiogram import types
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.default.settingsKeyboard import get_settings_keyboard
from utils import naming
from utils.validators import validate_date
from datetime import datetime


@dp.message_handler(state=PersonalData.change_birth_date)
async def changeLanguageHandler(message: types.Message):
    print("In change birthDate handler")
    birth_date_str = message.text
    user = await db.select_user(telegram_id=message.from_user.id)
    user_lang = user['language']
    telegram_id = user['telegram_id']

    if validate_date(birth_date_str):
        birth_date = datetime.strptime(birth_date_str, '%d.%m.%Y').date()
        await db.update_user_birth_date(birth_date, telegram_id)

        await message.answer(naming.accept_msg[user_lang])
        await message.answer(naming.SETTINGS_MSG[user_lang], reply_markup=get_settings_keyboard(user_lang))
        await PersonalData.settings.set()
    else:
        await message.answer(naming.BIRTH_DATE_MSG[user_lang])

