from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def it_savol1():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A) Kompyuter", callback_data="it9")],
        [InlineKeyboardButton(text="B) Stol", callback_data="it2")],
        [InlineKeyboardButton(text="C) Kitob", callback_data="it3")],
        [InlineKeyboardButton(text="D) Lampochka", callback_data="it4")],
    ])

def it_savol2():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A) Windows", callback_data="win")],
        [InlineKeyboardButton(text="B) Stol", callback_data="stol")],
        [InlineKeyboardButton(text="C) Kitob", callback_data="kitob")],
        [InlineKeyboardButton(text="D) Lampa", callback_data="lampa")],
    ])

def it_savol3():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A) Internet", callback_data="net")],
        [InlineKeyboardButton(text="B) Oyna", callback_data="oyna")],
        [InlineKeyboardButton(text="C) Choy", callback_data="choy")],
        [InlineKeyboardButton(text="D) Stol", callback_data="stol2")],
    ])

def it_savol4():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A) Klaviatura", callback_data="keyboard")],
        [InlineKeyboardButton(text="B) Stol", callback_data="stol3")],
        [InlineKeyboardButton(text="C) Kitob", callback_data="kitob2")],
        [InlineKeyboardButton(text="D) Lampa", callback_data="lampa2")],
    ])

def it_savol5():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A) Mouse", callback_data="mouse")],
        [InlineKeyboardButton(text="B) Stol", callback_data="stol4")],
        [InlineKeyboardButton(text="C) Kitob", callback_data="kitob3")],
        [InlineKeyboardButton(text="D) Lampa", callback_data="lampa3")],
    ])

def natija_btn():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📊 Natijani ko‘rish", callback_data="natija_it")]
    ])

def yonalishlar():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚗 Cars Test", callback_data="cars1")],
        [InlineKeyboardButton(text="📚 History Test", callback_data="history1")]
    ])