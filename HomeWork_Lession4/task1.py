# задача 1. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


def factoring(number):
    list = []
    i=2
    while number > 1:
        if number % i == 0:
            list.append(i)
            number = number / i
        else:
            i += 1
    return list

try:
    n = int(input("\nВведите число: "))
    print("Список простых множителей:\n", factoring(n))
except:
    print("Неверный ввод!")
