import random

n = int(input('введите ваше число- '))

lst = [random.randint(0, 25) for _ in range(10)] # генерируем список из 10 случайных от 0 до 25

print(lst)

if n in lst:
        print(lst.index(n)) #проверяем есть ли это число в списке
else:
        print('-1')
