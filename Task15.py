# 15. Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

N = int(input('Введите значение N: '))
temp = 1
result = list()

for i in range(1, N + 1):
    result.append(i * temp)
    temp *= i

print(result)