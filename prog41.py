# 10. Write a Python program to check whether an element exists within a tuple.

def check_item(tup, item):
    if item in tup:
        print(f'The element {item} exists in the tuple.')
    else:
        print(f'The element {item} does not exist in the tuple.')

my_tuple = (1, 2, 3, 4, 5, 6, 7, 87, 9)
num = 4
check_item(my_tuple, num)