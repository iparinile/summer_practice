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
    #bot.reply_to(message, 'Great!')
    mess = message.text
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text='Russia', callback_data=mess + '_1'))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Other countries', callback_data=mess + '_2'))
    bot.send_message(message.chat.id, 'Where are you from?',
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    state = call.data.split('_')[0]
    if call.data[-1] == '1':
        bot.send_message(call.message.chat.id,
                         'You are from Russia and you are '+
                         state, reply_markup=keyboard)
    else:
        bot.send_message(call.message.chat.id,
                         'You are not from Russia and you are ' +
                         state, reply_markup=keyboard)


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