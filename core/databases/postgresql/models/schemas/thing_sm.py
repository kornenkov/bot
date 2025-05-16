from .base_sm import BaseSm


class ThingSm(BaseSm):
    name: str
    quality: str
    bio: str | None
    price: int
    link: str | None
