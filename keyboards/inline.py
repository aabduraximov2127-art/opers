from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def start_menyu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🚗Car',callback_data="cars1")],
            [InlineKeyboardButton(text="🗼History",callback_data="history1")],
            [InlineKeyboardButton(text='🧑‍💻IT',callback_data="it1")],
        ]
    )

def savol1():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='A) Suv',callback_data="suv1")],
            [InlineKeyboardButton(text="B) Havo",callback_data="havo1")],
            [InlineKeyboardButton(text='C) Yoqilg‘i',callback_data="yoqilgi1")],
            [InlineKeyboardButton(text="D) Qum",callback_data="qum1")]
        ]
    )



def savol2():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Haydovchi", callback_data="haydovchi1")],
        [InlineKeyboardButton(text="Mexanik", callback_data="mexanik1")],
        [InlineKeyboardButton(text="Uchuvchi", callback_data="uchuvchi1")],
        [InlineKeyboardButton(text="Haydovchi yordamchisi", callback_data="haydovchi yordamchisi1")],
        
    ])


def savol33():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='A) Tormoz',callback_data="tormoz1")],
            [InlineKeyboardButton(text="B) Gaz",callback_data="gaz1")],
            [InlineKeyboardButton(text='C) Signal',callback_data="signal1")],
            [InlineKeyboardButton(text="D) Rul",callback_data="rul1")]
        ]
    )

def savol14():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='A) Tormoz',callback_data="tormoz2")],
            [InlineKeyboardButton(text="B)Debriyaj",callback_data="debriyaj1")],
            [InlineKeyboardButton(text='C) Signal',callback_data="signal2")],
            [InlineKeyboardButton(text="D) Gaz",callback_data="gaz2")]
        ]
    )

def savol25():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='A) Oyna',callback_data="oyna")],
            [InlineKeyboardButton(text="B) Rul",callback_data="rul")],
            [InlineKeyboardButton(text='C) Eshik',callback_data="eshik1")],
            [InlineKeyboardButton(text="D) Tablo",callback_data="tablo1")]
        ]
    )