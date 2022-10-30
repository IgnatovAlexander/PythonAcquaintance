# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

import re

pattern1 = r"[/,*,+,-]"
pattern2 = r"[0,1,2,3,4,5,6,7,8,9]"
# str_lst = "120*3/4-2"
str_lst=input('Введите выражение: ')
lst1 = re.split(pattern1, str_lst)
lst2 = re.split(pattern2, str_lst)
lst2 = [x for x in lst2 if x != ""]

number = []
a = len(lst1) + len(lst2)
i = 0
j = 0
while a != 0:
    if i < len(lst1):
        number.append(lst1[i])
        i += 1
        a -= 1
    if j < len(lst2):
        number.append(lst2[j])
        j += 1
        a -= 1

operators = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y),
             '*': (lambda x, y: x * y), '/': (lambda x, y: x / y)}

while len(number)>1:
    for i in range(0,len(number)-1):
        if number[i]=='*':
            x, y = float(number[i-1]), float(number[i+1])
            number[i]=operators['*'](x,y)
            number.pop(i-1)
            number.pop(i)
            i=0
            break
    while len(number)>1:
        for j in range(0,len(number)-1):
            if number[j]=='/':
                x, y = float(number[j-1]), float(number[j+1])
                number[j]=operators['/'](x,y)
                number.pop(j-1)
                number.pop(j)
                j=0
                break
        while len(number)>1:
            for k in range(0,len(number)-1):
                if number[k]=='+':
                    x, y = float(number[k-1]), float(number[k+1])
                    number[k]=operators['+'](x,y)
                    number.pop(k-1)
                    number.pop(k)
                    k=0
                    break
            while len(number)>1:
                for u in range(0,len(number)-1):
                    if number[u]=='-':
                        x, y = float(number[u-1]), float(number[u+1])
                        number[u]=operators['-'](x,y)
                        number.pop(u-1)
                        number.pop(u)
                        u=0
                        break
print(number[0])
