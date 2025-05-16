from aiogram.filters.callback_data import CallbackData
from enum import IntEnum, auto
from typing import Optional


class NavigationAction(IntEnum):
    GO_LEFT = auto()
    SELECT_PAGE = auto()
    GO_RIGHT = auto()
    DUMMY = auto()


class NavigationCbData(
    CallbackData,
    prefix="navigation",
):
    ACTION: NavigationAction
    CURRENT_PAGE: Optional[int] = None
    TOTAL_PAGES: Optional[int] = None
