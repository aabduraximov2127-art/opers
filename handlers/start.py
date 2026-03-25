from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.inline import start_menyu

router=Router()

@router.message(CommandStart())
async def start_handler(msg:Message):
    await msg.answer(f"Assalomu Alekom! Bu OperaBot")
    await msg.answer('Quydagilardan birini tanlang👇',reply_markup=start_menyu())