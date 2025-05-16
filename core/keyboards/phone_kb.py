from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def build_phone_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="отправить контакт",
        request_contact=True,
    )
    return builder.as_markup(resize_keyboard=True)
