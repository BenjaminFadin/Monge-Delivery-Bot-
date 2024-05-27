from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils import naming


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    # user = db.fetch_user(message.from_user.id)

    await message.answer("\n".join(naming.help_messages[user['language']]))

