# задача 3. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def equationCreation(number):
    from random import randint

    x = randint(0, 100)
    y = randint(0, 100)
    z = randint(0, 100)
    equation = [x, "*x^", number, "+", y, "*x", number, "+", z]
    eq = ""
    for i in equation:
        eq += str(i)

    eq = eq.replace("x^1+", "x+")
    eq = eq.replace("x^0", "")
    return eq


try:
    k = int(input("Введите коэффициент k: "))
    line= equationCreation(k)
    print("Уравнение: \n", line)
except:
    print("Неверный ввод!")

with open('HomeWork_Lession4\Equation.txt', 'w') as data:
    data.write(line)
