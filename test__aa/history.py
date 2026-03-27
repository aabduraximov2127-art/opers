from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.history_knopka.reply import savol1#,savol2,savol3,savol4,savol5
from keyboards.history_knopka.inline import savol11,savol22,savol33,savol44,savol55

router=Router()


@router.callback_query(F.data=='history1')
async def car1_savol(call:CallbackQuery):
    await call.message.answer("Siz Tarixga doir testlarni tanladingiz! Testni boshlatmiz")
    await call.message.answer("Agar xato javobni belgilasangiz keyingi savolga o'tishingizni so'rayman, qolgan javoblarni tanlamang!🙏",reply_markup=savol1())
    await call.answer()
    
@router.message(F.text=="1-savol")
async def savol(msg:Message):
    await msg.answer("1. Qaysi yil “Birinchi Jahon Urushi” boshlandi? ⚔️",reply_markup=savol11())
    
@router.message(F.text=="2-savol")
async def savol2(msg:Message):
    await msg.answer("2. “Amerika Mustaqillik Deklaratsiyasi” qachon qabul qilingan? 🗽",reply_markup=savol22())
    
@router.message(F.text=="3-savol")
async def savol3(msg:Message):
    await msg.answer("3. O‘zbekiston hududida qadimgi Xitoy va Rim savdo yo‘li qanday atalgan? 🏺",reply_markup=savol33())
    
@router.message(F.text=="4-savol")
async def savol4(msg:Message):
    await msg.answre("4. Qaysi shaxs Rossiyada “Bolshevik Inqilobi”ni boshqargan? 🏛️",reply_markup=savol44())
    
@router.message(F.text=="5-savol")
async def savol5(msg:Message):
    await msg.answer("5. Qaysi davlat “Katta Fransuz Inqilobi”ni boshida turgan? 🇫🇷",reply_markup=savol55())
    


    
    
    
