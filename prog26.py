# 12. Write a Python program to remove a key from a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
remove = my_dict.pop('b')
if remove:
    print('key remove successfully')
print(my_dict)