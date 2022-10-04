# Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10
# задается случайными целыми числами, выводится на экран,
# затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!

from random import randint

array = [0] * 10
for i in range(0, 10):
    array[i] = randint(0, 100)

array1 = [0] * 10
for j in range(0, 5):
    array1[j * 2] = array[j + 5]
    array1[j * 2 + 1] = array[j]


print("Изначальный массив:\n", array)

print("\n Измененный массив:\n", array1)
