new_list_element = []
list = []
while (new_list_element := int(input("Вводите число (0 - конец):"))) != 0:
    list.append(new_list_element)
list.pop()
k = int(input("Введите индекс необходимого числа \n"))
list.remove(list[k])
print(list)












