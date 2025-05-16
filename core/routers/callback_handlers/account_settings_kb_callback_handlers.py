from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from core.callback_data.account_settings_callback_data import (
    AccountSettingsAction,
    AccountSettingsCbData,
)

from core.states.account_settings_states import AccountSettings
from core.extra.validators import valid_phone_filter

from core.extra.functions import report_fault

from crud.update import update_profile

router = Router(name=__name__)


@router.callback_query(
    AccountSettingsCbData.filter(
        F.ACTION == AccountSettingsAction.FIRST_NAME,
    )
)
async def process_first_name_key(
    callback_query: types.CallbackQuery,
    state: FSMContext,
):
    await callback_query.answer()
    await callback_query.message.answer(text="введите новое имя")
    await state.set_state(AccountSettings.INPUT_FIRST_NAME)


@router.message(
    AccountSettings.INPUT_FIRST_NAME,
    F.text,
)
async def process_input_first_name(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
):
    await update_profile(
        session=session,
        tg_user_tg_id=message.from_user.id,
        ud_mapping={"first_name": message.text},
    )
    await message.reply("имя успешно изменено!")
    await state.clear()


@router.callback_query(
    AccountSettingsCbData.filter(
        F.ACTION == AccountSettingsAction.LAST_NAME,
    )
)
async def process_last_name_key(
    callback_query: types.CallbackQuery,
    state: FSMContext,
):
    await callback_query.answer()
    await callback_query.message.answer(text="введите новую фамилию")
    await state.set_state(AccountSettings.INPUT_LAST_NAME)


@router.message(
    AccountSettings.INPUT_LAST_NAME,
    F.text,
)
async def process_input_last_name(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
):
    await update_profile(
        session=session,
        tg_user_tg_id=message.from_user.id,
        ud_mapping={"last_name": message.text},
    )
    await message.reply("фамилия успешно изменена!")
    await state.clear()


@router.callback_query(
    AccountSettingsCbData.filter(
        F.ACTION == AccountSettingsAction.PATRONYMIC,
    )
)
async def process_patronymic_key(
    callback_query: types.CallbackQuery,
    state: FSMContext,
):
    await callback_query.answer()
    await callback_query.message.answer(text="введите новое отчество")
    await state.set_state(AccountSettings.INPUT_PATRONYMIC)


@router.message(
    AccountSettings.INPUT_PATRONYMIC,
    F.text,
)
async def process_input_patronymic(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
):
    await update_profile(
        session=session,
        tg_user_tg_id=message.from_user.id,
        ud_mapping={"patronymic": message.text},
    )
    await message.reply("отчество успешно изменено!")
    await state.clear()


async def process_invalid_input_patronymic(
    message: types.Message,
):
    await report_fault(
        message=message,
        entity="отчество",
    )


@router.callback_query(
    AccountSettingsCbData.filter(
        F.ACTION == AccountSettingsAction.PHONE,
    )
)
async def process_phone_key(
    callback_query: types.CallbackQuery,
    state: FSMContext,
):
    await callback_query.answer()
    await callback_query.message.answer(text="введите новый телефон")
    await state.set_state(AccountSettings.INPUT_PHONE)


@router.message(
    AccountSettings.INPUT_PHONE,
    F.cast(valid_phone_filter).as_(
        "phone",
    ),
)
async def process_input_phone(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
    phone: str,
):
    await update_profile(
        session=session,
        tg_user_tg_id=message.from_user.id,
        ud_mapping={"phone": int(phone)},
    )
    await message.reply("телефон успешно изменен!")
    await state.clear()
