row = input('Введите предложение\n')

# Первый способ, узнаем количество пробелов и прибавляем 1
row_count = row.count(' ') + 1
print("В этом предложении", row_count, "слов.")

# Второй способ, через split, а потом узнаем длинну через len
print("В этом предложении", (len(row.split(" "))), "слов.")










