# Write a Python program to flatten a shallow list.
# 	list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# 	o/p = [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

list = [[2,4,3],[1,5,6], [9], [7,9,0]]
flatten =[]
for i in list:
    for j in i:
        flatten.append(j)

print(flatten)

