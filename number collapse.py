number = input("Input number what you want collaps\n")

def number_collapse(number=str):

    if number.isdigit() == False:
        raise Exception("You must input only numbers")
    if int(number) <= 0:
        raise Exception("You must input number bigger them 0")
    if number.isdigit() == True:
        collapsed_num = 0
        for i in number:
            collapsed_num = int(i) + collapsed_num
    collapsed_num = str(collapsed_num)
    if len(collapsed_num) > 1:
        number_collapse(collapsed_num)
    else:
        print(collapsed_num)













number_collapse(number)