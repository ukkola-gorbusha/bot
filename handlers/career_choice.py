
from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.keyboards import kb1, kb2
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.prof_keyboards import make_row_keyboard


router = Router()

available_jobs = [
    "Software Engineer",
    "QA Engineer",
    "Product Manager",
    "UX Designer",
    "Data Scientist"
]

available_grades = [
    "Entry Level",
    "Mid Level",
    "Senior Level"

]


class choiceProfile(StatesGroup):
    job = State()
    grade = State()


@router.message(Command("prof"))
async def command_prof(message: types.Message, state: FSMContext):
    user_name = message.chat.id
    await message.answer(
    text="Выберите професcию", 
    reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(choiceProfile.job)

    @router.message(choiceProfile.job, F.text.in_(available_jobs))
    async def prof_chosen_grade(message: types.Message, state: FSMContext):
     await state.update_data(profession=message.text)
     await message.answer(
      text="Выберите уровень", 
      reply_markup=make_row_keyboard(available_grades))
     await state.set_state(choiceProfile.grade)


    @router.message(choiceProfile.job)
    async def prof_chosen(message: types.Message):
     await message.answer(
      text="Выберите професcию", 
      reply_markup=make_row_keyboard(available_jobs))
     
    @router.message(choiceProfile.grade, F.text.in_(available_grades))
    async def grade_chosen(message: types.Message, state: FSMContext):
     user_data = await state.get_data()
     await message.answer(f"Ваша профессия: {user_data['profession']}\n"
                          f"Ваш уровень: {message.text}",
                          reply_markup=types.ReplyKeyboardRemove())
     await state.clear()
    
    @router.message(choiceProfile.grade)
    async def grade_chosen_incorrect(message: types.Message):
     await message.answer(
      text="Выберите уровень", 
      reply_markup=make_row_keyboard(available_grades))
 

     
