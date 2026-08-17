# Write a Python script using a for loop over range(1, 11) (numbers 1 to 10) that:

# Keeps track of a total_sum starting at 0.

# For each number:

# If the number is even, add it to total_sum.

# If the number is odd, do nothing using the pass statement.

# After the loop finishes, print: f"The sum of even numbers is: {total_sum}".

total_sum = 0
for i in range (1, 11):
    if i % 2 == 0:
        total_sum += i
    else:
        pass
print(f"The sum of even numbers is: {total_sum}")
