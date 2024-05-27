from aiogram import types
from datetime import datetime
from aiogram.dispatcher.filters.builtin import CommandStart
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from utils import naming
from loader import dp, db
from keyboards.default.menuKeyboard import language_choices, get_main_menu_keyboard
from utils.validators import validate_date
from utils.db_api.postgresql import Database


@dp.message_handler(state=PersonalData.birthDate)
async def birthDateHandler(message: types.Message, state: FSMContext):
    birth_date_str = message.text
    state_data = await state.get_data()
    user_lang = state_data['language']

    if validate_date(birth_date_str):
        birth_date = datetime.strptime(birth_date_str, '%d.%m.%Y').date()
        print(state_data)
        await db.add_user(
            telegram_id=state_data['telegram_id'],
            username=state_data['username'],
            first_name=state_data['first_name'],
            last_name=state_data['last_name'],
            phone_number=state_data['phone_number'],
            lang=state_data['language'],
            birth_date=birth_date
        )

        await message.answer(naming.main_menu_response[user_lang], reply_markup=get_main_menu_keyboard(user_lang))
        await PersonalData.main_menu.set()
    else:
        await message.answer(naming.BIRTH_DATE_MSG[user_lang])
