from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def like_notlike():
    markup = InlineKeyboardMarkup()
    like = InlineKeyboardButton(
        'like', callback_data='like'
    )
    dithlike = InlineKeyboardButton(
        'dithlike', callback_data='dithlike'
    )
    markup.add(like, dithlike)
    return markup


async def referance():
    markup = InlineKeyboardMarkup()
    referance_menu = InlineKeyboardButton(
        'Реферальная кнопка', callback_data='reference_menu'
    )
    referance_list = InlineKeyboardButton(
        'Список рефератов', callback_data='reference_list'
    )
    markup.add(referance_menu, referance_list)
    return markup


async def referance_link():
    markup = InlineKeyboardMarkup()
    referance_link = InlineKeyboardButton(
        'reference_link', callback_data='links'
    )
    markup.add(referance_link, )
    return markup
