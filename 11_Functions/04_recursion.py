# Recursion is when a function calls itself.
# Every recursion MUST have:
# Stopping Condition (Base Case)
# Otherwise:
# It never stops.
# and Recursion case (call itself again)


'''this is what the fibonacci series is 
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 7...
they just keeps adding with the last number.

fib(0) = 0
fib(1) = 1 
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1)
'''


def fib(n):
    if (n == 0 or n == 1):
        return n
#  this is the Base case of the recurssion.
    return fib(n-2) + fib(n-1)

print(fib(7))






def fib(n):
    if (n == 0 or n == 1):
        return n
    return fib(n-2) + fib(n-1)

print(fib(6))

fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib (3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib (1) + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1

# this is what happn behind the code, value goes to the condition until it satisfies.





#  we can say that factorial n = n * factorial(n-1)

def factorial(n):
    if ( n == 0 or n == 1):
        return n
    return n * factorial(n-1)


a = factorial(5)
print(a)
# what happened here is that we create the fuction inside the fuction.
# first it wil do 5 * fact(n-1)
# then again it will and up to find the value of the n, until it meets the if condition and then it will print the result.
# 5 * factorial(n-1)
# 5 * 4 * factorial(n-1)
# 5 * 4 * 3 factorial(n-1)
# 5 * 4 * 3 * 2 factorial(n-1)
# 5 * 4 * 3 * 2 * 1 the output will will be 120.






# by tulosko : when a fuction call itself is recurssion
i = 0

def greet():
    global i
    i += 1
    print("Hello.", i)
    greet()
greet()