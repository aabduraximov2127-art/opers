from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.inline import savol1, savol2, savol33, savol14, savol25,start_menyu
from keyboards.reply import savol2ga_otish, savol3ga_otish, savol4ga_otish, savol5ga_otish

router = Router()


@router.callback_query(F.data=='cars1')
async def car1_savol(call: CallbackQuery, state: FSMContext):
    await state.update_data(score=0)
    await call.message.answer("Siz Moshinalarga doir testlarni tanladingiz! Testni boshlaymiz")
    await call.answer()
    await call.message.answer("Agar xato javobni belgilasangiz keyingi savolga o'tishingizni so'rayman, qolgan javoblarni tanlamang!🙏")
    await call.message.answer(
        "1-Savol\nMashinaning yurishi uchun asosiy narsa nima?", 
        reply_markup=savol1()
    )

# 1-savol
@router.callback_query(F.data=="yoqilgi1")
async def savol1_togri(call: CallbackQuery, state: FSMContext):
    await state.update_data(score=lambda s: s + 1)
    await call.message.answer("Tog'ri Javob✅", reply_markup=savol2ga_otish())
    await call.answer()

@router.callback_query(F.data.in_(["suv1","havo1","qum1"]))
async def savol1_xato(call: CallbackQuery):
    await call.message.answer("Xato❌", reply_markup=savol2ga_otish())
    await call.answer()

# 2-savol
@router.message(F.text=='2-savol')
async def savol3(msg: Message):
    await msg.answer("2. Mashinani kim boshqaradi?", reply_markup=savol2())
@router.callback_query(F.data=="haydovchi1")
async def savol2_togri(call: CallbackQuery, state: FSMContext):
    await state.update_data(score=lambda s: s + 1)
    await call.message.answer("Tog'ri Javob✅", reply_markup=savol3ga_otish())
    await call.answer()

@router.callback_query(F.data.in_(["uchuvchi1","haydovchi yordamchisi1","mexanik1"]))
async def savol2_xato(call: CallbackQuery):
    await call.message.answer("Xato❌", reply_markup=savol3ga_otish())
    await call.answer()

# 3-savol
@router.message(F.text=="3-savol")
async def savol3(msg:Message):
    await msg.answer("3. Mashinani to‘xtatish uchun nima bosiladi?",reply_markup=savol33())

@router.callback_query(F.data=="tormoz1")
async def savol3_togri(call: CallbackQuery, state: FSMContext):
    await state.update_data(score=lambda s: s + 1)
    await call.message.answer("Tog'ri Javob✅", reply_markup=savol4ga_otish())
    await call.answer()

@router.callback_query(F.data=="rul1")
async def savol3_xato(call: CallbackQuery):
    await call.message.answer("Xato❌", reply_markup=savol4ga_otish())
    await call.answer()
    
@router.callback_query(F.data=="gaz1")
async def savol3_xato(call: CallbackQuery):
    await call.message.answer("Xato❌", reply_markup=savol4ga_otish())
    await call.answer()

@router.callback_query(F.data=="signal1")
async def savol3_xato(call: CallbackQuery):
    await call.message.answer("Xato❌", reply_markup=savol4ga_otish())
    await call.answer()
# 4-savol
@router.message(F.text=='4-savol')
async def savol4(msg: Message):
    await msg.answer("4. Mashinada tezlikni oshirish uchun nima bosiladi?", reply_markup=savol14())


@router.callback_query(F.data=="gaz2")
async def savol4_togri(call: CallbackQuery, state: FSMContext):
    await state.update_data(score=lambda s: s + 1)
    await call.message.answer("Tog'ri Javob✅", reply_markup=savol5ga_otish())
    await call.answer()

@router.callback_query(F.data.in_(["tormoz2","debriyaj1","signal2"]))
async def savol4_xato(call: CallbackQuery):
    await call.message.answer("Xato❌", reply_markup=savol5ga_otish())
    await call.answer()

# 5-savol
@router.message(F.text=='5-savol')
async def savol5(msg: Message):
    await msg.answer("5. Mashinaning yo‘nalishini nima o‘zgartiradi?", reply_markup=savol25())

@router.callback_query(F.data=="rul")
async def savol5_togri(call: CallbackQuery, state: FSMContext):
    await state.update_data(score=lambda s: s + 1)
    data = await state.get_data()
    total = data.get("score", 0)
    await call.message.answer(f"Test yakunlandi! 🎉",reply_markup=start_menyu())
    await call.answer()

@router.callback_query(F.data.in_(["oyna1","eshik1","tablo1"]))
async def savol5_xato(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    total = data.get("score", 0)
    await call.message.answer(f"Test yakunlandi! 🎉✅", reply_markup=start_menyu())
    await call.answer()