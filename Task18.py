#18. Реализуйте алгоритм перемешивания списка.
import random
import copy

our_list = ['C#','Python','C++','PHP','Java', 'JavaScript']
res = copy.copy(our_list)
length = len(our_list)-1

for i in range(0,length):
    random_index = random.randint(0, length)
    temp = res[i]
    res[i] = res[random_index]
    res[random_index] = temp

print(res)
    

  
        



