from functools import reduce
# functool is an internal module 


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         [3, 3, 4, 5, 6, 7, 8, 9] this is what happen behide...
#         [6, 4, 5, 6, 7, 8 ,9]
#         [10, 5, 6, 7, 8, 9]
#         [15, 6, 7, 8, 9]
#         [21, 7, 8, 9]
#         [28, 8, 9]
#         [36, 9]
#         [45]

def new_num(a, b):
    return a + b 

new = reduce(new_num, numbers)
print("Reduced value is : ", new)


# The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value. reduce is not a built-in function; it must be imported from the functools module.