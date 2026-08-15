# q.1 print numbers from 1 to 100 using while loop.

# i = 1

# while i <= 100 :
#     print(i)
#     i += 1


# print numbers from 100 to 1.

# k = 100

# while k >= 1 :
#     print(k)
#     k -= 1


# print the multiplication table of the number n.

# num = int(input("Enter the number for multiplication : "))

# i = 1

# while i <= 100 :
#     print(f"{num}","x",i,"=",num * i)
#     i += 1
    



#  take an input from the user and sum it all
# num = int(input("Enter the number : "))

# total = 0
# i = 1

# while i <= num:
#     total += i
#     i += 1
# print(total)





# Find sum from 1 to n
# num = int(input("Enter the number : "))
# i = 1
# total = 0

# while i <= num:
#     total += i
#     i += 1
# print(total)





#  find the sum of even numbers from 2 to 20.

# i = 2
# total = 0

# while i <= 20 :
#     total += i
#     i += 2
# print(total)


# # Q12 — Sum of odd numbers (1 to 19)

# i = 1
# total = 0
# while i <= 19 :
#     total += i
#     i += 2
# print(total)


# # print the square from 1 to 10.

# i = 1

# while i <= 10 :
#     print(i**2 , end = " ")
#     i += 1

# #  print the number from 1 to 20 but only the even numbers.

# i = 2

# while i <= 20 :
#     print(i)
#     i += 2


# # Print numbers from 1 to 20 but skips the multiples of the 3.

# i = 1

# while i <= 20:
#     if i % 3 != 0:
#         print(i)
#     i += 1


#  write the program to print the number from 1 to 50 and skips the numbers that are divisible by 5.
# i = 1

# while i <= 50:
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)
#     i += 1



# #  take the number from user and write the sum of all numbers in it.
# k = int(input("enter the number : "))
# total = 0
# i = 1

# while i <= k:
#     total += i
#     i += 1
# print(total)


# # WAP for to find the nth factrial. using for function

# s = int(input("enter the number : "))

# fact = 1

# m = 1

# while m <= s:
#     fact *= m
#     m += 1
# print("factorial is ", fact)


# n = 5
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print(fact)
    

# Q.1 print the numbers from 1 to 10 using while loop.

i = 1
while i <= 10:
    print(i)
    i += 1


# write the program that keeps asking for the password until the correct one is entered.

password = "KETAN"

correct_pass = input("enter the correct password : ")

while (correct_pass != password):
    correct_pass = input("enter the correct password : ")
    
print("you r logged in")



