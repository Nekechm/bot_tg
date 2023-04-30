from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.files import JSONStorage
from dbi import create_sqlite_db_conn
import os

TOKEN = ''
BOT_NAME = 'RG_All_bot'



db_conn = create_sqlite_db_conn('database.db')
db_curr = db_conn.cursor()


#storage = JSONStorage('fsms.json')
storage=MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

