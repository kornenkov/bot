from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
)

from core.extra.buttons import main_menu_button


def build_about_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="связаться с разработчиком",
        url="https://t.me/kornenkov",
    )
    builder.add(main_menu_button)
    builder.adjust(1, 1)
    return builder.as_markup()
