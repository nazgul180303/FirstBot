from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentType

from config import bot
from database.sql_commands import Database


class FSMAnketa(StatesGroup):
    name = State()
    age = State()
    bio = State()
    hobby = State()
    photo = State()


async def start_anketa(message: types.Message):
    await FSMAnketa.name.set()
    await message.answer('Напите ваше имя?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAnketa.next()
    await message.answer('Укажите возраст?')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMAnketa.next()
    await message.answer('Расскажите про себя?')


async def load_bio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
    await FSMAnketa.next()
    await message.answer('Какие у вас хобби?')


async def load_hobby(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text
    await FSMAnketa.next()
    await message.answer('Ваше фото')


async def load_photo(message: types.Message, state: FSMContext):
    photo = await message.photo[-1].download(destination_dir='C:/Users/User/PycharmProjects/FirstBot/media')
    async with state.proxy() as data:
        data['photo'] = photo.name
    Database().sql_insert_anketa_command(
        name=data['name'],
        age= data['age'],
        bio = data['bio'],
        photo= data['photo'],
        hobby=data['hobby'],

    )
    await message.answer('Вы сохранены в анкету')

def register_fsm_anketa_handlers(dp: Dispatcher):
    dp.register_message_handler(start_anketa, commands=['anketa'])
    dp.register_message_handler(load_name, state=FSMAnketa.name, content_types=['text'])
    dp.register_message_handler(load_age, state=FSMAnketa.age, content_types=['text'])
    dp.register_message_handler(load_bio, state=FSMAnketa.bio, content_types=['text'])
    dp.register_message_handler(load_hobby, state=FSMAnketa.hobby, content_types=['text'])
    dp.register_message_handler(load_photo, state=FSMAnketa.photo, content_types=['photo'])