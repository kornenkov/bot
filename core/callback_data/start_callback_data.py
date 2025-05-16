from aiogram.filters.callback_data import CallbackData
from enum import IntEnum, auto
from .level_base_callback_data import BaseLevel


class StartAction(IntEnum):
    ABOUT = auto()
    ACCOUNT = auto()
    SYSTEM = auto()
    CATALOG = auto()


class StartCbData(
    CallbackData,
    prefix="start",
):
    ACTION: StartAction


class StartLevelCbData(
    CallbackData,
    prefix="start_level",
):
    LEVEL: BaseLevel
