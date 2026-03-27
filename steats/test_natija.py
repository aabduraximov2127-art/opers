from aiogram.fsm.state import State, StatesGroup

class QuizState(StatesGroup):
    question_index = State()
    score = State()
    
    