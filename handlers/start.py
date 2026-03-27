from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.inline import start_menyu
from keyboards.reply import register

router=Router()

@router.message(CommandStart())
async def start_handler(msg:Message):
    await msg.answer(f"Assalomu Alekom! Bu OperaBot")
    await msg.answer('Birinchi bolib Registratsiyadan otishingizni sorab qolaman,Agar Registratsiyadan otmasangiz botim siz uchun ishlamaydi!👉',reply_markup=register())