from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def build_skip_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="пропустить")
    return builder.as_markup(resize_keyboard=True)
