from aiogram import types
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from utils import naming
from loader import dp, db
from keyboards.default.settingsKeyboard import get_settings_keyboard


@dp.message_handler(state=PersonalData.main_menu)
async def mainMenuHandler(message: types.Message):
    print('In main menu')

    user = await db.select_specific_user(telegram_id=message.from_user.id)
    user_lang = user['language']
    
    msg = message.text

    if msg == naming.SALE[user_lang]:
        await db.get_orders_by_telegram_id(user['telegram_id'])
        await message.answer(naming.sale_no_data[user_lang])
    elif msg == naming.CURR_ORDERS[user_lang]:
        await message.answer("Current orders")
    elif msg == naming.SETTINGS[user_lang]:
        await message.answer(naming.SETTINGS_MSG[user_lang], reply_markup=get_settings_keyboard(user_lang))
        await PersonalData.settings.set()
    else:
        await message.answer(naming.error_msg[user_lang])

