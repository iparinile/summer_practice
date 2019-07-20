import sqlite3
import telebot
# from practice_5.database import *

bot = telebot.TeleBot("989390225:AAGHxvF6ZAFlH--DYcL0RObyjb28Wgrp7Wc")
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.row('Привет, да!')


# db = sqlite3.connect('database', check_same_thread=False)
# cursor = db.cursor()


@bot.message_handler(commands='start')
def send_hello(message):
    bot.send_message(message.chat.id,
                     'Привет, ' + message.from_user.first_name + ', хочешь записаться на какой-нибудь ivent?',
                     reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def send_message(message):
    if message.text == 'Привет, да!':
        bot.send_message(message.chat.id,
                         'Отлично, пока доступен только \"ivent1\", хочешь на него записаться? '
                         'Если да, то напиши мне название ивента ')

    elif message.text == 'ivent1':
        bot.send_message(message.chat.id, 'Отлично! Ты записался! Остальные функции будут доступны позже!')
        user = [str(message.from_user.id), message.from_user.first_name]
        print(user)
        #cursor.executemany("INSERT INTO users VALUES (?, ?)", user)
    else:
        bot.send_message(message.chat.id, 'Извини, но я тебя не понимаю, попробуй команду /help')


bot.polling()
