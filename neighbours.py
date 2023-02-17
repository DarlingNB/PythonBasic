# Просим пользователя ввести число
integer_list = []
# Создаем цикл в котором он будет добавлять числа в список
while (integer := int(input("Type number (0 - end):"))) != 0:
    integer_list.append(int(integer))


    integer_who_biggest = []
    counter = 0
    for i in range(1, len(integer_list) - 1):
        if integer_list[i - 1] < integer_list[i] > integer_list[i + 1]:
            counter += 1
            integer_who_biggest.append(integer_list[i])


print("Получился список:", integer_list)
print("Элементов:", len(integer_list))
print("Список чисел, которые больше своих соседей:", integer_who_biggest)
print("Количество чисел, которые больше своих соседей:", counter)






#СОВЕТ ОТ ПРЕПОДАВАТЕЛЯ
# 1) Чтобы не вводить числа, можно просто ипортировать random и создать список из случайных чисел
# 2) while (integer := int(input("Type number (0 - end):"))) != 0: вводить числа пока введенное число не соответсвует 0
# 3) Произвести расчет после полученного списка, а не во время цикла
#for i in range(1, len(integer_list) - 1):
#    if integer_list[i - 1] < integer_list[i] > integer_list[i + 1]:
#        counter += 1
#        integer_who_biggest.append(integer_list[i])

import random

integer_list = []
while (integer := int(input("Type number (0 - end):"))) != 0:
    integer_list.append(integer)

# я заміняв введення чисел для зручності тесту
# for i in range(1, 10):
#     integer_list.append(random.randint(1, 10))
print(integer_list)

integer_who_biggest = []
counter = 0
for i in range(1, len(integer_list) - 1):
    if integer_list[i - 1] < integer_list[i] > integer_list[i + 1]:
        counter += 1
        integer_who_biggest.append(integer_list[i])

print("Список чисел, которые больше своих соседей:", integer_who_biggest)
print("Количество чисел, которые больше своих соседей:", counter)



