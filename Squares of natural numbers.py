number = int(input("Введите число\n"))
i = 1

print(number, "\t\t", end=" ")
while i**2 <= number:
    print(i**2, end=" ")
    i = i + 1
