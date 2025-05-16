from aiogram.filters.callback_data import CallbackData
from enum import IntEnum, auto


class AccountSettingsAction(IntEnum):
    FIRST_NAME = auto()
    LAST_NAME = auto()
    PATRONYMIC = auto()
    PHONE = auto()


class AccountSettingsCbData(
    CallbackData,
    prefix="account_settings",
):
    ACTION: AccountSettingsAction
