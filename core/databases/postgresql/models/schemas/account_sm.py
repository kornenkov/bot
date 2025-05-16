from .tguser_sm import TgUserSm
from .profile_sm import ProfileSm


class AccountSm(ProfileSm):
    tg_user: TgUserSm
