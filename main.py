import logging

from aiogram import executor
from create_bot import dp,db_conn,db_curr
from handlers import client

logging.basicConfig(level='INFO')

async def on_startup(_):
    logging.info('Бот в онлайне')

async def on_shutdown(_):
    logging.info('Завершаем работу бота')
    db_conn.close()




client.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=False, on_startup=on_startup, on_shutdown=on_shutdown)

