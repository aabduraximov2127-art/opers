from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.inline import savol1, savol2, savol33, savol14, savol25, start_menyu

router = Router()


@router.callback_query(F.data == 'cars1')
async def start_test(call: CallbackQuery, state: FSMContext):
    await state.update_data(score=0)

    await call.message.answer("🚗 Moshina testi boshlandi!")
    await call.message.answer(
        "1-Savol:\nMashinaning yurishi uchun asosiy narsa nima?",
        reply_markup=savol1()
    )
    await call.answer()


@router.callback_query(F.data.in_(["yoqilgi1","suv1","havo1","qum1"]))
async def q1(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    score = data.get("score", 0)

    if call.data == "yoqilgi1":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    await state.update_data(score=score)

    await call.message.answer(
        "2-Savol:\nMashinani kim boshqaradi?",
        reply_markup=savol2()
    )
    await call.answer()


@router.callback_query(F.data.in_(["haydovchi1","uchuvchi1","haydovchi yordamchisi1","mexanik1"]))
async def q2(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    score = data.get("score", 0)

    if call.data == "haydovchi1":
        score += 1
        await call.message.answer("✅ Togri!")
    else:
        await call.message.answer("❌ Xato")

    await state.update_data(score=score)

    await call.message.answer(
        "3-Savol:\nMashinani to‘xtatish uchun nima bosiladi?",
        reply_markup=savol33()
    )
    await call.answer()


@router.callback_query(F.data.in_(["tormoz1","rul1","gaz1","signal1"]))
async def q3(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    score = data.get("score", 0)

    if call.data == "tormoz1":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    await state.update_data(score=score)

    await call.message.answer(
        "4-Savol:\nMashinada tezlikni oshirish uchun nima bosiladi?",
        reply_markup=savol14()
    )
    await call.answer()


@router.callback_query(F.data.in_(["gaz2","tormoz2","debriyaj1","signal2"]))
async def q4(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    score = data.get("score", 0)

    if call.data == "gaz2":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    await state.update_data(score=score)

    await call.message.answer(
        "5-Savol:\nMashinaning yo'nalishini nima o'zgartiradi?",
        reply_markup=savol25()
    )
    await call.answer()


@router.callback_query(F.data.in_(["rul","oyna1","eshik1","tablo1"]))
async def q5(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    score = data.get("score", 0)

    if call.data == "rul":
        score += 1
        text = "✅ To'g'ri!"
    else:
        text = "❌ Xato"

    
    if score == 5:
        result = "🔥 Qchg'!"
    elif score >= 3:
        result = "👍 Bolad-Ortacha!"
    else:
        result = "📚 Yomon xarakat qil!"

    await call.message.answer(
        f"{text}\n\n📊 Natija: {score}/5\n{result}",
        reply_markup=start_menyu()
    )

    await state.clear()
    await call.answer()