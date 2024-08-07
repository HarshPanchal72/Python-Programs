# 12. Write a Python program to print the numbers of a specified list after removing even numbers from it.
list = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in list:
    if i % 2 ==0:
        list.remove(i)
    
print('after removing even number in list')
print(list)

