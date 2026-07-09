import pdb

def divide(a, b):
    result = a / b
    return result

def main():
    x = 10
    y = 0
    pdb.set_trace()  # Program pauses here
    z = divide(x, y)
    print(f"Result: {z}")

if __name__ == "__main__":
    main()

'''type s to step into the divide function. Inside, type p a and p b 
to see the arguments. Type n to execute result = a / b and see the crash. 
To avoid this, you could use !y = 2 to change y's value before the division, 
then c to continue, and the program runs successfully.'''

