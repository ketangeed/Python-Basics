# variable scope.

# qs.1 write the function increment() that has local variable counter intialize to 0 and incremented by 1, each time it is called. observe whether the value persists across the function call.

# counter = 0 for the increment

def increment():
    # global counter (for the increment)
    counter = 0
    counter += 1
    print(counter)


increment()
increment()
increment()
increment()
# result is same no increment occur.



# qs 2. write the function multiply (a, b) that has proper docstring explaining what it does. then use help(multiply) to display the docstring.

def multiply(a, b):
    '''this is used for the multiplication.'''
    # write something long enough that can be used.
    return a*b

print(multiply.__doc__)
#  or
help(multiply)



# do bonus challenge..


