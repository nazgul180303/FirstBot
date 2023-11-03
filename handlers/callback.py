import random
import re

from aiogram import types, Dispatcher

from config import bot
from database.sql_commands import Database
from handlers.scraping.o_kg import ServiceOScrapper
from keyboards.inline_button import like_notlike, save_button
from handlers.scraping.async_scraper import AsyncScraper


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


async def service_o(call: types.CallbackQuery):
    scraper = ServiceOScrapper()
    data = scraper.parse_data()
    links = ServiceOScrapper.PLUS_URL
    for link in data:
        await  bot.send_message(chat_id=call.from_user.id, text=f"Услуги О!:"
                                                                f"\n{links}{link}", reply_markup=await save_button())


async def save_service_call(call: types.CallbackQuery):
    link = re.search(r'(https?://\S+)', call.message.text)
    if link:
        Database().sql_insert_best_servise_commands(owner_telegram_id=call.from_user.id, servise_link=
        link.group(0))

    await bot.send_message(chat_id=call.from_user.id, text="Вы сохранили ссылку")


async def async_service(call: types.CallbackQuery):
    data = await AsyncScraper().async_scrapers()
    links = AsyncScraper.PLUS_URL
    for link in data:
        await  bot.send_message(chat_id=call.from_user.id, text=f"Услуги О!:"
                                                                f"\n{links}{link}", reply_markup=await save_button())


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(random_users_next, lambda call: call.data == 'like' or call.data == 'dithlike')
    dp.register_callback_query_handler(service_o, lambda call: call.data == 'service_o')
    dp.register_callback_query_handler(save_service_call, lambda call: call.data == 'save_service')
    dp.register_callback_query_handler(async_service, lambda call: call.data == 'async_service')
