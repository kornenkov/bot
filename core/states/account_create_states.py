from aiogram.fsm.state import StatesGroup, State


class AccountCreate(StatesGroup):
    CREATE_FIRST_NAME = State()
    CREATE_LAST_NAME = State()
    CREATE_PATRONYMIC = State()
    CREATE_PHONE = State()
