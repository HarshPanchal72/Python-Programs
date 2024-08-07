#  Write a Python program to print a specified list after removing the 0th, 4th, and 5th elements. 
# 	Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# 	Expected Output : ['Green', 'White', 'Black']

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del list[5], list[4], list[0]  
print(list)