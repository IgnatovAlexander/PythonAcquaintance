# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def listCreation(number):
    import random

    list = [0] * int(number)
    for i in range(len(list)):
        list[i] = round(random.uniform(0, 20), 2)
    return list


def difMinAndMax(list):
    minValue = list[0] - int(list[0])
    maxValue = list[0] - int(list[0])
    for i in range(len(list)):
        a = list[i] - int(list[i])
        if a < minValue:
            minValue = a - int(a)
        elif a > maxValue:
            maxValue = a - int(a)
    difference = round(maxValue - minValue, 2)
    return difference


try:
    n = int(input("Введите количество элементов строки: "))
    list1 = listCreation(n)
    print("Исходная последовательность: \n", list1)
except:
    print("Неверный ввод!")

print(
    "\n Разница дробных экстремумов: \n",
    difMinAndMax(list1),
)
