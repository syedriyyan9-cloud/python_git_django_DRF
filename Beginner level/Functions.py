def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

result = add(3, 5)  # result becomes 8

def power(base, exponent=2):
    return base ** exponent

print(power(3))      # uses default exponent 2 → 9
print(power(3, 4))   # overrides exponent → 81



x = 10  # global variable

def modify():
    global x
    x = 20   # changes the global x

modify()
print(x)  # prints 20


def divide(a, b):
    """Return the division of a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def say_hello():
    print("Hi!")

result = say_hello()  # prints "Hi!"
print(result)         # prints None


def get_min_max(numbers):
    return min(numbers), max(numbers)  # returns a tuple

lowest, highest = get_min_max([4, 1, 9, 3])
print(lowest, highest)  # prints 1 9

def add_and_print(a, b):
    print(a + b)      # shows on screen

def add_and_return(a, b):
    return a + b      # sends back

# Can't use the printed version in math
result1 = add_and_print(3, 4) * 2  # TypeError: None * 2

result2 = add_and_return(3, 4) * 2  # works: result2 = 14


def divide_safely(a, b):
    if b == 0:
        return None  # early exit
    if not isinstance(a, (int, float)):
        return None
    return a / b

result = divide_safely(10, 0)
if result is None:
    print("Cannot divide")
else:
    print(result)


def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier  # returning a function

times_three = make_multiplier(3)
print(times_three(10))  # prints 30


def multiply(x, y):  # x and y are parameters
    return x * y

result = multiply(4, 7)   # 4 and 7 are arguments


def describe_pet(animal, name):
    print(f"{name} is a {animal}")

describe_pet("cat", "Whiskers")   # Whiskers is a cat
describe_pet("Whiskers", "cat")   # cat is a Whiskers (wrong!)


describe_pet(name="Fluffy", animal="hamster")  # order doesn't matter


def greet(name, punctuation="!"):  # punctuation has default "!"
    return f"Hello, {name}{punctuation}"

print(greet("Alice"))        # argument "Alice" for name, punctuation uses default
print(greet("Bob", "?"))     # both arguments provided


def power(base, exponent, verbose=False):
    result = base ** exponent
    if verbose:
        print(f"Computing {base}^{exponent}")
    return result

# Positional arguments: 2→base, 3→exponent
print(power(2, 3))                    # returns 8, no print

# Keyword argument overrides order
print(power(exponent=4, base=5))      # returns 625

# Mixing: positional then keyword
print(power(3, exponent=2, verbose=True))  # prints "Computing 3^2" then returns 9


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Uses default: "Hello, Alice!"
greet("Bob", "Hi")       # Overrides default: "Hi, Bob!"


# Correct order
def create_user(username, is_admin=False, age=18):
    return f"{username}, admin={is_admin}, age={age}"

# Wrong order - SyntaxError
# def create_user(username="guest", is_admin, age):
#     pass


def add_item(item, my_list=[]):  # Bad! Empty list created once
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - surprise! List persists across calls
print(add_item(3))  # [1, 2, 3]


def add_item(item, my_list=None):  # Good! None is immutable
    if my_list is None:
        my_list = []               # Create new list each call
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [2] - clean list each time
print(add_item(3, [10, 20]))  # [10, 20, 3] - custom list works too


def configure(width=800, height=600, fullscreen=False, title="App"):
    print(f"Size: {width}x{height}, Fullscreen: {fullscreen}, Title: {title}")

configure(1024, title="My Game")        # width=1024, height default, fullscreen default
configure(fullscreen=True)              # all defaults except fullscreen
configure(height=400, width=300)        # order doesn't matter with keywords


def connect(timeout=None, retries=3):
    """
    Connect to the server.
    
    Args:
        timeout: Maximum seconds to wait (None means wait forever)
        retries: Number of retry attempts (default 3)
    """
    actual_timeout = timeout if timeout is not None else float('inf')
    print(f"Connecting with timeout={actual_timeout}, retries={retries}")

connect()                    # timeout=inf, retries=3
connect(timeout=5)           # timeout=5, retries=3
connect(retries=1)           # timeout=inf, retries=1



def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))      # 6
print(sum_all(10, 20))       # 30
print(sum_all())             # 0 (empty tuple)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Paris")
# name: Alice
# age: 25
# city: Paris


def register_user(username, *args, **kwargs):
    print(f"Username: {username}")
    print(f"Extra positional args: {args}")
    print(f"Extra keyword args: {kwargs}")

register_user("alice99", "premium", "verified", age=30, country="USA")
# Username: alice99
# Extra positional args: ('premium', 'verified')
# Extra keyword args: {'age': 30, 'country': 'USA'}


def greet(greeting, name):
    print(f"{greeting}, {name}!")

positional_args = ["Hello", "Bob"]
greet(*positional_args)      # Unpacks to: greet("Hello", "Bob")

keyword_args = {"name": "Alice", "greeting": "Hi"}
greet(**keyword_args)        # Unpacks to: greet(name="Alice", greeting="Hi")


def universal_logger(*args, **kwargs):
    print(f"Called with positional: {args}")
    print(f"Called with keyword: {kwargs}")
    # You can then forward these to another function

universal_logger(1, 2, 3, name="test", active=True)
# Called with positional: (1, 2, 3)
# Called with keyword: {'name': 'test', 'active': True}

# Good: explicit for known options
def send_email(to, subject, body, cc=None, bcc=None):
    pass

# Also good: variable number of numbers
def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Bad: lazy design hiding required parameters
def process_data(*args, **kwargs):
    # What arguments does this need? No one knows without reading code
    pass


def my_function():
    x = 10          # local variable
    print(x)        # works fine

my_function()
print(x)            # NameError: name 'x' is not defined

message = "Hello"    # global variable

def show():
    print(message)   # reading global works

def change():
    message = "Hi"   # creates a NEW local variable, doesn't change global!

show()               # prints "Hello"
change()
show()               # still prints "Hello"

counter = 0

def increment():
    global counter   # without this, Python would create local 'counter'
    counter += 1

increment()
increment()
print(counter)       # 2

def outer():
    x = 10           # enclosing variable
    
    def inner():
        nonlocal x   # without this, x would be local to inner
        x += 5       # modifies outer's x
    
    inner()
    print(x)         # 15

outer()

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)          # finds "local" first (Local)
        print(len([1]))   # 'len' not found locally, goes to Built-in
    inner()

outer()  # prints "local", then 1


# Bad: functions with side effects
balance = 100
def withdraw(amount):
    global balance
    balance -= amount

# Good: pure functions
def withdraw(balance, amount):
    return balance - amount

balance = 100
balance = withdraw(balance, 30)  # explicit and clear


square = lambda x: x ** 2
print(square(5))  # 25

# The same as:
def square(x):
    return x ** 2

add = lambda a, b: a + b
max_of_three = lambda x, y, z: x if (x > y and x > z) else (y if y > z else z)
format_pair = lambda a, b=0: f"({a}, {b})"

print(add(3, 4))           # 7
print(max_of_three(5, 2, 9))  # 9
print(format_pair(10))     # (10, 0)

numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9, 16, 25]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# Sort strings by their last character
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda s: s[-1])  # ['banana', 'apple', 'cherry']

from collections import defaultdict

# Lambda provides default value for missing keys
d = defaultdict(lambda: "missing")
print(d["key"])  # "missing"

# Button callback in GUI programming (conceptual)
# button = Button(text="Click", command=lambda: print("Clicked!"))

# Temporary sorting key that shouldn't be named
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
students.sort(key=lambda student: student[1])  # Sort by age

# Bad - too complex for lambda
result = map(lambda x: x**2 if x > 0 else (x**3 if x < -5 else 0), numbers)

# Good - use a named function
def transform(x):
    if x > 0:
        return x ** 2
    elif x < -5:
        return x ** 3
    return 0

result = map(transform, numbers)

# List comprehension (often more readable)
squares = [x**2 for x in numbers]  # vs map(lambda x: x**2, numbers)

# Conditional logic in comprehension (clearer)
filtered = [x for x in numbers if x % 2 == 0]  # vs filter(lambda x: x%2==0, numbers)

# When lambda is still best (custom key)
data = ["apple", "banana", "Avocado", "cherry"]
data.sort(key=lambda s: s.lower())  # case-insensitive sort


