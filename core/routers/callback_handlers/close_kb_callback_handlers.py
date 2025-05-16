from aiogram import types, Router

from core.callback_data.close_callback_data import CloseCbData


router = Router(name=__name__)


@router.callback_query(CloseCbData.filter())
async def process_close_key(
    callback_query: types.CallbackQuery,
):
    await callback_query.answer()
    await callback_query.message.delete()
