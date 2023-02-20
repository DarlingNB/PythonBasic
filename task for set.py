import random
list1 = [random.randint(1, 10) for i in range(5)]
list2 = [random.randint(1, 10) for i in range(5)]
print('Первый список', list1)
print('Второй список', list2)
print('Уникальные числа первого списка', set(list1))
print('Уникальные числа второго списка', set(list2))
print('Уникальный числа в двух списках', (set(list1) | set(list2)))
print('Количество уникальный чисел в двух списках', len((set(list1) | set(list2))))


