import sqlite3
import random
from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_button import like_notlike, referance

async def start_button(message: types.Message):
    print(message)
    db = Database()
    db.sql_insert_user_query(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Доброго времени суток мои тестировщика бота', reply_markup= await referance()
    )


async def random_users(message: types.Message):
    users = Database().sql_select_anket_command()

    random_users = random.choice(users)
    response = f'Name: {random_users[1]}\n' \
               f'Age: {random_users[2]}\n' \
               f'Bio: {random_users[3]}\n' \
               f'hobby: {random_users[5]}\n'
    photo_path = random_users[4]
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=response,
                             reply_markup=await like_notlike())


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
    dp.register_message_handler(random_users, commands=['random'], )
