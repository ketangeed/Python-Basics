# Maps, reduce, filter are the higher order function.
# itrebles = list, tuples, sets, whose items will be processed..


numbers = [1, 2, 3, 45, 5, 6, 7, 8, 9]

def square(x):
    return x * x

new = list(map(square, numbers))
print(new)

# we just maped out the function for list, it can also for tuple, and set...
# it returns the maped itrebles

# lambda is widely used in this, its much more easier..


new1 = list(map(lambda x: x*x, numbers))
print(new1)