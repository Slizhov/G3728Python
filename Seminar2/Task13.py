# Задача 13.
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в 
# свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней
# длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная
# температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе. 
# Пользователь вводит число N - общее количество рассматриваемых дней (1<=N<=100).
# В следующих строках располагается N целых чисел.
# Каждое число - среднесуточная температура в соответствующий день.
# Температуры - целые числа и лежат в диапозоне от -50 до 50.
# Input 6 = 20,30,-40,50,10,-10, ответ 2.

import random
days = int(input("Введите количество дней: "))

today = 0
warms_days = 0
warms_period = 0
for i in range(days):
    print(today, end=" ")
    today += random.randint(-3,3) # диапозон изменения темп ежедневно
    if today > 0:
        warms_days +=1
    else:
        if warms_period < warms_days:
            warms_period = warms_days
else:            
    if warms_period < warms_days:
       warms_period = warms_days
    warms_days = 0
print("Самая долгая оттепель равна: ", warms_period)