from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from pyqiwip2p import QiwiP2P

api_key = "Njg3NWNiZjg4YzY4OTYyNjdmM2E4MzFkNmFlZDQ5YzI1ZmI4MmZiMjA0YzI1MzIzODhlZDYifX0="
p2p = QiwiP2P(auth_key=api_key)
bill = p2p.bill(amount=1,lifetime=15)
bill2 = p2p.bill(amount=1,lifetime=15)
link_oplata = bill.pay_url
print(link_oplata)

adk = InlineKeyboardButton('Рассылка')
ad = ReplyKeyboardMarkup(resize_keyboard=True)
ad.add(adk)

adk1 = InlineKeyboardButton('Мужчинам')
adk2 = InlineKeyboardButton('Девушкам')
adk3 = InlineKeyboardButton('Всем')
ad2 = ReplyKeyboardMarkup(resize_keyboard=True)
ad2.add(adk1).add(adk2)

k1 = KeyboardButton('Наши каналы и стикеры')
k2 = KeyboardButton('Задать вопрос')
k3 = KeyboardButton('Private')
k4 = KeyboardButton('Реферальная ссылка')
k5 = KeyboardButton('База данных тест')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(k1).insert(k2).add(k3).insert(k4).add(k5)


op = InlineKeyboardMarkup(row_width=2)
op.add(InlineKeyboardButton(text='Неделя - 80р.',callback_data='o1')).add(
    InlineKeyboardButton(text='Навсегда - 100 р.',callback_data='o2'))

op1 = InlineKeyboardMarkup(row_width=2)
op1.add(InlineKeyboardButton(text='ОПЛАТИТЬ',url=link_oplata)).add(
    InlineKeyboardButton(text='НАЗАД',callback_data='e'))


op4 = InlineKeyboardMarkup(row_width=2)
op4.add(InlineKeyboardButton(text='ОПЛАТИТЬ',callback_data='ppp')).add(
    InlineKeyboardButton(text='НАЗАД',callback_data='e'))

gen = InlineKeyboardMarkup(row_width=2)
gen.add(
    InlineKeyboardButton(text='Мужчина', callback_data='gender_male'),
    InlineKeyboardButton(text='Женщина', callback_data='gender_female'),
)

def buy_menu(isUrl=True,url="",bill=""):
    qiwiMenu = InlineKeyboardMarkup(row_width=2)
    if isUrl:
        btnUrlQIWI = InlineKeyboardMarkup(text='ОПЛАТИТЬ',url=url)
        btnUrlQIWI2 = InlineKeyboardMarkup(text="НАЗАД",callback_data='e')
        qiwiMenu.add(btnUrlQIWI).add(btnUrlQIWI2)

    btnCheckQIWI = InlineKeyboardButton(text="Проверить оплату",callback_data="check_"+bill)
    qiwiMenu.insert(btnCheckQIWI)
    return qiwiMenu

def buy_menu2(isUrl=True,url="",bill=""):
    qiwiMenu = InlineKeyboardMarkup(row_width=2)
    if isUrl:
        btnUrlQIWI = InlineKeyboardMarkup(text='ОПЛАТИТЬ',url=url)
        btnUrlQIWI2 = InlineKeyboardMarkup(text="НАЗАД",callback_data='e')
        qiwiMenu.add(btnUrlQIWI).add(btnUrlQIWI2)

    btnCheckQIWI = InlineKeyboardButton(text="Проверить оплату",callback_data="check_"+bill)
    qiwiMenu.insert(btnCheckQIWI)
    return qiwiMenu