from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
DESTINATION = '/Users/User/PycharmProjects/FirstBot'
dp = Dispatcher(bot=bot, storage=storage)
GROUP_ID = [-4014883320]