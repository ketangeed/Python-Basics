# Q1
# Take age input and print its type.
age = input()
print(type(age))
# Q2
# Take number as input and convert it into integer, then add 10 and print.
num = input("Enter the number: ")
num1 = int(num)
print(num1+10)
# Q3
name = "Ketan"
age = 18
is_student = True
print(f"Hi {name}, you are {age} years old, and that's {is_student}, that your are a student")
# Q4
# Take two numbers as input and print their sum.
a = int(input('Enter the first number: '))
b = int(input("Enter the second number: "))
print(a+b)


# Q1. # Take a number and print:
# "Even" if even
# "Odd" if odd
num = int(input("Enter the number : "))
if (num % 2) == 0:
    print("Even")
else:
    print("Odd")
# Q2.
# Take two numbers and print:
# which one is greater
# or "Equal"
a = int(input("Enter the first number: "))
b = int(input(("Enter the second number: ")))
if (a>b):
    print('a is greater number.')
elif(a==b):
    print("the numbers are equal.")
else:
    print("b is greater number")
# Q3.
# Take a number and print:
# "Divisible by 3 and 5"
# otherwise print "Not divisible"
# "hint" = If question says "divisible" → ALWAYS use %
number = int(input("Enter the number : "))
if (number % 3 == 0 and number % 5 == 0):
    print("Number Divisible by 3 and 5")
else:
    print("Not divisible.")
# qs.4 chcek the nume is it betn 10 aqnd 50.
number1 = int(input("Enter the number : "))
if (number1 > 10 and number1 < 50):
    print("Valid")
else:
    print("Not valid")




#Q1. Print numbers from 1 to 20 using for loop

for i in range(1, 11):
    print(i)

# Q2.Print numbers from 20 to 1 using while loop.

i = 20
while i <= 1:
    print(i)
    i -= 1


# Q3 Print: 1 4 9 16 25 ... up to 10 numbers
# for loop:

for i in range(1, 11):
    print(i*i)
    i += 1

# while loop:

i = 1
while i <= 10:
    print(i*i)
    i += 1


 # Q4.  Take a number and print its table (1 to 10)



num = int(input("enter the number : "))

for i in range(1, 10):
    print(num, "x", i, "=", num*i)
    i += 1


# Q5. Find sum of numbers from 1 to n.
# (input from user)

num = int(input("Enter the number : "))
total = 0
i = 1

while i<=num:
    total += i
    i += 1

print(total)