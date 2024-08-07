# 16.Write a Python program to get a dictionary from an object's fields.
class Animals: 
      
    def __init__(self): 
        self.lion = 'carnivore'
        self.dog = 'omnivore'
        self.giraffe = 'herbivore'
  
    def printit(self): 
        print('Dictionary from the object fields')

obj = Animals()
obj.printit()
print(obj.__dict__)
