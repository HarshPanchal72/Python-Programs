# 18. Write a Python program to check a dictionary is empty or not.
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
if person.items() == '':
        print('dictionary is empty')
else:
        print('not empty')