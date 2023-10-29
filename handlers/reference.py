import random
import binascii
import os
from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link
from config import bot
from database.sql_commands import Database
from keyboards.inline_button import referance_link


async def reference_menu(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id,
                           text='Вы вошли в меню реферала',
                           reply_markup=await referance_link())


async def reference_link_call(call: types.CallbackQuery):
    user = Database().sql_select_user_command(telegram_id=call.from_user.id)

    if not user[0][5]:
        token = binascii.hexlify(os.urandom(8)).decode('iso-8859-1')
        link = await _create_link(link_type='start', payload=token)
        print(link)
        Database().sql_insert_reference_link_query(telegram_id=call.from_user.id,
                                                   reference_link=link)
        Database().sql_update_reference_command(link=link, telegram_id=call.from_user.id)
        await bot.send_message(chat_id=call.from_user.id,
                               text='Создано ссылка')
    else:
        await bot.send_message(chat_id=call.from_user.id,
                               text=user[0][5])


async def reference_list(call: types.CallbackQuery):
    user = Database().sql_select_reference_command()
    if user:
        user_list = [list(i) for i in user]
        username = []
        for index, item in enumerate(user_list):
            username.append(item[2])
        link = []
        for index, item in enumerate(user_list):
            link.append(item[5])
        await bot.send_message(chat_id=call.from_user.id,
                               text=f'Список у кого есть рефераты:\n'
                                    f'{username}\n'
                                    f'{link}', )
    else:
        await bot.send_message(chat_id=call.from_user.id,
                               text='реферптов пока нет')


def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(reference_menu, lambda call: call.data == 'reference_menu')
    dp.register_callback_query_handler(reference_link_call, lambda call: call.data == "links")
    dp.register_callback_query_handler(reference_list, lambda call: call.data == 'reference_list')
