import telebot
from random import *
import json
from telebot import types
import XO
films=[]


def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")

def load():
    global films
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Фильмотека была успешно загружена")   

API_TOKEN='5323012092:AAFI4ggChHGk0wvgn9ix6UbfQNbxsYw0Ylw'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    # try:
    XO.startGame(message)
    bot.send_message(message.chat.id,"It's alive!")
    # except:
    #     bot.send_message(message.chat.id,"Что-то пошло не так")

bot.polling()