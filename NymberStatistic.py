# Задача на цикл и подсчет введенных данных

#ДЗ5 Программа спрашивает введение с клавиатуры целые числа
#пока не будет введено "0"
#Как только будет введено "0"
#программа должна просчитать и вывести на экран
#- количество введенных чисел
#- Их сумму
#- Среднее арифметическое всех введенных числе (кроме "0")
#- Максимальное и минимальное значение
#- посчитать количество парных и непарных элементов в последовательности

#------------------------------------------------------------------------------------------------------

# Просим пользователя ввести число
random_num = int(input("Введите любое целое число (Число 0 остановит программу)\n"))  #Добавил преобразование в int
number_of_entered_numbers = 0
sum_of_entered_numbers = 0
max = 0
min = random_num
paired = 0
not_paired = 0

# Было - while str(random_num) > "0": , но это ошибка, тк я сравнивал количество символов в строке, а не само число
# != сравнивает соответсвие
while random_num != 0:
    number_of_entered_numbers += 1
    sum_of_entered_numbers += random_num
    if max < random_num:
        max = random_num
    if random_num % 2 == 0:
        paired += 1
    if random_num % 2 > 0:
        not_paired += 1
    if min > random_num:
        min = random_num
    random_num = int(input("Введите любое целое число (Число 0 остановит программу)\n")) #Добавил преобразование в int


#тут был if random_num == "0": , но он слегка лишний тк принты появятся и так как только мы введем 0
# потому что закончится цикл

print("Количество введенных чисел:" , number_of_entered_numbers)
print("Сумма введенных чисел:", sum_of_entered_numbers)
print ("Среднее арифметическое:",sum_of_entered_numbers / number_of_entered_numbers )
print("Минимальное число:", min)
print("Максимальное число:", max)
print("Количество парных элементов:", paired)
print("Количество непарных элементов:", not_paired)
print("\n")
print("Программа завершила работу.")