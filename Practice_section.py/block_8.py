# Q1
# Create set with duplicate values and print it
set1 = {1, 2, 2, 3, 5, 7, 9}
print(set1)

# Q2
# Add a new value
set1.add(10)
print(set1)

# Q3
# Remove a value
set1.remove(2)
print(set1)

# Q4
# Check if value exists
set2 = {1, 3, 2, 2, 3, 5, 7}
user = int(input("Enter the number : "))

for i in set2 :
    if (i == user) :
        print("Value Exists.")

# Q5 (IMPORTANT)
# Find common elements between two sets

# a = {1, 3, 4, 5, 4, 2, 4}
# b = {2, 4, 5, 7, 2, 1}

# c = a.intersection(b)
# print(c)