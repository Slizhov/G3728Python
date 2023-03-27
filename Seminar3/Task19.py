# Задача №19. 
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

import random
my_list = [i for i in range(10)]
print(my_list)

shift = int(input("На сколько двигаем вправо: "))

for i in range(shift):
    temp = my_list.pop(len(my_list)-1)
    my_list.insert(0, temp)
    
print(my_list)