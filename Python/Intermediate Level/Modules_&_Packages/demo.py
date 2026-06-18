# demo.py
print(f"Outside block: __name__ = '{__name__}'")

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(f"Inside block: Running directly")
    print(greet("World"))