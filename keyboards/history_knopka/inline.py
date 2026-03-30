from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


def savol11():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A) 1914",callback_data="191")],
            [InlineKeyboardButton(text="B) 1920",callback_data="192")],
            [InlineKeyboardButton(text="C) 1905",callback_data="190")],
            [InlineKeyboardButton(text="D) 1939",callback_data="193")],
        ]
    )

def savol22():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A) 1776",callback_data="177")],
            [InlineKeyboardButton(text="B) 1789",callback_data="178")],
            [InlineKeyboardButton(text="C) 1804",callback_data="180")],
            [InlineKeyboardButton(text="D) 1750",callback_data="175")],
        ]
    )

def savol33():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A) Qimmatbaho Yo‘l",callback_data="qimmat")],
            [InlineKeyboardButton(text="B) Ipak Yoli",callback_data="ipak1")],
            [InlineKeyboardButton(text="C) Savdo Shosse",callback_data="savdo")],
            [InlineKeyboardButton(text="D) Sultan Yo‘li",callback_data="sultan1")],
        ]
    )

def savol44():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A) Peter I",callback_data="peter")],
            [InlineKeyboardButton(text="B) Joseph Stalin",callback_data="joseph")],
            [InlineKeyboardButton(text="C) Nicholas II",callback_data="nicholas1")],
            [InlineKeyboardButton(text="D) Vladimir Lenin",callback_data="vladimer1")],
        ]
    )

def savol55():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A) Ispaniya",callback_data="ispaniya1")],
            [InlineKeyboardButton(text="B) Angliya",callback_data="angliya1")],
            [InlineKeyboardButton(text="C) Fransiya",callback_data="fransiya1")],
            [InlineKeyboardButton(text="D) Germaniya",callback_data="germaniya1")],
        ]
    )