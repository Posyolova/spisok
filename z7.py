import random

print ("начальный списoк" , lst)

for i in range(10):

        lst.append(random.randint(0, 100)) #добавляет 10 случайных чисел в диапазоне от 0 до 100 в конец списка lst и выводит список до и после добавления этих чисел.

max_index = lst.index(max(numbers))# находим индкс самого большого и  самого маленкого
min_index = lst.index(min(numbers))

lst[max_index], lst[min_index] # меняем местами
lst[min_index], lst[max_index]

print ("измененный список:" ,  lst)
