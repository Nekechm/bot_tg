from aiogram import types, Dispatcher
from create_bot import dp, bot,db_conn,db_curr
from keybords.client_kb import kb,op,op1,op4,gen,buy_menu,ad,ad2,buy_menu2
import dbi
from create_bot import BOT_NAME
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
import time
import datetime
from pyqiwip2p import QiwiP2P
import datetime, threading, time
from datetime import timedelta
ADMIN = 5881798988

api_key = "FkNmFlZDQ5YzI1ZmI4MmZiMjA0YzI1MzIzODhlZDYifX0="
p2p = QiwiP2P(auth_key=api_key)
#bill = p2p.bill(amount=1,lifetime=15)
#bill2 = p2p.bill(amount=1,lifetime=15)


class Gender(StatesGroup):
    gender = State()


@dp.message_handler(commands=['start'],state=None)
async def start_com(message:types.Message):
    if message.from_user.id == ADMIN:
        await message.answer('Админ,добро пожаловать',reply_markup=kb)
    else:
        user_id = message.from_user.id
        start_command = message.text
        maybe_referrer_id = str(start_command[7:])
        referrer_id: [str,None] = maybe_referrer_id if maybe_referrer_id != '' else None
        await Gender.gender.set()
        await message.answer('Если вы мужчина введите - 1, женщина - 2')


        if not dbi.user_exists(db_curr,user_id):
            dbi.add_user(db_curr,user_id, referrer_id)

            if referrer_id == str(user_id):
                await bot.send_message(user_id, "Нельзя регистрироваться по собственной ссылке")


    db_conn.commit()

    #await message.answer(f'Бот в работе', reply_markup=kb)

@dp.message_handler(state=Gender.gender)
async def process_gender(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    gender = message.text
    girl = message.from_user.id
    men = message.from_user.id
    if message.text == '1' in message.text:
        dbi.add_men(db_curr,user_id,men)
        dbi.add_girl(db_curr,user_id,gender)
        db_conn.commit()
        await state.finish()
        await message.answer(
            f'Привет! Тут ты можешь купить проходку в приватный канал, задать нам вопрос или просто найти наши каналы и стикеры!',reply_markup=kb)
    elif message.text == '2' in message.text:
        dbi.add_girl(db_curr, user_id,girl)
        await state.finish()
        db_conn.commit()
        await message.answer(
            f'Привет! Тут ты можешь купить проходку в приватный канал, задать нам вопрос или просто найти наши каналы и стикеры!',
            reply_markup=kb)
    else:
        await message.answer(f'Вы не выбрали пол')

async def sub(message:types.Message):
    await message.answer(f'18+ фото: https://t.me/+Vk7DjXwzMLYzMmYy\n\n'
                         f'18+ видео: https://t.me/+XgJOq1GNXuA3ZWQy\n\n'
                         f'18+ стикеры: https://t.me/addstickers/Porn_private1_bot\n\n'
                         f'Хентай стикеры: https://t.me/addstickers/Porn_private1_bot2\n\n')

async def quiz(message:types.Message):
    await message.answer('Напиши свой вопрос или предложение, на него ответят в течении 10 минут.')



@dp.message_handler(commands=['sendallmen'])
async def men_spam(message: types.Message):
    text = message.text[12:]
    mens = dbi.all_users(db_curr)
    for row in mens:
        if not row[0]:
            continue
        try:
            await bot.send_message(row[0], text)
            print(f"Sent message to user {row[0]}")
        except  Exception as e:
            print(f"Error sending message to user {row[0]}: {e}")

@dp.message_handler(commands=['sendallgirl'])
async def girl_spam(message: types.Message):
    text = message.text[12:]
    mens = dbi.girl_spam(db_curr)
    for row in mens:
        if not row[0]:
            continue
        try:
            await bot.send_message(row[0], text)
            print(f"Sent message to user {row[0]}")
        except  Exception as e:
            print(f"Error sending message to user {row[0]}: {e}")

@dp.message_handler(commands=['sendall'])
async def all_spam(message: types.Message):
    text = message.text[12:]
    mens = dbi.all_users(db_curr)
    for row in mens:
        if not row[0]:
            continue
        try:
            await bot.send_message(row[0], text)
            print(f"Sent message to user {row[0]}")
        except  Exception as e:
            print(f"Error sending message to user {row[0]}: {e}")



async def admin_key(message: types.Message):
    await message.answer(f'Кому будет рассылка',reply_markup=ad2)


async def admin_key1(message: types.Message):
    text = message.text[12:]




async def admin_key2(message: types.Message):
    await message.answer()

async def admin_key3(message: types.Message):
    await message.answer()


async def oplata(message:types.Message):
    await message.answer(f'Выбирай тариф (неделя или навсегда) и получай доступ в приватный канал!',reply_markup=op)


@dp.callback_query_handler(text='o1')
async def weak_oplata(callback_query: types.CallbackQuery):
    bill = p2p.bill(amount=1, lifetime=15)
    bill2 = p2p.bill(amount=1, lifetime=15)
    await callback_query.answer()
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f'Тариф:Неделя - 80 р.\n'
                                f'Стоимость:80🇷🇺RUB\n'
                                f'Срок действия:7 дней\n\n'
                                f'Вы получите доступ к следующим ресурсам\n'
                                f'-private (канал)',reply_markup=buy_menu(url=bill.pay_url,bill=bill.bill_id))

def days_to_seconds(days):
    return days * 24 * 60 * 60

@dp.callback_query_handler(lambda c: c.data.startswith('check_'))
async def check(callback: types.CallbackQuery):
    bill = str(callback.data[6:])
    bill_a = p2p.bill(amount=1, lifetime=15)
    info = bill
    user_id = callback.message.from_user.id
    time_sub = str(int(time.time()) + days_to_seconds(7))
    print(time_sub)
    if info != False:
        if str(p2p.check(bill_id=bill).status) == "PAID":
            dbi.set_time_sub(db_curr,user_id,time_sub)
            await bot.send_message(callback.from_user.id,"Вам выдана подписка на неделю")
            #db_conn.commit()
        else:
            await bot.send_message(callback.from_user.id,"Вы не оплатили счет",reply_markup=buy_menu(url = bill_a ,bill=bill))
    else:
        await bot.send_message(callback.from_user.id,"Счет не найден")



@dp.callback_query_handler(text='o2')
async def weak_oplata(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f'Тариф:Навсегда - 100 р.\n'
                                f'Стоимость:100🇷🇺RUB\n'
                                f'Срок действия:бессрочно \n\n'
                                f'Вы получите доступ к следующим ресурсам\n'
                                f'-private (канал)',reply_markup=buy_menu2(url=bill2.pay_url,bill=bill2.bill_id))






@dp.callback_query_handler(text='e')
async def nazad(callback_query: types.CallbackQuery):
    text = (f'Выбирай тариф (неделя или навсегда) и получай доступ в приватный канал!')
    await callback_query.answer()
    await callback_query.message.edit_text(text,reply_markup=op)

@dp.callback_query_handler(text='end')
async def end(callback_query: types.CallbackQuery):
    text = (f'Тариф:Неделя - 80 р.\n'
            f'Стоимость:80🇷🇺RUB\n'
            f'Срок действия:7 дней\n\n'
            f'Вы получите доступ к следующим ресурсам\n'
            f'-private (канал)')
    await callback_query.message.edit_text(text,reply_markup=op1)

class Polia(StatesGroup):
    timee = State()


@dp.message_handler(commands=['test'],state=None)
async def start_com(message:types.Message):
    await Polia.timee.set()
    await message.answer('Введи время')


@dp.message_handler(state=Polia.timee)
async def test(messge: types.Message, state: FSMContext):
    time_sub = messge.text
    user_id = messge.from_user.id
    dbi.set_time_sub(db_curr,user_id,time_sub)
    db_conn.commit()
    await state.finish()


async def ref(message: types.Message):
    ref_count = dbi.count_referals(db_curr, message.from_user.id)
    user_id = message.from_user.id
    time_sub = int(time.time()) + days_to_seconds(7)
    await bot.send_message(message.from_user.id,f'https://t.me/{BOT_NAME}?start={message.from_user.id}\n'
                                                f'Количество приглашенных пользователей: {ref_count}')
    if {ref_count} == 30:
        dbi.set_time_sub(db_curr,user_id,time_sub)
        await message.answer("Поздравляем! Вам выдана подписка на неделю")




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(sub,text='Наши каналы и стикеры')
    dp.register_message_handler(quiz,text='Задать вопрос')
    dp.register_message_handler(oplata,text='Private')
    dp.register_message_handler(ref,text='Реферальная ссылка')
    dp.register_message_handler(admin_key, text='Рассылка')
    dp.register_message_handler(admin_key1,text='Мужчинам')
    dp.register_message_handler(admin_key2, text='Девушкам')
    dp.register_message_handler(admin_key3, text='Всем')
    #dp.register_message_handler(test, text='База данных тест')

