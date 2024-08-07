# 20. Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 0, 0, 10]

print('comparing two list is circularly or not')
print(''.join(map(str,list1)) in ''.join(map(str,list2)))

