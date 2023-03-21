# Задача 11.
# Дано натуральное число А>1. Определите, каким по счету числом Фибоначи оно является,
# т.е. введите такое число n, что ф(n)=A.
# Если не является числом Фибоначчи, выведите число -1.
# 0 1 2 3 4 5 6  7  8  9 - числа по счету
# 0 1 1 2 3 5 8 13 21 34 - числа Фибоначчи

number = int(input("Введите искомое число Фибоначчи: "))

fib_prev, fib_curr = 0, 1
index = 1

while fib_curr < number:
    fib_next = fib_prev + fib_curr
    fib_prev = fib_curr
    fib_curr = fib_next
    #другой способ решения
    # fib_prev, fib_curr = fib_curr, fib_prev + fib_curr 
    index +=1

if fib_curr == number:
    print(index)
else: 
    print (-1)
         