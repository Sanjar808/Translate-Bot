import logging

from random import randint, choice
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
from aiogram.dispatcher.filters import Text
from db_base import Database
from buttons import*
from config import API_TOKEN, admin # API_token va Adminlar ID kodlari


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator = Translator()
db = Database()
db.create_users()
# ________________________________________________________________________________


@dp.message_handler(commands=['start', 'boshlash'])
async def send_welcome(message: types.Message):
    data = db.select_users(message.from_user.id)
    print(f"\nID: {message.from_user.id}\nUsername: {message.from_user.username}\nIsmi: {message.from_user.first_name}\nFamiliyasi: {message.from_user.last_name}")
    if data:
        await message.answer(f"🇺🇿 Assalomu alaykum {message.from_user.first_name}\nTarjima qilish uchun so'z yoki matnni kiriting:\n🇷🇺 Привет {message.from_user.first_name}\nВведите слово или текст для перевода:\n🇺🇸 Hello {message.from_user.first_name}\nEnter a word or text to search:")
    else: 
        tel_id = message.from_user.id 
        name = message.from_user.first_name 
        db.insert_users(tel_id, name)


@dp.message_handler(commands=['users'], user_id=admin)
async def count(message: types.Message):
    data = db.count_users()
    await message.answer(f"Foydalanuvchilar soni: {data[0]} ta")


#________________________________________________________________________________


@dp.message_handler()
async def count(message: types.Message):
    global user_message
    user_message = message.text 
    btn = await lan_buttons()
    await message.answer("🇺🇿 Tilni tanlang:/🇷🇺 Выберите язык:/🇺🇸 Select a language:", reply_markup=btn)

#________________________________________________________________________________

@dp.callback_query_handler(Text(startswith="key_"))
async def translate_person(call: types.CallbackQuery):
    index = call.data.index("_")
    languagee = call.data[index+1:]
    for key, value in language.items():
        if languagee == key:
            translate = translator.translate(user_message, dest = languagee)
            await call.message.answer(translate.text)

#________________________________________________________________________________



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)