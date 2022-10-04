# Задача 2. Напишите программу, которая принимает на вход
# число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def multipllyNumber(n):
    array = [1] * n
    for i in range(0, n):
        number = i + 1
        f = 1
        while number > 1:
            f *= number
            number -= 1
            array[i] = f
    return array


a = int(input("Введите N "))
print(multipllyNumber(a))
