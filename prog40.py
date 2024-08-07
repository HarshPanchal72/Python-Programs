# 9. Write a Python program to find the repeated items of a tuple.
tup=(1,3,4,32,1,1,1,2,4,5,6,7,8,4)  
for i in tup:
    if tup.count(i) > 1:
        print('REPEATED' , i, '', end='')