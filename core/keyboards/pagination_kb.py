from aiogram.utils.keyboard import (
    ReplyKeyboardBuilder,
    ReplyKeyboardMarkup,
)


def build_pagination_kb(
    tabs: int,
) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for tab in range(1, tabs + 1):
        builder.button(text=str(tab))
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)
