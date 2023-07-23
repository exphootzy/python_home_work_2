#  Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num_value = int(input("Введите любое положительное число: "))
num_result = 1

while num_result < num_value:
    num_result = num_result * 2
    
print(int(num_result / 2))
