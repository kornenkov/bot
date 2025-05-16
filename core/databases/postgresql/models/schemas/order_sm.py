from .base_sm import BaseSm


class OrderSm(BaseSm):
    company: str | None
    insurance: int | None
    comment: str | None

    profile_id: int
    thing_id: int
