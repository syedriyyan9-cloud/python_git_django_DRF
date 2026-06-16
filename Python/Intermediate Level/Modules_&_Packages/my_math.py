"""
My math module that contains a few basic functions
"""

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    # Test code runs only when script is executed directly
    print("Testing mymath:", add(2, 3) == 5)