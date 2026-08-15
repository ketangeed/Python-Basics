# https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcQhR9SyDfNOpfNfw4ORJrvZk3kcOi56CVBlr_5Sp3bX57CxMEUxbObgeznHZ2HllT0vbVhUKRFF2_mzuUjLuCnCkYGulABc4cQIvGvDTSx3CP-EWzw





# A for loop is used to repeat something multiple times.

# for i in range( 1, 10): # range function goes from 1 to (10-1)
#     # i.e 9 in this case.
#     print(i)

# for i in range(1, 11):
#     print("5 x", i, "=", 5*(i))

# # here you can also go for (5*(i)).
# # range is (start, end - 1)


# # range(start, end, step)
# for k in range(1, 10, 2):
#   print(k)


#  for loops are generally are used for sequencial traversal.
#  for traversing for list, strings, tuples etc.

nums = [1,2,3,4,5,6,7]

for val in nums:
   print(val , end=" ")


# tup = (1, 4, 2, 5, 9, 4, 1)

# for num in tup:
#    print(num)

# str = "neuralmamba"
# for char in str:
#    print(char, end=" ")



list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 4)

k = 4
idx = 0

for i in list:
    if(i == k):
        print("k is found at idx", idx)
    idx += 1


n = int(input("Enter the number : "))

for i in range(1, 11):
    print(n*i)