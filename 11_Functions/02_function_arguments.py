# def add(a, b): #a and b are called parameters.
#     return a+b

# c = add(4, 8) # temporary assigned the value.
#  and 4, 8 are arguments.
# print(c)

# Parameters allow you to send data/input into a function.

# u can also do this
def add(a, b):
    x = a + b
    return x

c = add(40, 8) 
print(c)



# keyword arguments
# you can give the value in any order but you have to mention it.

# ex.
c = add(b= 5, a= 2)
print(c)


def person(name, city):
    print(f"{name} lives in {city}")

person ("Ketan", "Mumbai")





'''Use:

print() when:

You only want to display something.

Use:

return when:

You want to use/store/manipulate the result later.'''