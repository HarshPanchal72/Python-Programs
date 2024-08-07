# Write a Python program to find the second smallest number in a list.

def find_second_largest_and_smallest(list1):
    if len(list1) < 2:
        raise ValueError("List must have at least two elements")

    sorted_list = sorted(list1)
    second_largest = sorted_list[-2]
    second_smallest = sorted_list[1]

    print(f"Second Largest element is: {second_largest}")
    print(f"Second Smallest element is: {second_smallest}")

    return second_largest, second_smallest