import random

print ("начальный списoк" , lst)

for i in range(10):

        lst.append(random.randint(0, 100))

max_index = lst.index(max(numbers))# находим индкс самого большого и  самого маленкого
min_index = lst.index(min(numbers))

lst[max_index], lst[min_index] # меняем местами
lst[min_index], lst[max_index]

print ("измененный список:" ,  lst)
