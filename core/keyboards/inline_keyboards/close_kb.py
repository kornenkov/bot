from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from core.extra.buttons import close_button


def build_close_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(close_button)
    return builder.as_markup()
