# from django.core.management.base import BaseCommand
from django.conf import settings
# from telegram import Bot
# from telegram import Update
# from telegram.ext import CallbackContext
# from telegram.ext import Filters
# from telegram.ext import MessageHandler
# from telegram.ext import Updater
# from telegram.utils.request import Request
# from apps.Employees.models import Profile, Message
#
# @bot.messege_handler(comand=['start'])
# def start(bot: Bot, update: Update):
#     bot.send_message(chat_id=update.message.chat_id, text='Привет я бот который умеет отслеживать курс криптовалюты')
#
#
# def log_errors(f):
#     def inner(*args, **kwargs):
#         try:
#             return f(*args, **kwargs)
#         except Exception as e:
#             error_message = f'Error: {e}'
#             print(error_message)
#             raise e
#
#     return inner
#
#
# @log_errors
# def do_echo(update: Update, context: CallbackContext):
#     chat_id = update.message.chat_id
#     text = update.message.text
#
#     p, _ = Profile.objects.get_or_create(id_user=chat_id, defaults={'name': update.message.from_user.username})
#     Message(profile=p, text=text).save()
#
#     reply_text = f'Твой ID = {chat_id}\n{text}'
#     update.message.reply_text(text)
#
#
# class Command(BaseCommand):
#     help = 'Telegram-bot'
#
#     def handle(self, *args, **options):
#         request = Request(connect_timeout=0.5, read_timeout=1.0)
#         bot = Bot(request=request, token=settings.TOKEN)
#         print(bot.get_me)
#
#         # обработчик сообщений
#         updater = Updater(
#             bot=bot,
#             use_context=True
#         )
#         message_handler = MessageHandler(Filters.text, do_echo)
#         updater.dispatcher.add_handler(message_handler)
#
#         # Бесконечная обработка сообщений
#         updater.start_polling()
#         updater.idle()

from telebot import types
import telebot

bot = telebot.TeleBot(token=settings.TOKEN)


def registration():
    pass


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn = types.KeyboardButton('Зарегистрироваться')
    markup.add(itembtn)
    bot.send_message(message.chat.id, 'Для того чтобы продолжить, нажмите зарегистрироваться', reply_markup=markup)


def get_keyboard():
    # Генерация клавиатуры.
    buttons = [
        types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
        types.InlineKeyboardButton(text="+1", callback_data="num_incr"),
        types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


@bot.message_handler(commands=['user'])
def user(message):
    mess = f'{message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, f'Привет {mess}')


@bot.message_handler()
def get(message):
    bot.send_message(message.chat.id, message)


bot.polling(none_stop=True)
