# 17. Write a Python program to remove duplicates from the Dictionary..
student_data ={1:'python', 2:'java', 3:'c++', 4:'html', 1:'python', 2:'java'}

result = {}
for key,value in student_data:
    if value not in result.values():
        result[key] = value

print(result)