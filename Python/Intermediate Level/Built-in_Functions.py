# map in python
# maps element from iterable to a function one at a time, lazy in nature
# so always iterate over it to see results or store in list or tuple
# syntax of map: map(function, iterable)
# function can be user defined, lambda, or built in
# example
numbers = [x for x in range(0,11)]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))
# map object is returned, gets exhausted after one iteration

# filter in python
# filters out values based on give condition
# takes in a function that either returns true or false and an iterable
# returns a filter object, so convert to list, tuple or iterate over to see output
# example:
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
# just like map, filter gets exhausted after one complete iteration and then cannot be used again
