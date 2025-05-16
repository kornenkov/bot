from .base_sm import BaseSm


class TgUserSm(BaseSm):
    tg_id: int
    first_name: str
    last_name: str | None
    username: str | None
    active: bool = True

    @property
    def tg_full_name(self):
        return f"{self.first_name} {self.last_name or ''}"
