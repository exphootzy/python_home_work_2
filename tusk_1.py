# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и 
# той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

money_quantity = int(input("Введите число отображающее количество монет: "))
count_for_0 = 0
count_for_1 = 0

for _ in range(money_quantity):
    money_value = random.randint(0,1)
    print(money_value)
    
    if money_value == 0:
        count_for_0 = count_for_0 +1
    
    if money_value == 1:
        count_for_1 = count_for_1 +1

if count_for_0 < count_for_1:
    print("Минимальное количество монет, которые нужно перевернуть:", count_for_0)
else:
    print("Минимальное количество монет, которые нужно перевернуть:",count_for_1)