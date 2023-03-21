# Задача 10.
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые - гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input("Сколько лежит монеток на столе: "))
count_reshko = count_gerb = 0
for i in range (n):
    x = int(input("Орел(1) или решко (0)? "))
    if x == 1:
        count_gerb +=1
    else:
        count_reshko +=1
if count_gerb < count_reshko:
    print (f"Переверните {count_reshko} монет с решко на герб, их меньше всего") 
elif   count_reshko == count_gerb:
    print (f"Количество решко и гербов одинаково, по {count_reshko} штук ")  
else:
    print ((f"Переверните {count_gerb} монет с герба на решко, их меньше всего")) 