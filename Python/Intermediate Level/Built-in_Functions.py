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
# any in python
# evaluates if an iterable has one true value, if it does returns true else false
# opposite of all
# is lazy so we can use large amount of data in it for efficiency
# is better than explicit loops as it short circuits the process to find truthy value
# example
is_odd = any(x % 2 != 0 for x in range(0,12, 2))
# we would get [0,2,4,6,8,10] which are all even, iterable does not contain odd numbers
print(is_odd)
# better to use with generators as using it with lists mean that memory is occupied by list
# so efficieny does not give full benefit
#---------------------------------------------------------------
# all in python
# opposite of any
# returns true if all values in the iterable are true else false
# best used with generators for lazy evaluation of large amounts of data
# example
is_even = all(x % 2 == 0 for x in range(0,13,2))
# condition is satisfied as all the numbers generated are even
# print(is_even)
# if even one number was odd it would have returned false example
is_even = all(x % 2 == 0 for x in range(0,3))
# the iterable would contain values of 0,1,2 where only one value is odd 
# and does not satisfy the condition hence it will return false
print(is_even)
#---------------------------------------------------------------
# enumerate in python
# returns the index along with the tuple (item) when used on an iterable, returns a lazy obj
# when used on dicts it will only provide with index and keys not key value pairs
# if you want key value pairs using enumerate then use dict.items() with enumerate
# does not modify any original data
# has a start parameter which can be used to change the index number which starts with 0 by default
# example
list1 = [x for x in range(1,11)]    # a list of numbers from 1 to 10
for index, item in enumerate(list1, start=1):
    print(f"{index}: {item}")
dict1 = {k:v**2 for k, v in zip(range(1,11),range(1,11))}   # a dict containing squares of keys (numbers from 1 to 10)
for index, (key, value) in enumerate(dict1.items()):
    print(f"{index}: key = {key}, value = {value}")
#---------------------------------------------------------------
# reversed in python
# returns a lazy obj that contains a reversed version of a sequence type
# remember it only takes 1 parameter and it must be a sequence type
# does not work with non sequence type like sets
# works with dict however only reverses the keys in a dict
# does not modify any data in the original sequence
# example
for i in reversed(range(1,11)):
    print(i)
#---------------------------------------------------------------