import telebot

bot = telebot.TeleBot("844950001:AAHeEy2Jn3V1uoIO5Lv8R-RUBcj2_IRptho")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Где деньги, Лебовски?")


@bot.message_handler(content_types=["text"])
def message(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=["sticker"])
def sticker(sticker):
    bot.send_sticker(sticker.chat.id, sticker.sticker.file_id)


bot.polling()
