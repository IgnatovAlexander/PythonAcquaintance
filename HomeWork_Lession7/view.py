import logger as log

def user_input():
    return int(
        input(
            "Вычисление каких чисел собираетесь производить: 1 - рациональных, 2 - вещественных "
        )
    )


def input_data(b):
    if b == 1:
        formula = input("Введите уравнение: ")
        log.formula_logger(formula)
        return formula
    else:
        x1 = input("Введите первое комплексное число: ")
        y1 = input("Введите второе комплексное число: ")
        sign = str(input("Введите одно из выражений: +,-,*,/ "))
        log.complex_logger(x1,y1,sign)
        return x1, y1, sign

def iferror():
    a = print("Введите корректное выражение!")
    log.error_logger()
