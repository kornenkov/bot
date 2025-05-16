from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
)
from core.callback_data.system_callback_data import (
    SystemCbData,
    System,
)
from core.extra.buttons import main_menu_button


def build_system_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="ios",
        callback_data=SystemCbData(
            SYSTEM=System.IOS,
        ).pack(),
    )
    builder.button(
        text="android",
        callback_data=SystemCbData(
            SYSTEM=System.ANDROID,
        ).pack(),
    )
    builder.add(main_menu_button)
    builder.adjust(2, 1)
    return builder.as_markup()
