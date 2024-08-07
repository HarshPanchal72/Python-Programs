# check  substring of given string from list 

s = ['abc123', 'def456', 'ghi789']
a = 'abc12'
x = bool([i for i in s if a in s])
print(x)