# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях
# элементы 3 и 9, ответ: 12


def listCreation(number):
    from random import randint

    list = [0] * int(number)
    for i in range(len(list)):
        list[i] = randint(0, 10)
    return list


def sumPostion(list):

    sumofnumbers = 0
    for i in range(len(list)):
        a = i % 2
        if a != 0:
            sumofnumbers += list[i]
    return sumofnumbers


try:
    n = int(input("Введите количество элементов строки: "))
    list1 = listCreation(n)
    print("Исходная последовательность: \n", list1)
except:
    print("Неверный ввод!")

print(
    "\n Сумма элементов на нечетных позициях равна: \n",
    sumPostion(list1),
)
