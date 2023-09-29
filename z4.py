import random
lst = []

for i in range(10):
        lst.append(random.randint(0, 100))

summ = 0
proizv = 1

for i in lst:
        summ += i
        proizv *= i

print(summ, '\n', proizv)
