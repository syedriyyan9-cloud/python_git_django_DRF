'''
In Python Object-Oriented Programming (OOP), methods defined inside a class are 
categorized into three main types:
1. instance methods, also called object methods
2. class methods
3. static methods

instance methods are used on instances and are created with first parameter being
self, they have access to objects state or attrs.
these methods can also access class variables or attrs.

class methods are used on class variables and are created with first parameter
being cls, they have access to class variables and not obj varialbes

class variables are variables that are defined inside the class, and not inside
any other method, class variables are shared with entire class.

instance variables are variables defined inside init method, and they only belong
to the object that is being created at the time, there can be many objs

static methods are methods that neither use instace variables or class variables
they are present inside the class for utility.
'''

class MathUtils:
    '''a class representing math functions'''
    pi = 3.141  # class variable

    def __init__(self, value):
        self.value = value  # instance variable

    def square(self):   # instance method
        return self.value * self.value
    
    @classmethod    # notice this decorator is medatory for class method
    def circular_area(cls, radius): # class method
        return cls.pi * (radius ** 2)
    
    @staticmethod   # notice this decorator is a must for static method
    def is_even(value): # static method
        return True if value % 2 == 0 else False

obj = MathUtils(3)
# instance method is invoked on the object or instance of the class.
print(obj.square())

# notice below that class and static methods are invoked on the class and not on
# the object. they can be invoked on the object that result stays the same.
print(MathUtils.circular_area(3))
print(MathUtils.is_even(9))

    
