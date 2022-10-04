# Напишите программу, которая принимает на вход
# вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11


def sumOfNumbers(number):
    int_value = int(number)
    sum = int(0)
    counter = 0
    while int_value >= 1:
        sum = sum + int(int_value % 10)
        int_value = int_value / 10
        counter += 1

    fract_value = number - int(number)
    fract_value = round(fract_value, (len(str(number)) - counter + 1))

    while fract_value != 0:
        sum = sum + int(fract_value * 10) % 10
        fract_value = fract_value * 10 - int(fract_value * 10)
        fract_value = round(fract_value, (len(str(number)) - counter + 1))

    return sum


n = float(input("Введите целое или вещественное число: "))

print(sumOfNumbers(n))
