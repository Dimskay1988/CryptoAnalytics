import json
import string

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
    rmk.add(types.KeyboardButton('Зарегистрироваться'), types.KeyboardButton('Использовать данные телеграм'))

    msg = bot.send_message(message.chat.id, 'Для того чтоб продолжить, выберите способ для регистрации',
                           reply_markup=rmk)
    bot.register_next_step_handler(msg, user_register)


def user_register(message):
    if message.text == 'Использовать данные телеграм':
        bot.send_message(message.chat.id,
                         f'Вы зарегистрированы как: {message.from_user.first_name} {message.from_user.last_name}')
        Profile.objects.get_or_create(id_user=message.chat.id, defaults={'name': message.from_user.first_name,
                                                                         'surname': message.from_user.last_name})
    elif message.text == 'Зарегистрироваться':
        msg = bot.send_message(message.chat.id, 'Введите имя пользователя')
        bot.register_next_step_handler(msg, new_user_name)
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
def price(message):
    data = Coins.objects.all()
    coin = ''
    for co in data:
        coin += f'Криптавалюта: {co.name.upper()}, USD={co.usd}, EUR={co.eur}, UAH={co.uah}, CNY={co.cny}\n'
    bot.send_message(message.chat.id, f'Актуальный курс: \n{coin}')


bot.polling(none_stop=True)
