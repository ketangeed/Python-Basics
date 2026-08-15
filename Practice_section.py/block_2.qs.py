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


#  print the start pattern using loop.
for i in range(1, 6):
    print("*" * i)



# Take a number and find its factorial using loop

num = int(input("Enter the number: "))
result = 1
for i in range(1, num+1):
    result = result  * i
    i+=1
print(result)


    


    




