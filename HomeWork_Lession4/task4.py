# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.


def nok(a1, b1):
    if a1 > b1:
        i = b1
    else:
        i = a1

    while True:
        if i % a1 == 0 and i % b1 == 0:
            break
        i += 1
    return i


try:
    a = int(input("\nВведите число a: "))
    b = int(input("\nВведите число b: "))
    print("Наименьшее общее кратное:\n", nok(a, b))
except:
    print("Неверный ввод!")
