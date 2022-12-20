# 16. Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.


n = int(input("Введите значение числа N: "))
result = {i: (1+1/i)**i for i in range(1 , n+1)}
sum = 0

for n in result:
    sum += result[n]

print(result)    
print(f'Сумма значений = {sum}')