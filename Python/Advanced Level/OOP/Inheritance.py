'''
Inheritance is a technique that allows one class to use the properties of another class
one class can inherit from one or more classes
super method allows us to use parent method inside child classes.
if the inheritance is complex you can use mro method to look at how python preceives the inheritance chain
child classes can override parent's methods, these methods can be instance, class or static as long as correct decorators are being used.
'''
class Animal:
    '''represents animals'''
    def make_sound(self):
        return 'animal Sound'

class Dog(Animal):
    '''represents Dogs'''
    def make_sound(self):
        return 'Barks'

class Cat(Animal):
    '''represents cat'''
    def make_sound(self):
        return 'meows'

for i in [Animal(), Dog(), Cat()]:
    print(i.make_sound())

'''
the properties or attributes of a class can be set to public, protected or private.
python does not have strict rules for declaring public, private, or protected attributes like java or c++
so instead it relies on community's conventions
they are public by default
when prefixed by single underscore ( _ ) they are considered protected
when prefixed by double underscore ( __ ) they are considered private.
the double underscore in private attributes initiates the name mangling process which is just python's way to ensuring that
the attribute is not being used by mistake.
if you want to access private attributes then you have to use obj._classname__attributename
'''

class Person:
    '''represents person'''
    def __init__(self):
        self.name = 'some name' #public attribute
        self._age = 100 #protected attribute
        self.__email = 'something@something.com'    #private attribute

p1 = Person()
print(p1.name)
print(p1._age)
# print(p1.__email)     # results in error
print(p1._Person__email)


'''
python comes with @property decorator which allows you to use setter and getter methods without having to write them separately.
you must always declare getter functions before setter functions.
getter functions only contain the return statement
setter functions can hold logic and set the value for the variable
in both function use the prefeix of underscore ( _ ) when refering to the attributes
so the naming convention would be like _attrname in all getter and setter functions if it is already declared inside the class
for setter function use @attrname.setter to set up the setter function followed by the name of attribute as the funciton name,
remember setter function takes self, and some other arguement so that it can set the value of attr to the second arg.
you can also create attributes using @property which you can then get without having to declare them in class
@property also works with classes not just attributes
'''

class Circle:
    '''represents circle'''
    def __init__(self):
        self.radius = 2

    @property
    def radius(self):       # use the name of the attribute as methods name
        return self._radius

    @radius.setter
    def radius(self, value):
        # you can add logic as well
        if value < 0:
            print('Radius cannot be negative, setting value to 0')
            self._radius = 0
        else:
            self._radius = value
        # does not return the value, that's getters functionality

    @property
    def area(self):
        return 3.141 * (self.radius ** 2)

cir = Circle()
print(cir.radius)   # reads value using getter function
print(cir.area)     # this attribute was not declared inside class but was created using @property decorator, only value is returned
cir.radius = 30     # uses setter function to set the value of circle
print(cir.radius)   # gets the updated value of the circle
print(cir.area)     # updated value of area is returned