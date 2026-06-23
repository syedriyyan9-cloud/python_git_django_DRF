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
#---------------------------------------------------------------
# filter in python
# filters out values based on give condition
# takes in a function that either returns true or false and an iterable
# returns a filter object, so convert to list, tuple or iterate over to see output
# example:
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
# just like map, filter gets exhausted after one complete iteration and then cannot be used again
#---------------------------------------------------------------
# zip in python
# a built in function that can iterate over multiple iterators at the same time
# it does this by taking elements from each iterable one at a time and forming a tuple
# then using that tuple in the loop or function.
# it is lazy so it has to be iterated over to get result.
# it returns a zip object, can work with large data.
# however if iterables are of different lengths then zip iterates until the shortest iterable
# is exhuasted.
# you can unpack from a zip using *
# example
values = [x for x in range(0,11)]
squares = [x**2 for x in values]
for v,s in zip(values, squares):
    print(f"value {v} square is {s}")
# you can also turn it into a list of tuples
paired = list(zip(values, squares))
print(paired)
# to unzip use *
value, square = zip(*paired)
print(value, square)
#---------------------------------------------------------------
# sorted in python
# sorts a copy of the list and returns it
# has key and reverse parameters
# key parameter is used for comparision functions
# reverse is used to state order either ascending or desending
# example
values = [x for x in range(15,9,-1)]
print(values)
asending_order = sorted(values)
print(asending_order)
#---------------------------------------------------------------