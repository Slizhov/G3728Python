# Задача 2.
# Найдите сумму цифр трехзначного числа.

#Решение 1.
# number= input ("Введите трехзначное число: ")
# a = int(number[0])
# b = int(number[1])
# c = int(number[2])
# print(f"Сумма цифр числа: ", a+b+c)

# Решение 2.
number = input ("Введите трехзначное число: ")
number = int(number)
a = number%10
b = number%100//10
c = number//100
print (f"Сумма цифр числа: ", a+b+c)