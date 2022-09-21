import json
import string
from datetime import datetime, date, time
from django.conf import settings
from apps.Employees.models import Profile, MessageProfile
from apps.Coin.models import Coins
from apps.Coin.views import CoinsView
from telebot import types
import telebot
import time

bot = telebot.TeleBot(token=settings.TOKEN)


def registration():
    pass


@bot.message_handler(commands=['start'])
def start(message):
    rmk = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    rmk.add(types.KeyboardButton('Зарегистрироваться'),
            types.KeyboardButton('Зарегистрироваться с ипользованием данных телеграм'),
            types.KeyboardButton('Просмотреть актуальный курс криптовалют'),
            types.KeyboardButton('Выбрать криптовалюту и валюту'),
            types.KeyboardButton('HitGab'))
    msg = bot.send_message(message.chat.id, 'Выберите что вы хотите сделать', reply_markup=rmk)
    bot.register_next_step_handler(msg, user_reply)


def user_reply(message):
    if message.text == 'Зарегистрироваться с ипользованием данных телеграм':
        Profile.objects.update_or_create(id_user=message.chat.id, defaults={'name': message.from_user.first_name,
                                                                            'surname': message.from_user.last_name})
        bot.send_message(message.chat.id,
                         f'Вы зарегистрированы как: {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text == 'Зарегистрироваться':
        msg = bot.send_message(message.chat.id, 'Введите имя пользователя')
        bot.register_next_step_handler(msg, new_user_name)
    elif message.text == 'Выбрать криптовалюту и валюту':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Litecoin")
        btn2 = types.KeyboardButton("Ethereum")
        btn3 = types.KeyboardButton("Cardano")
        btn4 = types.KeyboardButton("Tether")
        btn5 = types.KeyboardButton("Bitcoin")
        btn6 = types.KeyboardButton("Solana")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        msg = bot.send_message(message.chat.id, 'Выберите криптовалюту', reply_markup=markup)
        bot.register_next_step_handler(msg, choice_cryptocurrency)
    elif message.text == 'Просмотреть актуальный курс криптовалют':
        msg = bot.send_message(message.chat.id, 'ввести симввол')
        bot.register_next_step_handler(msg, coin_price)
    elif message.text == 'HitGab':
        bot.send_message(message.chat.id, 'https://github.com/Dimskay1988/CryptoAnalytics')
    else:
        bot.send_message(message.chat.id, 'Пройдите пожалуйста регистрацию')


def new_user_name(message):
    last_name = message.text
    msg = bot.send_message(message.chat.id, f'Хорошо {last_name}, введите вашу фамилию')
    bot.register_next_step_handler(msg, new_last_name, last_name)


def new_last_name(message, last_name):
    first_name = message.text
    Profile.objects.update_or_create(id_user=message.chat.id, defaults={'name': last_name, 'surname': first_name})
    msg = bot.send_message(message.chat.id, f'Отлично, вы зарегистрированы как {last_name} {first_name}')
    bot.register_next_step_handler(msg, start)  # хз может и не надо


def coin_price(message):
    if Profile.objects.filter(id_user=message.chat.id).exists():
        data = Coins.objects.all()
        coin = ''
        for co in data:
            dat = co.updated_at.date()
            tim = str(co.updated_at.time()).split('.')
            coin += f'Криптавалюта: {co.name.upper()}, USD={co.usd}, EUR={co.eur}, UAH={co.uah}, CNY={co.cny}\n'
        msg = bot.send_message(message.chat.id, f'Актуальный курс {dat} {tim[0]}: \n{coin}')
        bot.register_next_step_handler(msg, user_reply)
    else:
        msg = bot.send_message(message.chat.id, f'Пройдите пожалуйста регистрацию')
        bot.register_next_step_handler(msg, user_reply)


def choice_cryptocurrency(message):
    currency = message.text
    bot.send_message(message.chat.id, f'Вы выбрали {currency}')
    if (currency.lower()) in ['bitcoin', 'litecoin', 'ethereum', 'solana', 'cardano', 'tether']:
        rmk = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("USD")
        btn2 = types.KeyboardButton("EUR")
        btn3 = types.KeyboardButton("UAH")
        btn4 = types.KeyboardButton("CNY")
        rmk.add(btn1, btn2, btn3, btn4)
        msg = bot.send_message(message.chat.id, f'Выберете валюту', reply_markup=rmk)
        bot.register_next_step_handler(msg, coin, currency)
    else:
        bot.send_message(message.chat.id, "Выберите из списка выше")


def coin(message, currency):
    coin = message.text
    if (coin.lower()) in ['usd', 'eur', 'uah', 'cny']:
        bot.send_message(message.chat.id, f'Вы выбрали {currency} в {coin}')
        data = Coins.objects.filter(name=(currency.lower())).values((coin.lower()))
        well = ''
        for i in data:
            well += str(i[f'{coin.lower()}'])
        profil = Profile.objects.filter(id_user=message.chat.id)
        MessageProfile.objects.create(id_profile=profil[0], coin=coin, currency=currency, price=well)
        bot.send_message(message.chat.id, f'Актуальный курс {currency} {well} {coin.upper()}')
        rmk = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Получать актуальный курс выброной валюты")
        # btn2 = types.KeyboardButton("прислать уведомление когда курс выростет")
        # btn3 = types.KeyboardButton("Прислать уведомление когда курс станет ниже")
        rmk.add(btn1) ### rmk.add(btn1, btn2, btn3)
        msg = bot.send_message(message.chat.id, f'Выберете действие', reply_markup=rmk)
        bot.register_next_step_handler(msg, task, coin, currency)
    else:
        bot.send_message(message.chat.id, f'Вы не правильно выбрали валюту')


def task(message, coin, currency):
    while True:
        time.sleep(60)
        ikm = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("СТОП", callback_data='stop')
        ikm.add(button1)

        profil = Profile.objects.filter(id_user=message.chat.id).values()
        well_message = MessageProfile.objects.filter(id_profile=profil[0]['id'])
        wel_price = (float(well_message.values().order_by('-id')[:1][0]['price']))

        well_coin = Coins.objects.filter(name=(currency.lower())).values((coin.lower()))
        wel = (float(well_coin[0][f'{coin.lower()}']))
        if wel_price > wel:
            bot.send_message(message.chat.id, f' ⬇️  Курс 1 {currency} = {wel} {coin}', reply_markup=ikm)
            profil = Profile.objects.filter(id_user=message.chat.id)
            MessageProfile.objects.create(id_profile=profil[0], coin=coin, currency=currency, price=wel)
        elif wel_price == wel:
            bot.send_message(message.chat.id, f' 🟰️  Курс 1 {currency} = {wel} {coin}', reply_markup=ikm)
        else:
            bot.send_message(message.chat.id, f' ⬆️️  Курс 1 {currency} = {wel} {coin}', reply_markup=ikm)
            profil = Profile.objects.filter(id_user=message.chat.id)
            MessageProfile.objects.create(id_profile=profil[0], coin=coin, currency=currency, price=wel)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'stop':
            bot.send_message(call.message.chat.id, f'Cтоп бот')
            mgs = bot.send_message(call.message.chat.id, f'Выберите что вы хотите сделать')
            bot.register_next_step_handler(mgs, start)


bot.polling(none_stop=True)
