# # for i in range(1, 6):
# #     print("*"*i)


# # num = int(input("num : "))

# # for i in range(1, num+1):
# #     for j in range(1, i):
# #         print(j, end="")
# #     print()


# # for i in range(1, num+1):
# #     for j in range(i):
# #         print(i, end="")
# #     print()



# # num = int(input())

# # for i in range(num, 0, -1):
# #     print("*" * i)






# # Q1
# # Reverse string using loop (NO slicing)
# name = "Ketan"
# reversed_name = ""
# for char in name:
#     reversed_name = char + reversed_name
# print(reversed_name)

# # Q2
# # Count vowels (handle uppercase too)
# txt = "i love python prOgraming."
# vowels = ["a", "e", "i", "o", "u"]
# count = 0
# for char in txt:
#     if char.lower() in vowels:
#         count += 1
# print(count) 

# # Q3
# # Count consonants
# stat = "KetanGeed"
# vowels = ["a","e","i","o","u"]
# count = 0
# for char in stat:
#     if char.lower() not in vowels:
#         count += 1
# print(count)

# #Q4
# # Remove all spaces
# name1 = " Neural Mamba "
# print(name1.strip())

# # Q5 (CHALLENGE)
# # Check if string is palindrome (without slicing)
# statement = input()
# a = statement[0:]
# b = statement[::-1]

# if a == b:
#     print("palindrome")    
# else:
#     print("not palindrome")























age = int(input("enter your age: "))


if (age >= 18 ):
    print("Adult")
else:
    print("Minor")


num = int(input("enter the number : "))

if (num > 0):
    print("Positive")
elif (num = 0):
    print("zero")
else:
    print("negative")


























