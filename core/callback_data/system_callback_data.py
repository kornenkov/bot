from aiogram.filters.callback_data import CallbackData
from enum import IntEnum, auto
from .level_base_callback_data import BaseLevel


class System(IntEnum):
    IOS = auto()
    ANDROID = auto()


class SystemCbData(
    CallbackData,
    prefix="system",
):
    SYSTEM: System


class SystemLevelCbData(
    CallbackData,
    prefix="system_level",
):
    LEVEL: BaseLevel
