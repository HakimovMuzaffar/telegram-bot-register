from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def phone_button():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="Kontakt jo'natish 📞", request_contact=True)]
    ], resize_keyboard=True)