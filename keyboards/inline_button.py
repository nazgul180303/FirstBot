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
    service_button = InlineKeyboardButton(
        'услуги О!', callback_data='service_o'
    )
    async_service_button = InlineKeyboardButton(
        'быстрые услуги О!', callback_data='async_service'
    )
    markup.add(referance_menu, referance_list)
    markup.add(service_button, async_service_button)
    return markup


async def referance_link():
    markup = InlineKeyboardMarkup()
    referance_link = InlineKeyboardButton(
        'reference_link', callback_data='links'
    )
    markup.add(referance_link, )
    return markup


async def save_button():
    markup = InlineKeyboardMarkup()
    save_service = InlineKeyboardButton(
        'Сохранить', callback_data='save_service'
    )
    markup.add(save_service)
    return markup
