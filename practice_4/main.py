import telebot
from practice_4.db_commands import *
import sqlite3

token = '784786449:AAHs_I7mD0KGoVY7o8uPn3kUijklgoOCcgM'
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)
keyboard.add('Hello')
# keyboard.row('How are you?', 'Bye')

db = sqlite3.connect('Users.sqlite', check_same_thread=False)
cursor = db.cursor()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello',
                     reply_markup=keyboard)
    add_user(message.from_user.id, cursor, db)

@bot.message_handler(content_types=['text'], func=lambda message:
                     get_state(message.from_user.id, cursor) == 2)
def answer(message):
    set_state(message.from_user.id, 1, cursor, db)
    bot.reply_to(message, 'Great!')


@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id,
                         'Hello. How are you?')
        set_state(message.from_user.id, 2, cursor, db)
    else:
        bot.send_message(message.chat.id, 'I don\'t understand',
                         reply_markup=keyboard)


@bot.message_handler(content_types=["sticker"])
def sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)


@bot.message_handler(content_types=["photo"])
def photo(message):
    bot.send_photo(message.chat.id, message.photo[-1].file_id)

bot.polling()