import telebot
from telebot import types

import excellentStudent as exS
import femail as femail
import noSubject as noS

API_TOKEN=''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Показать фамилии отличников")
    btn2 = types.KeyboardButton("Показать предметы, которые сдали девушки")
    btn3 = types.KeyboardButton("Показать предметы, по которым ни у кого нет зачета")
    markup.row(btn1, btn2, btn3)
    bot.send_message(message.chat.id,text="Выберете доступные действия",reply_markup=markup)

@bot.message_handler(content_types=['text'])
def frst(message):
    x = "HomeWork_Lession10\Students.json"
    y = "HomeWork_Lession10\AcademicP.json"
    z = "HomeWork_Lession10\Subject.json"
    if(message.text == "Показать фамилии отличников"):
        stlist = exS.student(x, y, z)
        bot.send_message(message.chat.id,stlist)
    elif(message.text == "Показать предметы, которые сдали девушки"):
        fem = femail.subject(x, y, z)
        bot.send_message(message.chat.id,fem)
    elif(message.text == "Показать предметы, по которым ни у кого нет зачета"):
        subj = noS.subject(x, y, z)
        bot.send_message(message.chat.id,subj)
    else:
        bot.send_message(message.chat.id,"Команда не корректна")

bot.polling()
