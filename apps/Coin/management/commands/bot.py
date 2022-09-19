import json
import string
from datetime import datetime, date, time
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
            dat = co.created_at.date()
            tim = str(co.created_at.time()).split('.')
            coin += f'Криптавалюта: {co.name.upper()}, USD={co.usd}, EUR={co.eur}, UAH={co.uah}, CNY={co.cny}\n'
        msg = bot.send_message(message.chat.id, f'Актуальный курс {dat} {tim[0]}: \n{coin}')
        bot.register_next_step_handler(msg, user_reply)
    else:
        msg = bot.send_message(message.chat.id, f'Пройдите пожалуйста регистрацию')
        bot.register_next_step_handler(msg, user_reply)


def choice_cryptocurrency(message):
    coin_up = message.text
    bot.send_message(message.chat.id, f'Вы выбрали {coin_up}')
    if (coin_up.lower()) in ['bitcoin', 'litecoin', 'ethereum', 'solana', 'cardano', 'tether']:
        rmk = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("USD")
        btn2 = types.KeyboardButton("EUR")
        btn3 = types.KeyboardButton("UAH")
        btn4 = types.KeyboardButton("CNY")
        rmk.add(btn1, btn2, btn3, btn4)
        msg = bot.send_message(message.chat.id, f'Выберете валюту', reply_markup=rmk)
        bot.register_next_step_handler(msg, choice_coin, coin_up)
    else:
        bot.send_message(message.chat.id, "Выберите из списка выше")


def choice_coin(message, coin):
    currency = message.text
    if (currency.lower()) in ['usd', 'eur', 'uah', 'cny']:
        bot.send_message(message.chat.id, f'Вы выбрали {coin} в {currency}')
        data = Coins.objects.filter(name=(coin.lower())).values((currency.lower()))
        well = ''
        for i in data:
            well += str(i[f'{currency.lower()}'])
        bot.send_message(message.chat.id, f'Актуальный курс {coin} {well} {currency.upper()}')
    else:
        bot.send_message(message.chat.id, f'Вы не правильно выбрали валюту')


bot.polling(none_stop=True)