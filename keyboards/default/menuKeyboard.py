from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from utils import naming
from loader import WEB_APP_URL

web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Web App🤷', web_app=WebAppInfo(url=WEB_APP_URL))
        ],
    ],
    resize_keyboard=True
)

language_choices = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇷🇺 RUS'),
            KeyboardButton(text='🇺🇿 UZB'),
            KeyboardButton(text='🇺🇸 ENG')
        ],
    ],
    resize_keyboard=True,
    row_width=1
)


def get_phone_number_button(lang):
    phone_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    phone_keyboard.add(KeyboardButton(text=naming.phone_number_msg[lang], request_contact=True))
    return phone_keyboard


def get_main_menu_keyboard(lang):
    rkm = ReplyKeyboardMarkup(True, row_width=1)
    rkm.add(*(KeyboardButton(btn[lang]) for btn in naming.MAIN_MENU_KEYBOARD))
    return rkm


remove_kb = ReplyKeyboardRemove()

