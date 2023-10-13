import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database


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
        text=f'Доброго времени суток мои тестировщика бота',
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
