# Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на 
# указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

N = int(input('Введите число N: '))
list=[]
res = 1

for i in range(-N, N+1):
    list.append(i) 
print(list)

text = 'file.txt'
data = open(text,'r')
for line in data:
    res *= list[int(line)]
data.close()
print(res)