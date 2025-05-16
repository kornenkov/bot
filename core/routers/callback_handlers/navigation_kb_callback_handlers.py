from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from core.keyboards.inline_keyboards.catalog_kb import build_catalog_kb
from core.keyboards.pagination_kb import build_pagination_kb

from core.callback_data.navigation_callback_data import (
    NavigationAction,
    NavigationCbData,
)

from core.states.catalog_states import Catalog
from core.extra.functions import report_fault, send_temporal_message
from core.extra.validators import valid_number_filter


router = Router(name=__name__)


@router.callback_query(
    NavigationCbData.filter(
        F.ACTION == NavigationAction.SELECT_PAGE,
    )
)
async def process_page_key(
    callback_query: types.CallbackQuery,
    callback_data: NavigationCbData,
    state: FSMContext,
) -> None:
    await callback_query.answer()
    target_message = await callback_query.message.answer(
        text="введите страницу, к которой хотите перейти",
        reply_markup=build_pagination_kb(
            callback_data.TOTAL_PAGES,
        ),
    )
    await state.update_data(
        target_callback_query=callback_query,
        target_callback_data=callback_data,
        target_message=target_message,
    )
    await state.set_state(Catalog.INPUT_PAGE)


@router.message(
    Catalog.INPUT_PAGE,
    F.cast(valid_number_filter).as_(
        "target_page",
    ),
)
async def process_input_page(
    message: types.Message,
    state: FSMContext,
    target_page: int,
) -> None:
    data = await state.get_data()

    target_callback_query = data.get("target_callback_query")
    target_callback_data = data.get("target_callback_data")
    target_message = data.get("target_message")

    await message.delete()

    if target_page != target_callback_data.CURRENT_PAGE:
        if 1 <= target_page <= target_callback_data.TOTAL_PAGES:
            await target_callback_query.message.edit_reply_markup(
                reply_markup=build_catalog_kb(
                    page=target_page,
                ),
            )
            await target_message.delete()
            await state.clear()
        else:
            await send_temporal_message(
                message=message,
                text="такой страницы нет! попробуйте еще раз",
            )
    else:
        await send_temporal_message(
            message=message,
            text=f"Вы уже находитесь на {target_page} странице! введите любую другую",
        )


@router.message(Catalog.INPUT_PAGE)
async def process_invalid_input_page(
    message: types.Message,
) -> None:
    await report_fault(
        message=message,
        entity="номер страницы",
    )


@router.callback_query(
    NavigationCbData.filter(
        F.ACTION == NavigationAction.DUMMY,
    )
)
async def process_dummy_key(
    callback_query: types.CallbackQuery,
) -> None:
    await callback_query.answer()


@router.callback_query(
    NavigationCbData.filter(
        F.ACTION.in_(
            (
                NavigationAction.GO_RIGHT,
                NavigationAction.GO_LEFT,
            )
        ),
    )
)
async def process_control_key(
    callback_query: types.CallbackQuery,
    callback_data: NavigationCbData,
) -> None:
    await callback_query.message.edit_text(
        text="каталог товаров",
        reply_markup=build_catalog_kb(
            callback_data.CURRENT_PAGE,
        ),
    )
