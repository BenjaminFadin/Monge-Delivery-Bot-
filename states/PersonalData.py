from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalData(StatesGroup):
    language = State()
    fullname = State()
    phoneNumber = State()
    birthDate = State()
    main_menu = State()
    settings = State()
    change_language = State()
    change_birth_date = State()
    change_phone_number = State()


