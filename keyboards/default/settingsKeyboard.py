from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from utils import naming


def get_settings_keyboard(lang):
    rkm = ReplyKeyboardMarkup(True, row_width=2)

    rkm.add(*(KeyboardButton(btn[lang]) for btn in naming.SETTINGS_KEYBOARD))
    return rkm

