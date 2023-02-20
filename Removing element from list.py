new_list_element = []
list = []

while (new_list_element := int(input("Вводите число (0 - конец):"))) != 0:
    list.append(new_list_element)
k = int(input("Введите индекс необходимого числа \n"))

# Второй вариант
list.insert(len(list),list[k])
list.remove(list[k])
list.pop()
print(list)

# Первый вариант
#k_item = (list[k])
#list.append(k_item)
#list.remove(k_item)
#list.pop()
#print(list)












