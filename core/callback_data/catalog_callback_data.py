from aiogram.filters.callback_data import CallbackData
from .level_base_callback_data import BaseLevel


class CatalogCbData(
    CallbackData,
    prefix="catalog",
):
    NAME: str
    ID: int


class CatalogLevelCbData(
    CallbackData,
    prefix="catalog_level",
):
    LEVEL: BaseLevel
