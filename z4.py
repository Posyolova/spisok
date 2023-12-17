import random
lst = []

for i in range(10):
        lst.append(random.randint(0, 100))

sum_lst = sum(lst)

proizv_lst = 1 #произведение элементов списка
for number in lst:
    proizv_lst *= number

print("сумма:", sum_lst)
print("произведение:" , proizv_lst)
