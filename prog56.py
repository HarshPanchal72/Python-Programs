
    #             1
    #           2 1 2
    #         3 2 1 2 3 
    #       4 3 2 1 2 3 4
    #     5 4 3 2 1 2 3 4 5
    #   6 5 4 3 2 1 2 3 4 5 6 

def full_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
    
        for k in range(i, 0, -1):
            print(k, end=" ")
        
        
        for k in range(2, i + 1):
            print(k, end=" ")

        print()

full_pyramid(5)
