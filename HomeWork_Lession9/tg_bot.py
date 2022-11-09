# import telebot
# from telebot import types

# API_TOKEN='5323012092:AAFI4ggChHGk0wvgn9ix6UbfQNbxsYw0Ylw'
# bot = telebot.TeleBot(API_TOKEN)
 
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     startGame(message)

# @bot.message_handler(content_types='text')
# def message_reply(mes):
#     send = bot.send_message(mes.chat.id,'Следующий ход')
#     bot.register_next_step_handler(send, game)

# def startGame(message):
#     step = int(firstStep(message))
#     game(step, message)

# def firstStep(message):
#     from random import randint

#     if randint(1, 3) == 1:
#         bot.send_message(message.chat.id,"Первым ходит игрок1")
#         step = 1
#         b = randint(1, 29)
#     else:
#         step = 2
#         bot.send_message(message.chat.id,"Первым ходит игрок2")
#     return step

# def game (player, message):
#     amount = 0
#     import re
#     pattern='\s+'
#     newM = newMatrix()
    
#     while amount < 9:
#         if player == 1:
#             bot.send_message(message.chat.id,"Игорк 1. Введите номер строки и столбца через пробел  ")
#             @bot.message_handler(content_types='text')
#             def message_reply(mes):
#                 send = bot.send_message(mes.chat.id,'Следующий ход')
#                 bot.register_next_step_handler(send, game)
#             str_lst=message_reply(mes)
#             str_lst = re.split(pattern, str_lst)
#             newM[int(str_lst[0])][int(str_lst[1])] = 'O'
#             amount += 1
#             player += 1
#             printMatrix(newM)
#             if checkWin (newM):
#                 bot.send_message(message.chat.id,"Победа за Игроком 1")
#                 # print("Победа за Игроком 1")
#                 quit()

#         else:
#             bot.send_message(message.chat.id,"Игорк 2. Введите номер строки и столбца через пробел  ")
#             message_reply()
#             str_lst = re.split(pattern,str_lst)
#             newM[int(str_lst[0])][int(str_lst[1])] = 'X'
#             amount += 1
#             player -= 1
#             printMatrix(newM)
#             if checkWin (newM):
#                 bot.send_message(message.chat.id,"Победа за Игроком 2")
#                 # print("Победа за Игроком 2")
#                 quit()

# def newMatrix():
#     matrix = []
#     for i in range(3):
#         sp = []
#         for j in range(3):
#             sp.append(".")
#         matrix.append(sp)
#     return matrix

# def printMatrix(matrix):
#     for i in range(3):
#         print(" ".join(matrix[i]))

# def checkWin(matrix):
#     result = False
#     a = 'X'
#     b = 'O'
#     for i in range(3):
#         if matrix[i][0]==matrix[i][1]==matrix[i][2]==a:
#             result = True
#         elif matrix[i][0]==matrix[i][1]==matrix[i][2]==b:
#             result = True
#     for i in range(3):
#         if matrix[0][i]==matrix[1][i]==matrix[2][i]==a:
#             result = True
#         elif matrix[0][i]==matrix[1][i]==matrix[2][i]==b:
#             result = True
#     if matrix[0][0]==matrix[1][1]==matrix[2][2]==a:
#             result = True
#     elif matrix[0][0]==matrix[1][1]==matrix[2][2]==b:
#         result = True
#     return result


# bot.polling()