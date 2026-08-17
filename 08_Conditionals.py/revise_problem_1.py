# Write a Python script using a for loop and range() that:

# Loops through numbers from 1 to 20 (inclusive).

# For each number:

# If the number is divisible by 3, print "Fizz".

# If the number is divisible by 5, print "Buzz".

# If it is divisible by both 3 and 5, print "FizzBuzz".

# Otherwise, simply print the number itself.


for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)