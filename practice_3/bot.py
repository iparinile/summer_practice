import telebot

bot = telebot.TeleBot("844950001:AAHeEy2Jn3V1uoIO5Lv8R-RUBcj2_IRptho")

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)  # 1 true - уменьшает размер кнопок,
# 2 - закрывает кнопки после нажатия
keyboard.row('Привет', 'Пока')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Где деньги, Лебовски?", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def message(message):
    if message.text.lower() == 'привет':  # Добавил функцию, теперь хоть 'ПрИВет' пиши, бот поймет
        bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, ' + message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=["sticker"])
def sticker(sticker):
    bot.send_sticker(sticker.chat.id, sticker.sticker.file_id)


@bot.message_handler(content_types=["photo"])
def photo(photo):
    print(photo)
    a = photo.photo[0]
    print(a)
    bot.send_photo(photo.chat.id, a.file_id)

bot.polling()
