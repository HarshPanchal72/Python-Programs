# 13. Write a Python program to map two lists into a dictionary.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['a', 'b', 'c', 'd', 'e']
map = zip(list1, list2)
dictionary = dict(map)

print(dictionary)
