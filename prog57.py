def full_pyramid(rows):
    for i in range(rows + 1):
       
        for j in range(rows - i):
            print(' ', end='')
        # Print asterisks
        for k in range(1, 2 * i):
            print('*', end='')
        print()

# Example usage:
full_pyramid(5)