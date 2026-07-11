import pdb

# pdb is a module used for debugging in python
# the main purpose is to allow user to go over our code step by step
# the debugger works in the terminal, and you would see (pdb) there which shows that debugger is working
# to start the debugger we use the set_trace method which starts the debugger in the code
# even if the code is working properly you can still review it, just ensure to use set_trace before the part where you want to see how the lines of code are being executed

def divide(n1: int, n2: int) -> float:
    '''divides two numbers, returns float'''
    return n1/n2

# now if we give value to this function we can see it working
# n1 = 10
# n2 = 0
# result = divide(n1,n2)
# print(result)

# here we can predict that we would get a zero division error

# before getting started here is a list of chars you should be familiar with:
# s (step): Executes the current line and steps into a function if possible.
# n (next): Executes the current line and moves to the next line in the current file without stepping inside functions.
# c (continue): Resumes program execution until the next breakpoint is encountered.
# p (print): Evaluates and prints the value of an expression (e.g., p my_variable).
# l (list): Displays 11 lines of source code centered around the current line.
# u (up): Moves the current frame one level up in the stack trace (useful to see who called your current function).
# d (down): Moves the current frame one level down in the stack trace.
# q (quit): Exits the debugger and aborts the script execution.
'''!(assign): this ! is used to assign variables values in terminal when dubugging. example: !n1 = 9 '''

# so lets now use pbd to debug it
pdb.set_trace()
n1 = 10
n2 = 0
result = divide(n1,n2)
print(result)

# now when we run the program we would get this: -> n1 = 10
# this just means taht are at this line of code, we can use n(next) to move onto the next line
# now we will get: -> n2 = 0
# so now we move onto the third step using 'n' again to move onto the next step
# here we can see that this is the part where we would get an error. so here we would step into the function using s
# now we would get something like this: -> def divide(n1: int, n2: int) -> float:
# this shows that now we are inside the function.
# here we can debug the values by first looking them up using p(print) followed by variable name
# so here it would be p n1, p n2
# now we can see that our n2 is 0, because of which we get the division by zero error
# now we can reassign the variable again using '!' along with variable name and assignment op followed by a valu
# example: !n2 = 2, this would reassign the value of n2 to 2
# then we can use 'c' continue to move onto the next breakpoint if there is any.
# this successfully debugs our code and now we know what changes we have to make to ensure the code works properly. 
