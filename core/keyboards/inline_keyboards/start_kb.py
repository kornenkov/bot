from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
)
from core.callback_data.start_callback_data import (
    StartCbData,
    StartAction,
)


def build_start_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="о dmallwww",
        callback_data=StartCbData(
            ACTION=StartAction.ABOUT,
        ).pack(),
    )

    builder.button(
        text="ответы на вопросы",
        url="https://telegra.ph/FAQ-05-16-15",
    )

    builder.button(
        text="аккаунт",
        callback_data=StartCbData(
            ACTION=StartAction.ACCOUNT,
        ).pack(),
    )

    builder.button(
        text="маркетплейсы",
        callback_data=StartCbData(
            ACTION=StartAction.SYSTEM,
        ).pack(),
    )

    builder.button(
        text="каталог товаров",
        callback_data=StartCbData(
            ACTION=StartAction.CATALOG,
        ).pack(),
    )

    builder.adjust(1, 2, 2)
    return builder.as_markup()
