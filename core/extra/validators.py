from aiogram import types
from typing import Optional

from phonenumbers import parse, is_possible_number
from phonenumbers.phonenumberutil import NumberParseException


def valid_phone_filter(
    message: types.Message,
) -> Optional[str]:
    contact = message.contact
    if contact:
        return contact.phone_number
    try:
        phone = parse(message.text, "RU")
        if is_possible_number(phone):
            return f"{phone.country_code}{phone.national_number}"
    except NumberParseException:
        pass
    return None


def valid_number_filter(
    message: types.Message,
) -> Optional[int]:
    try:
        return int(message.text)
    except TypeError:
        return None
