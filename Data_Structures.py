"""

A file for practicing built-in data structures in python

"""

"""list"""
my_list = []  # creates an empty list
my_list_2 = [x for x in range(1,11)]    # creates a list using comprehension
print(my_list, my_list_2)

# built in list methods
my_list = my_list_2.copy()    # copies the list of b to variable a
print(my_list)    # same elements as b, any modifications to one does not affect the other
my_list.append(11)    # adds 11 at the end of the list
c = my_list.pop() # removes the last element and returns it
            # can take index as argument to remove the value at specific position
print(c)
my_list.sort(reverse=True)    # reverses the order of the list
print(my_list)
my_list.extend(my_list_2) # extends a by adding b to it
print(my_list, my_list_2)
print(my_list.count(5))   # prints the returned count of a number in a list

"""Tuples"""
my_tuple = () # empty tuple
my_tuple_2 = tuple(x ** 2 for x in range(1,6))  # contains sqr of numbers from 1 to 5, created using generator expression converted into tuple, tuples do not have comprehensions
print(my_tuple, my_tuple_2)
"""Tuple have only 2 methods"""
c = my_tuple_2.count(1)  # returns the number of times an int is present otherwise error
print(c)
c = my_tuple_2.index(16)  # returns the index of an int otherwise error
print(c)

"""Dictionaries"""
