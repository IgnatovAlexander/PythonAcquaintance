#  Напишите программу для. проверки истинности утверждения 
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

numbers = ["X", "Y", "Z"]

for i in range (3):
    a = input (f'Введите {numbers[i]} ')
    numbers.append (a)

if (not (numbers[0] or numbers[1] or numbers[2])) == (not numbers[0] and not numbers[1] and not numbers[2]):
    print("Истина")
else:
    print ("Ложь")
