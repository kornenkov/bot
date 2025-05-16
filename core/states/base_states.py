from aiogram.fsm.state import StatesGroup, State


class AccountBase(StatesGroup):
    INPUT_FIRST_NAME = State()
    INPUT_LAST_NAME = State()
    INPUT_PATRONYMIC = State()
    INPUT_PHONE = State()
