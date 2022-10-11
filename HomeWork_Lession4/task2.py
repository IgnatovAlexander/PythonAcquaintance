# задача 2 . Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.


def listCreation(number):
    from random import randint

    list = [0] * int(number)
    for i in range(len(list)):
        list[i] = randint(0, 10)
    return list


def uniqueListCreation(list):
    list2 = []
    for i in list:
        if i in list2:
            continue
        else:
            list2.append(i)
    return list2


try:
    n = int(input("Введите количество элементов строки: "))
    list1 = listCreation(n)
    print("Исходная последовательность: \n", list1)
except:
    print("Неверный ввод!")

print(
    "\n список уникальных элементов: \n",
    uniqueListCreation(list1),
)
