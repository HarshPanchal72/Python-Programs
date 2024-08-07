# 6. Write a Python program to convert a tuple to a string.
def convert_tuple(tup):
    return ''.join(map(str, tup))

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
result = convert_tuple(my_tuple)
print('Converting successfully', type(result), 'elements are', result)