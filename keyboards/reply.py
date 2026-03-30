from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


def register():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Register")]
        ],
        resize_keyboard=True
    )


def profile():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Profile")]
        ],resize_keyboard=True
    )