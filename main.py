from aiogram import executor
from config import dp
from handlers import start, chat_action, fsm_anketa, callback
from database.sql_commands import Database


async def onstart_up(_):
    db = Database()
    db.create_tables()

callback.register_callback_handler(dp=dp)
fsm_anketa.register_fsm_anketa_handlers(dp=dp)
start.register_start_handlers(dp=dp)

chat_action.register_chat_action_handlers(dp=dp)
if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=onstart_up
    )
