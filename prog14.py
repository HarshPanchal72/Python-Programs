# Write a Python program to get the frequency of the elements in a list.
def frequency(list, element):
    return list.count(element)

list = [10, 20, 10, 20, 4, 4, 40, 40, 50, 41, 10]
element = 10
fre = frequency(list, element)
print(element, ':' , fre)

