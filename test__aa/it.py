from aiogram import Router, F
from aiogram.types import CallbackQuery,InlineKeyboardButton,InlineKeyboardMarkup
from keyboards.it_keyboard.inline import it_savol1,it_savol2,it_savol3,it_savol4,it_savol5,natija_btn

router = Router()


user_scores = {} 




@router.callback_query(F.data == "it1")
async def start_it(call: CallbackQuery):
    user_scores[call.from_user.id] = {"it": 0}

    await call.message.answer("💻 IT testi boshlandi!")
    await call.message.answer(
        "1. Qaysi narsa kompyuter hisoblanadi?",
        reply_markup=it_savol1()
    )
    await call.answer()


@router.callback_query(F.data.in_(["it9","it2","it3","it4"]))
async def q1(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, {"it": 0})["it"]

    if call.data == "it9":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id]["it"] = score

    await call.message.answer(
        "2. Qaysi operatsion tizim kompyuterlarda ishlaydi?",
        reply_markup=it_savol2()
    )
    await call.answer()


@router.callback_query(F.data.in_(["win","stol","kitob","lampa"]))
async def q2(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, {"it": 0})["it"]

    if call.data == "win":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id]["it"] = score

    await call.message.answer(
        "3. Qaysi narsa internetga ulanadi?",
        reply_markup=it_savol3()
    )
    await call.answer()


@router.callback_query(F.data.in_(["net","oyna","choy","stol2"]))
async def q3(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, {"it": 0})["it"]

    if call.data == "net":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id]["it"] = score

    await call.message.answer(
        "4. Qaysi narsa kompyuterga yozuv kiritish uchun ishlatiladi?",
        reply_markup=it_savol4()
    )
    await call.answer()


@router.callback_query(F.data.in_(["keyboard","stol3","kitob2","lampa2"]))
async def q4(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, {"it": 0})["it"]

    if call.data == "keyboard":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id]["it"] = score

    await call.message.answer(
        "5. Qaysi narsa kursorni harakatlantiradi?",
        reply_markup=it_savol5()
    )
    await call.answer()


@router.callback_query(F.data.in_(["mouse","stol4","kitob3","lampa3"]))
async def q5(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, {"it": 0})["it"]

    if call.data == "mouse":
        score += 1
        await call.message.answer("✅ To'g'ri!")
    else:
        await call.message.answer("❌ Xato")

    user_scores[user_id]["it"] = score

    await call.message.answer(
        "Test tugadi! 📊 Natijani ko'rish uchun tugmani bosing 👇",
        reply_markup=natija_btn()
    )
    await call.answer()


@router.callback_query(F.data == "natija_it")
async def show_it_result(call: CallbackQuery):
    user_id = call.from_user.id
    score = user_scores.get(user_id, {"it": 0})["it"]

    if score == 5:
        result = "🔥 Zo'r!"
    elif score >= 3:
        result = "👍 Yaxshi!"
    else:
        result = "📚 Yana mashq qil!"

    await call.message.answer(
        f"💻 IT Test Natijasi: {score}/5 - {result}\n\nYana test ishlamoqchimisiz? 👇",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🚗 Cars Test", callback_data="cars1")],
            [InlineKeyboardButton(text="📚 History Test", callback_data="history1")]
        ])
    )

    user_scores.pop(user_id, None)
    await call.answer()