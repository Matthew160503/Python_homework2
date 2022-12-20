# 14. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

num = input("Введите вещественное число: ")
list_num = num.split(".")
list_num = list(map(int,list_num))
sum = 0

for i in list_num:
    while i > 0:
        digit = i % 10
        i = i // 10
        sum += digit
print(f'Сумма всех цифр числа num = {sum}')