# 12. Write a Python program to remove an item from a tuple.
# Original tuple
tup = (1, 3, 4, 32, 1, 1, 1, 2, 4, 5, 6, 7, 8, 4)
item_to_remove = 1
new_tup = tuple(i for i in tup if i != item_to_remove)

print(new_tup)