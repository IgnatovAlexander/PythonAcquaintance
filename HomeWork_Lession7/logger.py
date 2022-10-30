from datetime import datetime as dt
from time import time


def formula_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("HomeWork_Lession7/log.csv", "a") as file:
        file.write("{};formula;{}\n".format(time, data))


def complex_logger(data1, data2, data3):
    time = dt.now().strftime("%H:%M")
    with open("HomeWork_Lession7/log.csv", "a") as file:
        file.write(
            "{};Number1;{};Number2;{};Operation;{}\n".format(time, data1, data2, data3)
        )

def error_logger():
    time = dt.now().strftime("%H:%M")
    with open("HomeWork_Lession7/log.csv", "a") as file:
        file.write("{};Error\n".format(time))

def result_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("HomeWork_Lession7/log.csv", "a") as file:
        file.write("{};result;{}\n".format(time, data))
