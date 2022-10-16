# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

def firstStep():
    from random import randint

    if randint(1, 3) == 1:
        print("Первым ходит Бот")
        step = 1
        b = randint(1, 29)
    else:
        step = 2
        print("Первым ходит игрок")
    return step

def game (player):
    amountOfCandies = 202
    while amountOfCandies > 28:
        if player == 1:
            if amountOfCandies >= 29 and amountOfCandies < 56:
                a = amountOfCandies - 29
            else:
                a = 29 - b
            print("Бот берет себе", a, "конфет")
            amountOfCandies -= a
            player += 1
            if amountOfCandies <= 28:
                print("Победа за игроком!")
        else:
            b = int(input("Ход игрока 2: "))
            amountOfCandies -= b
            player -= 1
            if amountOfCandies <= 28:
                print("Победа за ботом!")
        print("Оставшееся количество конфет: ", amountOfCandies)

step = int(firstStep())
game(step)
