# tuples....

# Q1
# Create a tuple of 5 numbers and print all elements.
num = (1, 3, 5, 7, 9)
print(num[0:])

# Q2
# Print first and last element
a = (1, 3, 4, 5, 2)
print(a[0])
print(a[-1])

# Q3
# Count how many times a number appears.
b = (2, 4, 2, 1, 4, 5, 2)
user = int(input("Enter the number : "))
count = 0
for i in b:
    if i == user:
        count += 1
print(count)

# Q4
# Find maximum number in tuple
c = (2, 33, 12, 56, 78, 3, 45)
print(max(c))

# Q5 (LOGIC)
# Convert tuple into list and print it
d = (2, 5, 88, 34, 0, 1)
my_list = list(d)
print(my_list)