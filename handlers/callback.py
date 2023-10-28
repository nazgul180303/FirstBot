import random

from aiogram import types, Dispatcher

from config import bot
from database.sql_commands import Database
from keyboards.inline_button import like_notlike


async def random_users_next(message: types.CallbackQuery):
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

def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(random_users_next, lambda call: call.data == 'like' or call.data == 'dithlike')


