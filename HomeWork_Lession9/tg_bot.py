import telebot
from telebot import types
import json

API_TOKEN='5323012092:AAFI4ggChHGk0wvgn9ix6UbfQNbxsYw0Ylw'
bot = telebot.TeleBot(API_TOKEN)
 
@bot.message_handler(commands=['start'])
def start_message(message):
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Бросьте монетку")
    markup0.add(btn1)
    bot.send_message(message.chat.id,text="Игра запущена, бростье монетку",reply_markup=markup0)
    markup0 = telebot.types.ReplyKeyboardRemove()
    
@bot.message_handler(content_types=['text'])
def frst(message):
    if(message.text == "Бросьте монетку"):
        from random import randint
        a = telebot.types.ReplyKeyboardRemove()
        if randint(1, 3) == 1:
            bot.send_message(message.chat.id,text="Первым ходит игрок 1. Поставьте X", reply_markup=boardCreate())
            bot.register_next_step_handler(message, game1)
        else:
            bot.send_message(message.chat.id,text="Первым ходит игрок 2. Поставьте O", reply_markup=boardCreate())
            bot.register_next_step_handler(message, game2)
    else:
        bot.send_message(message.chat.id,"Ну что ж вы так!")
 
@bot.message_handler(content_types=['text'])
def game1(message):
    a = 'X'
    if checkWin ():
        bot.send_message(message.chat.id,text="Победа за Игроком 2. Игра завершена")
        quit()
    else:
        bot.send_message(message.chat.id,text="Ход игрока 2. Поставьте O",reply_markup=boardChange(message, a))
        bot.register_next_step_handler(message, game2)

@bot.message_handler(content_types=['text'])
def game2(message):
    a = 'O'
    if checkWin ():
        bot.send_message(message.chat.id,text="Победа за Игроком 1. Игра завершена")
        quit()
    else:
        bot.send_message(message.chat.id,text="Ход игрока 1.Поставьте X",reply_markup=boardChange(message, a))
        bot.register_next_step_handler(message, game1)

def boardCreate():
    XO_BDinit = XO_board()
    markup = types.ReplyKeyboardMarkup(row_width=3)
    row = [types.KeyboardButton(x) for x in XO_BDinit[:3]]
    markup.add(*row)
    row = [types.KeyboardButton(x) for x in XO_BDinit[3:6]]
    markup.add(*row)
    row = [types.KeyboardButton(x) for x in XO_BDinit[6:]]
    markup.add(*row)
    return markup

def boardCreate2():
    global XO_BD_changed
    markup = types.ReplyKeyboardMarkup(row_width=3)
    row = [types.KeyboardButton(x) for x in XO_BD_changed[:3]]
    markup.add(*row)
    row = [types.KeyboardButton(x) for x in XO_BD_changed[3:6]]
    markup.add(*row)
    row = [types.KeyboardButton(x) for x in XO_BD_changed[6:]]
    markup.add(*row)
    return markup

def XO_board():
    XO_BD_init = ["1","2","3","4","5","6","7","8","9"]
    return XO_BD_init

def boardChange(message,a):
    global XO_BD
    XO_BD = XO_board()
    global XO_BD_changed
    for i in range(0,9):
        if XO_BD[i] == message.text:
            XO_BD_changed [i] = a
    return boardCreate2()

def checkWin():
    result = False
    global XO_BD_changed
    matrix = XO_BD_changed
    a = 'X'
    b = 'O'
    i = 0
    if matrix[i]==matrix[i+1]==matrix[i+2]==a:
        result = True
    elif matrix[i]==matrix[i+1]==matrix[i+2]==b:
            result = True
    i = 3
    if matrix[i]==matrix[i+1]==matrix[i+2]==a:
        result = True
    elif matrix[i]==matrix[i+1]==matrix[i+2]==b:
            result = True
    i = 6
    if matrix[i]==matrix[i+1]==matrix[i+2]==a:
        result = True
    elif matrix[i]==matrix[i+1]==matrix[i+2]==b:
            result = True
    if matrix[0]==matrix[4]==matrix[8]==a:
            result = True
    elif matrix[0]==matrix[4]==matrix[8]==b:
        result = True
    if matrix[2]==matrix[4]==matrix[6]==a:
            result = True
    elif matrix[2]==matrix[4]==matrix[6]==b:
        result = True
    if matrix[0]==matrix[3]==matrix[6]==a:
            result = True
    elif matrix[0]==matrix[3]==matrix[6]==b:
        result = True 
    if matrix[1]==matrix[4]==matrix[7]==a:
            result = True
    elif matrix[1]==matrix[4]==matrix[7]==b:
        result = True  
    if matrix[2]==matrix[5]==matrix[8]==a:
            result = True
    elif matrix[2]==matrix[5]==matrix[8]==b:
        result = True
    return result

XO_BD_changed = ["1","2","3","4","5","6","7","8","9"]

bot.polling()

