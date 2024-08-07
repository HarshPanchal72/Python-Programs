#  Write a Python script to check if a given key already exists in a dictionary.
def check_key(dictionary, key):
 
    return key in dictionary

my_dict = {"name": "John", "age": 30}
print(check_key(my_dict, "name"))