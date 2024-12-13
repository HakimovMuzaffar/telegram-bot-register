from aiogram import Bot,Dispatcher,executor
from aiogram.types import Message
from keyboards import *
from database import *
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN, parse_mode='HTML')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f'Salom <b>{full_name}</b> botga xush kelibsiz!')
    await register_user(message)


async def register_user(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    user = first_name_user(chat_id)
    if user:
        await message.answer(f'Xush kelibsiz {full_name} 😎')
    else:
        first_register_user(chat_id,full_name)
        await message.answer("Ro'yxatdan o'tishingiz uchun kontaktingizni jo'nating 📲", reply_markup=phone_button())


@dp.message_handler(content_types=['contact'])
async def finish_register(message: Message):
    chat_id = message.chat.id
    phone = message.contact.phone_number
    update_user_to_finish_register(chat_id, phone)
    await create_cart_for_user(message)
    await message.answer("Ro'yxatdan mufaqiyatli o'ttingiz ✔")

async def create_cart_for_user(message: Message):
    chat_id = message.chat.id
    try:
        insert_to_cart(chat_id)
    except:
        pass


executor.start_polling(dp)