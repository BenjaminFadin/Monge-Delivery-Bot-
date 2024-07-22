from aiogram import types
from states.PersonalData import PersonalData
from aiogram.dispatcher import FSMContext
from utils import naming
from loader import dp, db
from keyboards.default.settingsKeyboard import get_settings_keyboard
from keyboards.default.OrdersKeyboard import get_order_inline_keyboard
from utils.db_api.messages import format_orders



@dp.message_handler(state=PersonalData.main_menu)
async def mainMenuHandler(message: types.Message):
    print("Nain menu") 
    
    user = await db.select_specific_user(telegram_id=message.from_user.id)
    user_lang = user['language']
    
    msg = message.text

    if msg == naming.ORDERS[user_lang]:
        orders = await db.getOrders()
        print(orders)
        if orders:
            formatted_orders = format_orders(orders, user_lang)
            for order, formatted_order in zip(orders, formatted_orders):
                order_id = order['id']  # Assuming each order has an 'id' field
                keyboard = get_order_inline_keyboard(order_id)
                await message.answer(formatted_order, reply_markup=keyboard)
        else:
            await message.answer(naming.sale_no_data[user_lang])

    elif msg == naming.CURR_ORDERS[user_lang]:
        await message.answer(naming.MY_ORDERS[user_lang])
    elif msg == naming.SETTINGS[user_lang]:
        await message.answer(naming.SETTINGS_MSG[user_lang], reply_markup=get_settings_keyboard(user_lang))
        await PersonalData.settings.set()
    else:
        await message.answer(naming.error_msg[user_lang])

