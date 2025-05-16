__all__ = ("router",)


from aiogram import Router

from .start_kb_callback_handlers import (
    router as start_kb_callback_router,
)
from .system_kb_callback_handlers import (
    router as system_kb_callback_router,
)
from .close_kb_callback_handlers import (
    router as close_kb_callback_router,
)
from .catalog_kb_callback_handlers import (
    router as catalog_kb_callback_router,
)
from .navigation_kb_callback_handlers import (
    router as navigation_kb_callback_router,
)
from .account_settings_kb_callback_handlers import (
    router as account_settings_kb_callback_router,
)


router = Router(name=__name__)


router.include_routers(
    start_kb_callback_router,
    system_kb_callback_router,
    close_kb_callback_router,
    catalog_kb_callback_router,
    navigation_kb_callback_router,
    account_settings_kb_callback_router,
)
