def reverse_triangle(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print("*", end="")
        print()

reverse_triangle(7)