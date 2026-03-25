from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def start_menyu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🚗Car',callback_data="cars1"),InlineKeyboardButton(text="🗼History",callback_data="history1")],
            [InlineKeyboardButton(text='🧑‍💻IT',callback_data="it1")],
        ]
    )