__all__ = ("router",)


from aiogram import Router

from core.routers.account.account_shared_handlers import (
    router as profile_base_handlers_router,
)


router = Router()


router.include_routers(
    profile_base_handlers_router,
)
