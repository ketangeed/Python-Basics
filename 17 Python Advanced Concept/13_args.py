#  *args basically collect all the arguments and creates an tuple

def sum(*args):
    # args will be a tuple to all the value passed.
    total = 0
    for items in args:
        total += items
    return total

print(sum(23, 55, 789, 4))


# *args (Positional Arguments)
# *args collects any extra positional arguments passed to a function into a tuple. The name args is just a convention; you could use any valid variable name preceded by a single asterisk (e.g., *values, *numbers).