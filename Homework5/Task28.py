# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4 
first_number = int(input('Введите первое число: '))
second_number= int(input('Введите второе число: '))
def sum(first_number, second_number):

     if second_number == 0:
         return first_number
     return 1 + sum(first_number, second_number - 1)

print(f"Выводим сумму чисел", sum(first_number, second_number))

# второй вариант:
# a = int(input('Введите первое число: '))
# b= int(input('Введите второе число: '))

# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         if b > 0:
#             return sum(a + 1, b - 1)
#         else:
#             return sum(a - 1, b + 1)

# print(sum(int(input()), int(input())))