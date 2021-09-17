import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def SayHello(message) :

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Вопрос")
	item2 = types.KeyboardButton("Неполадка")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать!\nЭто техническая поддержка UMAG.\nЧем мы можем Вам помочь?", reply_markup=markup)
	bot.send_message(message.chat.id, "1.Вопрос по использованию UMAG\n2.Технические неполадки")

@bot.message_handler(content_types=["text"])
def WhatHappend(message):
	if message.chat.type == 'private':
		if message.text == 'Вопрос':
			bot.send_message(message.chat.id, "Задайте вопрос:")
		elif message.text == 'Неполадка':
			bot.send_message(message.chat.id, "Что именно не работает?")
		else: bot.send_message(message.chat.id, "<Примерное решение>Спасибо за обращение!")
	
bot.polling(none_stop=True)