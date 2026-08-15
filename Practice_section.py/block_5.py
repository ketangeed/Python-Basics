# Q1
# Create list of 5 numbers and print all
list = [1, 2, 3, 4, 5]
print(list)

# Q2
# Print only even numbers from list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list1:
    if i % 2 == 0:
        print(i)

# Q3
# Find sum of all elements in list
list2 = [2, 4, 6, 8, 10]
total = 0
for i in list2:
    total += i
print(total)

# Q4
# Find largest number in list
list3 = [22, 57, 87, 24, 99]
print(max(list3))

# Q5 (IMPORTANT)
# Count how many numbers are greater than 10
list4 = [10, 36, 2, 80, 35, 4, 98]
count = 0
for i in list4:
    if i>10:
        count += 1
print(count)