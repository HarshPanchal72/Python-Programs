# 15. Write a Python program to get the difference between the two lists. 

list = [1,2,3,4,5,6,7,89]
list2 = [21,1,2,4,5,6,14,25,20]

temp = []
for i in list2:
    if i not in list:
        temp.append(i)
print(temp)

