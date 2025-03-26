from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def make_row_keyboard(button: list[str]) -> ReplyKeyboardMarkup: 
    row = [KeyboardButton(text=button) for button in button]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


