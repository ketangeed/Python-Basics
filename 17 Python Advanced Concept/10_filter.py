def is_greater_than_only(x):
    if x>9:
        return True
    else:
        return False
    
numbers = [1, 2, 4, 5, 55, 677, 7, 8, 99, 34, 66, 89, 9] #this are the itrebles...

new = list(filter(is_greater_than_only, numbers))
print(new)
# will fiter the list.... and return the filtered object...
# filter function will only create the new object or new value that is true...

#  can use lambda as well, 

new1 = list(filter(lambda x: x>9, numbers))
print(new1)