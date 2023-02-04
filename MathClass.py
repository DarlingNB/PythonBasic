# Решение, подсказанное преподавателем как пример ---------------------------------------------------------------------
class_1 = input("Введите количество школьников в первом классе")
class_2 = input("Введите количество школьников в втором классе")
class_3 = input("Введите количество школьников в третьем классе")

#Складывает количество учеников
total_students = int(class_1) + int(class_2) + int(class_3)

# количество парт = количество студентов
count_of_tables = total_students // 2 + 1 * total_students % 2

print(count_of_tables)



# Окончательный мой вариант решения, с точным количеством карт чтобы хватило каждому классу в отдельности ---------------------------

#Получаем количество учеников в каждом классе
first_class = int((input("Введите количество учеников в первом классе")))
second_class = int((input("Введите количество учеников во втором классе")))
third_class = int((input("Введите количество учеников в третьем классе")))

# проводим расчет по необходимости получения парт для каждого класса отдельно
first_class_count = first_class / 2
need_tables_first_class = first_class % 2
all_tables_first_class = first_class_count + need_tables_first_class

second_class_count = second_class / 2
need_tables_second_class = second_class % 2
all_tables_second_class = second_class_count + need_tables_second_class

third_class_count = third_class / 2
need_tables_third_class = third_class % 2
all_tables_third_class = third_class_count + need_tables_third_class

# Поскольку получается float, переводим в int и складываем
print("Для 3х классов необходимо закупить", int(all_tables_first_class) + int(all_tables_second_class) + int(all_tables_third_class) , "парт.")



# Вариант решения задачи 2 --------------------------------------------------------------------------------------------

#Получаем количество учеников в каждом классе
first_class = int((input("Введите количество учеников в первом классе")))
second_class = int((input("Введите количество учеников во втором классе")))
third_class = int((input("Введите количество учеников в третьем классе")))

#Складываем общее количество учеников во всех трех классах
all_pupils = first_class + second_class + third_class
# Делим на 2
tables = all_pupils / 2
# Узнаем неделимый остаток
need_tables = all_pupils % 2
# Складываем полученные данные
all_tables = tables + need_tables

# Поскольку получается float, переводим в int
print("Для 3х классов необходимо закупить", int(all_tables) , "парт.")




# Первый вариант решения задачи через импорт math ---------------------------------------------------------------------------------

import math

#Получаем количество учеников в каждом классе
first_class = int((input("Введите количество учеников в первом классе")))
second_class = int((input("Введите количество учеников во втором классе")))
third_class = int((input("Введите количество учеников в третьем классе")))

#Складываем общее количество учеников во всех трех классах
all_pupils = first_class + second_class + third_class
# Делим на 2
tables = all_pupils / 2
# Получаем число, и если оно не целое то округляем в большую сторону
all_tables = ( math.ceil(tables) )


print("Для 3х классов необходимо закупить", all_tables , "парт.")
