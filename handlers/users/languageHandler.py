from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.menuKeyboard import remove_kb, language_choices
from utils import naming


@dp.message_handler(state=PersonalData.language)
async def languageHandler(message: types.Message, state: FSMContext):
    msg = message.text
    if msg in naming.languages:
        await state.update_data({'language': naming.languages[msg]})
        user_data = await state.get_data()
        await PersonalData.fullname.set()
        await message.answer(naming.language_response[msg], reply_markup=remove_kb)

    else:
        await message.answer("Xato kiritildi!")
