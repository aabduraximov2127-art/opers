from aiogram import Router,F
from aiogram.types import Message,CallbackQuery

router=Router()


@router.callback_query(F.data=='cars1')
async def car1_savol(call:CallbackQuery):
    await call.message.answer("Siz Moshinalarga doir testlarni tanladingiz! Testni boshlatmiz")
    await call.answer()