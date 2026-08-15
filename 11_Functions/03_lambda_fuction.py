square = lambda x : x*x #here we assignd the value of x, which is x*x means a square.

'''as good as writing the
# def square(x):
    return x*x
    
d = square(x)
print(d)'''

# they are just for the convenience.


sum = lambda x, y : x + y

print(square(5)) # result is 25.
print(sum(5, 5)) #result is 10.

''' 
It is as good as this :
def sum(a, b):

    return a + b
o1 = sum(2 , 5)
print(o1)
'''
# but we still use just for the convenience.


def square(x):
    return x*x
    
d = square(5)
print(d)



def sum(a, b):
    return a+b
print(sum(2, 3))