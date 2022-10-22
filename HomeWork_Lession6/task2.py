# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;

import re
pattern1=r'[/,*,+,-]+'
str_lst = (input("Введите выражение: "))
# str1_lst = re.split(pattern,str_lst)
lst1 = re.split(pattern1, str_lst)
print(lst1)
lst2=[]
for i in lst1:
    pattern2=i
    lst2.append(re.split(pattern2, str_lst))
lst3 = lst2[0]
print (lst3[0])
lst4=[]
for i in lst3:
    if str(lst3[i])!='':
        lst4.append(lst3[i])
print(lst4)

