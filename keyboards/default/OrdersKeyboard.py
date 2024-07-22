from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_order_inline_keyboard(order_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="View Order Details", callback_data=f"view_order_{order_id}")
    keyboard.add(button)
    return keyboard


