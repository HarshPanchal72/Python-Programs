# 14. Write a Python program to sort a dictionary by key.

dict1 = {1: 1, 8: 4, 7: 9, 4: 16, 5: 25, 6: 36, 17: 49, 13: 64, 78: 81, 10: 100, 11: 121, 12: 144}
sorted_keys = sorted(dict1.keys())
result = {key: dict1[key] for key in sorted_keys}
print(result)