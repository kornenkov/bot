from .base_sm import BaseSm


class ProfileSm(BaseSm):
    first_name: str
    last_name: str
    patronymic: str | None
    phone: int
    tg_user_tg_id: int

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.patronymic or ''}"
