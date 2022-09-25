from datetime import datetime, date, time
from django.conf import settings
from apps.Employees.models import Profile, MessageProfile
from apps.Coin.models import Coins
from telebot import types
import telebot
import time

bot = telebot.TeleBot(token=settings.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    if Profile.objects.filter(id_telegram=message.chat.id).exists():
        rmk = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        rmk.add(types.KeyboardButton('Просмотреть актуальный курс криптовалют'),
                types.KeyboardButton('Получить актуальный курс криптовалюты'),
                types.KeyboardButton('HitGab'))
        msg = bot.send_message(message.chat.id, 'Выберите что вы хотите сделать', reply_markup=rmk)
        bot.register_next_step_handler(msg, user_reply)
    else:
        bot.send_message(message.chat.id,
                         f'Для того что-бы начать пользоваться, небходимо пройти регистрацию.')
        rmk = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        rmk.add(types.KeyboardButton('Зарегистрироваться'))
        msg = bot.send_message(message.chat.id, 'Пройдите регистрацию', reply_markup=rmk)
        bot.register_next_step_handler(msg, user_reply)


@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(message.chat.id, 'https://t.me/Dimskay1')
    return start(message)


@bot.message_handler(commands=['stats'])
def stats(message):
    profile = Profile.objects.filter(id_telegram=message.chat.id).values()
    bot.send_message(message.chat.id, F'Вы зарегистрованы как {profile[0]["username"]} ')
    return start(message)


def user_reply(message):
    if message.text == 'Зарегистрироваться':
        return new_user(message)
    elif message.text == 'Получить актуальный курс криптовалюты':
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
        return coin_price(message)
    elif message.text == 'HitGab':
        bot.send_message(message.chat.id, 'https://github.com/Dimskay1988/CryptoAnalytics')
        return start(message)
    else:
        return start(message)


def new_user(message):
    msg = bot.send_message(message.chat.id, 'Введите имя пользователя')
    bot.register_next_step_handler(msg, new_username)


def new_username(message):
    username = message.text
    msg = bot.send_message(message.chat.id, f'Хорошо, теперь введите пароль')
    bot.register_next_step_handler(msg, new_password, username)


def new_password(message, username):
    password = message.text
    bot.send_message(message.chat.id, f'Отлично, вы зарегистрированы как {username}')
    Profile.objects.update_or_create(id_telegram=message.chat.id, defaults={'username': username, 'password': password})
    return start(message)


def coin_price(message):
    data = Coins.objects.all()
    coin = ''
    for co in data:
        coin += f'Криптавалюта: {co.name.upper()}, USD={co.usd}, EUR={co.eur}, UAH={co.uah}, CNY={co.cny}\n'
    bot.send_message(message.chat.id, f'{coin}')
    return start(message)


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
        return start(message)


def coin(message, currency):
    coin = message.text
    if (coin.lower()) in ['usd', 'eur', 'uah', 'cny']:
        bot.send_message(message.chat.id, f'Вы выбрали {currency} в {coin}')
        data = Coins.objects.filter(name=(currency.lower())).values((coin.lower()))
        well = ''
        for i in data:
            well += str(i[f'{coin.lower()}'])
        profile = Profile.objects.filter(id_telegram=message.chat.id)
        MessageProfile.objects.create(id_profile=profile[0], coin=coin, currency=currency, price=well,
                                      tracking_status='Start tracking')
        bot.send_message(message.chat.id, f'Актуальный курс {currency} {well} {coin.upper()}')
        return start(message)


# def coin(message, currency):
#     coin = message.text
#     if (coin.lower()) in ['usd', 'eur', 'uah', 'cny']:
#         bot.send_message(message.chat.id, f'Вы выбрали {currency} в {coin}')
#         data = Coins.objects.filter(name=(currency.lower())).values((coin.lower()))
#         well = ''
#         for i in data:
#             well += str(i[f'{coin.lower()}'])
#         profile = Profile.objects.filter(id_telegram=message.chat.id)
#         MessageProfile.objects.create(id_profile=profile[0], coin=coin, currency=currency, price=well,
#                                       tracking_status='Start tracking')
#         bot.send_message(message.chat.id, f'Актуальный курс {currency} {well} {coin.upper()}')
#         rmk = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
#         btn1 = types.KeyboardButton("Получать актуальный курс выбраной валюты")
#         # btn2 = types.KeyboardButton("Получать уведомление только о повышении курса ⬆")
#         # btn3 = types.KeyboardButton("Получать уведомление только о понижении курса ⬇")
#         rmk.add(btn1)  # rmk.add(btn1, btn2, btn3)
#         msg = bot.send_message(message.chat.id, f'Выберете действие', reply_markup=rmk)
#         bot.register_next_step_handler(msg, task, coin, currency)
#     else:
#         bot.send_message(message.chat.id, f'Вы не правильно выбрали валюту')
#         return start(message)
#
#
# def task(message, coin, currency):
#     key = []
#     message_keybord = message.text
#     if message_keybord == "Получать актуальный курс выбраной валюты":
#         key.append(1)
#         bot.send_message(message.chat.id, f'Вам будут приходить уведомления о актуальномм курсе каждую минуту')
#     elif message_keybord == 'Получать уведомление только о повышении курса ⬆':
#         key.append(2)
#         bot.send_message(message.chat.id, f'Вам будут приходить уведомления только когда курс повысится')
#     elif message_keybord == 'Получать уведомление только о понижении курса ⬇':
#         key.append(3)
#         bot.send_message(message.chat.id, f'Вам будут приходить уведомления только когда курс уменьшится')
#     return message_task(message, coin, currency)
#
#
# def message_task(message, coin, currency):
#     profile = Profile.objects.filter(id_telegram=message.chat.id).values()
#     well_message = MessageProfile.objects.filter(id_profile=profile[0]['id'])
#     wel_price = (float(well_message.values().order_by('-id')[:1][0]['price']))  # отслеживаемый курс
#     well_coin = Coins.objects.filter(name=(currency.lower())).values((coin.lower()))
#     wel = (float(well_coin[0][f'{coin.lower()}']))  # актуальный курс
#     prof = Profile.objects.filter(id_telegram=message.chat.id)
#     ikm = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton("СТОП", callback_data='stop')
#     ikm.add(button1)
#     if wel_price > wel:
#         bot.send_message(message.chat.id, f' ⬇ Курс 1 {currency} = {wel} {coin}', reply_markup=ikm)
#         MessageProfile.objects.create(id_profile=prof[0], coin=coin, currency=currency, price=wel,
#                                       tracking_status='Trecking')
#     elif wel_price == wel:
#         bot.send_message(message.chat.id, f' 🟰️ Курс 1 {currency} = {wel} {coin}', reply_markup=ikm)
#     elif wel_price < wel:
#         bot.send_message(message.chat.id, f' ⬆ Курс 1 {currency} = {wel} {coin}', reply_markup=ikm)
#         MessageProfile.objects.create(id_profile=prof[0], coin=coin, currency=currency, price=wel,
#                                       tracking_status='Trecking')
#
#     if MessageProfile.objects.filter(
#             id_profile=Profile.objects.filter(id_telegram=message.chat.id).values('id')[0]['id']).values().order_by(
#         '-id')[:1][0]['tracking_status'] != 'Stop':
#         message_task(message, coin, currency)
#         print(MessageProfile.objects.filter(
#             id_profile=Profile.objects.filter(id_telegram=message.chat.id).values('id')[0]['id']).values().order_by(
#             '-id')[:1][0]['tracking_status'])
#     else:
#         print('сработало else')
#         return
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data == 'stop':
#         print("СТОП")
#         profile = Profile.objects.filter(id_telegram=call.message.chat.id)
#         MessageProfile.objects.create(id_profile=profile[0], coin='Stop', currency='Stop', price=0.1,
#                                       tracking_status='Stop')
#         return start(call.message), message_task(call.message, coin='bitcoin', currency='usd')


bot.polling(none_stop=True)
