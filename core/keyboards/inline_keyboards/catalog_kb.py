from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
)

from core.callback_data.catalog_callback_data import CatalogCbData
from core.callback_data.navigation_callback_data import (
    NavigationCbData,
    NavigationAction,
)
from core.extra.functions import chunks
from core.extra.buttons import main_menu_button, cross_dummy_button, blank_dummy_button

################################################################################

from garbage import products

################################################################################

ITEMS_PER_PAGE = 12
BUTTONS_PER_ROW = 3


PAGES_DATA = chunks(products, ITEMS_PER_PAGE)
PAGES_DATA_LEN = len(PAGES_DATA)


def build_catalog_kb(
    page: int,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    page_data = PAGES_DATA[page - 1]
    page_data_len = len(page_data)

    is_first = page == 1
    is_last = page == PAGES_DATA_LEN

    for item in page_data:
        builder.button(
            text=item.name,
            callback_data=CatalogCbData(
                NAME=item.name,
                ID=item.primary_key,
            ).pack(),
        )

    fill_count = (ITEMS_PER_PAGE - page_data_len) % BUTTONS_PER_ROW
    if fill_count:
        for _ in range(fill_count):
            builder.add(blank_dummy_button)

    if is_first:
        builder.add(cross_dummy_button)
    else:
        previous_page = page - 1
        builder.button(
            text="⬅️",
            callback_data=NavigationCbData(
                ACTION=NavigationAction.GO_LEFT,
                CURRENT_PAGE=previous_page,
            ),
        )

    builder.button(
        text=f"{page}/{PAGES_DATA_LEN}",
        callback_data=NavigationCbData(
            ACTION=NavigationAction.SELECT_PAGE,
            CURRENT_PAGE=page,
            TOTAL_PAGES=len(PAGES_DATA),
        ).pack(),
    )

    if is_last:
        builder.add(cross_dummy_button)
    else:
        next_page = page + 1
        builder.button(
            text="➡️",
            callback_data=NavigationCbData(
                ACTION=NavigationAction.GO_RIGHT,
                CURRENT_PAGE=next_page,
            ),
        )
    builder.add(main_menu_button)

    builder.adjust(BUTTONS_PER_ROW)
    return builder.as_markup()
