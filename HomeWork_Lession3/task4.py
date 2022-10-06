# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def numberCreation(number):
    b = ''
    while number > 0:
        b = str(number % 2) + b
        number = number // 2
    b = int(b)
    return b


try:
    n = int(input("Введите десятичное число: "))
    print ("Двоичный вид числа: ", numberCreation(n))
except:
    print("Неверный ввод!")
