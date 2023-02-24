# ПЕЧАТЬ ТРЕУГОЛЬНИКА А
print()
triangle_lengh = int(input("Введите высоту фигуры A: "))
space = " "
progression = -3
decrease = triangle_lengh - 1
print()

for i in range(triangle_lengh):
    if i == triangle_lengh - 1:
      print(space * decrease,"*" * (progression + 4))
    elif i == 0:
      print(space * decrease, "*")
    elif i == 1:
       print(space * decrease,"*","*")
    elif triangle_lengh > (i > 0):
       print(space * decrease,"*",space * progression,"*")
    progression += 2
    decrease -= 1







# ПЕЧАТЬ ТРЕУГОЛЬНИКА B
print()
triangle_lengh = int(input("Введите высоту фигуры B: "))
space = " "
progression = 3
decrease = triangle_lengh - 1
print()


for i in range(triangle_lengh):
    if i == 0:
      print(space * decrease, "*")
    elif i > 0:
        print(space * decrease, "*" * progression)
        progression += 2
    decrease -= 1



# ПЕЧАТЬ ТРЕУГОЛЬНИКА C
print()
triangle_lengh = int(input("Введите высоту фигуры C: "))
space = " "
progression = 3
decrease = triangle_lengh - 1
half_triangle = int((triangle_lengh + 1) / 2)


for i in range(half_triangle):
    if i == 0:
      print(space * decrease, "*")
    elif i > 0:
        print(space * decrease, "*" * progression)
        progression += 2
    decrease -= 1
# Вторая половина треугольника C
decrease = (triangle_lengh - half_triangle) - 1

for i in range(half_triangle):
    if i == half_triangle - 1:
        print(space * decrease, "*","*")
    elif i > 1:
        print(space * decrease, "*", space * (progression - 4),"*")

    progression -= 2
    decrease += 1
    if i == half_triangle - 1:
        print(space * decrease,"*")



# ПЕЧАТЬ ТРЕУГОЛЬНИКА D
print()
triangle_lengh = int(input("Введите высоту фигуры D: "))
space = " "
progression = 3
decrease = triangle_lengh - 1
half_triangle = int((triangle_lengh + 1) / 2)


for i in range(half_triangle):
    if i == 0:
      print(space * decrease, "*")
    elif i > 0:
        print(space * decrease, "*" * progression)
        progression += 2
    decrease -= 1



# Вторая половина треугольника C
# Могу разместить 6 элементов в пространство между звездами
progression -= 7
stars_space_count = int(progression / 2)
decrease = (triangle_lengh - half_triangle) - 1

for i in range(half_triangle):

    if i == half_triangle - 2:
        print(space * decrease,"* * *")
        continue
    if i == half_triangle - 1:
        print(space * (decrease + 1),"***")
        print(space * (decrease + 2), "*")
        continue
    if i > 1:
        print(space * decrease,"*", space * stars_space_count, "*" , space * stars_space_count ,"*")
    stars_space_count -= 1
    decrease += 1



