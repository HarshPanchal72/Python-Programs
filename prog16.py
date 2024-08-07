dict1 = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1, 'elderberry': 7}


sorted_dict_ascending = dict(sorted(dict1.items(), key=lambda item: item[1]))
print("Sorted dictionary by value in ascending order:")
print(sorted_dict_ascending)


sorted_dict_descending = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
print("\nSorted dictionary by value in descending order:")
print(sorted_dict_descending)