# function arguments and return values.

# qs.1 write the full name(first,last) and return the single string in the format of "first last" .


def name(first, last):
    return f"{first} {last}"

name("Ketan", "Geed")





# qs.2 write the function calaulate_area(length, width=10), that return the area of rectangle. test it by calling the function with.
# 1. both length and width
# 2. only length (use default with)


# 1. 

def function_area(length, width):
    return length*width

print(function_area(13, 20))


# 2. 
def function_area(length, width=10): #default width is 10. can change it if you want just give the diff val in print.
    return length*width

print(function_area(13, 20))





def rec(a, b=10):
    return a*b

print(f"The area of rectangle is {rec(13, 20)}")
print(rec(13))