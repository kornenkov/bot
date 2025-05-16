from aiogram import Router, types

from core.callback_data.catalog_callback_data import CatalogCbData


router = Router(name=__name__)


@router.callback_query(CatalogCbData.filter())
async def process_catalog_key(
    callback_query: types.CallbackQuery,
    callback_data: CatalogCbData,
) -> None:
    await callback_query.answer(text="гуд!")
    print(callback_data.NAME)
    print(callback_data.ID)
