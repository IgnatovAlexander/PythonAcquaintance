# Задача 2. Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def listCreation(number):
    from random import randint

    list = [0] * int(number)
    for i in range(len(list)):
        list[i] = randint(0, 10)
    return list


def newList(list):
    list2 = [0] * int(len(list) / 2 + 0.5)
    j = int(len(list))
    for i in range(len(list2)):
        list2[i] = list[i] * list[j-1]
        j -= 1
    return list2


try:
    n = int(input("Введите количество элементов строки: "))
    list1 = listCreation(n)
    print("Исходная последовательность: \n", list1)
except:
    print("Неверный ввод!")

print(
    "\n Новый список: \n",
    newList(list1)
)
