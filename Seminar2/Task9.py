# Задача 9.
# По данному целому неотрицательному n вычислите значение n!. (Факториал числа).
# N!=1*2*3...*N (произведение всех чисел от 1 до N) 0!=1
# Решить задачу используя цикл while.

while True:
    number = input("Введите число: ")
    if number.isdigit():     #этот метод говорит, что внутри строки только цифра
        number = int(number) 
        break
    else:
        print("Введите целое число: ")

# number = abs(int(input("Введите целое число: ")))
#abs - любое отрицательное число превращает в положительное
factorial = 1
while number > 1:
    factorial *= number #факториал умножаем на число number
    number -= 1 #цикл: число number уменьшаем на 1, т.е. если число 6 умножаем на 5, 4, 3, 2, 1.

print(factorial)    