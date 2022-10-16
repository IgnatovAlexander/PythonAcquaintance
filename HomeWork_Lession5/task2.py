# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

with open("HomeWork_Lession5\RLE_decoded.txt", "r") as data:
    text1 = data.read()


def coding(text1):
    newtext1=''
    previous = ''
    count = 1
    for i in text1:
        if i != previous:
            if previous:
                newtext1 += str(count)+previous
            count=1
            previous = i
        else:
            count +=1
    print(newtext1)


coding(text1)

with open("HomeWork_Lession5\RLE_coded.txt", "r") as data:
    text2 = data.read()


def decoding(text2):
    count = ''
    newtext2 = ''
    for i in text2:
        if i.isdigit():
            count += i 
        else:
            newtext2 += i * int(count)
            count = ''
    print(newtext2)

decoding(text2)
