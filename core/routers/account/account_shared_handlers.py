from aiogram import Router, types

from core.states.account_settings_states import AccountSettings
from core.states.account_create_states import AccountCreate

from core.extra.functions import report_fault


router = Router(name=__name__)


@router.message(AccountSettings.INPUT_FIRST_NAME)
@router.message(AccountCreate.CREATE_FIRST_NAME)
async def process_invalid_input_first_name(
    message: types.Message,
) -> None:
    await report_fault(
        message=message,
        entity="имя",
    )


@router.message(AccountSettings.INPUT_LAST_NAME)
@router.message(AccountCreate.CREATE_LAST_NAME)
async def process_invalid_input_last_name(
    message: types.Message,
) -> None:
    await report_fault(
        message=message,
        entity="фамилию",
    )


@router.message(AccountSettings.INPUT_PATRONYMIC)
@router.message(AccountCreate.CREATE_PATRONYMIC)
async def process_invalid_input_patronymic(
    message: types.Message,
) -> None:
    await report_fault(
        message=message,
        entity="отчество",
    )


@router.message(AccountSettings.INPUT_PHONE)
@router.message(AccountCreate.CREATE_PHONE)
async def process_invalid_input_phone(
    message: types.Message,
) -> None:
    await report_fault(
        message=message,
        entity="телефон",
    )
