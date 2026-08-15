# Q1.Write function to print:
# Hello, Ketan

def hello(name):
    print(f"Hello, {name}")
hello("Ketan")

# Q2Function that takes number and prints:
# square of number

def square(num):
    return num*num
result = square(5)
print(result)

# Q.3. 
# Function that takes 2 numbers and returns:
# greater number

def num(a, b):
    if a > b:
        return(a)
    elif a < b:
        return(b)
    else:
        return "Similar"
result = num(5, 4)
print(result)
       
# Q4 (IMPORTANT)
# Function to check:
# even or odd
def fun(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
ans = fun(4)
print(ans)

# Q5 (LOGIC BUILDER)
# Function that returns:
# sum of numbers from 1 to n
def num(a):
    total = 0
    for i in range(1, a+1):
        total += i
    return total
b = num(5)
print(b)


