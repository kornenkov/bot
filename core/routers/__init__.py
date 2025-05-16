__all__ = ("router",)


from aiogram import Router

from .commands import router as commands_router
from .common import router as common_router

from .callback_handlers import router as callbacks_router

from .account.account_create_handlers import router as account_create_router
from .account import router as account_router


router = Router(name=__name__)

router.include_routers(
    commands_router,
    callbacks_router,
    account_create_router,
    account_router,
)

router.include_router(common_router)
