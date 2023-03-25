# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

number = int(input('Введите число: '))
degree = int(input('Введите степень, в которую возводим число: '))
def recApowB(number, degree):
    if degree == 0:
        return 1
    return number * recApowB(number, degree - 1)

print(recApowB(number, degree))
