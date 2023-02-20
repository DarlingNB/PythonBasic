words = "Hi hello new all new Hi all"
word_list = words.split( )
dict = {}

for each_element in word_list:
    count = dict.get(each_element, 0)
    dict[each_element] = count + 1

print(dict)

#  ---Вариант от преподавателя---
# Тут цикл for который:
# В words.split() разделяет все слова по пробелу, и добавляет их в созданный список word
# word - переменная, которая живет внутри цикла, содержит в себе список слов из words
# words.count(word) - количество слов в строке words по элементам word
# dict - словарь в котором слова и их количества
#dict = {word: words.count(word) for word in words.split()}

#print(dict)