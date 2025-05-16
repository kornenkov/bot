from aiogram.types import InlineKeyboardButton

from core.callback_data.level_base_callback_data import BaseLevel
from core.callback_data.close_callback_data import CloseCbData
from core.callback_data.start_callback_data import StartLevelCbData
from core.callback_data.navigation_callback_data import (
    NavigationCbData,
    NavigationAction,
)


main_menu_button = InlineKeyboardButton(
    text="вернуться в главное меню",
    callback_data=StartLevelCbData(
        LEVEL=BaseLevel.FIRST,
    ).pack(),
)

close_button = InlineKeyboardButton(
    text="закрыть",
    callback_data=CloseCbData().pack(),
)

cross_dummy_button = InlineKeyboardButton(
    text="🚫",
    callback_data=NavigationCbData(
        ACTION=NavigationAction.DUMMY,
    ).pack(),
)

blank_dummy_button = InlineKeyboardButton(
    text=" ",
    callback_data=NavigationCbData(
        ACTION=NavigationAction.DUMMY,
    ).pack(),
)
