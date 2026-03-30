from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.inline import start_menyu
from keyboards.reply import register

router=Router()

@router.message(CommandStart())
async def start_handler(msg: Message,db):
    if await db.is_user_exists(msg.from_user.id):
        await msg.answer(f'Assalomu Aleykum {msg.from_user.full_name}, Botimizga yozganingizdan xursandmiz!\nSiz avval royxatdan otgansiz ',reply_markup=start_menyu())
    else:
        await msg.answer('Assalomu Alekom botga yozganingizdan xursandmiz\nBotimizni qoiadalariga amal qilgan xolda royhatan otishingizni sorayaman: ')
        await msg.answer('Bot toliq ishlashi uchun Registratsiyadan o\'ting',reply_markup=register())