# Write a Python program to generate and print a list of the first and last 5 elements
#  where the values are square of numbers between 1 and 30 (both included)

def values():
    x = list()
    for i in range(0,30):
        x.append(i**2)
    print(x[:5])
    print(x[-5:])
values()
