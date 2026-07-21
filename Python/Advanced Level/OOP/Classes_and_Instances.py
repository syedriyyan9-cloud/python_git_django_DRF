'''
A class is a blueprint from which objects are created.
An object is an instance (variable) of the class
Every object can have same or different state depending on how they were created
'''
# example of a class
class Dog:
    '''A class representing Dogs'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''
init method is used as an initializer, not constructor, when we create an instance
the constructor is __new__() but it is rarly used as initializer first calls
the constructor and then initializes the object with the given arguments
'''

dog = Dog('Rex', 12)

'''
self is not a keyword, it is a convention that is used by python community
self refers to the object itself
'''

print(f"dog is {dog.age} years old, and his name is {dog.name}")

'''
dot after the name of the object is used to access the attrs of the obj
'''
# now as you can see Dog, with capital D is the class where as the dog, with 
# lowercase d is the obj of the class, we can create multiple objs from same class

dog1 = Dog('lex', 3)
print(f"dog is {dog1.age} years old, and his name is {dog1.name}")

'''
notice that both have different names and ages, and work completely fine
also notice that both take only two arguments as we have only decided to 
give them two attrs in the class definition.
'''


