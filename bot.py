import telebot
from telebot import types

TOKEN = "8029766430:AAGXDpfRX1pBD3-1mOyiQhSH2vnOJsLYq-E"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📚 Python")
    btn2 = types.KeyboardButton("🤖 Сени ким жасады")
    btn3 = types.KeyboardButton("😄 Салам айт")
    btn4 = types.KeyboardButton("❤️Мен сени суйом")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, "Салам Расул! Төмөндөн вариант танда 👇",reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text == "📚 Python":
        bot.send_message(message.chat.id, "Python — эң күчтүү жана жеңил тил 💪")

    elif message.text == "🤖 Сени ким жасады":
        bot.send_message(message.chat.id, "Мен атым /rasul_helper/, мен сага жардам берем, кандай суроолорун бар ?")

    elif message.text == "😄 Салам айт":
        bot.send_message(message.chat.id, "Салам Расул 🤝 жакшы күн!")

    elif message.text == ("❤️Мен сени суйом"):
        bot.send_message(message.chat.id, "Мен да сени суйом❤️, ийй милашкам десе")

    else:
        bot.send_message(message.chat.id, "Варианттардан танда 😅")




print("Бот иштеп жатат...")
bot.polling(none_stop=True, interval=0)