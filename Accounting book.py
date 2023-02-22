# Первый вариант решения задачи
# def info(list_of_books):
#    for counter in range(0,4):
#        sum = list_of_books[counter][2] * list_of_books[counter][3]
#        if sum < 100:
#            sum = sum + 10
#        i = list_of_books[counter][0], sum
#        print(i)
#
# info([
#    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
#    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
#    [77226, 'Head First Python, Paul Barry', 3, 32.95],
#    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
#




# Попытка решить задачу применяя filter,lambda,map)

list_of_books = [
   [34587, 'Learning Python, Mark Lutz', 4, 40.95],
   [98762, 'Programming Python, Mark Lutz', 5, 56.80],
   [77226, 'Head First Python, Paul Barry', 3, 32.95],
   [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]




def take_order_id(list_of_books):
    order_id = list_of_books[0][0]
    return order_id
def myltiplie(list_of_books):
    index_price = list_of_books[0][3]
    index_count = list_of_books[0][2]
    order_id = list_of_books[0][0]
    sum = index_count * index_price
    if sum < 100:
        sum = sum + 10
    return sum


print(list(map(myltiplie(list_of_books),list_of_books)))






