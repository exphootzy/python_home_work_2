# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и 
# той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

money_quantity = int(input("Введите число отображающее количество монет: "))

for _ in range(money_quantity):
    money_value = random.randint(0,1)
    print(money_value)