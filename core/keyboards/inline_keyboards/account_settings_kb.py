from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
)
from core.callback_data.account_settings_callback_data import (
    AccountSettingsCbData,
    AccountSettingsAction,
)
from core.extra.buttons import main_menu_button
from core.databases.postgresql.models.schemas import AccountSm


def build_account_settings_kb(
    account: AccountSm,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=f"имя: {account.first_name}",
        callback_data=AccountSettingsCbData(
            ACTION=AccountSettingsAction.FIRST_NAME,
        ).pack(),
    )

    builder.button(
        text=f"фамилия: {account.last_name}",
        callback_data=AccountSettingsCbData(
            ACTION=AccountSettingsAction.LAST_NAME,
        ).pack(),
    )

    if account.patronymic:
        builder.button(
            text=f"отчество: {account.patronymic}",
            callback_data=AccountSettingsCbData(
                ACTION=AccountSettingsAction.PATRONYMIC,
            ).pack(),
        )

    builder.button(
        text=f"телефон: {account.phone}",
        callback_data=AccountSettingsCbData(
            ACTION=AccountSettingsAction.PHONE,
        ).pack(),
    )

    builder.add(main_menu_button)

    builder.adjust(2, 1, 1)
    return builder.as_markup()
