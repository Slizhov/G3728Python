# Задача 5.
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
# (при этом иногда вагоны нумеруются от "головы" поезда, а иногда - с 
# "хвоста"; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда
# и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего
# вагонов в электричке. Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.

i= int(input ("Введите номер вагона в который сел Витя: "))
j= int(input ("Введите номер вагона который увидел Витя : "))
# i=3
# j=4
if i==j:
    print("Не можем определить")
else:
    print (f"{i+j-1} вагонов")    