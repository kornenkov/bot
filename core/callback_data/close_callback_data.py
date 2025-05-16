from aiogram.filters.callback_data import CallbackData


class CloseCbData(
    CallbackData,
    prefix="close",
):
    pass
