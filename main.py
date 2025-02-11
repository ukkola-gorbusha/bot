import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from datetime import datetime
import asyncio
import config
import locale
import calendar
from keyboards import kb1, kb2
from random_fox import fox
from random import randint






# Ваш токен бота
TOKEN = config.token


# логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хэндлер для команды /start
@dp.message(Command("start"))
@dp.message(F.text == '🔄')
async def start_handler(message: Message):
    await message.reply("Выбери опцию")
    await message.answer("\u2B07,\u2B07,\u2B07",reply_markup=kb1)




# Хэндлер для команды /user
@dp.message(Command("user"))
@dp.message(F.text == 'Мой профиль')
async def user_handler(message: Message):
    user_info = (
        f"Ваше имя: {message.from_user.full_name}\n"
        f"Ваш ID: {message.from_user.id}\n"
        f"Ваше имя пользователя: @{message.from_user.username if message.from_user.username else 'отсутствует'}"
    )
    await message.reply(user_info)

#  Хэндлер для команды /help
@dp.message(Command("help"))
@dp.message(F.text == 'Помощь')
async def help_handler(message: Message):
    help_text = (
        "🛠 *Вот что я могу для вас сделать:*\n"
        "📌 /user - _показать информацию о вашем профиле_\n"
        "📌 /time - _показать время_\n"
        "📌 /date - _показать дату_\n"
        "📌 /calendar - показать календарь\n"
        "📌 /info - _показать информацию о боте_\n"
        "🎉 Спасибо, что используете меня!!"
    )
    await message.reply(help_text, parse_mode="Markdown")


# Функция для создания календаря с выделением текущего дня
def get_calendar_with_highlight():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # Генерация календаря
    cal = calendar.TextCalendar(calendar.MONDAY)
    lines = cal.formatmonth(year, month).split("\n")  # Разбиваем календарь на строки

    highlighted_calendar = []
    for line in lines:
        # Ищем текущий день в строках календаря
        if f"{day:2}" in line:
            # Заменяем текущий день на выделенную версию (например, с `*`)
            line = line.replace(f"{day:2}", f"[{day:02}]")
        highlighted_calendar.append(line)

    # Собираем календарь обратно в текст
    return f"📅 Календарь на {calendar.month_name[month]} {year}:\n```\n" + "\n".join(highlighted_calendar) + "\n```"

# Хэндлер для команды /calendar
@dp.message(Command("calendar"))
@dp.message(F.text == 'Календарь')
async def calendar_handler(message: Message):
    calendar_output = get_calendar_with_highlight()
    await message.reply(calendar_output, parse_mode="Markdown")




# Хэндлер для команды /time
@dp.message(Command("time"))
@dp.message(F.text == 'Время')
async def time_handler(message: Message):
    # Получаем текущее время сервера
    current_time = datetime.now().strftime('%H:%M:%S')
    await message.reply(f"🕒 `Текущее время: {current_time}`", parse_mode="Markdown")

    

# Хэндлер для команды /about
@dp.message(Command("info"))
@dp.message(F.text == 'Инфо')
async def info_handler(message: Message):
    bot_info = (
        "🤖 *О боте*\n\n"
        "Привет! Я бот, созданный для демонстрации функционала в рамках обучения.\n\n"
        "🔧 *Возможности:*\n"
        "- Отправка информации о пользователе.\n"
        "- Отображение текущего времени.\n"
        "- Отображение текущей даты.\n\n"
        "📌 *Создатель:*\n"
        "Этот бот был разработан для учебных целей. "
        "Если у вас есть вопросы или предложения, пишите разработчику @IMEIZ.\n\n"
        "Спасибо за использование бота! 😊"
    )
    await message.reply(bot_info, parse_mode="Markdown")



# Устанавливаем локаль для отображения месяца на русском
locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')

# Словарь с названиями месяцев в родительном падеже
months_genitive = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}

# Хэндлер для команды /date
@dp.message(Command("date"))
@dp.message(F.text == 'Дата')
async def date_handler(message: Message):
    # Получаем текущую дату
    now = datetime.now()
    # Форматируем дату с использованием словаря
    current_date = f"{now.day} {months_genitive[now.month]} {now.year}"
    # Отправляем сообщение
    await message.reply(f"📅 `Сегодня: {current_date}`", parse_mode="Markdown")


#Хендлер на команду /fox
@dp.message(Command("fox"))
@dp.message(Command("Лиса"))
@dp.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Дeржи лису,{name}')
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)
  

@dp.message(F.text.lower() == 'число')
async def send_random(message: types.Message):
   number = randint(1,10)
   await message.answer_dice(emoji="🎲")
   await message.answer(f"{number}")
   
   



#Хэндлер для сообщеий
@dp.message(F.text)
async def msg_echo(message: types.Message):
     msg_user = message.text
     name = message.chat.first_name
     if "Привет" in msg_user:
       await message.answer(f'Привет, {name}')
     elif "Пока" in msg_user:
      await message.answer(f'пока, {name}')
     elif "Ты кто?" in msg_user:
      await message.answer_dice(emoji="🎲")
     elif "лиса" == msg_user:
      await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb1)
     else:
      await message.answer(f'Я не знаю такого слова')
    


    
    

# Хэндлер для эхо-ответа
@dp.message()
async def echo_handler(message: Message):
    await message.reply(message.text)

# Основная точка входа
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

