num = 6
count = 0
for i in range(1, num + 1):
    count +=1
    print(count, end=' * ')

    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()
