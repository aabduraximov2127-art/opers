# natija/natija.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton


router = Router()


user_scores = {

}


def natija_btn():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📊 Natijani ko‘rish", callback_data="natija_kor")]
    ])


def yonalishlar():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚗 Cars Test", callback_data="cars1")],
        [InlineKeyboardButton(text="📚 History Test", callback_data="history1")]
    ])


@router.callback_query(F.data == "natija_kor")
async def show_result(call: CallbackQuery):
    user_id = call.from_user.id
    scores = user_scores.get(user_id, {"cars": 0, "history": 0})

    cars_score = scores.get("cars", 0)
    history_score = scores.get("history", 0)

    def get_result(score):
        if score == 5:
            return "🔥 Zo‘r!"
        elif score >= 3:
            return "👍 Yaxshi!"
        else:
            return "📚 Yana mashq qil!"

    result_text = (
        f"🚗 Cars Test: {cars_score}/5 - {get_result(cars_score)}\n"
        f"📚 History Test: {history_score}/5 - {get_result(history_score)}"
    )

    await call.message.answer(
        f"📊 Sizning natijalaringiz:\n\n{result_text}\n\nYana test ishlamoqchimisiz? 👇",
        reply_markup=yonalishlar()
    )


    user_scores.pop(user_id, None)
    await call.answer()