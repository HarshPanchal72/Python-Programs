# Write a Python program to iterate over dictionaries using for loops
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key,value in person.items():
    print (f"{key}, {value}")