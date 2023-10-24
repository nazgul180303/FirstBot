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
