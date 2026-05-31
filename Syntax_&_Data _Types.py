
"""Variables"""
name = 'bob'
location_of_name = id(name) # id checks memory address
print(location_of_name)

"""Strings"""
text = 'hello world'
first_char = text[0]
last_char = text[-1]
substring = text[1:-2]
# strings are immutable
# text[0] = 'j' will give typeerror

"""strings methods"""
fruits = 'apple,banana,cherry'
fruit_list = fruits.split(',')
# print(fruit_list)
fruits_basket = ', '.join(fruit_list)
print(fruits_basket)
# better to use join than concatenation as it is more efficient
fruits_replaced = fruits.replace('apple', 'pineapple')
print(fruits_replaced)
print(fruits.find('b'))

"""Integers"""
"""conversion between different number systems"""
binary = 0b01111
octal = 0o17
hexadeciaml = 0xf
print(binary, octal, hexadeciaml)
print(bin(binary))
print(oct(octal))
print(hex(hexadeciaml))
# int with string can use base argument to convert to desired base
print(int('0b01111',base=2))
# Left shift doubles the value
shifted = 5 << 1      # 10 (binary 101 becomes 1010)
halved = shifted >> 1
print(shifted, halved)

"""Floats"""
import math
# Special float values
positive_inf = float('inf')
negative_inf = float('-inf')
not_a_number = float('nan')
print(math.isinf(positive_inf))
print(math.isinf(negative_inf))
print(math.isnan(not_a_number))

"""Booleans"""
# Boolean literals and type checking
is_active = True
is_deleted = False
print(type(is_active))          # <class 'bool'>
print(isinstance(True, int))    # True (bool is int subclass)

# Boolean in arithmetic (possible but often confusing)
count = True + True + False     # 2
print(f"Total: {count}")        # Total: 2

# Best practice - avoid arithmetic with booleans
# Use integers explicitly if you need counting
active_count = sum([True, True, False])  # Still 2, but more readable

# all() and any() for iterable validation (backend common)
user_permissions = [True, True, False, True]
print(all(user_permissions))      # False (not all true)
print(any(user_permissions))      # True (at least one true)

"""None"""
# None basics and singleton property
empty_value = None
result = None

# Checking None (ALWAYS use 'is', never '==')
if result is None:
    print("No result available")

# None is a singleton
a = None
b = None
print(a is b)        # True (same object)
print(id(a))         # Same memory address
print(id(b))         # Same memory address

# Comparing with == works but is not idiomatic
print(a == None)     # True but don't do this

# Common pitfall - methods that modify in place
my_list = [3, 1, 2]
returned = my_list.sort()  # Sorts the list but returns None
print(returned)            # None
print(my_list)             # [1, 2, 3] (list was modified)

"""Type Conversion"""
# str() vs repr() for debugging
from datetime import date
today = date.today()
print(str(today))          # "2026-05-25" (user-friendly)
print(repr(today))         # "datetime.date(2026, 5, 25)" (developer-friendly)

