# 2. l1 = [1,2,3,4] ,l2 = [5,6,7,8] convert two list into dictionary.using lambda and list comprehension.
#                 o/p = {'1':5, '2':6 ,'3':7 ,'4':8}  

l1 = [1,2,3,4] 
l2 = [5,6,7,8]
d = {str(x): y for x, y in zip(l1, l2)}
print(d)

to_str = lambda x: str(x)
d = dict(zip(map(str,l1),l2))

print(d)  