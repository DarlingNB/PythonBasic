# number = input("Input number\n")
number = 70304

def expanded_form(number):
    num_str = str(number)
    result = []
    for i in range(len(num_str)):
        if num_str[i] != '0':
            result.append(num_str[i] + '0' * (len(num_str) - i - 1))
    print(' + '.join(result))



expanded_form(number)
