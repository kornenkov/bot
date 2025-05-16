from aiogram import Router, types, F

from core.keyboards.inline_keyboards.apps_kb import build_apps_kb
from core.keyboards.inline_keyboards.close_kb import build_close_kb
from core.keyboards.inline_keyboards.system_kb import build_system_kb

from core.callback_data.level_base_callback_data import BaseLevel
from core.callback_data.system_callback_data import (
    System,
    SystemCbData,
    SystemLevelCbData,
)

from core.schemas.apps_sm import Apps


router = Router(name=__name__)


ios_malls = Apps(
    poizon="https://clck.ru/3F3dPc",
    fenapp="https://clck.ru/3F3em6",
    taobao="https://clck.ru/3F3eRm",
    pinduoduo="https://clck.ru/3F66xd",
)

android_malls = Apps(
    poizon="https://goo.su/ebUQnl1",
    fenapp="https://goo.su/16Rlv8A",
    taobao="https://goo.su/TQPlRUB",
    pinduoduo="https://goo.su/8BNE3",
)


@router.callback_query(
    SystemCbData.filter(
        F.SYSTEM == System.IOS,
    ),
)
async def process_ios_key(
    callback_query: types.CallbackQuery,
):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="cсылки для <b>ios</b>",
        reply_markup=build_apps_kb(
            app=ios_malls,
        ),
    )
    await callback_query.message.answer(
        text="pinduoduo <b>нет</b> в российском AppStore! для скачивания приложения смените регион",
        reply_markup=build_close_kb(),
    )


@router.callback_query(
    SystemCbData.filter(
        F.SYSTEM == System.ANDROID,
    ),
)
async def process_android_key(
    callback_query: types.CallbackQuery,
):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="приложения для <b>android</b>",
        reply_markup=build_apps_kb(
            app=android_malls,
        ),
    )


@router.callback_query(
    SystemLevelCbData.filter(
        F.LEVEL == BaseLevel.SECOND,
    ),
)
async def process_second_level_key(
    callback_query: types.CallbackQuery,
):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="Вы вернулись назад к выбору системы",
        reply_markup=build_system_kb(),
    )
