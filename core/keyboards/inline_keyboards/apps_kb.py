from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
)

from core.callback_data.level_base_callback_data import BaseLevel
from core.callback_data.system_callback_data import SystemLevelCbData
from core.extra.buttons import main_menu_button

from core.schemas.apps_sm import Apps


def build_apps_kb(
    app: Apps,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for name, link in app:
        builder.button(
            text=name,
            url=link,
        )
    builder.button(
        text="вернуться назад",
        callback_data=SystemLevelCbData(
            LEVEL=BaseLevel.SECOND,
        ).pack(),
    )
    builder.add(main_menu_button)
    builder.adjust(2, 2, 1)
    return builder.as_markup()
