import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from datetime import datetime
import asyncio
import config
import locale
import calendar
from keyboards.keyboards import kb1, kb2
from utils.random_fox import fox
from random import randint
from handlers import common, career_choice

 



# Ваш токен бота
TOKEN = config.token


# логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(common.router)
#dp.include_router(career_choice.router)


# Основная точка входа
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

