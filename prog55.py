# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1
# 1 0 1 0 1 0

rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        if j % 2 == 0:
            print(0, end='')
        else:
            print(1, end='')
    print()
        