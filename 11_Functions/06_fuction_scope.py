# In python varibles have scope, scope(where they can be accesed), and lifetime(for how long they exist.)


def sum(a, b):
#  therefore the a, b are the local varible, they cannot be accessed out side of it.
    c = a+b
    print(z)
    return c
# fuctions only keeps variables until it returns.
z = 8 # z is the global varible so it can be accessed.
print(sum(3, 7))
# print(c) this cant be happn, because when the 3 and 7 are given as a nd b then it performs the fuction and then returns. and then python fuction wipes out the a, b, c. thats it.





'''# code with harry notes : 
# x = 10  # Global variable

# def my_func():
#     x = 5  # Local variable
#     print(x)  # Output: 5

# my_func()
# print(x)  # Output: 10 (global x remains unchanged)'''



'''Using the global Keyword
To modify a global variable inside a function, use the global keyword:

x = 10  # Global variable
 
def modify_global():
    global x
    x = 5  # Modifies the global x
 
modify_global()
print(x)  # Output: 5'''