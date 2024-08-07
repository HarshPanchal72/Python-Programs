# 3. Create a Class with instance attributes

class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
obj = Demo('Harsh', 20)
print(obj.name, obj.age)