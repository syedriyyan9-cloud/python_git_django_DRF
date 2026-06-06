score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Output: Grade: B

# Count from 1 to 5 with step of 2
for i in range(1, 6, 2):
    print(i, end=" ")
# Output: 1 3 5

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output: 0: apple, 1: banana, 2: cherry

student = {"name": "Alice", "age": 20, "major": "CS"}
for key, value in student.items():
    print(f"{key} = {value}")
# Output: name = Alice, age = 20, major = CS

# Searching for a number
for num in [2, 4, 7, 9, 10]:
    if num % 2 != 0:
        print(f"First odd: {num}")
        break
else:
    print("No odd numbers found")
# Output: First odd: 7

# Simple countdown using while
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
# Output: 5 4 3 2 1 Blast off!

# Keep asking until user enters a positive number
while True:
    user_input = input("Enter a positive number: ")
    number = int(user_input)
    if number > 0:
        break
    print("That's not positive, try again!")
print(f"Thanks! You entered {number}")

# For loop (cleaner for counting)
for i in range(3):
    print(i)

# While loop (better for unknown iterations)
response = ""
while response != "quit":
    response = input("Type 'quit' to exit: ")

# Searching with while-else
password = "secret"
attempt = ""
tries = 0
while tries < 3:
    attempt = input("Enter password: ")
    if attempt == password:
        print("Access granted")
        break
    tries += 1
else:
    print("Access denied - too many attempts")
# else runs only if break never happened


# Finding the first even number
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even found: {num}")
        break
# Output: First even found: 8 (stops without checking 9 and 10)

# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers entirely
    print(i, end=" ")
# Output: 1 3 5 7 9

# Using pass as a placeholder
def future_function():
    pass  # Will implement this later

class MyClass:
    pass  # Empty class is valid with pass

for item in range(3):
    if item == 1:
        pass  # Do nothing special for item 1
    print(item)
# Output: 0 1 2

# Demonstration of all three
for num in range(6):
    if num == 0:
        pass  # Do nothing for zero (still prints 0)
    elif num == 3:
        continue  # Skip printing 3 entirely
    elif num == 5:
        break  # Stop completely at 5
    print(num, end=" ")
# Output: 0 1 2 4 (3 is skipped, 5 stops before printing)