# Recurrsion.

# qs.1 write the recurssion function factorial(n) that return the factorial of a number.



def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)

print(sum_of_digits(69))



# write the recursive function sum_of_digits(n) that return the sum of all digits of the given number.


