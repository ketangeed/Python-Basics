# The Anatomy of a Function:
# def: Tells Python "I am building a machine."
# The Name: What the machine is called.
# The Input (Parameters): The raw material you give the machine.
# return: What the machine gives back to you when it's done.


# A function is a block of code that performs a specific task whenever you call/use it.
# to change something code you have to change eveywhere, but in funtion/ using fuction you need to.

# without function we have to write it seperatly.
# print("Hello")
# print("Welcome")
# print("Bye")

# but with function

# def greet():
#     print("Hello")
#     print("Welcome")
#     print("Bye")

# greet()
# greet()



# we can print it just by calling.
# def = define/create function
# greet = function name
# () = function container

# def welcome():
#     print("Welcome to the python")
#     print("Python is fuun")
#     print("I love python")

# welcome()
# welcome()



# lets suppose i want to find the avg the i have to do this:

# a = 4
# b = 7
# c = 2

# d = (a+b+c)/3
# print(d)

# but what if want to do multiple times then i just simply create the function.
# def avg (a, b, c):
#     d = (a + b + c)/3
#     print(d)

# avg( 1, 2, 8)
# i just jave to call the function and it will do the fuction for me.


#  use the return to send a value back.
# return sends a value back from a function so you can use/store it later.
# you can store the answer in a variable.


def avg (a, b, c):
    d = (a + b + c)/3
    print(d)
    return 

o1 = avg( 1, 2, 8)
o2 = avg( 3, 9, 5)

print(o1) # result None
print(o2) # result None

# but to assign the value of the function to the variable we ll use the return fuction.



# return gives the answer back to variable.

def multiply(a, b):
    return a*b

result = multiply(2, 5)

print(result)



# Use:

# print() when:

# You only want to display something.

# Use:

# return when:

# You want to use/store/manipulate the result later.