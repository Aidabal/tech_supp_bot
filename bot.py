import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.token)

updater = Updater(token, use_context=True)

updater.start_polling()
updater.idle()

@bot.message_handler(commands=['start'])
def SayHello(message) :

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Вопрос")
	item2 = types.KeyboardButton("Неполадка")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать!\nЭто техническая поддержка UMAG.\nЧем мы можем Вам помочь?", reply_markup=markup)
	bot.send_message(message.chat.id, "1.Вопрос по использованию UMAG\n2.Технические неполадки")

@bot.message_handler(content_types=["text"])

def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я Валютный бот")
	
def WhatHappend(message):
	if message.chat.type == 'private':
		if message.text == 'Вопрос':
			bot.send_message(message.chat.id, "Задайте вопрос:")
		elif message.text == 'Неполадка':
			bot.send_message(message.chat.id, "Что именно не работает?")
		else: bot.send_message(message.chat.id, "<Примерное решение>Спасибо за обращение!")
	
bot.polling(none_stop=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
updater.start_polling()
updater.idle()
