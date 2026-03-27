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
