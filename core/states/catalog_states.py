from aiogram.fsm.state import StatesGroup, State


class Catalog(StatesGroup):
    INPUT_PAGE = State()
