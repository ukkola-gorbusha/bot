from aiogram import types


button1 = types.KeyboardButton(text='Время')
button2 = types.KeyboardButton(text='Мой профиль')
button3 = types.KeyboardButton(text='🔄')
button4 = types.KeyboardButton(text='Покажи лису')
button5 = types.KeyboardButton(text='Помощь')
button6 = types.KeyboardButton(text='Календарь')
button7 = types.KeyboardButton(text='Время')
button8 = types.KeyboardButton(text='Дата')
button9 = types.KeyboardButton(text='Время')
button10 = types.KeyboardButton(text='Число')

keyboard1 = [
    [button4, button2, button5, button10],
    [button8, button1, button6, button3]
]


keyboard2 = [
    [button2]
 

    ]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1,resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2,resize_keyboard=True)

