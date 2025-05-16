from aiogram import Router, F, types

from sqlalchemy.ext.asyncio import AsyncSession

from core.callback_data.level_base_callback_data import BaseLevel
from core.callback_data.start_callback_data import (
    StartAction,
    StartCbData,
    StartLevelCbData,
)

from core.keyboards.inline_keyboards.catalog_kb import build_catalog_kb
from core.keyboards.inline_keyboards.about_kb import build_about_kb
from core.keyboards.inline_keyboards.system_kb import build_system_kb
from core.keyboards.inline_keyboards.start_kb import build_start_kb
from core.keyboards.inline_keyboards.account_settings_kb import (
    build_account_settings_kb,
)

from crud.read import get_user_and_profile_by_tg_id


router = Router(name=__name__)


about = "dmallwww предоставляет удобную и надёжную доставку товаров из Китая: от техники и электроники до одежды, аксессуаров и товаров для дома. Вы выбираете товары на торговых площадках, а мы заботимся о выкупе и доставке."


@router.callback_query(
    StartCbData.filter(
        F.ACTION == StartAction.ABOUT,
    )
)
async def process_about_key(
    callback_query: types.CallbackQuery,
):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=about,
        reply_markup=build_about_kb(),
    )


@router.callback_query(
    StartCbData.filter(
        F.ACTION == StartAction.ACCOUNT,
    )
)
async def process_account_settings_key(
    callback_query: types.CallbackQuery,
    session: AsyncSession,
):
    await callback_query.answer()
    account = await get_user_and_profile_by_tg_id(
        session=session,
        tg_id=callback_query.from_user.id,
    )
    if not account:
        await callback_query.message.answer(text="у вас еще нет аккаунта. /account")
        return
    await callback_query.message.edit_text(
        text="Ваш профиль",
        reply_markup=build_account_settings_kb(
            account=account,
        ),
    )


@router.callback_query(
    StartCbData.filter(
        F.ACTION == StartAction.SYSTEM,
    ),
)
async def process_system_key(
    callback_query: types.CallbackQuery,
):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="выберите свою ос",
        reply_markup=build_system_kb(),
    )


@router.callback_query(
    StartCbData.filter(
        F.ACTION == StartAction.CATALOG,
    ),
)
async def process_catalog_key(
    callback_query: types.CallbackQuery,
):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="каталог товаров",
        reply_markup=build_catalog_kb(
            page=1,
        ),
    )


@router.callback_query(
    StartLevelCbData.filter(
        F.LEVEL == BaseLevel.FIRST,
    )
)
async def process_first_level_key(
    callback_query: types.CallbackQuery,
):
    await callback_query.message.edit_text(
        text="Вы вернулись в главное меню",
        reply_markup=build_start_kb(),
    )
