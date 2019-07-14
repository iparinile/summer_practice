import telebot

bot = telebot.TeleBot("844950001:AAHeEy2Jn3V1uoIO5Lv8R-RUBcj2_IRptho")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
