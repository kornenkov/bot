from aiogram import Router, types


router = Router(name=__name__)


@router.message()
async def process_strange_message(
    message: types.Message,
):
    await message.answer("Я не понимаю")
