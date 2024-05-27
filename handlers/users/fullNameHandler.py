from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from utils import naming
from loader import dp, db
from keyboards.default.menuKeyboard import get_phone_number_button, remove_kb


@dp.message_handler(state=PersonalData.fullname)
async def fullname_handler(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(
        {'fullname': msg, 'first_name': message.from_user.first_name, 'last_name': message.from_user.last_name,
         'username': message.from_user.username})

    state_data = await state.get_data()
    user_lang = state_data.get('language')

    await message.answer(naming.phone_number_msg[user_lang], reply_markup=get_phone_number_button(user_lang))

    await PersonalData.phoneNumber.set()
    print("State set to phonenumber")

# @dp.message_handler(state=PersonalData.phoneNumber, content_types=['contact'])
# async def phoneNumberHandler(message: types.Message, state: FSMContext):
#     print('In phone number')
#     msg = message.text
#     print(msg)
#     print(message.contact.phone_number)
#
#     state_data = await state.get_data()
#     user_lang = state_data['language']
#
#     await message.answer(naming.main_menu_response[user_lang], reply_markup=remove_kb)
#
#     await PersonalData.main_menu.set()
#
