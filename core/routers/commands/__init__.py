__all__ = ("router",)


from aiogram import Router

from .base_commands import router as base_router
from .admin_commands import router as admin_router


router = Router(name=__name__)

router.include_routers(
    base_router,
    admin_router,
)
