import json
import string
import datetime
from django.conf import settings
from apps.Employees.models import Profile
from apps.Coin.models import Coins
from apps.Coin.views import CoinsView
from telebot import types
import telebot

bot = telebot.TeleBot(token=settings.TOKEN)


def registration():
    pass


@bot.message_handler(commands=['start'])
def start(message):
    rmk = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    rmk.add(types.KeyboardButton('Зарегистрироваться'),
            types.KeyboardButton('Зарегистрироваться с ипользованием данных телеграм'),
            types.KeyboardButton('Просмотреть актуальный курс криптовалют'),
            types.KeyboardButton('Отследить на повышение курса'),
            types.KeyboardButton('Отследить на понижение курса'))

    msg = bot.send_message(message.chat.id, 'Выберите что вы хотите сделать',
                           reply_markup=rmk)
    bot.register_next_step_handler(msg, user_message)


def user_message(message):
    if message.text == 'Зарегистрироваться с ипользованием данных телеграм':
        Profile.objects.get_or_create(id_user=message.chat.id, defaults={'name': message.from_user.first_name,
                                                                         'surname': message.from_user.last_name})
        bot.send_message(message.chat.id,
                         f'Вы зарегистрированы как: {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text == 'Зарегистрироваться':
        msg = bot.send_message(message.chat.id, 'Введите имя пользователя')
        bot.register_next_step_handler(msg, new_user_name)
    elif message.text == 'Отследить на повышение курса':
        msg = bot.send_message(message.chat.id, 'Выберите какую валюту хотите отследить')
        bot.register_next_step_handler(msg, coin_price_ap)
    elif message.text == 'Просмотреть актуальный курс криптовалют':
        msg = bot.send_message(message.chat.id, 'Не понтяное')
        bot.register_next_step_handler(msg, coin_price)
    else:
        bot.send_message(message.chat.id, 'Пройдите пожалуйста регистрацию')


def new_user_name(message):
    last_name = message.text
    msg = bot.send_message(message.chat.id, f'Хорошо {last_name} введите вашу фамилию')
    bot.register_next_step_handler(msg, new_last_name, last_name)


def new_last_name(message, last_name):
    first_name = message.text
    Profile.objects.get_or_create(id_user=message.chat.id, defaults={'name': last_name, 'surname': first_name})
    bot.send_message(message.chat.id, f'Отлично, вы зарегистрированы как {last_name} {first_name}')


@bot.message_handler(commands=['coin_price'])
def coin_price(message):
    if Profile.objects.filter(id_user=message.chat.id).exists():
        data = Coins.objects.all()
        coin = ''
        date = ''
        for co in data:
            date = co.created_at
            coin += f'Криптавалюта: {co.name.upper()}, USD={co.usd}, EUR={co.eur}, UAH={co.uah}, CNY={co.cny}\n'
        bot.send_message(message.chat.id, f'Актуальный курс {date}: \n{coin}')
    else:
        msg = bot.send_message(message.chat.id, f'Пройдите пожалуйста регистрацию')
        bot.register_next_step_handler(msg, user_message)


def coin_price_ap(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Litecoin")
    btn2 = types.KeyboardButton("Ethereum")
    btn3 = types.KeyboardButton("Cardano")
    btn4 = types.KeyboardButton("Tether")
    btn5 = types.KeyboardButton("Bitcoin")
    btn6 = types.KeyboardButton("Solana")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    coin_up = message.text
    print(coin_up)
    msg = bot.send_message(message.chat.id, 'Выберите валюту в которой хотите отслеживать', reply_markup=markup)
    currency_ap = message.text
    print(currency_ap)

    # data = Coins.objects.filter(name=coin_up).values(currency_ap).values_list()
    # print(type(data))
    # bot.send_message(message.chat.id, f'Курс {coin_up} = {data} {currency_ap}')


bot.polling(none_stop=True)
