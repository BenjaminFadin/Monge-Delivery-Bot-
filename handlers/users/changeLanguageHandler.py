from aiogram import types
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.default.settingsKeyboard import get_settings_keyboard
from utils import naming


@dp.message_handler(state=PersonalData.change_language)
async def changeLanguageHandler(message: types.Message):
    print("In change language handler")
    msg = message.text
    user = await db.select_user(telegram_id=message.from_user.id)
    user_lang = naming.languages[msg]
    telegram_id = user['telegram_id']
    print(msg, telegram_id)

    await db.update_user_language(user_lang, telegram_id)
    await message.answer(naming.accept_msg[user_lang])
    await message.answer(naming.accept_msg[user_lang], reply_markup=get_settings_keyboard(user_lang))
    await PersonalData.settings.set()

