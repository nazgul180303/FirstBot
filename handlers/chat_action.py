from aiogram import types,Dispatcher

from config import GROUP_ID, bot
from database.sql_commands import Database

async def echo(message:types.Message):
    print(message.chat.id)
    bad_word = ['damm', ]
    if message.chat.id in GROUP_ID:
        for word in bad_word:
            if word in message.text.lower():
                ban_users = Database().sql_select_command()
                print(ban_users)
                if ban_users and ban_users[0][2] >= 3:
                    print('kek')
                    await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                if ban_users:
                    Database().sql_update_count_command(telegram_id=message.from_user.id)
                else:
                    Database().sql_insert_ban_user_query(telegram_id=message.from_user.id)

                await bot.delete_message(chat_id=message.chat.id,
                                         message_id=message.message_id)
                await message.answer('НЕ ПИШИ ПЛОХИЕ СЛОВА')
def register_chat_action_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)