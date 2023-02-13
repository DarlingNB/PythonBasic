s = input("Введіть рядок:")
ch = input("Введіть символ:")

if s.count(ch) >= 1:
    indexes = [i for i, c in enumerate(s) if c == ch]
    print("Символ", ch, "повторяется", s.count(ch), "раз.")
    print("Символ", ch, "находится по индексам", indexes)
else:
    print("Такого символа нет!")
