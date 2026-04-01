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

def admin_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Profile'),KeyboardButton(text='Admin panel')]
        ],
        resize_keyboard=True
    )

def admin_panel():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Users')]
        ],resize_keyboard=True
    )