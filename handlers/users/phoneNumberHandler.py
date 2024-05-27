from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from utils import naming, validators
from loader import dp
from keyboards.default.menuKeyboard import language_choices, remove_kb


@dp.message_handler(state=PersonalData.phoneNumber, content_types='contact')
async def phoneNumberHandler(message: types.Message, state: FSMContext):
    print("In phone number")
    msg = message.text

    state_data = await state.get_data()

    user_lang = state_data['language']
    phone_number = validators.get_phone_number(message.contact)

    print(f"Phone number here .........           {phone_number}")

    await state.update_data({'phone_number': phone_number, 'telegram_id': message.from_user.id})

    await message.answer(naming.BIRTH_DATE_MSG[user_lang], reply_markup=remove_kb)
    await PersonalData.birthDate.set()
    # await PersonalData.main_menu.set()

