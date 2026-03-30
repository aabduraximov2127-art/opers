from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards.history_knopka.inline import savol11, savol22, savol33, savol44, savol55

router = Router()
user_scores = {}


@router.callback_query(F.data == 'history1')
async def car1_savol(call: CallbackQuery):
    user_scores[call.from_user.id] = 0

    await call.message.answer("Siz Tarix testini tanladingiz 📚")
    await call.message.answer(
        "1. Qaysi yil “Birinchi Jahon Urushi” boshlandi? ⚔️",
        reply_markup=savol11()
    )
    await call.answer()


@router.callback_query(F.data.in_(["191","192","190","193"]))
async def q1(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, 0)

    if call.data == "191":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id] = score

    await call.message.answer(
        "2. “Amerika Mustaqillik Deklaratsiyasi” qachon qabul qilingan? 🗽",
        reply_markup=savol22()
    )
    await call.answer()


@router.callback_query(F.data.in_(["177","178","180","175"]))
async def q2(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, 0)

    if call.data == "177":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id] = score

    await call.message.answer(
        "3. Qadimgi savdo yo‘li qanday atalgan? 🏺",
        reply_markup=savol33()
    )
    await call.answer()


@router.callback_query(F.data.in_(["qimmat","ipak1","savdo","sultan1"]))
async def q3(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, 0)

    if call.data == "ipak1":
        score += 1
        await call.message.answer("✅ To'g'ri!!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id] = score

    await call.message.answer(
        "4. Qaysi shaxs Bolshevik Inqilobini boshqargan? 🏛️",
        reply_markup=savol44()
    )
    await call.answer()


@router.callback_query(F.data.in_(["peter","joseph","nicholas1","vladimer1"]))
async def q4(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, 0)

    if call.data == "vladimer1":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id] = score

    await call.message.answer(
        "5. Katta Fransuz inqilobi qaysi davlatda bo‘lgan? 🇫🇷",
        reply_markup=savol55()
    )
    await call.answer()


@router.callback_query(F.data.in_(["ispaniya1","angliya1","fransiya1","germaniya1"]))
async def q5(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, 0)

    if call.data == "fransiya1":
        score += 1
        text = "✅ To'g'ri!"
    else:
        text = "❌ Xato"


    if score == 5:
        result = "🔥 Zo‘r!"
    elif score >= 3:
        result = "👍 Yaxshi!"
    else:
        result = "📚 Yana o‘rganing!"

    await call.message.answer(f"{text}\n\n📊 Natija: {score}/5\n{result}")

    user_scores.pop(user_id, None)
    await call.answer()