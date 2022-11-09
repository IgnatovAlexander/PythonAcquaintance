import telebot
from telebot import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN='5323012092:AAFI4ggChHGk0wvgn9ix6UbfQNbxsYw0Ylw'
bot = telebot.TeleBot(API_TOKEN)
 
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Бросьте монетку")
    markup.add(btn1)
    bot.send_message(message.chat.id,text="Игра запущена, бростье монетку",reply_markup=markup)
    markup = telebot.types.ReplyKeyboardRemove()
    

@bot.message_handler(content_types=['text'])
def frst(message):
    if(message.text == "Бросьте монетку"):
        from random import randint
        if randint(1, 3) == 1:
            bot.send_message(message.chat.id,"Первым ходит игрок 1.")
            bot.send_message(message.chat.id,"Введите через пробел индексы матрицы 3х3")
            bot.register_next_step_handler(message, game1)
        else:
            bot.send_message(message.chat.id,"Первым ходит игрок2")
            bot.send_message(message.chat.id,"Введите через пробел индексы матрицы 3х3")
            bot.register_next_step_handler(message, game2)
    else:
        bot.send_message(message.chat.id,"Ну что ж вы так!")
 
@bot.message_handler(content_types=['text'])
def game1(message):
    if (message.text == "1 1"):
        bot.send_message(message.chat.id,"Выиграл игрок 1")

@bot.message_handler(content_types=['text'])
def game2(message):
    if (message.text == "1 1"):

bot.polling()