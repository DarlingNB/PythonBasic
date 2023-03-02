# number = input("Input number\n")
number = 0

def expanded_form(number):
    num_str = str(number)
    result = []
    if int(number) <= 0:
        raise Exception("You must input number bigger them 0")
    for i in range(len(num_str)):
        if num_str[i] != '0':
            result.append(num_str[i] + '0' * (len(num_str) - i - 1))
    print(' + '.join(result))



expanded_form(number)
